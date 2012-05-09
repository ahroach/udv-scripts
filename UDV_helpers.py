import read_ultrasound_new as rudv
import math
import cmath
import scipy
import scipy.interpolate
import subprocess
import os
import shutil
import glob
import matplotlib.animation as animation
from numpy import *
from pylab import *
import shot_params as sp
import shot_db_ops as sdo

r1 = 7.06 #Position of IC in cm
r2 = 20.30 #Position of OC in cm
radial_probe_offset = 0.72 #Distance from transducer face to OC wall in cm
tan_probe_offset = 0.95 #Transducer face to OC wall in cm
tan_probe_offset_675 = 0.41
tan_probe_offset_676 = 0.53
tan_probe_angle = 20.3 #Angle of tangential probe to radial
global_beta=0
radial_probe_angle= -0.75

rpmtorads = lambda x: x*2.0*pi/60.0
degstorads = lambda x: x*pi/180.0

class Shot:
    def __init__(self, shot_num):
        '''Creates a new Shot object, looks up and adds shot parameters
        to the object, and runs add_channel_data() for all channels'''
        self.number = shot_num
        self.filename = str(shot_num) + '.BDD'
        self.shot_length = sp.shot_params[shot_num]['shot_length']
        self.ICspeed = sp.shot_params[shot_num]['ICspeed']
        self.IRspeed = sp.shot_params[shot_num]['IRspeed']
        self.ORspeed = sp.shot_params[shot_num]['ORspeed']
        self.OCspeed = sp.shot_params[shot_num]['OCspeed']
        self.current = sp.shot_params[shot_num]['current']
        self.field_delay = sp.shot_params[shot_num]['field_delay']
        self.field_length = sp.shot_params[shot_num]['t_field']
        self.udv_delay = sp.shot_params[shot_num]['udv_delay']
        self.channels_used = sp.shot_params[shot_num]['channels']
        self.channels = {}
        self.velocities = []
        self.idealcouette = CouetteProfile(self)

    def add_all_channels(self):
        '''Adds all available channels to the Shot object'''
        for channel in self.channels_used:
            add_channel(channel)
    
    def add_channel(self, channel_num):
        '''Adds and returns a ChannelData object corresponding to channel_num
        for this Shot.'''
        if(not(self.channels_used.__contains__(channel_num))):
            print "Error: Shot "+str(self.number)+" doesn't use channel "+str(channel_num)
            return False
        
        self.channels[channel_num] = ChannelData(self, channel_num)
        return self.channels[channel_num]
    
    def get_channel(self, channel_num):
        '''Returns a ChannelData object corresponding to channel_num. Should
        be equivalent to Shot.channels[channel_num], with the only difference
        being that this routine will add the channel data if it has not
        already been added to the shot.'''
        #Check to see if we've added this channel data before, and, if so,
        #return it
        for key in self.channels.keys():
            if self.channels[key].channel == channel_num:
                return self.channels[key]
        #Otherwise add the channel and return that.
        return self.add_channel(channel_num)

    def add_velocity(self, channel_nums):
        '''Adds and returns a Velocity object produced using channel_nums
        for this Shot.'''
        channel_nums = self.sanitize_channel_nums_for_velocities(channel_nums)
        
        #Make sure we actually have all of these channels.
        for channel_num in channel_nums:
            if(not(self.channels_used.__contains__(channel_num))):
                print "Error: Shot "+str(self.number)+" doesn't use channel "+str(channel_num)
                return False

        
        self.velocities.append(Velocity(self, channel_nums))
        return self.velocities[-1]
    
    def get_velocity(self, channel_nums):
        '''Returns a Velocity object produced using the specified
        channel_nums for this Shot.'''
        channel_nums = self.sanitize_channel_nums_for_velocities(channel_nums)

        #Check to see if we've processed this velocity data before, and, if so,
        #return it

        for idx in range(0, self.velocities.__len__()):
            #First make a list of the channel numbers from all of the
            #progenitor ChannelData objects for this Velocity object
            progenitor_list = list()
            for progenitor in self.velocities[idx].progenitors:
                progenitor_list.append(progenitor.channel)

            #Now check to see if these channels match the channel_nums, and,
            #if so, return that.
            progenitor_list.sort()
            if progenitor_list == channel_nums:
                return self.velocities[idx]

        #Otherwise add this new velocity set and return that.
        return self.add_velocity(channel_nums)

    def sanitize_channel_nums_for_velocities(self, channel_nums):
        '''Makes sure we have the channel_nums as a sorted list, even if
        we get weird things on input'''
        if(type(channel_nums) is int):
            channel = channel_nums
            channel_nums = list()
            channel_nums.append(channel)
        elif(not(type(channel_nums) is list)):
            channels = channel_nums
            channel_nums = list(channels)
        
        channel_nums.sort()
        return channel_nums


    def list_params(self):
        '''Lists information about the shot'''
        print "Shot number: %d" % self.number
        print "Component speeds: {%d, %d, %d, %d RPM}" % (self.ICspeed,
                                                                  self.IRspeed,
                                                                  self.ORspeed,
                                                                  self.OCspeed)
        print "Shot length: %ds, UDV Delay: %ds" % (self.shot_length,
                                                        self.udv_delay)
        print "Field delay: %ds, Field length: %ds" % (self.field_delay,
                                                           self.field_length)
        field = self.current*2.8669
        print "%dA applied current -> %dG" % (self.current,
                                                  field)
        
    
class ChannelData:
    def __init__(self, shot, channel_num):
        '''Initialize a ChannelData object. Note that shot is a Shot object,
        which must be created before. Ideally, this function is only run
        from Shot.add_channel_data(), and was most likely already run
        from Shot.__init__().'''
        if(not(shot.channels_used.__contains__(channel_num))):
            print "Error: Shot "+str(shot_num)+" doesn't use channel "+str(channel_num)
            return False

        self.shot = shot
        params = sp.shot_params[shot.number]
        
        if(params.__contains__('trouble_flag')):
            print "Warning: Shot "+str(shot_num)+" has trouble_flag set. Check notebook to see why."


        
        data = rudv.read_ultrasound(shot.filename, channel_num)

        self.velocity = data['velocity']
        self.echo = data['echo']
        self.energy = data['energy']
        self.depth = data['depth']
        self.time = data['time']
        self.channel = data['channel']
        self.maxvelocity = data['maxvelocity']
        
        
        channel_idx = params['channels'].index(channel_num)
        
        self.A = params['As'][channel_idx]
        self.B = params['Bs'][channel_idx]
        self.offset = params['offsets'][channel_idx]
        self.port = params['ports'][channel_idx]
        
        self.time_points = self.time.size
        self.spatial_points = self.depth.size
        self.unwrap_velocity()
        self.calculate_radius()
        self.calculate_azimuth()
        self.calculate_height()

    def unwrap_velocity(self, threshold=1.5):
        '''Adds the unwrapped velocity to the channel information, done using
        the specified threshold.'''
        #Add the unwrapped velocity to the channel information
        self.unwrapped_velocity = zeros(self.velocity.shape)
        self.unwrap_threshold = threshold
    
        maxvelocity = self.maxvelocity
    
        for j in range(0, self.time_points):
            wraps = zeros(self.spatial_points)
            for i in range(10, self.spatial_points):
                if (self.velocity[j, i] -
                    self.velocity[j, i-1]) < -threshold*maxvelocity:
                    wraps[i] = wraps[i-1] + 1
                elif (self.velocity[j, i] -
                      self.velocity[j, i-1]) > threshold*maxvelocity:
                    wraps[i] = wraps[i-1] -1
                else:
                    wraps[i] = wraps[i-1]
            v_correction = wraps*2.0*maxvelocity
            self.unwrapped_velocity[j,:] = self.velocity[j,:] + v_correction
    
    def calculate_radius(self):
        '''Calculate the radial location of the measured points'''
        d = self.depth - self.offset
        self.r = zeros(self.depth.size)

        sinA = sin(degstorads(self.A))
        cosA = cos(degstorads(self.A))
        sinB = sin(degstorads(self.B))
        for i in range(0,d.size):
            self.r[i] = sqrt((d[i]*sinA*sinB)**2 + (r2 - d[i]*cosA)**2)
    
    def calculate_azimuth(self):
        '''Calculate the azimuthal location of the measured points'''
        d = self.depth - self.offset
        self.azimuth = zeros(self.depth.size)
        azimuthoffset = sp.ports[self.port]['theta']

        sinA = sin(degstorads(self.A))
        cosA = cos(degstorads(self.A))
        sinB = sin(degstorads(self.B))
        
        for i in range(0,d.size):
            self.azimuth[i] = arcsin(d[i]*sinA*sinB/
                                     sqrt((d[i]*sinA*sinB)**2 +
                                          (r2 - d[i]*cosA)**2))
            self.azimuth[i] = wrap_phase(self.azimuth[i] + azimuthoffset)    
    
    def calculate_height(self):
        '''Calculate the height of the measured points'''
        d = self.depth - self.offset
        self.z = zeros(self.depth.size)
        
        zoffset = sp.ports[self.port]['z']
        
        sinA = sin(degstorads(self.A))
        cosA = cos(degstorads(self.A))
        sinB = sin(degstorads(self.B))
        cosB = cos(degstorads(self.B))
        
        for i in range(0,d.size):
            self.z[i] = d[i]*sinA*cosB + zoffset

    def get_index_after_time(self, time):
        '''Find the index in the time_array of the first element after
        the specified time'''
        idx = nan
        temp_idx = self.time_points - 1
        while(temp_idx >=0):
            if self.time[temp_idx] > time:
                idx = temp_idx
            temp_idx = temp_idx - 1
        return idx

    def list_params(self):
        '''Lists information about the channel'''
        print "Shot: %d, Channel: %d, Port: %d" % (self.shot.number,
                                                   self.channel,
                                                   self.port)
        print "A = %g, B = %g, offset = %gmm" % (self.A,
                                                 self.B,
                                                 self.offset)
        print "UDV delay: %ds, Data-taking time: %gs" % (self.shot.udv_delay,
                                                         self.time[-1])


