import read_ultrasound_new as rudv
import UDV_helpers as udvh
import math
import cmath
import scipy
import scipy.interpolate
import subprocess
import os
import shutil
from numpy import *
from pylab import *



def extract_spiral_modes(filename, channel, omega2, start_time, end_time, desiredcells=200, rin=udvh.r1, filter_threshold=1000, background_subtract=0, derotate=0, maxv=10000, minv=-10000, max_diff_mean=10000, levels=0, smoothradial=0):

    if(rudv.read_ultrasound("960.BDD", 1)):
        has_radial=1
    else:
        has_radial=0
    

    #I use the novr option to generate v_t, so that it is less susceptible
    #to noise on the radial transducer, and then run again to get the v_r
    #data separately.
    #If we don't have radial data, just use data_vt for the radial dataset,
    #so v_r will just be 0.
    data_vt = udvh.generate_profiles_alltime_novr(filename, channel, omega2)
    if(has_radial):
        data_vr = udvh.generate_profiles_alltime(filename, channel, omega2)
    else:
        data_vr = data_vt

    phase = linspace(-pi, pi, 100)
    time = data_vt['time']
    vt = data_vt['vt']
    vr = data_vr['vr']
    r = data_vt['r']

    if (derotate != 0):
        derotate_angle = start_time*2.0*pi/(end_time-start_time)
        derotate_angle = fmod(derotate_angle, 2.0*pi)

    for i in range(0, time.size):
        if (time[i] > start_time) & (time[i-1] <= start_time):
            start_pos = i
        elif (time[i] > end_time) & (time[i-1] <= end_time):
            end_pos = i-1

    #Trim the arrays
    time = time[start_pos-10:end_pos+10]
    vt = vt[start_pos-10:end_pos+10,:]
    vr = vr[start_pos-10:end_pos+10,:]

    #Now convert time to phase
    time = time - start_time
    measured_phase = time*2.0*pi/(end_time-start_time) - pi

    resampled_vt = zeros([phase.size, r.size])
    resampled_vr = zeros([phase.size, r.size])

    #Now resample for each element of r
    for i in range(0, r.size):
        #Filter the data to remove spurious measurements
        for k in range (0, 5):
            if (vt[k,i] > maxv):
                vt[k,i] = maxv
            if (vt[k,i] < minv):
                vt[k,i] = minv
        for k in range (5, vt[:,i].size):
            if abs(vt[k,i] - vt[k-5:k-1,i].mean()) > filter_threshold:
                vt[k,i] = vt[k-5:k-1,i].mean()
            if (vt[k,i] > maxv):
                vt[k,i] = maxv
            if (vt[k,i] < minv):
                vt[k,i] = minv

        #Need to offset theta to account for the angular extent of the
        #the measurement chord.
        #Note that there is some weirdness because of the branchcuts of asin.
        vt_theta_offset = pi - udvh.tan_probe_angle*pi/180 - (pi - math.asin(udvh.r2*math.sin(udvh.tan_probe_angle*pi/180)/r[i]))
        vt_temp_measured_phase = measured_phase - vt_theta_offset

        #This is just set by the port plugs where the transducers are
        #installed.  The radial transducer leads the azimuthal transducer
        #by 90 degrees
        vr_theta_offset = -pi/2
        vr_temp_measured_phase = measured_phase - vr_theta_offset

        #Now resample.  Array is reversed, since measurements in experiment
        #are made from larger phase down to smaller phase
        #(features flowing past transducer)
        
        tck_vt = scipy.interpolate.splrep(vt_temp_measured_phase, vt[:,i], s=0)
        resampled_vt[:,i] = (scipy.interpolate.splev(phase, tck_vt, der=0))[::-1]

        tck_vr = scipy.interpolate.splrep(vr_temp_measured_phase, vr[:,i], s=0)
        resampled_vr[:,i] = (scipy.interpolate.splev(phase, tck_vr, der=0))[::-1]
        
        if(background_subtract == 1):
            resampled_vt[:,i] = resampled_vt[:,i]-resampled_vt[:,i].mean()

    if(smoothradial == 1):
        for i in range(0, phase.size):
            tck_sr = scipy.interpolate.splrep(r, resampled_vr[i,:], s=100)
            resampled_vr[i,:] = (scipy.interpolate.splev(r,
                                                         tck_sr, der=0))
        
    #r and phase contain the and theta coordinates
    #vr and vt are arrays, with the first index the phase,
    #and the second index r
    
    data = {'r': r, 'phase': phase, 'vr': resampled_vr, 'vt': resampled_vt}
    return data



