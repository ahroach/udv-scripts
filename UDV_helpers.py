"""Provides a number of routines for plotting and analyzing UDV data

When a channel or velocity is required as input to a routine, it is
referring to a ChannelData or Velocity object as defined in
udv_classes.py. The get_shot() method of the ShotList class in
udv_classes.py is the best way to get a Shot object, and the
get_channel() or get_velocity() methods of the Shot object should be
used to get the appropriate ChannelData or Velocity object. As an
example, we might run

   import udv_classes
   udv_classes.set_data_path("/u/aroach/ultrasound_data")
   get_shot = udv_classes.ShotList().get_shot
   plot_avg_vtheta_profile(get_shot(852).get_velocity(1,2), 100, 150)

to plot the average vtheta obtained from combining channels 1 and 2
from shot 852."""

import math
import cmath
import scipy
import scipy.interpolate
from scipy.interpolate import UnivariateSpline
import scipy.optimize
import scipy.signal
import subprocess
import os
import shutil
import glob
import string
import matplotlib.animation as animation
from numpy import *
from pylab import *

r1 = 7.06 #Position of IC in cm
r2 = 20.30 #Position of OC in cm

rpmtorads = lambda x: x*2.0*pi/60.0
degstorads = lambda x: x*pi/180.0

def wrap_phase(angle):
    '''Make phase fit in the range -pi to pi.'''
    while (angle > pi):
        angle = angle - 2.0*pi

    while (angle < -pi):
        angle = angle + 2.0*pi

    return angle


def filter_velocity(data, filter_threshold):
    '''Provides a simple filter for outliers in a velocity vector'''

    for i in range(5, data.size-5):
        #Get the mean from the previous 5 measurements, excluding nans
        meandata = ma.masked_array(data[i-5:i], isnan(data[i-5:i])).mean()
        if isnan(meandata):
            #Uhoh. It looks like everything ahead of us was a nan.
            #I guess all we can do is look ahead and hope for the best.
            meandata = ma.masked_array(data[i+1:i+6],
                                       isnan(data[i+1:i+6])).mean()
        if (abs(data[i] - meandata) > filter_threshold):
            #If the point looks bad, make it a nan.
            data[i] = nan

    #Don't want to leave nans in the data, so replace them with the
    #mean around that measurement.
    for i in range(2, data.size-2):
        if isnan(data[i]):
            data[i]=ma.masked_array(data[i-2:i+3],isnan(data[i-2:i+3])).mean()

    return data


def plot_channel_velocity(channel, start_num, end_num, unwrapped=0,
                          labelstring="", time=0):
    '''Plots the velocity measured by a specified channel. start_num
    and end_num are the indices to average between, unless time != 0, in
    which case those are time points to average between. Unwrapped velocity
    is plotted instead of raw velocity if unwrapped != 0'''
    if(time != 0):
        start_num = channel.get_index_near_time(start_num)
        end_num = channel.get_index_near_time(end_num)

    if (unwrapped == 0):
        profile = mean(channel.velocity[start_num:end_num,:], axis=0)
    else:
        profile = mean(channel.unwrapped_velocity[start_num:end_num,:], axis=0)
        
    plot(channel.depth, profile, '-o', label=labelstring)
    print "Maximum velocity = %.3g" % channel.maxvelocity
    print "Time = %.3g to %.3g" % (channel.time[start_num],
                                   channel.time[end_num])  


def plot_single_vtheta_profile(velocity, profile_num):
    '''Plot a single azimuthal velocity profile for a velocity object.'''
    label_str = "Shot %d: t=%0.3g" % (velocity.shot.number,
                                      velocity.time[profile_num])

    plot(velocity.r, velocity.vtheta[profile_num,:], label=label_str)
    plot(velocity.shot.idealcouette.r, velocity.shot.idealcouette.vtheta)


def plot_avg_vtheta_profile(velocity, start_num, end_num):
    '''Plot the average azimuthal velocity profile for a Velocity object,
    from the specified start index to the end index.'''
    label_str = "%d: Avg from t=%.3g to t=%.3g" % (velocity.shot.number,
                                                   velocity.time[start_num],
                                                   velocity.time[end_num])

    plot(velocity.r,
         mean(velocity.vtheta[start_num:end_num, :], axis=0),
         label = label_str)
    plot(velocity.shot.idealcouette.r, velocity.shot.idealcouette.vtheta)


def plot_raw_data_all_channels(shot, start_time, end_time,
                               offset=0, scale=1.0):
    for ch_num in shot.channels_used:
        ch = shot.get_channel(ch_num)
        start_idx = ch.get_index_near_time(start_time)
        end_idx = ch.get_index_near_time(end_time)
        if (sin(ch.B) > 0):
            labelstring = "Ch.%d" % ch_num
        else:
            labelstring = "-Ch.%d" % ch_num
        
        if(offset):
            plot(ch.depth-ch.offset,
                 (scale*sin(ch.B) *
                  mean(ch.unwrapped_velocity[start_idx:end_idx,:], axis=0)),
                 label=labelstring)
        else:
            plot(ch.depth-ch.offset,
                 (scale*sin(ch.B) *
                  mean(ch.unwrapped_velocity[start_idx:end_idx,:], axis=0)),
                 label=labelstring)
        legend(loc='upper left')
                 

def plot_channel_velocity_contour(channel, unwrapped=0, n=30):
    '''Makes a contour plot of the raw velocity as a function of depth for a
    channel'''
    if (unwrapped == 0):
        contourf(channel.time, channel.depth, channel.velocity.T, n)
    else:
        contourf(channel.time, channel.depth, channel.unwrapped_velocity.T, n)
    xlabel("Time [sec]")
    ylabel("depth [cm]")
    colorbar()


def plot_two_component_velocity_contours(velocity, start_time, end_time, n=30):
    start_idx = velocity.get_index_near_time(start_time)
    end_idx = velocity.get_index_near_time(end_time)

    subplot(2,1,1)
    contourf(velocity.time[start_idx:end_idx],
             velocity.r, velocity.vr[start_idx:end_idx,:].T, n)
    ylabel("r [cm]")
    title('vr')
    colorbar()

    subplot(2,1,2)
    contourf(velocity.time[start_idx:end_idx],
             velocity.r, velocity.vtheta[start_idx:end_idx,:].T, n)
    xlabel("Time [s]")
    ylabel("r [cm]")
    title('vt')
    colorbar()

    