class Velocity():
    def __init__(self, shot, channel_nums):
        self.shot = shot
        if size(channel_nums) == 0:
            print "Error: 0 channels presented to Velocity.__init__()."
            return None
        elif size(channel_nums) == 1:
            self.generate_velocity_one_transducer(channel_nums)
        elif size(channel_nums) == 2:
            self.generate_velocity_two_transducers(channel_nums)
        elif size(channel_nums) == 3:
            self.generate_velocity_three_transducers(channel_nums)
        else:
            print "Error: Don't know how to generate velocity from %d measurements" % size(channel_nums)
            return None

    def generate_velocity_one_transducer(self, channel_num):
        '''Generate velocity from a single transducer. If it is purely radial
        or purely vertical, a purely radial or vertical velocity is created.
        Otherwise, the velocity is assumed to be in the azimuthal direction,
        and the appropriate angle corrections are applied to the velocity.'''
        self.progenitors = []
        self.progenitors.append(self.shot.get_channel(channel_num[0]))

        channel = self.progenitors[0]
        self.time = channel.time
        self.r = channel.r
        self.azimuth = channel.azimuth
        self.z = channel.z
        

        if (((channel.B == 0) or (channel.B == -180) or (channel.B == 180)) and
            (channel.A == 90)):
            #This thing is just pointed vertically, so just use the unwrapped
            #velocity and the the position from the original channel
            self.vr = ones(channel.unwrapped_velocity.shape)*nan
            self.vtheta = ones(channel.unwrapped_velocity.shape)*nan
            self.vz = channel.unwrapped_velocity/cos(degstorads(channel.B))
        elif (channel.A == 0):
            #In the unlikely event that we got this dead on in the radial
            #direction
            self.vr = -1.0*channel.unwrapped_velocity
            self.vtheta = ones(channel.unwrapped_velocity.shape)*nan
            self.vz = ones(channel.unwrapped_velocity.shape)*nan
        else:
            #Otherwise, just assume the velocity is in the azimuthal direction
            self.vr = ones(channel.unwrapped_velocity.shape)*nan
            self.vtheta = zeros(channel.unwrapped_velocity.shape)
            self.vz = ones(channel.unwrapped_velocity.shape)*nan

            sinA = sin(degstorads(channel.A))
            cosA = cos(degstorads(channel.A))
            sinB = sin(degstorads(channel.B))
            cosB = cos(degstorads(channel.B))
            d = channel.depth
        
            anglefactor = zeros(self.r.size)
            
            for i in range(0, self.r.size):
                anglefactor[i] = (sqrt(1-sinA**2*cosB**2)*
                                  sin(math.atan(sinA*sinB/cosA) +
                                      math.asin(d[i]*sinA*sinB/self.r[i])))
            
            #Now iterate over the entire dataset
            for i in range(0, self.time.size):
                self.vtheta[i,:] = ((channel.unwrapped_velocity[i,:]/
                                     anglefactor) +
                                    self.r*rpmtorads(self.shot.OCspeed))


    def generate_velocity_two_transducers(self, channel_num):
        '''Generate velocity from two transducers. Currently assumes we are
           just getting contributions from v_r and v_theta'''
        self.progenitors = []
        self.progenitors.append(self.shot.get_channel(channel_num[0]))
        self.progenitors.append(self.shot.get_channel(channel_num[1]))

        ch1 = self.progenitors[0]
        ch2 = self.progenitors[1]

        ch1_last_idx = ch1.r.argmin()
        ch2_last_idx = ch2.r.argmin()

        #First find out has the least radial penetration, and use that 
        #Also reverse the array, so smaller radii are first.
        if (ch1.r.min() > ch2.r.min()):
            use_ch1_r = True
            self.r = ch1.r[0:ch1_last_idx][::-1]
        else:
            use_ch1_r = False
            self.r = ch2.r[0:ch2_last_idx][::-1]

        self.time = ch1.time
        #With two transducers, it's less clear what the z and azimuth
        #coordinates should be. Just make them nans.
        self.z = ones(self.r.size)*nan
        self.azimuth = ones(self.r.size)*nan

        
        self.vr = zeros((self.time.size, self.r.size))
        self.vtheta = zeros((self.time.size, self.r.size))
        self.vz = ones((self.time.size, self.r.size))*nan

        #Set up some temporary arrays to store the velocities
        ch1_v = zeros((self.time.size, self.r.size))
        ch2_v = zeros((self.time.size, self.r.size))

        #Now interpolate and resample the velocity onto the same radial grid
        #Again keeping in mind that we need to reverse these arrays as inputs
        #into the interpolation routines, so that smaller measured radii
        #are first. Now everything in ch1_v, ch2_v and self.r will
        #be stored from smaller radii to larger.
        for i in range (0, self.time.size):
            if(use_ch1_r):
                ch1_v[i,:] = ch1.unwrapped_velocity[i,0:ch1_last_idx][::-1]
                tck = scipy.interpolate.splrep(ch2.r[0:ch2_last_idx][::-1],
                                               ch2.unwrapped_velocity[i,0:ch2_last_idx][::-1],
                                               s=0)
                ch2_v[i,:] = scipy.interpolate.splev(self.r, tck, der=0)
            else:
                ch2_v[i,:] = ch2.unwrapped_velocity[i,0:ch2_last_idx][::-1]
                tck = scipy.interpolate.splrep(ch1.r[0:ch1_last_idx][::-1],
                                               ch1.unwrapped_velocity[i,0:ch1_last_idx][::-1],
                                               s=0)
                ch1_v[i,:] = scipy.interpolate.splev(self.r, tck, der=0)

        #Now define a matrix for doing the transformations.
        #v = T \cdot v_measured
        #[ v1 ] = [A11 A12][ v_r ]
        #[ v2 ]   [A21 A22][ v_t ]
        #where T_{0,0} = -\sqrt{1 - \sin^2 A_1 \cos^2 B_1}\cos\xi_1
        #  and T_{0,1} = \sqrt{1 - \sin^2 A_1 \cos^2 B_1}\sin\xi_1
        #  and T_{1,0} = -\sqrt{1 - \sin^2 A_2 \cos^2 B_2}\cos\xi_2
        #  and T_{1,1} = \sqrt{1 - \sin^2 A_2 \cos^2 B_2}\sin\xi_2
        #  \xi = \theta + \alpha, where \alpha = \arctan(\tan A \sin B)
        #  \theta = \arcsin\left[\frac{d\sin A \sin B}{r} \right]
        #  and d = \frac{r_2 cos \A - sqrt{r^2(\sin^2 A \sin ^2 B + \cos ^2 A)
        #  - r_2^2 \sin^2 A \sin^2 B}}{\sin^2 A \sin ^2 B + \cos^2 A}

        #Define some trigonometric quantities that I need
        sinA1 = sin(degstorads(ch1.A))
        cosA1 = cos(degstorads(ch1.A))
        sinB1 = sin(degstorads(ch1.B))
        cosB1 = cos(degstorads(ch1.B))
        sinA2 = sin(degstorads(ch2.A))
        cosA2 = cos(degstorads(ch2.A))
        sinB2 = sin(degstorads(ch2.B))
        cosB2 = cos(degstorads(ch2.B))

        alpha1 = arctan(sinA1*sinB1/cosA1)
        alpha2 = arctan(sinA2*sinB2/cosA2)

        T = zeros([2,2])

        for i in range(0, self.r.size):
            r = self.r[i]
            d1 = ((r2*cosA1 - sqrt(r**2*(sinA1**2*sinB1**2 + cosA1**2) -
                                   r2**2*sinA1**2*sinB1**2)) /
                  (sinA1**2*sinB1**2 + cosA1**2))
            d2 = ((r2*cosA2 - sqrt(r**2*(sinA2**2*sinB2**2 + cosA2**2) -
                                   r2**2*sinA2**2*sinB2**2)) /
                  (sinA2**2*sinB2**2 + cosA2**2))
            theta1 = arcsin(d1*sinA1*sinB1/r)
            theta2 = arcsin(d2*sinA2*sinB2/r)
            xi1 = alpha1 + theta1
            xi2 = alpha2 + theta2

            T[0,0] = -sqrt(1 - sinA1**2*cosB1**2)*cos(xi1)
            T[0,1] = sqrt(1 - sinA1**2*cosB1**2)*sin(xi1)
            T[1,0] = -sqrt(1 - sinA2**2*cosB2**2)*cos(xi2)
            T[1,1] = sqrt(1 - sinA2**2*cosB2**2)*sin(xi2)
            Tinv = linalg.inv(T)
            for j in range(0, self.time.size):
                [self.vr[j,i], self.vtheta[j,i]] = dot(Tinv,
                                                       [ch1_v[j,i],
                                                       ch2_v[j,i]])
                #Now add the azimuthal velocity offset.
                self.vtheta[j,i] = (self.vtheta[j,i] +
                                    rpmtorads(self.shot.OCspeed)*r)
                  
    
    def list_progenitors(self):
        num_progenitors = size(self.progenitors)
        print "Derived from %d progenitor(s)" % num_progenitors
        for i in range(0, num_progenitors):
            progenitor = self.progenitors[i]
            print "%d: A=%g, B=%g, port=%d" % (i,
                                               progenitor.A,
                                               progenitor.B,
                                               progenitor.port)