def extract_spiral_modes_good(filename, channel, omega2, start_time, end_time, desiredcells=200, rin=udvh.r1, filter_threshold=1000, background_subtract=0, derotate=0, maxv=10000, minv=-10000, max_diff_mean=10000, levels=0, smoothradial=0, smoothingfactor=100):

    oscillation_time = end_time-start_time
    #I use the novr option to generate v_t, so that it is less susceptible
    #to noise on the radial transducer, and then run again to get the v_r
    #data separately.
    r_data = rudv.read_ultrasound(filename, 1)
    t_data = rudv.read_ultrasound(filename, channel)
    
    r, v_r, v_t = udvh.reconstruct_avg_velocities_nonaxisymmetric(r_data, t_data, 
                                                                  100, omega2,
                                                                  oscillation_time)
    vt = zeros([r_data['time'].size, r.size])
    vr = zeros([r_data['time'].size, r.size])

    #Because of the resampling interval that I do in 
    #reconstruct_avg_velocities_nonaxisymmetric, I can't go all the way to the
    #ends of the time interval.
    boundary = int(oscillation_time/(t_data['time'][5]-t_data['time'][4]))/2 + 2
    for i in range(boundary, r_data['time'].size-boundary):
        r, v_r, v_t = udvh.reconstruct_avg_velocities_nonaxisymmetric(r_data, t_data, 
                                                                      i, omega2,
                                                                      oscillation_time)
        vt[i,:] = v_t
        vr[i,:] = v_r


    phase = linspace(-pi, pi, 100)
    time = r_data['time']

    if (derotate != 0):
        derotate_angle = start_time*2.0*pi/(end_time-start_time)
        derotate_angle = fmod(derotate_angle, 2.0*pi)

    for i in range(0, time.size):
        if (time[i] > start_time) & (time[i-1] <= start_time):
            start_pos = i
        elif (time[i] > end_time) & (time[i-1] <= end_time):
            end_pos = i-1
            
    #Trim the arrays
    time = time[start_pos-10:end_pos+10]
    vt = vt[start_pos-10:end_pos+10,:]
    vr = vr[start_pos-10:end_pos+10,:]

    #Now convert time to phase
    time = time - start_time
    measured_phase = time*2.0*pi/(end_time-start_time) - pi

    resampled_vt = zeros([phase.size, r.size])
    resampled_vr = zeros([phase.size, r.size])
    
    #Now resample for each element of r
    for i in range(0, r.size):
        #Filter the data to remove spurious measurements
        for k in range (0, 5):
            if (vt[k,i] > maxv):
                vt[k,i] = maxv
            if (vt[k,i] < minv):
                vt[k,i] = minv
        for k in range (5, vt[:,i].size):
            if abs(vt[k,i] - vt[k-5:k-1,i].mean()) > filter_threshold:
                vt[k,i] = vt[k-5:k-1,i].mean()
            if (vt[k,i] > maxv):
                vt[k,i] = maxv
            if (vt[k,i] < minv):
                vt[k,i] = minv
 
        #Now resample.  Array is reversed, since measurements in experiment
        #are made from larger phase down to smaller phase
        #(features flowing past transducer)
        
        tck_vt = scipy.interpolate.splrep(measured_phase, vt[:,i], s=0)
        resampled_vt[:,i] = (scipy.interpolate.splev(phase, tck_vt, der=0))[::-1]

        tck_vr = scipy.interpolate.splrep(measured_phase, vr[:,i], s=0)
        resampled_vr[:,i] = (scipy.interpolate.splev(phase, tck_vr, der=0))[::-1]
        
        if(background_subtract == 1):
            resampled_vt[:,i] = resampled_vt[:,i]-resampled_vt[:,i].mean()

    if(smoothradial == 1):
        for i in range(0, phase.size):
            tck_sr = scipy.interpolate.splrep(r, resampled_vr[i,:],
                                              s=smoothingfactor)
            resampled_vr[i,:] = (scipy.interpolate.splev(r,
                                                         tck_sr, der=0))
        
    #r and phase contain the and theta coordinates
    #vr and vt are arrays, with the first index the phase,
    #and the second index r
    
    data = {'r': r, 'phase': phase, 'vr': resampled_vr, 'vt': resampled_vt}
    return data