def plot_timeseries(channel, radius, labelstring='', withpts=0):
    """Plot timeseries of the velocity measured by a channel at one radius"""
    idx = channel.get_index_near_radius(radius)
    if(len(labelstring) == 0):
        labelstring="Shot %d, Ch. %d:\nd=%.3gcm, r=%.3gcm"%(channel.shot.number,
                                                            channel.channel,
                                                            channel.depth[idx],
                                                            channel.r[idx])
        
    if(withpts):
        plot(channel.time, channel.velocity[:,idx], '.-', label=labelstring)
    else:
        plot(channel.time, channel.velocity[:,idx], '-', label=labelstring)

    xlabel("Time [sec]")
    ylabel("Velocity [cm/sec]")


def plot_two_component_velocity_timeseries(velocity, radius, ls='.-'):
    '''Plot timeseries of a velocity object at a specified radius'''
    idx = velocity.get_index_near_radius(radius)

    titlestring = "Shot %d, r=%.3gcm" % (velocity.shot.number,
                                         velocity.r[idx])
    plot(velocity.time, velocity.vr[:,idx], ls, label=r"$v_r$")
    plot(velocity.time, velocity.vtheta[:,idx], ls, label=r"$v_\theta$")
    xlabel("Time [sec]")
    ylabel("Velocity [cm/sec]")
    title(titlestring)


def plot_wave_amplitude_profile(velocity, component, start_time, end_time,
                                freqband_min = 0, freqband_max = 0,
                                filter_threshold=1000):
    '''Plots the amplitude of velocity fluctuations in a given frequency
    band as a function of radius. Note that the peak-to-peak velocity
    is twice the amplitude.'''
    if(component == 'vr'):
        data = velocity.vr.copy()
        labelstring = r"$|\tilde{v_r}|$"
    elif(component == 'vtheta'):
        data = velocity.vtheta.copy()
        labelstring = r"$|\tilde{v_\theta}|$"
    elif(component == 'vz'):
        data = velocity.vz.copy()
        labelstring = r"$|\tilde{v_z}|$"
    else:
        print "Error: Allowable components are 'vr', 'vtheta', or 'vz'."
        return False
    

    start_num = velocity.get_index_near_time(start_time)
    end_num = velocity.get_index_near_time(end_time)
    
    amplitude = zeros(velocity.r.size)
    for i in range(0, amplitude.size):
        power = get_power_in_band(velocity.time[start_num:end_num],
                                  filter_velocity(data[start_num:end_num, i],
                                                  filter_threshold),
                                  freqband_min = freqband_min,
                                  freqband_max = freqband_max)
        amplitude[i] = sqrt(power)

    plot(velocity.r, amplitude, label=labelstring)
    xlabel(r"$r$ [cm]")
    ylabel("Velocity [cm/s]")


def plot_wave_amplitude_profile_vert(velocity, component, start_time, end_time,
                                     freqband_min = 0, freqband_max = 0,
                                     filter_threshold=1000):
    '''Plots the amplitude of velocity fluctuations in a given frequency
    band as a function of radius. Note that the peak-to-peak velocity
    is twice the amplitude.'''
    if(component == 'vr'):
        data = velocity.vr.copy()
        labelstring = r"$|\tilde{v_r}|$"
    elif(component == 'vtheta'):
        data = velocity.vtheta.copy()
        labelstring = r"$|\tilde{v_\theta}|$"
    elif(component == 'vz'):
        data = velocity.vz.copy()
        labelstring = r"$|\tilde{v_z}|$"
    else:
        print "Error: Allowable components are 'vr', 'vtheta', or 'vz'."
        return False
    

    start_num = velocity.get_index_near_time(start_time)
    end_num = velocity.get_index_near_time(end_time)
    
    amplitude = zeros(velocity.z.size)
    for i in range(0, amplitude.size):
        power = get_power_in_band(velocity.time[start_num:end_num],
                                  filter_velocity(data[start_num:end_num, i],
                                                  filter_threshold),
                                  freqband_min = freqband_min,
                                  freqband_max = freqband_max)
        amplitude[i] = sqrt(power)

    plot(velocity.z, amplitude, label=labelstring)
    xlabel(r"$z$ [cm]")
    ylabel("Velocity [cm/s]")


def plot_power_spectrum_velocity(velocity, component, radius, start_time,
                                 end_time, freqband_min = 0, freqband_max = 0,
                                 filter_threshold=1000):
    '''Plot the power spectrum for a velocity component at specified radius.'''
    
    if(component == 'vr'):
        data = velocity.vr.copy()
    elif(component == 'vtheta'):
        data = velocity.vtheta.copy()
    elif(component == 'vz'):
        data = velocity.vz.copy()
    else:
        print "Error: Allowable components are 'vr', 'vtheta', or 'vz'."
        return False

    start_num = velocity.get_index_near_time(start_time)
    end_num = velocity.get_index_near_time(end_time)
    idx = velocity.get_index_near_radius(radius)

    freq,power=calculate_power_from_fft(*calculate_fft(velocity.time[start_num:end_num],
                                                       filter_velocity(data[start_num:end_num, idx],
                                                                       filter_threshold)))

    subplot(2,1,1)
    semilogy(freq, power)
    xlabel("Freq [Hz]")
    ylabel("Power Spectrum")
    xlim(xmin=0.0)
    grid(b=1)
    
    subplot(2,1,2)
    plot(velocity.time[start_num:end_num], data[start_num:end_num, idx])
    xlabel("Time [sec]")
    ylabel("Velocity [cm/sec]")
    
    pinband = get_power_in_band(velocity.time[start_num:end_num],
                                filter_velocity(data[start_num:end_num, idx],
                                                filter_threshold),
                                freqband_min,
                                freqband_max)
    output1 = "Power in band = %0.5g at r = %0.3gcm, " % (pinband,
                                                          velocity.r[idx])
    output2 = "Trough-to-peak velocity = %0.5gcm/sec" % (2*sqrt(pinband))
    print output1 + output2


