"""Module for calculating the speed of sound with the UDV diagnostic.

Measurements should be with the UDV diagnostic recording the echo, and
with an identical presumed speed of sound provided to the UDV control
software for all the shots. The measurements should be recorded in a
list of files each separated by 1mm of displacement. The first and
last of those files should be fed to find_speed_of_sound, which will
process each file to find the location of the echo and will perform
the linear regression to determine the speed of sound."""

import numpy
from pylab import *
import math
import cmath
import scipy
import scipy.interpolate
import scipy.stats
import read_ultrasound_new
import glob

def trim_leading_edge(data):
    velocity = data['velocity'][:,20:]
    echo = data['echo'][:,20:]
    depth = data['depth'][20:]
    time = data['time']

    trimmed_data = {'velocity': velocity, 'echo': echo,
                    'depth': depth, 'time': time}
    return trimmed_data

#Assume that the peak of interest is the tallest one
def normalize_echo(echo):
    """Normalizes an echo signal so that the maximum echo is 1.0."""
    max_value = echo.max()

    normalized_echo = echo/max_value

    return normalized_echo


def find_half_height(depth, echo):
    """Takes in depth and echo vectors. Interpolates the echo onto a finer
    grid, normalizes the echo so the maximum echo is 1.0, and then returns
    the half-height crossing position."""
    tck = scipy.interpolate.splrep(depth,echo,s=0)

    finer_depth = arange(depth[0], depth[-1], (depth[-1]-depth[0])/2048)

    finer_echo = scipy.interpolate.splev(finer_depth,tck,der=0)

    normalized_echo = normalize_echo(finer_echo)
    
    #Now find half-height crossing

    i = 0
    for d in finer_depth:
        if ((normalized_echo[i] < 0.5) and (normalized_echo[i+1] > 0.5)):
            #linearly interpolate
            m = (normalized_echo[i+1]-normalized_echo[i])/(finer_depth[i+1]-
                                                           finer_depth[i])
            dx = (normalized_echo[i+1] - normalized_echo[i])/m
            crossing_depth = finer_depth[i] + dx
            print "crossing found at", crossing_depth
            break
        i = i + 1

    return crossing_depth


def find_echo_location(file):
    """A wrapper for find_half_height."""
    data = read_ultrasound_new.read_ultrasound(file, 1)
    trimmed_data = trim_leading_edge(data)
    crossing_depth = find_half_height(trimmed_data['depth'],
                                      trimmed_data['echo'][5])
    return crossing_depth


def get_echo_locations_list(minfile, maxfile):
    """Given the first and list files of a list of files where the transducer
    is progressively moved 1mm toward a target, find the displacement
    (assumed from the file order), and the measured depth."""

    #See if we've specified a different directory than the current one
    if (minfile.count('/') > 0):
        #If so, make the file string using the specified directory
        filestring = minfile.rsplit('/', 1)[0] + "/*.BDD"
    else:
        #Otherwise, we're just sticking to the current working directory.
        filestring = "*.BDD"

    allfiles = glob.glob(filestring)
    files = []
    allfiles.sort()
    for file in allfiles:
        if (file >= minfile) and (file <= maxfile):
            files.append(file)

    numfiles = len(files)    
    #Find the displacements in centimeters.
    displacement = -0.1*np.arange(numfiles)
    
    measured_depth = np.zeros(numfiles)
    
    for i in range(0, displacement.size):
        measured_depth[i] = find_echo_location(files[i])
        
    measured_depth = measured_depth - measured_depth[0]

    return (-displacement, -measured_depth)



def find_speed_of_sound(minfile, maxfile, plot_fit=0):
    """Takes in the first and last files of a group of files that are
    separated by 1mm in displacement from an object. All measurements should
    have been taken with the same assumed c_s in the control software. Finds
    the location of the echo peak, and performs a linear regression to
    determine the speed of sound."""
    
    (displacement, measured_depth) = get_echo_locations_list(minfile, maxfile)
    #Get the speed of sound that was used for the measurements. Note that
    #the speed of sound stored in the UDV files is in m/s, so we must
    #convert this.
    fid = open(minfile, mode='rb')
    cs_orig = 100.0*read_ultrasound_new.udv_params(fid, 1, 19)
    print cs_orig
    fid.close()
    
    #Now find the delay times that would have led to those measured
    #echo depths. 
    
    deltat = 2.0*measured_depth/cs_orig
    
    #Fit a line y = m*x + b to this
    #y = deltat, x = displacement
    (m, b, r, two_tailed, err) = scipy.stats.linregress(displacement, deltat)

    #Because we expect that deltat = 2.0*displacement/cs + b,
    #this means cs = 2.0/m
    cs = 2.0/m
    
    if(plot_fit):
        fit = m*displacement + b
    
        title("Speed of sound measurement")
        xlabel("Displacement of transducer [cm]")
        ylabel("Additional echo delay [s]")
        labelstring = "c_s = %g cm/s, r= %g" % (cs, r)
        
        plot(displacement, deltat, '.')
        plot(displacement, fit, label=labelstring)
        legend(loc='upper left')
        #Necessary to make the floating point numbers on the y-axis
        #render correctly.
        gca().yaxis.set_major_formatter(FormatStrFormatter("%g"))
    
    results = {'displacement': displacement, 'measured_depth': measured_depth,
               'deltat': deltat, 'm': m, 'b': b, 'cs': cs, 'r': r}
    return results