class CouetteProfile():
    def __init__(self, shot):
        self.shot = shot
        self.r = linspace(r1, r2, 200)
        self.vtheta = zeros(self.r.size)
        v1 = rpmtorads(shot.ICspeed)*r1
        v2 = rpmtorads(shot.OCspeed)*r2
        a = (v1*r1 - v2*r2)/(r1**2 - r2**2)
        b = (v1*r1 - a*r1**2)

        for i in range(0, self.vtheta.size):
            self.vtheta[i] = a*self.r[i] + b/self.r[i]

    
def wrap_phase(angle):
    while (angle > pi):
        angle = angle - 2.0*pi

    while (angle < -pi):
        angle = angle + 2.0*pi

    return angle

def correct_vtan(usound_data, profile, omega2):
    omega2 = omega2*2*pi/60 #Convert omega2 in RPM to omega2 in rad/sec

    if usound_data['channel'] != 2:
        print "Not a tangential measurement.  Not correcting."
        return profile

    cosangle = cos(pi*tan_probe_angle/180)
    alpha = zeros(usound_data['depth'].size)

    for i in range(0, alpha.size):
        d = usound_data['depth'][i] - tan_probe_offset
        alpha[i] = arccos((d - r2*cosangle)/(sqrt(d**2 - 2*r2*d*cosangle + r2**2)))

    v_corrected = zeros(usound_data['depth'].shape)
    r = calculate_radius(usound_data)

    for i in range(0,alpha.size):
        scalefactor = 1.0/sin(alpha[i])
        offset = omega2*r[i]
        v_corrected[i] = scalefactor*profile[i]  + offset
        
    return v_corrected



def show_logs(start_file, end_file):
    allfiles = glob.glob('*.BDD')
    files=[]
    for file in allfiles:
        if (file >= start_file) and (file <= end_file):
            files.append(file)

    files = sort(files)

    for file in files:
        print file
        usound_data = rudv.read_ultrasound(file, 0)
        print     

def plot_channel_velocity(channel, start_num, end_num, unwrapped=0,
                          labelstring="", time=0):
    '''Plots the velocity measured by a specified channel. start_num
    and end_num are the indices to average between, unless time != 0, in
    which case those are time points to average between. Unwrapped velocity
    is plotted instead of raw velocity if unwrapped != 0'''
    if(time != 0):
        start_num = channel.find_index_after_time(start_num)
        end_num = channel.find_index_after_time(end_num)

    if (unwrapped == 0):
        profile = mean(channel.velocity[start_num:end_num,:], axis=0)
    else:
        profile = mean(channel.unwrapped_velocity[start_num:end_num,:], axis=0)
        
    plot(channel.depth, profile, '-o', label=labelstring)
    print "Maximum velocity = " + str(channel.maxvelocity)
    print "Time = " + str(channel.time[start_num]) + " to " + str(channel.time[end_num])  


def plot_single_vtheta_profile(vel_obj, profile_num):
    label_str = str(vel_obj.shot.number) +": t="+str(vel_obj.time[profile_num])

    plot(vel_obj.r, vel_obj.vtheta[profile_num,:], label=label_str)
    plot(vel_obj.shot.idealcouette.r, vel_obj.shot.idealcouette.vtheta)

def plot_avg_vtheta_profile(vel_obj, start_num, end_num):
    label_str = "%d: Avg from t=%.3g to t=%.3g" % (vel_obj.shot.number,
                                                   vel_obj.time[start_num],
                                                   vel_obj.time[end_num])

    plot(vel_obj.r,
         mean(vel_obj.vtheta[start_num:end_num, :], axis=0),
         label = label_str)
    plot(vel_obj.shot.idealcouette.r, vel_obj.shot.idealcouette.vtheta)

def plot_profile(usound_data, profile, omega1, omega2, labelstring):
    v1 = 2*pi*omega1*r1/60.0
    v2 = 2*pi*omega2*r2/60.0
    a = (v1*r1 - v2*r2)/(r1**2-r2**2)
    b = (v1*r1 - a*r1**2)
    r = calculate_radius(usound_data)

    couette = zeros(usound_data['depth'].size)
    for i in range(0, couette.size):
        couette[i] = a*r[i] + b/r[i]

    plot(r, profile, label = labelstring)
    axvline(x=r1, color='black')
    axvline(x=r2, color='black')
    xlabel("r [cm]")
    if (usound_data['channel'] == 2): #Tangential
        plot(r, couette, 'k-')
        ylabel(r"$v_\theta$ [cm/sec]")
    else:
        ylabel(r"$v_r$ [cm/sec]")
        axhline(y=0, color='black')
    legend()
    grid(b=1)

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

def plot_all_timeseries_velocity(filename, start_time, end_time, omega1, omega2):
    r_data = rudv.read_ultrasound(filename, 1)
    t_data = rudv.read_ultrasound(filename, 2)

    time = r_data['time']
    #Run once just to get the r vector
    r, vr, vt = reconstruct_avg_velocities(r_data, t_data, 0, 0, omega2)

    v1 = 2*pi*omega1*r1/60.0
    v2 = 2*pi*omega2*r2/60.0
    a = (v1*r1 - v2*r2)/(r1**2-r2**2)
    b = (v1*r1 - a*r1**2)

    couette = zeros(r.size)
    for i in range(0, couette.size):
        couette[i] = a*r[i] + b/r[i]

    start_pos = 0
    end_pos = time.size-1
    for i in range(0, time.size):
        if (time[i] > start_time) & (time[i-1] < start_time):
            start_pos = i
        elif (time[i] > end_time) & (time[i-1] < end_time):
            end_pos = i-1

    clipped_time = time[start_pos:end_pos]

    vr_time = zeros([clipped_time.size, vr.size])
    vt_time = zeros([clipped_time.size, vr.size])
    for i in range(start_pos, end_pos):
        r, vr, vt = reconstruct_avg_velocities(r_data, t_data, i, i, omega2)
        vr_time[i-start_pos,:] = vr
        vt_time[i-start_pos,:] = vt - couette

    v = arange(-14, 8, 2)
    z = arange(-88, 32, 12)

    subplot(2,1,1)
    contourf(clipped_time, r, vr_time.T, v, extend='both')
    xlabel("Time [s]")
    ylabel("r [cm]")
    title(filename + ' vr')
    colorbar()

    subplot(2,1,2)
    contourf(clipped_time, r, vt_time.T, z, extend='both')
    xlabel("Time [s]")
    ylabel("r [cm]")
    title('vt - ideal couette')
    colorbar()
    
def plot_timeseries(filename, channel, element, labelstring='', nopoints=0,
                    color="", depth=0):
    data = rudv.read_ultrasound(filename, channel)
    r = calculate_radius(data)
    
    if(len(labelstring) == 0):
        if (depth==0):
            labelstring = filename+": r="+str(round(r[element],2))+" cm"
        else:
            labelstring = filename+": depth="+str(round(data['depth'][element],2))+" cm"

    if(nopoints):
        line=plot(data['time'], data['velocity'][:,element], '-', label=labelstring)
    else:
        line=plot(data['time'], data['velocity'][:,element], '.-', label=labelstring)

    if(color):
        setp(line, color=color)
    
    xlabel("Time [sec]")
    if channel == 1:
        ylabel("Radial transducer [cm/sec]")
    if channel == 2:
        ylabel("Tangential transducer [cm/sec]")
    legend()
    grid(b=1)

def plot_timeseries_velocity(filename, radius, omega1, omega2, scaleshift=0, timeshift=0):
    r_data = rudv.read_ultrasound(filename, 1)
    t_data = rudv.read_ultrasound(filename, 2)
    #Resample r time onto t grid, with timeshift if needed.
    if(timeshift == 0):
        time = r_data['time']
    else:        
        r_time = r_data['time'] + timeshift
        t_time = t_data['time']
        time = t_time
        for i in range(0, r_data['depth'].shape[0]):
            tck = scipy.interpolate.splrep(r_time, r_data['velocity'][:,i], s=0)
            r_data['velocity'][:,i] = scipy.interpolate.splev(t_time, tck, der=0)
    
        
    vr_series = zeros(time.size)
    vt_series = zeros(time.size)

    r, vr, vt = reconstruct_avg_velocities(r_data, t_data, 0, 0, omega2)
    element = find_element_r(r, radius)
    print element

    for i in range(0, time.size):
        r, vr, vt = reconstruct_avg_velocities(r_data, t_data, i, i, omega2)
        vr_series[i] = vr[element]
        vt_series[i] = vt[element]

    if (scaleshift != 0):
        vt_series = vt_series - scaleshift

    #Some goofiness to get rid of spurious measurements