def plot_power_spectrum_channel(channel, idx, start_time,
                                end_time, freqband_min = 0, freqband_max = 0,
                                filter_threshold=1000):
    '''Plot the power spectrum from a point in a measurement channel'''
    start_num = channel.get_index_near_time(start_time)
    end_num = channel.get_index_near_time(end_time)

    freq,power=calculate_power_from_fft(*calculate_fft(channel.time[start_num:end_num],
                                                       filter_velocity(channel.velocity[start_num:end_num, idx],
                                                                       filter_threshold)))

    subplot(2,1,1)
    semilogy(freq, power)
    xlabel("Freq [Hz]")
    ylabel("Power")
    legend()
    xlim(xmin=0.0)
    grid(b=1)
    
    subplot(2,1,2)
    plot(channel.time[start_num:end_num],
         channel.velocity[start_num:end_num, idx], '.-')
    xlabel("Time [s]")
    ylabel("Velocity [cm/s]")
    
    pinband = get_power_in_band(channel.time[start_num:end_num],
                                filter_velocity(channel.velocity[start_num:end_num, idx],
                                                filter_threshold),
                                freqband_min,
                                freqband_max)
    output1 = "Power in band = %0.5g at depth = %0.3gcm, " % (pinband,
                                                          channel.depth[idx])
    output2 = "Peak-to-peak velocity = %0.5gcm/sec" % (2*sqrt(pinband))
    print output1 + output2


def calculate_fft(time, data):
    '''Calculate the fft given the time and data vectors. Returns the
    fftshifted results (with frequency=0 in the middle).'''
    
    if (len(time) != len(data)):
        print "Error in calculate_fft(): Time and data must be same length."
        return False
    
    fourier = fft(data)
    n = len(time)
    timestep = time[1] - time[0]
    freq = fftfreq(n, d=timestep)

    fourier = fftshift(fourier)
    freq = fftshift(freq)
    return freq, fourier, n


def calculate_power_from_fft(freq, fourier, n):
    '''Calculate the one-sided power-spectrum density from an fft. Look
    at comments for notes about the normalization. As normalized, the
    half-height (in other words, the A in front of A sin (\omega t)) of a
    velocity fluctuation at a given frequency should be sqrt(power) at that
    frequency.'''

    #Find the zero index.
    zero_idx = abs(freq).argmin()
    newfreq = freq[zero_idx:]
    newfourier = fourier[zero_idx:]

    #Note the normalization here:
    #The inverse transform a_m ~ (1/n) sum(k) A_k ...
    #The velocity due to a frequency component will be
    #(1/n)A_k + (1/n)A_-k. Since the magnitude of these two should be the
    #same, it will be (2/n)mag(A_k). So the power, going as velocity^2,
    #will be (4/n^2)*A_k*A_k.conjugate. Like this, the magnitude of the
    #velocity due to a given frequency component will be sqrt(power).

    #Note that I have to cast this as a real even though the quantity
    #is already real, because Python gets confused and casts it as
    #complex with Im{power} = 0 otherwise.
    power = real(4*newfourier*newfourier.conjugate()/(n*n))

    return newfreq, power


def get_power_in_band(time, data, freqband_min, freqband_max):
    freq, power = calculate_power_from_fft(*calculate_fft(time, data))
    
    powerinband = 0
    for i in range(0, freq.size):
        if (freq[i] > freqband_min) & (freq[i] < freqband_max):
            powerinband = powerinband + power[i]
    
    return powerinband    


def fit_frequency_channel(channel, idx, start_time, end_time,
                          start_amplitude = 1.0, start_frequency=1.0,
                          start_phase=0, start_offset=0):
    '''Fit a sinusoid to fluctuations seen on a given channel.'''

    start_pos = channel.get_index_near_time(start_time)
    end_pos = channel.get_index_near_time(end_time)
    time = channel.time[start_pos:end_pos]
    velocity = channel.velocity[start_pos:end_pos,idx]
    
    def residuals(p, y, t):
        A,frequency,theta,offset = p
        err = y - (A*sin(2.0*pi*frequency*t + theta) + offset)
        return err

    def peval(t, p):
        return p[0]*sin(2.0*p[1]*x + p[2]) + p[3]

    p0 = [start_amplitude, start_frequency, start_phase, start_offset]

    plsq = scipy.optimize.leastsq(residuals, p0, args=(velocity, time),
                                  full_output=1)

    print "Amplitude = %0.3g +/- %0.3g" % (plsq[0][0], sqrt(plsq[1][0][0]))
    print "Frequency = %0.3g +/- %0.3g" % (plsq[0][1], sqrt(plsq[1][1][1]))
    print "Phase = %0.3g +/- %0.3g" % (plsq[0][2], sqrt(plsq[1][2][2]))
    print "Offset = %0.3g +/- %0.3g" % (plsq[0][3], sqrt(plsq[1][3][3]))

    fitted_time = linspace(time[0], time[-1], 200)
    fitted_amplitude = (plsq[0][0]*sin(2*pi*plsq[0][1]*fitted_time
                                       + plsq[0][2])
                        + plsq[0][3])
    initial_guess = p0[0]*sin(2*pi*p0[1]*fitted_time + p0[2]) + p0[3]
    
    plot(time, velocity, '-o')
    plot(fitted_time, fitted_amplitude, label="Fitted")
    xlabel("Time [sec]")
    ylabel("Velocity [cm/sec]")


def get_autocorrelation(ch, r, t_start, t_end):
    ridx = ch.get_index_near_radius(r)
    startidx = ch.get_index_near_time(t_start)
    endidx = ch.get_index_near_time(t_end)

    ac = scipy.signal.correlate(ch.unwrapped_velocity[startidx:endidx,
                                                      ridx],
                                ch.unwrapped_velocity[startidx:endidx,
                                                      ridx])
    dt = linspace(-(ch.time[endidx-1]-ch.time[startidx]),
                  (ch.time[endidx-1] - ch.time[startidx]),
                  num=(2*ch.unwrapped_velocity[startidx:endidx,
                                               ridx].size - 1))
    return dt, ac


def get_crosscorrelation(ch1, ch2, r, t_start, t_end):
    ridx1 = ch1.get_index_near_radius(r)
    ridx2 = ch2.get_index_near_radius(r)
    startidx = ch1.get_index_near_time(t_start)
    endidx = ch1.get_index_near_time(t_end)

    cc = scipy.signal.correlate(ch1.unwrapped_velocity[startidx:endidx,
                                                       ridx1],
                                ch2.unwrapped_velocity[startidx:endidx,
                                                       ridx2])
    dt = linspace(-(ch1.time[endidx-1]-ch1.time[startidx]),
                  (ch1.time[endidx-1] - ch1.time[startidx]),
                  num=(2*ch1.unwrapped_velocity[startidx:endidx,
                                               ridx1].size - 1))

    #We must account for the offset due to the slightly different time bases
    #for the two channels.
    dt = dt - (ch2.time[endidx-1] - ch1.time[endidx-1])
    
    return dt, cc