def find_vr_no_vz(data):
    r = data['r']
    phase = data['phase']
    vt = data['vt']

    vr = zeros(vt.shape)
    vtderiv = zeros(vt.shape)

    for i in range(1, r.size):
        for k in range(1, phase.size):
            #theta term in del \dot v = 0: (1/r)(d/d\theta)(v_theta)
            vtderiv[k,i] = (1.0/r[i])*(vt[k,i]-vt[k-1,i])/(phase[k]-phase[k-1])

    for i in range(1, r.size):
        for k in range(1, phase.size):
            for j in range(i,r.size):
                vr[k,i] = vr[k,i] + (1.0/r[i])*(r[j]-r[j-1])*r[j]*vtderiv[k,j]

    returneddata = {'r': r, 'phase': phase, 'vr': vr, 'vt': vt}
    return returneddata



def generate_derivative_modes(data):
    r = data['r']
    phase = data['phase']
    vr = data['vr']
    vt = data['vt']

    vrderiv = zeros(vr.shape)
    vtderiv = zeros(vr.shape)
    vzderiv = zeros(vr.shape)

    for i in range(1, r.size):
        for k in range(1, phase.size):
            #r term in del \dot v = 0: (1/r)(d/dr)(r*v_r)
            vrderiv[k,i] = (1.0/r[i])*(r[i]*vr[k,i]
                                       - r[i-1]*vr[k,i-1])/(r[i]-r[i-1])
            #theta term in del \dot v = 0: (1/r)(d/d\theta)(v_theta)
            vtderiv[k,i] = (1.0/r[i])*(vt[k,i]-vt[k-1,i])/(phase[k]-phase[k-1])
            #vz term in del dot v = 0: (d/dz)v_z
            #Here set by \nabla\cdot\vec{v} = 0
            vzderiv[k,i] = -vrderiv[k,i] - vtderiv[k,i]

    returndata = {'r': r, 'phase': phase, 'vrderiv': vrderiv,
                  'vtderiv': vtderiv, 'vzderiv': vzderiv}
    return returndata
    

def plot_spiral_quantity(r, phase, quantity, desiredcells=200, rin=udvh.r1,
                         levels=0, max_diff_mean=10000, background_subtract=0,
                         titlestring='', showcolorbar=1, noaxisequalize=0,
                         renormalize=1, labelstring=""):

    #Need to do this resampling
    xi = linspace(-udvh.r2, udvh.r2, desiredcells)
    yi = linspace(-udvh.r2, udvh.r2, desiredcells)
    zi = zeros((desiredcells, desiredcells))

    i = 0
    for x in xi:
        k = 0
        for y in yi:
            r_temp = math.sqrt(x**2 + y**2)
            if ((r_temp > rin) and (r_temp < udvh.r2)):
                element_r = udvh.find_element_r(r, r_temp)

                angle = math.atan2(y,x)
                #if (derotate !=0):
                    ###First put the measured angle on a 0 to 2pi scale
                    #angle = angle + pi
                    ###Now add the derotation angle
                    #angle = angle + derotate_angle
                    #angle = math.fmod(angle, 2.0*pi)
                    ###And now back to the -pi to pi scale
                    #angle = angle - pi

                
                element_phase = 0
                for n in range(0, phase.size):
                    if (phase[n] > angle) & (phase[n-1] < angle):
                        element_phase = n
                        
                zi[k,i] = quantity[element_phase, element_r]
                if ((background_subtract == 1) & (zi[k,i] > max_diff_mean)):
                    zi[k,i] = max_diff_mean
                if ((background_subtract == 1) & (zi[k,i] < -max_diff_mean)):
                    zi[k,i] = -max_diff_mean
            else:
                zi[k,i] = -1e12

            k = k + 1
        i = i + 1
        print i

    #Use numpy's masked values to mask the nans
    zi_masked = ma.masked_values(zi, -1e12)

    zi_masked = zi_masked/renormalize

    if(isscalar(levels) == 1):
        C = contourf(xi, yi, zi_masked, 50)
    else:
        C = contourf(xi, yi, zi_masked, levels)

    xlim(-udvh.r2, udvh.r2)
    ylim(-udvh.r2, udvh.r2)
    if(noaxisequalize==0):
        axes().set_aspect('equal')
    
    xlabel("x [cm]")
    ylabel("y [cm]")
    title(titlestring)
    if(showcolorbar):
        bar_instance = colorbar(format='%.2f', pad=0.01, fraction=0.09)
        #if(background_subtract == 0):
        #    matplotlib.colorbar.ColorbarBase.set_label(bar_instance, r"$v_{\theta}$ [cm/sec]")
        #if(background_subtract == 1):
        #    matplotlib.colorbar.ColorbarBase.set_label(bar_instance, r"$v_{\theta} - \bar{v_{\theta}}$ [cm/sec]")

    if(showcolorbar):
        matplotlib.colorbar.ColorbarBase.set_label(bar_instance, labelstring)
        return C.levels
    else:
        return 0