#    for i in range(0, time.size):
#        if vt_series[i] > 400:
#            vt_series[i] = vt_series[i-1]
#        if vt_series[i] < 0:
#            vt_series[i] = vt_series[i-1]
    

    titlestring = filename+": r="+str(r[element])
    plot(time, vr_series, '.-', label=r"$v_r$")
    plot(time, vt_series, '.-', label=r"$v_\theta$")
    xlabel("Time [sec]")
    ylabel("Velocity [cm/sec]")
    title(titlestring)
    legend()

def generate_profiles_alltime(filename, channel, omega2):
    r_data = rudv.read_ultrasound(filename, 1)
    t_data = rudv.read_ultrasound(filename, channel)
    time = t_data['time']

    r, vr, vt = reconstruct_avg_velocities(r_data, t_data, 0, 0, 53, unwrap=0)
    
    vt_profiles = zeros([time.size, r.size])
    vr_profiles = zeros([time.size, r.size])
    
    for i in range(0, time.size):
        r, vr, vt = reconstruct_avg_velocities(r_data, t_data, i, i, 53)
        vt_profiles[i,:] = vt
        vr_profiles[i,:] = vr
        
    data = {'r': r, 'time': time, 'vr': vr_profiles, 'vt': vt_profiles}
    return data

def generate_profiles_alltime_novr(filename, channel, omega2):
    r_data = rudv.read_ultrasound(filename, 1)
    t_data = rudv.read_ultrasound(filename, channel)
    time = t_data['time']

    r, vr, vt = reconstruct_avg_velocities_novr(r_data, t_data, 0, 0, 53, unwrap=0)
    
    profiles = zeros([time.size, r.size])
    
    for i in range(0, time.size):
        r, vr, vt = reconstruct_avg_velocities_novr(r_data, t_data, i, i, 53)
        profiles[i,:] = vt

    vr = zeros(profiles.shape)
    data = {'r': r, 'time': time, 'vt': profiles, 'vr': vr}
    return data

def plot_wave_amplitude_profile(filename, channel, omega2, start_time, end_time, freqband_min = 0, freqband_max = 0, filter_threshold=1000):
    data = generate_profiles_alltime_novr(filename, channel, omega2)
    amplitude = zeros(size(data['r']))
    for i in range(0, size(data['r'])):
        r, power = get_power_in_band_velocity(data, i, start_time, end_time, freqband_min=freqband_min, freqband_max=freqband_max, filter_threshold=filter_threshold)
        amplitude[i] = sqrt(power)

    plot(data['r'], amplitude)

def plot_power_spectrum_velocity(filename, channel, element, omega2, start_time, end_time, freqband_min = 0, freqband_max = 0, filter_threshold=1000):
    data = generate_profiles_alltime_novr(filename, channel, omega2)
    velocity = data['vt'][:,element]
    #Filter the data
    for i in range(5, velocity.size):
        if abs(velocity[i] - 0.2*(velocity[i-1] + velocity[i-2] + velocity[i-3] + velocity[i-4] + velocity[i-5])) > filter_threshold:
            velocity[i] = velocity[i-1]


    freq, fourier, n = calculate_fft_timeseries(data['time'],
                                             velocity,
                                             start_time, end_time)
    #Note that we needed to normalize by 1/N^2
    #Factor of 2 is to account for negative frequencies, since we'll
    #just deal with the positive part of the spectrum.
    power = 2*fourier*fourier.conjugate()/(n*n)
    phase = zeros(fourier.size)
    for i in range(0,fourier.size):
        phase[i] = cmath.phase(fourier[i])
    
    subplot(3,1,1)
    semilogy(freq, power)
    xlabel("Freq [Hz]")
    ylabel("Power Spectrum")
    legend()
    axes = axis()
    newaxes = [0.0, axes[1], axes[2], axes[3]]
    axis(newaxes)
    grid(b=1)

    subplot(3,1,2)
    plot(freq, phase)

    subplot(3,1,3)
    start_pos = 0
    end_pos = time.size
    for i in range(0, data['time'].size):
        if (data['time'][i] > start_time) & (data['time'][i-1] <= start_time):
            start_pos = i
        elif (data['time'][i] > end_time) & (data['time'][i-1] <= end_time):
            end_pos = i-1

    velocity = velocity[start_pos:end_pos]
    time = data['time'][start_pos:end_pos]
    plot(time, velocity)
    xlabel("Time [sec]")
    ylabel("Velocity [cm/sec]")

    if(freqband_min != 0):
        powerinband = 0
        for i in range(0, freq.size):
            if (freq[i] > freqband_min) & (freq[i] < freqband_max):
                powerinband = powerinband + power[i]
        print "powerinband = " + str(powerinband) + " at r = " + str(data['r'][element]) + " cm, amplitude = " + str(sqrt(powerinband)) + " cm/sec"
    return data['r'][element], powerinband    


def get_power_in_band_velocity(data, element, start_time, end_time, freqband_min = 0, freqband_max = 0, filter_threshold=1000):

    velocity = data['vt'][:,element]
    #Filter the data
    for i in range(5, velocity.size):
        if abs(velocity[i] - 0.2*(velocity[i-1] + velocity[i-2] + velocity[i-3] + velocity[i-4] + velocity[i-5])) > filter_threshold:
            velocity[i] = velocity[i-1]
    
    freq, fourier, n = calculate_fft_timeseries(data['time'],
                                             velocity,
                                             start_time, end_time)
    #Note that we needed to normalize by 1/N^2
    #Factor of 2 is to account for negative frequencies, since we'll
    #just deal with the positive part of the spectrum.
    power = 2*fourier*fourier.conjugate()/(n*n)
    
    if(freqband_min != 0):
        powerinband = 0
        for i in range(0, freq.size):
            if (freq[i] > freqband_min) & (freq[i] < freqband_max):
                powerinband = powerinband + power[i]
        print "powerinband = " + str(powerinband) + " at r = " + str(data['r'][element]) + " cm, amplitude = " + str(sqrt(powerinband)) + " cm/sec"
    return data['r'][element], powerinband    


def plot_power_spectrum(filename, channel, element, start_time, end_time, freqband_min = 0, freqband_max = 0, logscale=1):
    data = rudv.read_ultrasound(filename, channel)
    r = calculate_radius(data)
    time = data['time']
    velocity = data['velocity'][:,element]
    freq, fourier, n = calculate_fft_timeseries(time,
                                             velocity,
                                             start_time, end_time)
    #Note that we needed to normalize by 1/N^2
    power = 2*fourier*fourier.conjugate()/(n*n)
    #By this definition you can find the peak to peak velocity by taking the
    #power in the positive frequency band, multiplying by 2 to get the total
    #power at that frequency (positive and negative), then taking the square
    #root of that, then multiplying by two again
    #Peak to peak velocity = 2*sqrt(2*positive_power)
    
    labelstring = filename+": r="+str(r[element])

    subplot(2,1,1)
    if(logscale==1):
        semilogy(freq, power)
    else:
        plot(freq, power)
    xlabel("Freq [Hz]")
    if channel == 1:
        ylabel("Power Spectrum of radial transducer")
    if channel == 2:
        ylabel("Power Spectrum of tangential transducer")
    axes = axis()
    newaxes = [0.0, axes[1], axes[2], axes[3]]
    axis(newaxes)
    grid(b=1)


    subplot(2,1,2)
    start_pos=0
    end_pos=time.size-1
    for i in range(0, time.size):
        if (time[i] > start_time) & (time[i-1] <= start_time):
            start_pos = i
        elif (time[i] > end_time) & (time[i-1] <= end_time):
            end_pos = i-1

    velocity = velocity[start_pos:end_pos]
    time = time[start_pos:end_pos]
    plot(time, velocity, label=labelstring)
    legend()
    xlabel("Time [sec]")
    ylabel("Velocity [cm/sec]")

    if(freqband_min != 0):
        powerinband = 0
        for i in range(0, freq.size):
            if (freq[i] > freqband_min) & (freq[i] < freqband_max):
                powerinband = powerinband + power[i]
        print "powerinband = " + str(powerinband)
    
def get_power_spectrum(filename, channel, element, start_time, end_time):
    data = rudv.read_ultrasound(filename, channel)
    r = calculate_radius(data)
    time = data['time']
    velocity = data['velocity'][:,element]
    freq, fourier, n = calculate_fft_timeseries(time,
                                             velocity,
                                             start_time, end_time)
    #Note that we needed to normalize by 1/N^2
    power = 2*fourier*fourier.conjugate()/(n*n)
    #By this definition you can find the peak to peak velocity by taking the
    #power in the positive frequency band, multiplying by 2 to get the total
    #power at that frequency (positive and negative), then taking the square
    #root of that, then multiplying by two again
    #Peak to peak velocity = 2*sqrt(2*positive_power)
    return freq, power