def plot_correlations(shot, r, t_start, t_end, ch1=2, ch2=3):
    plot(*get_autocorrelation(shot.get_channel(ch1), r, t_start, t_end),
         ls='-', marker='.')
    plot(*get_crosscorrelation(shot.get_channel(ch2), shot.get_channel(ch1),
         r, t_start, t_end), ls='-', marker='.')


def plot_spectrogram(channel, idx, start_time=0, end_time=1000, timechunk=3):
    '''Plots a spectrogram of the velocity measured on the specified channel
    object at the location specified by the index idx.'''
    start = channel.get_index_near_time(start_time)
    end = channel.get_index_near_time(end_time)
    fig = figure()

    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2, sharex=ax1)
    ax1.plot(channel.time[start:end], channel.velocity[start:end, idx], '.-')
    ax1.set_ylabel("Velocity [cm/s]")
    titlestring = "Shot %d, Ch. %d: r=%.3gcm" % (channel.shot.number,
                                                 channel.channel,
                                                 channel.r[idx])
    ax1.set_title(titlestring)

    fs = 1.0/(channel.time[2]-channel.time[1])
    nfft = int(fs*timechunk)
    noverlap=nfft-1
    Pxx, freqs, bins, im = ax2.specgram(channel.velocity[start:end, idx],
                                        NFFT=nfft, Fs=fs, noverlap=noverlap)
    ax2.set_xlabel("Time [s]")
    ax2.set_ylabel("Frequency [Hz]")
    

def plot_two_component_avg_velocities(velocity, start_num, end_num,
                                      labelstring='', scale=1, rlim=0, time=0):
    '''Plots the average v_r and v_theta for the specified Velocity object.
    start_num and end_num are the indices to average between, unless time=1,
    in which case they are times in seconds.'''
    if(time == 1):
        start_num = velocity.get_index_near_time(start_num)
        end_num = velocity.get_index_near_time(end_num)

    if (start_num < 0) or (end_num > size(velocity.time)):
        print "Invalid start or end time indices."
        return False
    
    rlimin = velocity.get_index_near_radius(rlim)
    rlimout = velocity.get_index_near_radius(r2)

    subplot(2,1,1)
    ylabel(r"$v_\theta$ [cm/sec]")
    if(len(labelstring) == 0):
        labelstring= "Shot %d: %d to %d" % (velocity.shot.number,
                                            start_num,
                                            end_num)
    plot(velocity.r[rlimin:rlimout],
         scale*mean(velocity.vtheta[start_num:end_num,
                                    rlimin:rlimout], axis=0),
         label=labelstring)     
    axvline(x=r1, color='black')
    axvline(x=r2, color='black')
    plot(velocity.shot.idealcouette.r,
         velocity.shot.idealcouette.vtheta*scale, 'k-')
    grid(b=1)
    legend()

    subplot(2,1,2)
    xlabel("r [cm]")
    ylabel(r"$v_r$ [cm/sec]")
    plot(velocity.r[rlimin:rlimout],
         scale*mean(velocity.vr[start_num:end_num,
                                rlimin:rlimout], axis=0))
    axhline(y=0, color='black')
    axvline(x=r1, color='black')
    axvline(x=r2, color='black')
    grid(b=1)


def find_avg_velocity_at_r(velocity, start, end, radius, time=0):
    '''Finds the mean and stddev of v_r and v_theta at the specified radius.
    If time = 1, start and end and starting and ending times. Otherwise, they
    directly refer to indices in the time array. Returns vr_mean, vr_stddev,
    vt_mean, vt_stddev.'''
    if(time == 1):
        start = velocity.get_index_near_time(start)
        end = velocity.get_index_near_time(end)

    r_idx = velocity.get_index_near_radius(radius)
    vr = velocity.vr[start:end, r_idx]
    vt = velocity.vtheta[start:end, r_idx]

    return vr.mean(), vr.std(), vt.mean(), vt.std()


def plot_twopoint_avg_shear(velocity, start_time, end_time, rlimin, rlimout):
    """Find and plot the shear defined by two radial points"""

    omega = (velocity.mean_t(start_time, end_time)['vtheta'] /
             velocity.r)

    #Convert rlimits to element number
    rlimin_idx = velocity.get_index_near_radius(rlimin)
    rlimout_idx = velocity.get_index_near_radius(rlimout)
    
    avg_shear = ((omega[rlimout_idx] - omega[rlimin_idx]) / 
                 (velocity.r[rlimout_idx] - velocity.r[rlimin_idx]))
    offset = omega[rlimout_idx] - avg_shear*velocity.r[rlimout_idx]
    
    shear_fit_line = avg_shear*velocity.r + offset

    xlabel("r [cm]")
    ylabel(r"$\Omega$ [rad/sec]")
    plot(velocity.r, omega, label="Shot %g: %i-%is" % (velocity.shot.number,
                                                       start_time,
                                                       end_time))
    axvline(x=r1, color='black')
    axvline(x=r2, color='black')
    plot(velocity.shot.idealcouette.r,
         velocity.shot.idealcouette.vtheta/velocity.shot.idealcouette.r,
         'k-', label="Ideal Couette profile")
    fitlabelstring="Shear: " + str(avg_shear) + " rad/cm*sec"
    plot(velocity.r, shear_fit_line,
         label="Shear: %g; offset: %g" % (avg_shear, offset))
    grid(b=1)
    legend(loc='best')


def filter_outliers(x, stddevs):
    mx = median(x)
    b = abs(x-mx)
    #calculate median of absolute deviation
    mad = median(b)
    #Now calculate a modified z score
    mzx = (x-mx)/mad

    x_masked = ma.masked_inside(x, mx - mad*stddevs, mx + mad*stddevs)
    return x_masked


