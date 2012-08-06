import read_magnetics
import scipy
from matplotlib import pyplot
import numpy

def get_timeseries(shot_dir, channel, t_init=0.0, t_final=1e4):
    t = read_magnetics.read_time(shot_dir)
    signal = read_magnetics.read_channel(shot_dir, channel)

    #find positions of start time and end time
    pos_init = 0
    pos_final = t.size
    for i in range(0, t.size):
        if (t[i] > t_init) & (t[i-1] <= t_init):
            pos_init = i
        elif (t[i] > t_final) & (t[i-1] <= t_final):
            pos_final = i-1

    #Now trim the arrays
    trimmed_t = t[pos_init:pos_final]
    trimmed_signal = signal[pos_init:pos_final]

    return trimmed_t, trimmed_signal


def get_spectrum(shot_dir, channel, t_init=0.0, t_final=1e4):

    trimmed_t, trimmed_signal = get_timeseries(shot_dir, channel,
                                               t_init, t_final)
    
    samples = trimmed_t.size
    stepsize = trimmed_t[1] - trimmed_t[0]

    freq = numpy.fft.fftfreq(samples, d=stepsize)
    F = (scipy.fft(trimmed_signal))
    return freq, F


def plot_power_spectrum(shot_dir, channel, t_init=0.0, t_final=1e4,
                        freq_correct=0, labelstring="", logscale=1):

    freq, F = get_spectrum(shot_dir, channel, t_init, t_final)
    power = F*F.conjugate()
    fig = pyplot.figure()
    ax = fig.add_subplot(1,1,1)
    
    if(freq_correct==0):
        if(logscale==1):
            ax.semilogy(freq, power, label=labelstring)
        else:
            ax.plot(freq, power, label=labelstring)
        ax.set_ylabel("Power")
        ax.set_xlabel("Frequency [Hz]")
    if(freq_correct==1):
        if(logscale==1):
            ax.semilogy(freq, power/(freq*freq), label=labelstring)
        else:
            ax.plot(freq, power/(freq*freq), label=labelstring)
        ax.set_ylabel("Power/freq^2")
        ax.set_xlabel("Frequency [Hz]")


def filter_spectrum(shot_dir, channel, t_init=0.0, t_final=1e4,
                    f_min=0.0, f_max=1000):

    freq, F = get_spectrum(shot_dir, channel, t_init, t_final)

    for i in range(freq.size):
        if (abs(freq[i]) <= f_min) or (abs(freq[i]) >= f_max):
            F[i] = 0.0

    return freq, F


def filter_time_signal(shot_dir, channel, t_init=0.0, t_final=1e4,
                       f_min=0.0, f_max=1000, freq_correct=0):
    
    t, signal_orig = get_timeseries(shot_dir, channel, t_init, t_final)

    freq, F = filter_spectrum(shot_dir, channel, t_init, t_final, f_min, f_max)
    #Do frequency correction if required
    if(freq_correct==1):
        #This is to avoid blowing up at zero frequency, which leads to
        #NaNs in the reconstructed timeseries
        #plot(freq, F.real)
        F[1:] = F[1:]/abs(freq[1:])
        #plot(freq, F.real)
        
    #reconstruct signal
    signal_filt = numpy.fft.ifft(F)

    return t, signal_filt
    