def fit_frequency(filename, channel, element, start_time, end_time, start_amplitude = 1.0, start_frequency=1.0, start_phase=0, start_offset=0):
    data = rudv.read_ultrasound(filename, channel)
    r = calculate_radius(data)
    time = data['time']
    start_pos = 0
    end_pos = time.size
    for i in range(0, time.size):
        if (time[i] > start_time) & (time[i-1] <= start_time):
            start_pos = i
        elif (time[i] > end_time) & (time[i-1] <= end_time):
            end_pos = i-1

    time = data['time'][start_pos:end_pos]
    velocity = data['velocity'][start_pos:end_pos,element]
    
    def residuals(p, y, t):
        A,frequency,theta,offset = p
        err = y - (A*sin(2.0*pi*frequency*t + theta) + offset)
        return err

    def peval(t, p):
        return p[0]*sin(2.0*p[1]*x + p[2]) + p[3]

    p0 = [start_amplitude, start_frequency, start_phase, start_offset]

    plsq = scipy.optimize.leastsq(residuals, p0, args=(velocity, time), full_output=1)

    print "Amplitude = " + str(plsq[0][0]) + " +/- " + str(sqrt(plsq[1][0][0]))
    print "Frequency = " + str(plsq[0][1]) + " +/- " + str(sqrt(plsq[1][1][1]))
    print "Phase = " + str(plsq[0][2]) + " +/- " + str(sqrt(plsq[1][2][2]))
    print "Offset = " + str(plsq[0][3]) + " +/- " + str(sqrt(plsq[1][3][3]))

    fitted_time = linspace(time[0], time[-1], 200)
    fitted_amplitude = plsq[0][0]*sin(2*pi*plsq[0][1]*fitted_time + plsq[0][2]) + plsq[0][3]
    initial_guess = p0[0]*sin(2*pi*p0[1]*fitted_time + p0[2]) + p0[3]
    
    plot(time, velocity, '-o')
    plot(fitted_time, fitted_amplitude, label="Fitted")
    xlabel("Time [sec]")
    ylabel("Velocity [cm/sec]")
    



def plot_spectrogram(filename, channel, element, start_time=0, end_time=1000, timechunk=3):
    data = rudv.read_ultrasound(filename, channel)
    r = calculate_radius(data)
    time = data['time']

    start_pos = 0
    end_pos = time.size-1
    for i in range(0, time.size):
        if (time[i] > start_time) & (time[i-1] < start_time):
            start_pos = i
        elif (time[i] > end_time) & (time[i-1] < end_time):
            end_pos = i-1

    x = data['velocity'][start_pos:end_pos,element]
    t = time[start_pos:end_pos]

    subplot(2,1,1)
    plot(t, x)
    ylabel("Velocity [cm/sec]")
    titlestring = filename+": r="+str(r[element])
    title(titlestring)

    subplot(2,1,2)
    fs = 1.0/(data['time'][2]-data['time'][1])
    nfft = round(timechunk/(data['time'][2]-data['time'][1]))
    noverlap=nfft-1
    Pxx, freqs, bins, im = specgram(x, NFFT=nfft, Fs=fs, noverlap=noverlap)
    xlabel("Time [sec]")
    ylabel("Frequency [Hz]")
    

def plot_avg_velocities(filename, start_num, end_num, omega1, omega2, labelstring='', scale=1, rlim=0, channel=2, time=0):
    r_data = rudv.read_ultrasound(filename, 1)
    t_data = rudv.read_ultrasound(filename, channel)

    if(time == 1):
        start_num = find_profile_after_time(filename, channel, start_num)
        end_num = find_profile_after_time(filename, channel, end_num)

    r, vr, vt = reconstruct_avg_velocities(r_data, t_data, start_num,
                                           end_num, omega2)
    v1 = 2*pi*omega1*r1/60.0
    v2 = 2*pi*omega2*r2/60.0
    a = (v1*r1 - v2*r2)/(r1**2-r2**2)
    b = (v1*r1 - a*r1**2)
    couette = zeros(r.shape)
    for i in range(0, couette.size):
        couette[i] = a*r[i] + b/r[i]
    rcouette = r

    rlim = find_element_r(r, rlim)
    r = r[rlim:]
    vr = vr[rlim:]
    vt = vt[rlim:]

    subplot(2,1,1)
    xlabel("r [cm]")
    ylabel(r"$v_\theta$ [cm/sec]")
    if(len(labelstring) == 0):
        labelstring=filename + ": "+str(start_num)+"-"+str(end_num)
    plot(r, vt*scale, label=labelstring)     
    axvline(x=r1, color='black')
    axvline(x=r2, color='black')
    plot(rcouette, couette*scale, 'k-')
    grid(b=1)
    legend()

    subplot(2,1,2)
    ylabel(r"$v_r$ [cm/sec]")
    plot(r, vr*scale)
    axhline(y=0, color='black')
    axvline(x=r1, color='black')
    axvline(x=r2, color='black')
    grid(b=1)

def find_avg_velocity_at_r(filename, start_num, end_num, omega1, omega2, r_avg, channel=2, time=0, labelstring=''):
    r_data = rudv.read_ultrasound(filename, 1)
    t_data = rudv.read_ultrasound(filename, channel)

    if(time == 1):
        start_num = find_profile_after_time(filename, channel, start_num)
        end_num = find_profile_after_time(filename, channel, end_num)

    samples = end_num - start_num
    vrs = zeros(samples)
    vts = zeros(samples)
    
    for i in range(start_num, end_num):
        r, vr, vt = reconstruct_avg_velocities(r_data, t_data, i,
                                           i, omega2)
        r_avg_elem = find_element_r(r, r_avg)
        vrs[i-start_num] = vr[r_avg_elem]
        vts[i-start_num] = vt[r_avg_elem]

    #hist(vts, label=labelstring)
    vr_average = mean(vrs)
    vr_std = std(vrs)
    vt_average = mean(vts)
    vt_std = std(vts)

    return vr_average, vr_std, vt_average, vt_std


def find_shear(filename, start_time, end_time, omega1, omega2, rlimin, rlimout, channel=2):
    r_data = rudv.read_ultrasound(filename, 1)
    t_data = rudv.read_ultrasound(filename, channel)

    start_num = find_profile_after_time(filename, channel, start_time)
    end_num = find_profile_after_time(filename, channel, end_time)

    num_profiles = end_num - start_num

    print("Number of profiles used: " + str(num_profiles))

    r, vr, vt = reconstruct_avg_velocities_novr(r_data, t_data, start_num,
                                                end_num, omega2)
    omega = zeros(vt.shape)
    for i in range(0, omega.size):
        omega[i] = vt[i]/r[i]
    v1 = 2*pi*omega1*r1/60.0
    v2 = 2*pi*omega2*r2/60.0
    a = (v1*r1 - v2*r2)/(r1**2-r2**2)
    b = (v1*r1 - a*r1**2)
    couette = zeros(r.shape)
    for i in range(0, couette.size):
        couette[i] = a + b/(r[i]*r[i])
    rcouette = r



    #Convert rlimits to element number
    rlimin = find_element_r(r, rlimin)
    rlimout = find_element_r(r, rlimout)

    print("rlimin " + str(rlimin) + "rlimout" + str(rlimout))

    avg_shear = (omega[rlimout] - omega[rlimin])/(r[rlimout] - r[rlimin])
    offset = omega[rlimout]-avg_shear*r[rlimout]
    
    shear_fit_line = zeros(r.shape)
    for i in range(0, shear_fit_line.size):
        shear_fit_line[i] = avg_shear*r[i] + offset

    xlabel("r [cm]")
    ylabel(r"$\Omega$ [rad/sec]")
    datalabelstring=filename + ": "+str(start_num)+"-"+str(end_num)
    plot(r, omega, label=datalabelstring)
    axvline(x=r1, color='black')
    axvline(x=r2, color='black')
    plot(rcouette, couette, 'k-', label="Ideal Couette profile")
    fitlabelstring="Shear: " + str(avg_shear) + " rad/cm*sec"
    plot(r, shear_fit_line, label=fitlabelstring)
    grid(b=1)
    legend()

def filter_outliers(x, stddevs):
    mx = median(x)
    b = abs(x-mx)
    #calculate median of absolute deviation
    mad = median(b)
    #Now calculate a modified z score
    mzx = (x-mx)/mad

    x_masked = ma.masked_inside(x, mx - mad*stddevs, mx + mad*stddevs)
    return x_masked

def show_shear_layer_evolution(filename, omega1, omega2, channel=2, rmin=10,
                               rmax=18, filteroutliers=0):
    r_data = rudv.read_ultrasound(filename, 1)
    t_data = rudv.read_ultrasound(filename, channel)
    time = t_data['time']
    layer_width = zeros(time.size)
    layer_amplitude = zeros(time.size)
    layer_location = zeros(time.size)
    layer_avg = zeros(time.size)

    for i in range(0, time.size):
        a, avg_amp = eval_shear_layer(r_data, t_data, i, omega1, omega2,
                                      channel, time=0, rmin=rmin, rmax=rmax)
        layer_amplitude[i] = avg_amp
        layer_width[i] = a[1]
        if(layer_width[i] > r2-r1):
            layer_width[i] = r2-r1        
        layer_location[i] = a[2]
        layer_avg[i] = a[3]
        
        if(i%10 == 0):
            print i

    if(filteroutliers):
        layer_amplitude_masked = filter_outliers(layer_amplitude, 3)
        layer_width_masked = filter_outliers(layer_width, 3)
        layer_location_masked = filter_outliers(layer_location, 3)
        layer_avg_masked = filter_outliers(layer_avg, 3)
        layer_shear_masked = filter_outliers(layer_amplitude/layer_width, 3)
        
        figure()
        subplot(2,2,1)
        plot(time[layer_width_masked.mask],
             layer_width[layer_width_masked.mask])
        ylabel("Layer width [cm]")
        xlabel("Time [sec]")
        subplot(2,2,2)
        plot(time[layer_amplitude_masked.mask],
             layer_amplitude[layer_amplitude_masked.mask])
        ylabel("Layer amplitude [rad/sec]")
        xlabel("Time [sec]")
        subplot(2,2,3)
        plot(time[layer_location_masked.mask],
             layer_location[layer_location_masked.mask])
        ylabel("Radial layer location [cm]")
        xlabel("Time [sec]")
        subplot(2,2,4)
        plot(time[layer_shear_masked.mask],
             layer_shear_masked.data[layer_shear_masked.mask])
        ylabel("Shear parameter [1/cm*sec]")
        xlabel("Time [sec]")
    else:
        figure()
        subplot(2,2,1)
        plot(time, layer_width)
        ylabel("Layer width [cm]")
        xlabel("Time [sec]")
        subplot(2,2,2)
        plot(time, layer_amplitude)
        ylabel("Layer amplitude [rad/sec]")
        xlabel("Time [sec]")
        subplot(2,2,3)
        plot(time, layer_location)
        ylabel("Radial layer location [cm]")
        xlabel("Time [sec]")
        subplot(2,2,4)
        plot(time, layer_amplitude/layer_width)
        ylabel("Shear parameter [1/cm*sec]")
        xlabel("Time [sec]")