def show_shear_layer_evolution(velocity, rmin=9, rmax=19,
                               filteroutliers=0, tavg_start=0, tavg_end=0,
                               return_data=0):
    layer_width = zeros(velocity.time.size)
    layer_amplitude = zeros(velocity.time.size)
    layer_location = zeros(velocity.time.size)
    layer_avg = zeros(velocity.time.size)

    for i in range(0, velocity.time.size):
        a, avg_amp = eval_shear_layer(velocity, i, time=0,
                                      rmin=rmin, rmax=rmax)
        layer_amplitude[i] = avg_amp
        layer_width[i] = a[1]
        if(layer_width[i] > r2-r1):
            layer_width[i] = r2-r1        
        layer_location[i] = a[2]
        layer_avg[i] = a[3]

    if (tavg_start != 0) and (tavg_end != 0):
        start_idx = velocity.get_index_near_time(tavg_start)
        end_idx = velocity.get_index_near_time(tavg_end)
        pvalues = (tavg_start, tavg_end,
                   layer_amplitude[start_idx:end_idx].mean(),
                   layer_width[start_idx:end_idx].mean(),
                   layer_location[start_idx:end_idx].mean())
        print "Between %g and %gs: amplitude = %g, width=%g, location=%g" % pvalues
            

        

    if(filteroutliers):
        layer_amplitude_masked = filter_outliers(layer_amplitude, 3)
        layer_width_masked = filter_outliers(layer_width, 3)
        layer_location_masked = filter_outliers(layer_location, 3)
        layer_avg_masked = filter_outliers(layer_avg, 3)
        layer_shear_masked = filter_outliers(layer_amplitude/layer_width, 3)
        
        figure()
        subplot(2,2,1)
        plot(velocity.time[layer_width_masked.mask],
             layer_width[layer_width_masked.mask])
        ylabel("Layer width [cm]")
        xlabel("Time [sec]")
        subplot(2,2,2)
        plot(velocity.time[layer_amplitude_masked.mask],
             layer_amplitude[layer_amplitude_masked.mask])
        ylabel("Layer amplitude [rad/sec]")
        xlabel("Time [sec]")
        subplot(2,2,3)
        plot(velocity.time[layer_location_masked.mask],
             layer_location[layer_location_masked.mask])
        ylabel("Radial layer location [cm]")
        xlabel("Time [sec]")
        subplot(2,2,4)
        plot(velocity.time[layer_shear_masked.mask],
             layer_shear_masked.data[layer_shear_masked.mask])
        ylabel("Shear parameter [1/cm*sec]")
        xlabel("Time [sec]")
    else:
        figure()
        subplot(2,2,1)
        plot(velocity.time, layer_width)
        ylabel("Layer width [cm]")
        xlabel("Time [sec]")
        subplot(2,2,2)
        plot(velocity.time, layer_amplitude)
        ylabel("Layer amplitude [rad/sec]")
        xlabel("Time [sec]")
        subplot(2,2,3)
        plot(velocity.time, layer_location)
        ylabel("Radial layer location [cm]")
        xlabel("Time [sec]")
        subplot(2,2,4)
        plot(velocity.time, layer_amplitude/layer_width)
        ylabel("Shear parameter [1/cm*sec]")
        xlabel("Time [sec]")

    if(return_data):
        return {'time': array(velocity.time),
                'layer_amplitude': layer_amplitude, 'layer_width': layer_width,
                'layer_radius': layer_location, 'layer_offset': layer_avg}
    

def eval_shear_layer(velocity, profile_num,
                     time=0, rmin=9, rmax=19, display=0):

    if(time == 1):
        profile_num = velocity.get_index_near_time(profile_num)

    omega = velocity.vtheta[profile_num,:]/velocity.r
    
    if(display==1):
        plot(velocity.r, omega)
    
    avg_ampl_in = omega[velocity.get_index_near_radius(9):
                        velocity.get_index_near_radius(11)].mean()
    avg_ampl_out = omega[velocity.get_index_near_radius(18):
                         velocity.get_index_near_radius(20)].mean()
    avg_ampl = avg_ampl_in-avg_ampl_out

    #Trim the arrays so we're only looking in the vicinity of the shear layer.
    rmin_idx = velocity.get_index_near_radius(rmin)
    rmax_idx = velocity.get_index_near_radius(rmax)

    #a[0] is the amplitude of the tanh, from bottom to top.
    #a[1] is the width, and a[2]
    #is the radial position offset and a[3] is the horizontal offset.

    model_func = lambda a, r:-0.5*a[0]*tanh((1/a[1])*(r-a[2])) + a[3]

    #define the error function

    err = lambda a, r, omega: (model_func(a, r) - omega)

    a0 = [velocity.shot.ICspeed*2*pi/60, 4.0, 13.0,
          0.5*(velocity.shot.ICspeed-velocity.shot.OCspeed)*2*pi/60]
    a, success = scipy.optimize.leastsq(err, a0, 
                                        args=(velocity.r[rmin_idx:rmax_idx],
                                              omega[rmin_idx:rmax_idx]), 
                                        maxfev=10000)

    if(display == 1):
        plot(velocity.r, model_func(a, velocity.r),
             label=r"H: %g, $w_l$: %g, A: %g" % (a[0], a[1], avg_ampl))
    
    return a, avg_ampl


def eval_shear_layer_2(velocity, profile_num,
                       time=0, rmin=10, rmax=18, display=0, knots=8):

    if(time == 1):
        profile_num = velocity.get_index_near_time(profile_num)


    omega = velocity.vtheta[profile_num,:]/velocity.r
    
    if(display==1):
        plot(velocity.r, omega)
    
    avg_ampl_in = omega[velocity.get_index_near_radius(9):
                        velocity.get_index_near_radius(11)].mean()
    avg_ampl_out = omega[velocity.get_index_near_radius(18):
                         velocity.get_index_near_radius(20)].mean()
    avg_ampl = avg_ampl_in-avg_ampl_out

    #Trim the arrays so we're only looking in the vicinity of the shear layer.
    rmin_elm = velocity.get_index_near_radius(rmin)
    rmax_elm = velocity.get_index_near_radius(rmax)
    r = velocity.r[rmin_elm:rmax_elm]
    omega = omega[rmin_elm:rmax_elm]

    #Fit spline with explicit knots
    t = linspace(r[0], r[-1], knots)
    #I think that it includes the end knots automatically, so trim those out
    t=t[1:-1]
    fit = scipy.interpolate.splrep(r, omega, t=t, k=4)


    if(display == 1):
        plot(r, scipy.interpolate.splev(r, fit),
             label="Fit with %i knots" % knots)
        plot(r, scipy.interpolate.splev(r, fit, der=1), label="1st der")
        plot(r, scipy.interpolate.splev(r, fit, der=2), label="2nd der")
             
        legend()

    a = 5
    return a, avg_ampl