def eval_shear_layer(r_data, t_data, profile_num, omega1, omega2, channel=2,
                     time=0, rmin=10, rmax=18, display=0):

    if(time == 1):
        desired_time = profile_num
        profile_num = 0
        for i in range(0, t_data['time'].size):
            if (t_data['time'][i] > desired_time) & (t_data['time'][i-1] < desired_time):
                profile_num = i                

    r, vr, vt = reconstruct_avg_velocities_novr(r_data, t_data, profile_num,
                                                profile_num, omega2)
    omega = vt/r
    
    if(display==1):
        plot(r, omega)

    
    avg_ampl_in = omega[find_element_r(r,9):find_element_r(r,11)].mean()
    avg_ampl_out = omega[find_element_r(r,18):find_element_r(r,20)].mean()
    avg_ampl = avg_ampl_in-avg_ampl_out

    #Trim the arrays so we're only looking in the vicinity of the shear layer.
    rmin_elm = find_element_r(r, rmin)
    rmax_elm = find_element_r(r, rmax)
    r = r[rmin_elm:rmax_elm]
    vr = vr[rmin_elm:rmax_elm]
    omega = omega[rmin_elm:rmax_elm]

    #a[0] is the amplitude of the tanh, from bottom to top.
    #a[1] is the width, and a[2]
    #is the radial position offset and a[3] is the horizontal offset.

    model_func = lambda a, r:-0.5*a[0]*tanh((1/a[1])*(r-a[2])) + a[3]

    #define the error function

    err = lambda a, r, omega: (model_func(a, r) - omega)

    a0 = [omega1*2*pi/60, 2.0, 14.0, (omega1-omega2)*2*pi/60]
    a, success = scipy.optimize.leastsq(err, a0, args=(r, omega), maxfev=10000)

    if(display == 1):
        labelstring = "H: " + str(a[0]) + ", W: " + str(a[1]) + ", A: " + str(avg_ampl)
        plot(r, model_func(a, r), label=labelstring)
        #legend()

    
    return a, avg_ampl


def eval_shear_layer_2(r_data, t_data, profile_num, omega1, omega2, channel=2,
                       time=0, rmin=10, rmax=18, display=0, knots=8):

    if(time == 1):
        profile_num = find_profile_after_time(filename, channel,
                                              profile_num)

    r, vr, vt = reconstruct_avg_velocities_novr(r_data, t_data, profile_num,
                                                profile_num, omega2)
    omega = vt/r
    
    if(display==1):
        plot(r, omega)

    
    avg_ampl_in = omega[find_element_r(r,9):find_element_r(r,11)].mean()
    avg_ampl_out = omega[find_element_r(r,18):find_element_r(r,20)].mean()
    avg_ampl = avg_ampl_in-avg_ampl_out

    #Trim the arrays so we're only looking in the vicinity of the shear layer.
    rmin_elm = find_element_r(r, rmin)
    rmax_elm = find_element_r(r, rmax)
    r = r[rmin_elm:rmax_elm]
    vr = vr[rmin_elm:rmax_elm]
    omega = omega[rmin_elm:rmax_elm]

    #Fit spline with explicit knots
    t = linspace(r[0], r[-1], knots)
    #I think that it includes the end knots automatically, so trim those out
    t=t[1:-1]
    fit = scipy.interpolate.splrep(r, omega, t=t, k=4)


    if(display == 1):
        labelstring = "Fit with" + str(knots) + "knots"
        plot(r, scipy.interpolate.splev(r, fit), label=labelstring)
        plot(r, scipy.interpolate.splev(r, fit, der=1), label="1st der")
        plot(r, scipy.interpolate.splev(r, fit, der=2), label="2nd der")
             
        legend()

    a = 5
    return a, avg_ampl



def plot_avg_velocities_novr(filename, start_num, end_num, omega1, omega2, labelstring='', scale=1, rlim=0, channel=2, time=0, omega=0, unwrap=1):
    r_data = rudv.read_ultrasound(filename, 1)
    t_data = rudv.read_ultrasound(filename, channel)

    if(time == 1):
        start_num = find_profile_after_time(filename, channel, start_num)
        end_num = find_profile_after_time(filename, channel, end_num)

    r, vr, vt = reconstruct_avg_velocities_novr(r_data, t_data, start_num,
                                                end_num, omega2, unwrap=unwrap)
    v1 = 2*pi*omega1*r1/60.0
    v2 = 2*pi*omega2*r2/60.0
    a = (v1*r1 - v2*r2)/(r1**2-r2**2)
    b = (v1*r1 - a*r1**2)
    couette = zeros(r.shape)
    for i in range(0, couette.size):
        couette[i] = a*r[i] + b/r[i]
    rcouette = r

    rlim = find_element_r(r, rlim)
    r = r[rlim:]
    vr = vr[rlim:]
    vt = vt[rlim:]

    xlabel("r [cm]")
    if(omega==1):
        ylabel(r"$\Omega$ [1/sec]")
    else:
        ylabel(r"$v_\theta$ [cm/sec]")

    if(len(labelstring) == 0):
        labelstring=filename + ": "+str(start_num)+"-"+str(end_num)

    if(omega==1):
        plot(r, vt*scale/r, label=labelstring)
    else:
        plot(r, vt*scale, label=labelstring)
        
    axvline(x=r1, color='black')
    axvline(x=r2, color='black')
    if(omega==0):
        plot(rcouette, couette*scale, 'k-')
    
    grid(b=1)
    legend()
    return axis()

def save_avg_profile(filename, start_num, end_num, omega1, omega2,
                     savefilename, scale=1, saveideal=0):
    r_data = rudv.read_ultrasound(filename, 1)
    t_data = rudv.read_ultrasound(filename, 2)

    r, vr, vt = reconstruct_avg_velocities(r_data, t_data, start_num,
                                           end_num, omega2)
    omega = vt/r

    plot(r, omega, label="data")
    ylabel(r"$\Omega$ [1/sec]")
    xlabel("r [cm/sec]")

    #Trim out the first few centimeters, and the points
    #after the outer cylinder
    first_index = 0
    last_index = r.size-1
    for i in range(0, r.size):
        if r[i] < 11.0:
            first_index = i
        if r[i] < r2:
            last_index = i
    r = r[first_index:last_index]
    omega = omega[first_index:last_index]

    #Now define the point at the inner cylinder by the inner cylinder speed
    r[0] = r1
    omega[0] = omega1*2.0*pi/60.0

    #Now fit a polynomial to this data
    z = polyfit(r, omega, 6)
    p = poly1d(z)

    newr = linspace(r1, r2, 150)
    newomega = p(newr)

    plot(newr, newomega, label="Fitted")

    newomega = newomega*scale

    plot(newr, newomega, label="Fitted and scaled")

    v1 = 2*pi*omega1*r1/60.0
    v2 = 2*pi*omega2*r2/60.0
    a = (v1*r1 - v2*r2)/(r1**2-r2**2)
    b = (v1*r1 - a*r1**2)
    couette = zeros(newr.shape)
    for i in range(0, couette.size):
        couette[i] = a + b/(newr[i]*newr[i])

    couette=couette*scale

    plot(newr, couette, label="Ideal Couette solution")
    legend()
    
    if(saveideal==0):
        savetxt(savefilename, c_[newr, newomega], fmt="%12.6G")
    else:
        print("Saving Ideal Couette profile")
        savetxt(savefilename, c_[newr, couette], fmt="%12.6G")


def find_element_r(r, desired_radius):
    element = 0
    for i in range(0, r.size):
        if (r[i] > desired_radius) & (r[i-1] < desired_radius):
            element = i
    return element

def calculate_fft_timeseries(time, data, start_time, end_time, filter_threshold=1000):
    start_pos = 0
    end_pos = time.size
    for i in range(0, time.size):
        if (time[i] > start_time) & (time[i-1] <= start_time):
            start_pos = i
        elif (time[i] > end_time) & (time[i-1] <= end_time):
            end_pos = i-1

    fourier = fft(data[start_pos:end_pos])
    n = end_pos - start_pos
    timestep = time[start_pos+1] - time[start_pos]
    freq = fftfreq(n, d=timestep)

    fourier = fftshift(fourier)
    freq = fftshift(freq)
    return freq, fourier, n


def reconstruct_avg_velocities(r_data, t_data, start_num, end_num, omega2, unwrap=1):
    #Get an averaged, unwrapped radial profile

    r_profiles = zeros([r_data['depth'].shape[0],
                        end_num - start_num + 1])
    for i in range(start_num, end_num+1):
        unwrapped_profile = unwrap_profile(r_data,
                                           r_data['velocity'][i,:])
        r_profiles[:,(i-start_num)] = unwrapped_profile

    r_avg_profile = mean(r_profiles,1)
    r_std_profile = std(r_profiles,1)

    #Get an average, unwrapped tangential profile

    t_profiles = zeros([t_data['depth'].shape[0],
                        end_num - start_num + 1])
    for i in range(start_num, end_num+1):
        unwrapped_profile = unwrap_profile(t_data,
                                           t_data['velocity'][i,:])
        t_profiles[:,(i-start_num)] = unwrapped_profile

    t_avg_profile = mean(t_profiles,1)
    t_std_profile = std(t_profiles,1)

    #Generate the radiuses for both sets of data
    r_r = calculate_radius(r_data)
    r_t = calculate_radius(t_data)

    #Find the last good radius
    for i in range(0, r_r.size):
        if r_r[i] > r1:
            r_good_index = i

    for i in range(0, r_t.size):
        if r_t[i] < r_t[i-1]:
            t_good_index = i-1

    #Trim the arrays
    r_r = r_r[0:r_good_index]
    r_avg_profile = r_avg_profile[0:r_good_index]

    r_t = r_t[0:t_good_index]
    t_avg_profile = t_avg_profile[0:t_good_index]

    #Now reverse all the arrays
    r_r = r_r[::-1]
    r_avg_profile = r_avg_profile[::-1]

    r_t = r_t[::-1]
    t_avg_profile = t_avg_profile[::-1]

    tck = scipy.interpolate.splrep(r_r, r_avg_profile, s=0)

    r_avg_resampled = scipy.interpolate.splev(r_t, tck, der=0)

    #r_t is now the definitive radial coordinate
    r = r_t

    v_r = zeros(r.shape)
    v_t = zeros(r.shape)

    #Define matrix for doing the transformation
    A = zeros([2,2])
    for i in range(0, r.size):
        sinalpha_r = (r2/r[i])*sin(radial_probe_angle*pi/180)
        A[0,0] = -cos(arcsin(sinalpha_r))
        A[0,1] = sinalpha_r
        sinalpha_t = (r2/r[i])*sin(tan_probe_angle*pi/180)
        A[1,0] = -cos(arcsin(sinalpha_t))
        A[1,1] = sinalpha_t
        B = linalg.inv(A)
        v_meas = [r_avg_resampled[i], t_avg_profile[i]]
        v_actual = dot(B, v_meas)
        v_r[i] = v_actual[0]
        v_t[i] = v_actual[1]

    #Now fix the vt offset
    omega2 = omega2*2*pi/60
    offset = omega2*r
    v_t = v_t + offset

    return r, v_r, v_t


def reconstruct_avg_velocities_nonaxisymmetric(r_data, t_data, profile_num, omega2, oscillation_time):
    #Get an unwrapped radial profile

    r_profile = unwrap_profile(r_data, r_data['velocity'][profile_num,:])
    num_points_needed = int(oscillation_time/(t_data['time'][5]-t_data['time'][4]))
    #Get an unwrapped tangential profile in a block around the desired profile
    #number
    t_profiles=zeros([t_data['depth'].size,num_points_needed])
    t_profiles_phases = zeros(num_points_needed)
    for i in range(0, num_points_needed):
        t_profiles[:,i] = unwrap_profile(t_data, t_data['velocity'][(profile_num-num_points_needed/2)+i,:])
        #Base phase, accounting for pi/2 difference from portplug spacing
        t_profiles_phases[i] = t_data['time'][profile_num-num_points_needed/2+i]*2.0*pi/oscillation_time - pi/2.0

    desiredphase = r_data['time'][profile_num]*2.0*pi/oscillation_time
    
    t_profile = zeros(t_data['depth'].size)

    #Resample this thing in time so that the correct phase is selected.
    for i in range(t_profile.size):
        #Roughly account for additional phase offset with depth, need to fix this.
        phaseoffset = math.atan((-20.30+t_data['depth'][i]*cos(tan_probe_angle*pi/180))/
                                (t_data['depth'][i]*sin(tan_probe_angle*pi/180))) + pi/2
        temp_phases = t_profiles_phases - phaseoffset
        tck_t = scipy.interpolate.splrep(temp_phases, t_profiles[i,:], s=0)
        t_profile[i] = scipy.interpolate.splev(desiredphase, tck_t, der=0)    
    
    #Generate the radiuses for both sets of data
    r_r = calculate_radius(r_data)
    r_t = calculate_radius(t_data)

    #Find the last good radius
    for i in range(0, r_r.size):
        if r_r[i] > r1:
            r_good_index = i

    for i in range(0, r_t.size):
        if r_t[i] < r_t[i-1]:
            t_good_index = i-1

    #Trim the arrays
    r_r = r_r[0:r_good_index]
    r_profile = r_profile[0:r_good_index]

    r_t = r_t[0:t_good_index]
    t_profile = t_profile[0:t_good_index]

    #Now reverse all the arrays
    r_r = r_r[::-1]
    r_profile = r_profile[::-1]

    r_t = r_t[::-1]
    t_profile = t_profile[::-1]

    tck = scipy.interpolate.splrep(r_r, r_profile, s=0)

    r_resampled = scipy.interpolate.splev(r_t, tck, der=0)

    #r_t is now the definitive radial coordinate
    r = r_t

    #Now we need to resample vt in time

    v_r = zeros(r.shape)
    v_t = zeros(r.shape)

    #Define matrix for doing the transformation
    A = zeros([2,2])
    for i in range(0, r.size):
        sinalpha_r = (r2/r[i])*sin(radial_probe_angle*pi/180)
        A[0,0] = -cos(arcsin(sinalpha_r))
        A[0,1] = sinalpha_r
        sinalpha_t = (r2/r[i])*sin(tan_probe_angle*pi/180)
        A[1,0] = -cos(arcsin(sinalpha_t))
        A[1,1] = sinalpha_t
        B = linalg.inv(A)
        v_meas = [r_resampled[i], t_profile[i]]
        v_actual = dot(B, v_meas)
        v_r[i] = v_actual[0]
        #Just find v_t based on azimuthal transducer.  In other words,
        #pretend that v_r is zero to avoid the noise of the radial transducer.
        v_t[i] = t_profile[i]/sinalpha_t

    #Now fix the vt offset
    omega2 = omega2*2*pi/60
    offset = omega2*r
    v_t = v_t + offset

    return r, v_r, v_t


def reconstruct_avg_velocities_novr(r_data, t_data, start_num, end_num, omega2, unwrap=1):
    #Get an average, unwrapped tangential profile

    t_profiles = zeros([t_data['depth'].shape[0],
                        end_num - start_num + 1])
    for i in range(start_num, end_num+1):
        if(unwrap==1):
            unwrapped_profile = unwrap_profile(t_data,
                                               t_data['velocity'][i,:])
            t_profiles[:,(i-start_num)] = unwrapped_profile
        else:
            t_profiles[:,(i-start_num)] = t_data['velocity'][i,:]
    

    t_avg_profile = mean(t_profiles,1)
    t_std_profile = std(t_profiles,1)

    #Generate the radiuses for both sets of data
    r_t = calculate_radius(t_data)

    #Find the last good radius
    for i in range(0, r_t.size):
        if r_t[i] < r_t[i-1]:
            t_good_index = i-1

    #Trim the arrays
    r_t = r_t[0:t_good_index]
    t_avg_profile = t_avg_profile[0:t_good_index]

    #Now reverse all the arrays
    r_t = r_t[::-1]
    t_avg_profile = t_avg_profile[::-1]


    r_avg_resampled = zeros(r_t.size)

    #r_t is now the definitive radial coordinate
    r = r_t

    v_r = zeros(r.shape)
    v_t = zeros(r.shape)

    #Now do the transformation.
    for i in range(0, r.size):
        sinalpha_t = (r2/r[i])*sin(tan_probe_angle*pi/180)
        v_t[i] = t_avg_profile[i]/sinalpha_t

    #Now fix the vt offset
    if(unwrap == 1):
        omega2 = omega2*2*pi/60
        offset = omega2*r
        v_t = v_t + offset

    return r, v_r, v_t

def get_statistics(filename, channel, element, start_time, end_time):
    data = rudv.read_ultrasound(filename, channel)
    time = data['time']
    velocity = data['velocity'][:,element]
    start_pos=0
    end_pos=time.size
    for i in range(0, time.size):
        if (time[i] > start_time) & (time[i-1] < start_time):
            start_pos = i
        elif (time[i] > end_time) & (time[i-1] < end_time):
            end_pos = i-1

    trimmed_velocity=velocity[start_pos:end_pos]
    mean = trimmed_velocity.mean()
    stddev = trimmed_velocity.std()

    return mean, stddev