def save_avg_profile(velocity, start_num, end_num, savefilename, scale=1,
                     saveideal=0):

    r = velocity.r.copy()
    omega = mean(velocity.vtheta[start_num:end_num, :], axis=0)/r

    plot(r, omega, label="data")
    ylabel(r"$\Omega$ [1/sec]")
    xlabel("r [cm/sec]")


    #Trim out the first few centimeters, and the points
    #after the outer cylinder
    first_index = velocity.get_index_near_radius(11.0)
    last_index = velocity.get_index_near_radius(r2 - 0.2)
    r = r[first_index:last_index]
    omega = omega[first_index:last_index]


    #Now define the point at the inner cylinder by the inner cylinder speed
    r[0] = r1
    omega[0] = rpmtorads(velocity.shot.ICspeed)

    #Now fit a polynomial to this data
    z = polyfit(r, omega, 6)
    p = poly1d(z)

    newr = linspace(r1, r2, 150)
    newomega = p(newr)

    plot(newr, newomega, label="Fitted")

    newomega = newomega*scale

    plot(newr, newomega, label="Fitted and scaled")

    r_c = velocity.shot.idealcouette.r.copy()
    couette= velocity.shot.idealcouette.vtheta*scale/r_c

    plot(r_c, couette, label="Ideal Couette solution")
    legend()
    
    if(saveideal==0):
        savetxt(savefilename, c_[newr, newomega], fmt="%12.6G")
    else:
        print("Saving Ideal Couette profile")
        savetxt(savefilename, c_[r_c, couette], fmt="%12.6G")


def plot_vtheta_on_rt_plane(velocity, mid_time, rin=r1, rout=r2,
                            minvelocity=nan, maxvelocity=nan,
                            nlevels=50, subtract_m0=1):
    '''Simply plot the structure of a nonaxisymmetric vtheta mode,
    without the axisymmetric background.'''
    x, y, v = project_velocity_timeseries_on_rt_plane(velocity, 'vtheta',
                                                      mid_time, numpoints=400,
                                                      rin=rin, rout=rout,
                                                      subtract_m0=subtract_m0,
                                                      plot_rotation=0)
    
    contourf(x, y, v.clip(minvelocity, maxvelocity), nlevels)
    axis('equal')
    xlim(-r2, r2)
    ylim(-r2, r2)
    colorbar()


def plot_vr_on_rt_plane(velocity, mid_time, rin=r1, rout=r2,
                        minvelocity=nan, maxvelocity=nan,
                        nlevels=50, subtract_m0=1):
    '''Simply plot the structure of a nonaxisymmetric vr mode,
    without the axisymmetric background.'''
    x, y, v = project_velocity_timeseries_on_rt_plane(velocity, 'vr',
                                                      mid_time, numpoints=400,
                                                      rin=rin, rout=rout,
                                                      subtract_m0=subtract_m0,
                                                      plot_rotation=0)
    
    contourf(x, y, v.clip(minvelocity, maxvelocity), nlevels)
    axis('equal')
    xlim(-r2, r2)
    ylim(-r2, r2)
    colorbar()


def project_velocity_timeseries_on_rt_plane(velocity, component,
                                            mid_time,
                                            numpoints=400,
                                            rin=r1, rout=r2,
                                            subtract_m0 = 0,
                                            plot_rotation=0):
    '''Projects a timeseries onto the r-\theta plane.

    Measurements should be at the same azimuthal location for most
    accurate results. The m and period for the nonaxisymmetric modes
    are brought along in the Velocity object. You just have to specify
    the mid-point time for the desired projection. If subtract_m0 is
    set, the axisymmetric contribution is subtracted off. The
    plot_rotation angle specifies the number of radians to rotate the
    plot of the mode. Returns an x vector, a y vector, and the
    velocity array'''

    x = linspace(-r2, r2, num=numpoints)
    y = linspace(-r2, r2, num=numpoints)
    v = zeros([x.size, y.size])

    if(component == 'vr'):
        v_component = velocity.vr
    elif(component == 'vtheta'):
        v_component = velocity.vtheta
    elif(component == 'vz'):
        v_component = velocity.vz
    else:
        print "Unrecognized component. Must be 'vr', 'vtheta', or 'vz'."
        return False
    

    #The phase decreases with time, for a function going as
    #exp(k\cdot x - \omega t)
    phase = -2.0*pi*velocity.time/velocity.period

    #Define this function, so we can find the nearest phase measurement
    #that we have for each desired phase.
    #We know that this was created with a linear fit, so it should be easy.
    b = phase[0]
    m = (phase[-1] - b)/(phase.size-1)
    minv = 1.0/m
    def get_index_near_phase(desired_phase):
        return rint((desired_phase-b)*minv)

    #If we want to subtract off the axisymmetric component, take the 
    #average of velocities over the full range of the phases that will
    #be plotted, to be subtracted later.
    if(subtract_m0):
        mean = zeros(velocity.r.size)
        phase_min = -pi*abs(velocity.m) - mid_time*2.0*pi/velocity.period
        phase_max = pi*abs(velocity.m) - mid_time*2.0*pi/velocity.period
        phase_min_idx = get_index_near_phase(phase_min)
        phase_max_idx = get_index_near_phase(phase_max)
        for i in range(0, mean.size):
            #I flip the indices here because phase becomes more negative
            #with time.
            mean[i] = v_component[phase_max_idx:phase_min_idx, i].mean()
    
    #Note what appear to be flipped indices in vr and vt below. This
    #is so the call to contour(x, y, v) displays properly.
    for i in range(0, x.size):
        for j in range(0, y.size):
            r = sqrt(x[i]**2 + y[j]**2)
            if ((r < rin) or (r > rout)):
                v[j][i] = nan
            else:
                #Find the azimuth of a point in the plot. Take into account
                #the desired overall plot rotation. Subtracting here leads
                #to a clockwise plot rotation.
                azimuth = wrap_phase(math.atan2(y[j], x[i]) - plot_rotation)
                desired_phase = (velocity.m*azimuth -
                                 mid_time*2*pi/velocity.period)

                #Just do a nearest-neighbor thing in radius and phase,
                #since these are fairly fine-grained measurements in
                #these dimensions now.
                ridx = velocity.get_index_near_radius(r)
                phaseidx = get_index_near_phase(desired_phase)
                v[j][i] = v_component[phaseidx, ridx]

                #And subtract off the axisymmetric component at that radius,
                #if desired.
                if(subtract_m0):
                    v[j][i] -= mean[ridx]
    
    return x, y, v


def save_vtheta_mode_animation(velocity, filename, start_time=nan,
                               end_time=nan, rin=r1,
                               rout=r2, fps=24, speed=1.0,
                               minvelocity=nan, maxvelocity=nan,
                               numpoints=400, nlevels=50,
                               rotate_with_mode=0):
    '''Create an animation of an azimuthal velocity mode.'''
    tmpfilebase = "/tmp/__tmp%s%s" % (string.ascii_letters[randint(0,51)],
                                      string.ascii_letters[randint(0,51)])
    
    #Make sure that the start and end times are outside of the range
    #that would lead to extrapolation, and hence unexpected results.
    
    min_time = velocity.time[0] + velocity.m*velocity.period/2.0
    max_time = velocity.time[-1] - velocity.m*velocity.period/2.0
    
    if((isnan(start_time)) or (start_time < min_time)
       or (start_time > max_time)):
        start_time = min_time
    
    if((isnan(end_time)) or (end_time < min_time)
       or (end_time > max_time)):
        end_time = max_time
    
    #Calculate the time step from frame to frame, and set up an array
    #of every time that we want to display.
    dt = 1.0*speed/fps
    
    times = arange(start_time, end_time, dt)
    
    #If we want to rotate with the mode, set up an array of the rotation
    #angle corresponding to each time.
    if(rotate_with_mode):
        rot_angles = -(2.0*pi*times/(velocity.m*velocity.period) % (2*pi))
    else:
        rot_angles = zeros(times.size)
    
    
    #Now set everything up for the plots
    fig = figure(figsize=(6, 6), dpi=80)
    subplots_adjust(left=0.0, right=1.0, bottom=0.0, top=1.0)
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(-rout,rout),
                         ylim=(-rout, rout))
    axis('equal')
    
    levels=linspace(minvelocity, maxvelocity, nlevels)
    
    #Now do the transformations of all of the velocity fields, and stick
    #them in a list
    print "Beginning to process frames"
    framefilenames = {}
    for i in range(0,times.size):
        x, y, v = \
        project_velocity_timeseries_on_rt_plane(velocity, 'vtheta',
                                                times[i], numpoints=numpoints,
                                                rin=rin, rout=rout,
                                                subtract_m0=1,
                                                plot_rotation = rot_angles[i])
        #Draw the contour plot
        v.clip(minvelocity, maxvelocity)        
        ax.contourf(x, y, v, levels)
        
        #Set the label text
        ax.text(0.05, 0.95, "t=%0.4gs" % times[i], transform=ax.transAxes)
        
        #For some reason this gets reset when I do cla() on the previous frame
        ax.set_xticks([])
        ax.set_yticks([])
        
        #Save the png file
        framefilenames[i] = "%s%0.4d.png" % (tmpfilebase, i)
        savefig(framefilenames[i])
        
        #And clear for the next round
        ax.cla()
        sys.stdout.write('\x1b[1A\x1b[2K\x1b[J')
        print "%d of %d frames assembled" % (i+1, times.size)
    
    close(fig)
    assemblecmd = ['avconv', '-y', '-r', str(fps), '-b', '1800k', '-i',
                   '%s%%04d.png' % tmpfilebase, filename]
    
    subprocess.check_call(assemblecmd)
    for framefilename in framefilenames:
        os.remove(framefilenames[framefilename])


def save_velocity_mode_animation(velocity, filename, start_time=nan,
                                 end_time=nan, rin=r1,
                                 rout=r2, fps=24, speed=1.0,
                                 minvelocityvt=nan, maxvelocityvt=nan,
                                 minvelocityvr=nan, maxvelocityvr=nan,
                                 numpoints=400, nlevels=50,
                                 rotate_with_mode=0):
    '''Create an animation of the azimuthal and radial velocity modes.'''
    tmpfilebase = "/tmp/__tmp%s%s" % (string.ascii_letters[randint(0,51)],
                                      string.ascii_letters[randint(0,51)])
    
    #Make sure that the start and end times are outside of the range
    #that would lead to extrapolation, and hence unexpected results.
    
    min_time = velocity.time[0] + velocity.m*velocity.period/2.0
    max_time = velocity.time[-1] - velocity.m*velocity.period/2.0
    
    if((isnan(start_time)) or (start_time < min_time)
       or (start_time > max_time)):
        start_time = min_time
    
    if((isnan(end_time)) or (end_time < min_time)
       or (end_time > max_time)):
        end_time = max_time
    
    #Calculate the time step from frame to frame, and set up an array
    #of every time that we want to display.
    dt = 1.0*speed/fps
    
    times = arange(start_time, end_time, dt)
    
    #If we want to rotate with the mode, set up an array of the rotation
    #angle corresponding to each time.
    if(rotate_with_mode):
        rot_angles = -(2.0*pi*times/(velocity.m*velocity.period) % (2*pi))
    else:
        rot_angles = zeros(times.size)
    
    
    #Now set everything up for the plots
    fig = figure(figsize=(12, 6), dpi=80)
    subplots_adjust(left=0.0, right=1.0, bottom=0.0, top=1.0)
    ax1 = fig.add_subplot(1,2,1, autoscale_on=False, xlim=(-rout,rout),
                          ylim=(-rout, rout))
    ax2 = fig.add_subplot(1,2,2, autoscale_on=False, xlim=(-rout,rout),
                          ylim=(-rout, rout))
    ax1.set_aspect('equal')
    ax2.set_aspect('equal')
    
    levelsvt=linspace(minvelocityvt, maxvelocityvt, nlevels)
    levelsvr=linspace(minvelocityvr, maxvelocityvr, nlevels)
    
    #Now do the transformations of all of the velocity fields, and stick
    #them in a list
    print "Beginning to process frames"
    framefilenames = {}
    for i in range(0,times.size):
        x1, y1, vt = \
        project_velocity_timeseries_on_rt_plane(velocity, 'vtheta',
                                                times[i], numpoints=numpoints,
                                                rin=rin, rout=rout,
                                                subtract_m0=1,
                                                plot_rotation = rot_angles[i])
        x2, y2, vr = \
        project_velocity_timeseries_on_rt_plane(velocity, 'vr',
                                                times[i], numpoints=numpoints,
                                                rin=rin, rout=rout,
                                                subtract_m0=1,
                                                plot_rotation = rot_angles[i])

        #Draw the contour plot
        small=0.001
        vt.clip(minvelocityvt, maxvelocityvt)        
        vr.clip(minvelocityvr, maxvelocityvr)
        ax1.contourf(x1, y1, vt, levelsvt, extend='both')
        ax2.contourf(x2, y2, vr, levelsvr, extend='both')
        
        #Set the time text
        ax1.text(0.05, 0.95, "t=%0.4gs" % times[i], transform=ax1.transAxes)
        
        #Set the label text
        ax1.text(0.95, 0.05, r"$v_\theta$", transform=ax1.transAxes)
        ax2.text(0.95, 0.05, r"$v_r$", transform=ax2.transAxes)

        #Save the png file
        framefilenames[i] = "%s%0.4d.png" % (tmpfilebase, i)
        savefig(framefilenames[i])
        
        #And clear for the next round
        ax1.cla()
        ax2.cla()
        sys.stdout.write('\x1b[1A\x1b[2K\x1b[J')
        print "%d of %d frames assembled" % (i+1, times.size)
    
    close(fig)
    assemblecmd = ['avconv', '-y', '-r', str(fps), '-b', '1800k', '-i',
                   '%s%%04d.png' % tmpfilebase, filename]
    
    subprocess.check_call(assemblecmd)
    for framefilename in framefilenames:
        os.remove(framefilenames[framefilename])