def gen_vtheta_movie(filename, channel, omega2, primary_oscillation_start_time, primary_oscillation_end_time, start_time, end_time, desiredcells=200, rin=r1, filter_threshold=1000, background_subtract=0, derotate=0, maxv=10000, minv=-10000, max_diff_mean=10000, fps=10.0, speed=1.0, basedir='/tmp/abcd000', moviefilename='movie.avi'):

    #To be sure fps isn't cast as an integer, screwing up later math.
    fps = float(fps)

    #First get the primary oscillation info
    levels = plot_vtheta_mode(filename, channel, omega2, primary_oscillation_start_time, primary_oscillation_end_time, desiredcells=desiredcells, rin=rin, filter_threshold=filter_threshold, background_subtract=background_subtract, maxv=maxv, minv=minv, max_diff_mean=max_diff_mean)

    #Now start assembling these frames
    osc_period = primary_oscillation_end_time - primary_oscillation_start_time
    num_frames = int((end_time - start_time)*fps/speed)

    os.mkdir(basedir)
    
    for i in range(0, num_frames):
        frame_start_time = start_time + i/(fps/speed)
        frame_end_time = frame_start_time + osc_period

        clf()
        plot_vtheta_mode(filename, channel, omega2, frame_start_time, frame_end_time, desiredcells=desiredcells, rin=rin, filter_threshold=filter_threshold, background_subtract=background_subtract, derotate=derotate, maxv=maxv, minv=minv, max_diff_mean=max_diff_mean, levels=levels)
        outputfile = basedir + '/' + str("%04d" % i) + '.png'
        savefig(outputfile)
        print 'Wrote file', outputfile

    #Now compile into a movie
    command = ('mencoder',
               'mf://' + basedir + '/????.png',
               '-mf',
               'type=png:fps=' + str(fps),
               '-ovc',
               'lavc',
               '-lavcopts',
               'vcodec=mpeg4',
               '-oac',
               'copy',
               '-o',
               moviefilename)

    subprocess.check_call(command)
    shutil.rmtree(basedir)

def plot_vtheta_mode(filename, channel, omega2, start_time, end_time, desiredcells=200, rin=r1, filter_threshold=1000, background_subtract=0, derotate=0, maxv=10000, minv=-10000, max_diff_mean=10000, levels=0):

    data = generate_profiles_alltime_novr(filename, channel, omega2)

    phase = linspace(-pi, pi, 100)
    time = data['time']
    velocity = data['vt']
    r = data['r']

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
    velocity = velocity[start_pos-10:end_pos+10,:]

    #Now convert time to phase
    time = time - start_time
    measured_phase = time*2.0*pi/(end_time-start_time) - pi

    resampled_velocity = zeros([phase.size, r.size])

    #temp_measured_phase=zeros(measured_phase.size)

    #Now resample for each element of phase
    for i in range(0, r.size):
        #Filter the data to remove spurious measurements
        for k in range (0, 5):
            if (velocity[k,i] > maxv):
                velocity[k,i] = maxv
            if (velocity[k,i] < minv):
                velocity[k,i] = minv
        for k in range (5, velocity[:,i].size):
            if abs(velocity[k,i] - velocity[k-5:k-1,i].mean()) > filter_threshold:
                velocity[k,i] = velocity[k-5:k-1,i].mean()
            if (velocity[k,i] > maxv):
                velocity[k,i] = maxv
            if (velocity[k,i] < minv):
                velocity[k,i] = minv

        #Need to offset theta to account for the angular extent of the
        #the measurement chord.
        #Note that there is some weirdness because of the branchcuts of asin.
        theta_offset = pi - tan_probe_angle*pi/180 - (pi - math.asin(r2*math.sin(tan_probe_angle*pi/180)/r[i]))
        temp_measured_phase = measured_phase - theta_offset

        #Now resample.  Array is reversed, since measurements in experiment are
        #made from larger phase down to smaller phase
        #(features flowing past transducer)
        
        tck = scipy.interpolate.splrep(temp_measured_phase, velocity[:,i], s=0)
        resampled_velocity[:,i] = (scipy.interpolate.splev(phase, tck, der=0))[::-1]
        if(background_subtract == 1):
            resampled_velocity[:,i] = resampled_velocity[:,i]-resampled_velocity[:,i].mean()

    #Need to do this resampling
    xi = linspace(-r2, r2, desiredcells)
    yi = linspace(-r2, r2, desiredcells)
    zi = zeros((desiredcells, desiredcells))

    i = 0
    for x in xi:
        k = 0
        for y in yi:
            r_temp = math.sqrt(x**2 + y**2)
            if ((r_temp > rin) and (r_temp < r2)):
                element_r = find_element_r(r, r_temp)

                angle = math.atan2(y,x)
                if (derotate !=0):
                    #First put the measured angle on a 0 to 2pi scale
                    angle = angle + pi
                    #Now add the derotation angle
                    angle = angle + derotate_angle
                    angle = math.fmod(angle, 2.0*pi)
                    #And now back to the -pi to pi scale
                    angle = angle - pi

                
                element_phase = 0
                for n in range(0, phase.size):
                    if (phase[n] > angle) & (phase[n-1] < angle):
                        element_phase = n
                        
                zi[k,i] = resampled_velocity[element_phase, element_r]
                if ((background_subtract == 1) & (zi[k,i] > max_diff_mean)):
                    zi[k,i] = max_diff_mean
                if ((background_subtract == 1) & (zi[k,i] < -max_diff_mean)):
                    zi[k,i] = -max_diff_mean
            else:
                zi[k,i] = nan

            k = k + 1
        i = i + 1
        print i

    if(isscalar(levels) == 1):
        C = contourf(xi, yi, zi, 50)
    else:
        C = contourf(xi, yi, zi, levels)
    
    xlim(-r2, r2)
    ylim(-r2, r2)
    axes().set_aspect('equal')
    xlabel("x [cm]")
    ylabel("y [cm]")
    title(filename + ": " + str(start_time) + " to " + str(end_time) + " sec")
    bar_instance = colorbar()
    if(background_subtract == 0):
        matplotlib.colorbar.ColorbarBase.set_label(bar_instance, r"$v_{\theta}$ [cm/sec]")
    if(background_subtract == 1):
        matplotlib.colorbar.ColorbarBase.set_label(bar_instance, r"$v_{\theta} - \bar{v_{\theta}}$ [cm/sec]")
        
    return C.levels


def gen_profile_movie(filename, omega1, omega2, start_time, end_time, channel=2, labelstring='', rlim=0, speed=1.0, basedir='/tmp/abcd000', moviefilename='movie.avi'):

    dt = find_time_of_profile(filename, channel, 3) - find_time_of_profile(filename, channel, 2)
    fps = speed*1.0/dt

    #First find the acqusition rate of this channel
    initial_profile = find_profile_after_time(filename, channel, start_time)
    final_profile = find_profile_after_time(filename, channel, end_time)
    if(final_profile == 0):
        final_profile = find_number_of_profiles(filename, channel)    

    os.mkdir(basedir)

    axes = plot_avg_velocities_novr(filename, initial_profile, initial_profile, omega1, omega2, rlim=rlim, channel=channel)
    
    for i in range(initial_profile, final_profile):
        clf()
        t = find_time_of_profile(filename, channel, i)
        finallabel = labelstring + ": t=" + str(t)
        plot_avg_velocities_novr(filename, i, i, omega1, omega2, labelstring=finallabel, rlim=rlim, channel=channel)
        axis(axes)
        outputfile = basedir + '/' + str("%04d" % i) + '.png'
        savefig(outputfile)
        print 'Wrote file', outputfile

    #Now compile into a movie
    command = ('mencoder',
               'mf://' + basedir + '/????.png',
               '-mf',
               'type=png:fps=' + str(fps),
               '-ovc',
               'lavc',
               '-lavcopts',
               'vcodec=mpeg4',
               '-oac',
               'copy',
               '-o',
               moviefilename)

    subprocess.check_call(command)
    shutil.rmtree(basedir)

def play_channel_velocity_animation(channel, speed=1.0):
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
    
    ani = animation.FuncAnimation(fig, draw_raw_profile,
                                  range(0, channel.time.size),
                                  interval = dt*1000, blit=True,
                                  init_func=init)
    
    #I have no idea why this is here, but the animaion doesn't run without
    #having something to generate an error here?!
    magic_squirrel()


def gen_raw_profile_movie(filename, start_time, end_time, channel=2, labelstring='', speed=1.0, basedir='/tmp/abcd000', moviefilename='movie.avi'):

    dt = find_time_of_profile(filename, channel, 3) - find_time_of_profile(filename, channel, 2)
    fps = speed*1.0/dt

    #First find the acqusition rate of this channel
    initial_profile = find_profile_after_time(filename, channel, start_time)
    final_profile = find_profile_after_time(filename, channel, end_time)
    if(final_profile == 0):
        final_profile = find_number_of_profiles(filename, channel)    

    os.mkdir(basedir)

    axes = plot_raw_profile(filename, initial_profile, initial_profile, channel)

    for i in range(initial_profile, final_profile):
        clf()
        t = find_time_of_profile(filename, channel, i)
        finallabel = labelstring + ": t=" + str(t)
        plot_raw_profile(filename, i, i, channel)
        axis(axes)
        title(finallabel)
        outputfile = basedir + '/' + str("%04d" % i) + '.png'
        savefig(outputfile)
        print 'Wrote file', outputfile

    #Now compile into a movie
    command = ('mencoder',
               'mf://' + basedir + '/????.png',
               '-mf',
               'type=png:fps=' + str(fps),
               '-ovc',
               'lavc',
               '-lavcopts',
               'vcodec=mpeg4',
               '-oac',
               'copy',
               '-o',
               moviefilename)

    subprocess.check_call(command)
    shutil.rmtree(basedir)