def play_channel_velocity_animation(channel, speed=1.0,
                                    saveoutput=0, savefilename=''):
    '''Plays an animation of the raw data from the specified Channel object.
    If saveoutput=1 is specified and a filename is given, an mpeg4 movie
    will be written. Note that this requires having ffmpeg in the path
    somewhere. Consider adding a symlink to avconv if appropriate for your
    system.'''
    dt = (channel.time[1]-channel.time[0])/speed
    
    fig = figure()
    
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(0,channel.depth[-1]),
                         ylim=(-channel.maxvelocity, channel.maxvelocity))
    xlabel("Depth [cm]")
    ylabel("Raw velocity [cm/sec]")
    ax.grid()
    
    line, = ax.plot([], [], '.-', lw=2)
    time_template = 'time = %.1fs'
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
    
    def init():
        line.set_data([], [])
        time_text.set_text('')
        return line, time_text
    
    def draw_raw_profile(i):
        line.set_data(channel.depth, channel.velocity[i,:])
        time_text.set_text(time_template%(channel.time[i]))
        return line, time_text

    if(saveoutput):
        ani = animation.FuncAnimation(fig, draw_raw_profile,
                                      range(0, channel.time.size),
                                      interval = 1, blit=True,
                                      init_func=init)
        ani.save(savefilename, fps=int(1.0/dt))
        #If this fails, keep in mind that the routine expects ffmpeg
        #to be in the path somewhere, but Debian has libav-tools.
        #Consider ln -s /usr/bin/avconv /usr/bin/ffmpeg
    else:
        ani = animation.FuncAnimation(fig, draw_raw_profile,
                                      range(0, channel.time.size),
                                      interval = dt*1000, blit=True,
                                      init_func=init)
        
    #I have no idea why this is here, but the animaion doesn't run without
    #having something to generate an error here?!
    magic_squirrel()


def play_two_component_velocity_animation(velocity, speed=1.0,
                                          rlim=0.0, fps=24.0,
                                          saveoutput=0,
                                          savefilename=''):

    '''Plays an animation of the v_r and v_theta velocity components
    from the specified Velocity object. If saveoutput=1 is specified
    and a filename is given, an mpeg4 movie will be written. Note that
    this requires having ffmpeg in the path somewhere. Consider adding
    a symlink to avconv if appropriate for your system.'''
    dt = (velocity.time[1]-velocity.time[0])/speed
    if (dt < 1.0/fps):
        #The time sampling rate is larger than we actually need for the movie.
        dt = 1.0/fps

    rlim_idx = velocity.get_index_near_radius(rlim)
    
    fig = figure()
    
    ax1 = fig.add_subplot(211, autoscale_on=False, xlim=(r1,r2),
                         ylim=(velocity.vtheta[:,rlim_idx:].min(),
                               velocity.vtheta[:,rlim_idx:].max()))
    ylabel(r"$v_\theta$ [cm/sec]")
    ax2 = fig.add_subplot(212, autoscale_on=False, xlim=(r1,r2),
                          ylim=(velocity.vr[:,rlim_idx:].min(),
                                velocity.vr[:,rlim_idx:].max()))

    ylabel(r"$v_r$ [cm/sec]")
    xlabel("r [cm]")

    ax1.grid()
    ax2.grid()
                          
    
    line1, = ax1.plot([], [], '.-', lw=2)
    line2, = ax2.plot([], [], '.-', lw=2)
    couetteline = ax1.plot(velocity.shot.idealcouette.r,
                           velocity.shot.idealcouette.vtheta,
                           'k-', lw=1)
    time_template = 'time = %.1fs'
    time_text = ax1.text(0.05, 0.9, '', transform=ax1.transAxes)
    
    def init():
        line1.set_data([], [])
        line2.set_data([], [])
        time_text.set_text('')
        return line1, line2, time_text
    
    def draw_velocities(t):
        t_idx = velocity.get_index_near_time(t)
        line1.set_data(velocity.r[rlim_idx:],
                       velocity.vtheta[t_idx,rlim_idx:])
        line2.set_data(velocity.r[rlim_idx:],
                       velocity.vr[t_idx,rlim_idx:])
        time_text.set_text(time_template%(velocity.time[t_idx]))
        return line1, line2, time_text

    if (saveoutput):
        ani = animation.FuncAnimation(fig, draw_velocities,
                                      arange(0, velocity.time[-1], dt),
                                      interval = 1, blit=True,
                                      init_func=init)
        
        ani.save(savefilename, fps=int(1.0/dt))
        #If this fails, keep in mind that the routine expects ffmpeg
        #to be in the path somewhere, but Debian has libav-tools.
        #Consider ln -s /usr/bin/avconv /usr/bin/ffmpeg
    else:
        ani = animation.FuncAnimation(fig, draw_velocities,
                                      arange(0, velocity.time[-1], dt),
                                      interval = dt*1000, blit=True,
                                      init_func=init)
        
    
    #I have no idea why this is here, but the animaion doesn't run without
    #having something to generate an error here?!
    magic_squirrel()
