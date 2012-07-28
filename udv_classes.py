"""Provides Shot, ChannelData, Velocity, and ShotList objects for UDV data.

A typical workflow might look like:
    import udv_classes
    udv_classes.set_data_path("/u/aroach/ultrasound_data")
    get_shot = udv_classes.ShotList().get_shot #Initialize a new ShotList

Then to get Shot, Channel, or Velocity objects:
    shot = get_shot(948)
    channel = get_shot(948).get_channel(2)
    velocity = get_shot(948).get_velocity(1,2)

Or to get a velocity object assuming a nonaxisymmetric mode structure:
    velocity = get_shot(948).get_velocity(1, 2, m=1, period=1.2)
"""

import read_ultrasound_new as rudv
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import LSQUnivariateSpline
from copy import deepcopy
import shot_params as sp
import shot_db_ops as sdo
import numpy as np
import math
import os

#Define some handy variables and functions
r1 = 7.06
r2 = 20.30
rpmtorads = lambda x: x*2.0*math.pi/60.0
degstorads = lambda x: x*math.pi/180.0

data_path=''
def set_data_path(new_path):
    """Set the path where the UDV data is located to the string new_path.
    If new_path is empty, the path will be the current working directory."""

    #Make sure we have data_path in the module scope.
    global data_path

    if(new_path == ''):
        new_path = os.getcwd()
    
    #If the path is not empty (which would translate to just using the current
    #directory), and the path does not end in a /, add one.
    if(not(new_path == '') and not(new_path[-1] == '/')):
        new_path = new_path + '/'
    
    data_path = new_path

#Initialize data_path to the current working directory.
set_data_path('')


class Shot:
    """A class for data from an individual shot.
    
    A shot is initialized with a shot number. Parameters for that shot
    number are read from shot_params.py. Raw data from an individual
    channel can be accessed in a ChannelData object returned from the
    get_channel() method. Data processed into individual velocity
    components can be accessed in a Velocity object returned from the
    get_velocity() method."""
    
    def __init__(self, shot_num):
        """Creates a new Shot object.
        
        Looks up and adds shot parameters to the object from the shot
        database. Also creates a CouetteProfile object with the ideal
        Couette profile for this set of parameters"""

        if(not(sp.shot_params.has_key(shot_num))):
            raise ValueError('Shot %d not in database.' % shot_num)
        
        self.number = shot_num
        self.filename = data_path + str(shot_num) + '.BDD'
        if(not(os.path.exists(self.filename))):
            raise ValueError('Data file %s does not exist.' % self.filename)
        
        self.shot_length = sp.shot_params[shot_num]['shot_length']
        self.ICspeed = sp.shot_params[shot_num]['ICspeed']
        self.IRspeed = sp.shot_params[shot_num]['IRspeed']
        self.ORspeed = sp.shot_params[shot_num]['ORspeed']
        self.OCspeed = sp.shot_params[shot_num]['OCspeed']
        self.current = sp.shot_params[shot_num]['current']
        self.field_delay = sp.shot_params[shot_num]['field_delay']
        self.field_length = sp.shot_params[shot_num]['t_field']
        self.udv_delay = sp.shot_params[shot_num]['udv_delay']
        #list() used to make a copy of channels.
        self.channels_used = list(sp.shot_params[shot_num]['channels'])
        self.channels = {}
        self.velocities = []
        self.idealcouette = CouetteProfile(self)

    def add_all_channels(self):
        '''Adds all available channels to the Shot object'''
        for channel in self.channels_used:
            add_channel(channel)

    def get_channel(self, channel_num):
        '''Returns ChannelData object for specified channel for this Shot.

        Returns a ChannelData object corresponding to channel_num. Should
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
    
    def add_channel(self, channel_num):
        '''Adds and returns a ChannelData object corresponding to channel_num
        for this Shot.'''
        
        try:
            channel = ChannelData(self, channel_num)
        except:
            raise

        self.channels[channel_num] = channel
        return self.channels[channel_num]

    def del_channel(self, channel_num):
        '''Delete a channel and associated velocity objects.
        
        Note that this is a rather destructive action, since it also
        wipes out all velocity objects that used that channel, so it
        should be used with caution.'''
        
        #First get rid of all of the velocity objects that use this channel.
        self.del_velocities_derived_from_channel(channel_num)
        
        #Now that we've done that, get rid of the channel
        self.channels.pop(channel_num)
    
    def del_velocities_derived_from_channel(self, channel_num):
        """Delete velocity objects associated with a channel

        Gets rid of all velocity objects that were derived from a
        certain channel. This is useful if we want to change some
        aspect of the channel, like the transducer angle if we've
        found a better calibration, or the threshold used to unwrap
        the velocity, and we want to be sure that none of the velocity
        objects that use the old definitions will still be around."""
        
        velocities_to_be_removed = []
        #Check all of the velocity objects to see if this channel
        #is used in its progenitors. If so, add it to the list of
        #objects that we're going to get rid of.
        for velocity in self.velocities:
            if(velocity.used_channel(channel_num)):
                velocities_to_be_removed.append(velocity)

        #Now get rid of all of those objects.
        for velocity in velocities_to_be_removed:
            self.velocities.remove(velocity)
    
    def get_velocity(self, *channels, **nonaxiargs):        
        """Return a Velocity object for this Shot

        Returns a Velocity object produced using the channel
        numbers specified in *channels for this Shot. Optional 'm' and
        'period' arguments in **nonaxiargs can be specified to do
        nonaxisymmetric velocity reconstructions. If the desired
        velocity object already exists, it is returned and
        add_velocity() is not called."""

        #Grab the channel numbers, and get the list of channel nums
        channel_nums = self.sanitize_channel_nums_for_velocities(channels)

        #Grab the optional arguments
        m = nonaxiargs.pop('m', 0)
        period = nonaxiargs.pop('period', 0)
        for k in nonaxiargs.keys():
            print "Unrecognized argument to get_velocity(): %s" % k

        for velocity in self.velocities:
            #Now check to see if the progenitor channels the channel_nums, and
            #that m also matches. If m!=0, also check to make sure that
            #the period times match. If all that checks out, return this
            #velocity.
            if ((velocity.get_progenitor_channels() == channel_nums) and
                (velocity.m == m) and
                ((m==0) or (velocity.period == period))):
                return velocity

        #Otherwise add this new velocity set and return that.
        return self.add_velocity(*channel_nums, m=m, period=period)

    def add_velocity(self, *channels, **nonaxiargs):
        """Add and return a Velocity object for this Shot

        Adds and returns a Velocity object produced using the
        channel numbers specified in *channels for this Shot. Optional
        'm' and 'period' arguments in **nonaxiargs can be specified to
        do nonaxisymmetric velocity reconstructions."""

        #Grab the channel numbers, and get the list of channel nums
        channel_nums = self.sanitize_channel_nums_for_velocities(channels)

        #Grab the optional arguments
        m = nonaxiargs.pop('m', 0)
        period = nonaxiargs.pop('period', 0)
        for k in nonaxiargs.keys():
            print "Unrecognized argument to add_velocity(): %s" % k

        #Now generate the velocity object
        try:
            velocity = Velocity(self, channel_nums, m=m, period=period)
        except:
            raise

        #And append it to the velocities list for this Shot
        self.velocities.append(velocity)
        return self.velocities[-1]
    
    def del_velocity(self, *channels, **nonaxiargs):
        """Delete a Velocity object for this Shot
        
        Removes a Velocity object from a shot matching the specified
        parameters. Functional call is in the same format as to
        add_velocity() and get_velocity() methods."""
        
        #Grab the channel numbers, and get the list of channel nums
        channel_nums = self.sanitize_channel_nums_for_velocities(channels)
        
        #Grab the optional arguments
        m = nonaxiargs.pop('m', 0)
        period = nonaxiargs.pop('period', 0)
        for k in nonaxiargs.keys():
            print "Unrecognized argument to del_velocity(): %s" % k
        
        #Try to find this velocity.

        for velocity in self.velocities:
            #First make a list of the channel numbers from all of the
            #progenitor ChannelData objects for this Velocity object
            progenitor_list = list()
            for progenitor in velocity.progenitors:
                progenitor_list.append(progenitor.channel)

            #Now check to see if these channels match the channel_nums, and
            #that m also matches. If m!=0, also check to make sure that
            #the period times match.
            progenitor_list.sort()
            if ((progenitor_list == channel_nums) and
                (velocity.m == m) and
                ((m==0) or (velocity.period == period))):
                self.velocities.remove(velocity)
    
    def sanitize_channel_nums_for_velocities(self, channel_nums):
        """Makes sure we have the channel_nums as a sorted list, even if
        we get weird things on input"""

        #If we received a tuple, list, dict, or array on input to
        #get_velocity or add_velocity, that object will be in the
        #first position of the arguments list. So grab that argument,
        #and make a list out of it.

        t = type(channel_nums[0])
        if (t == dict) or (t==list) or (t==tuple) or (t==np.ndarray):
            channels = channel_nums[0]
            channel_nums = list(channels)
        else:
            #Otherwise, the channel numbers were listed separately. So
            #make the whole thing a list.
            channel_nums = list(channel_nums)

        #Now sort them, so the channel numbers are in order when comparing
        #to other Velocity objects.
        channel_nums.sort()
        return channel_nums


    def list_params(self):
        '''Lists information about the shot'''
        print "Shot number: %d" % self.number
        print "Component speeds: {%g, %g, %g, %g RPM}" % (self.ICspeed,
                                                          self.IRspeed,
                                                          self.ORspeed,
                                                          self.OCspeed)
        print "Shot length: %gs, UDV Delay: %gs" % (self.shot_length,
                                                    self.udv_delay)
        print "Field delay: %gs, Field length: %gs" % (self.field_delay,
                                                       self.field_length)
        field = self.current*2.8669
        print "%gA applied current -> %gG" % (self.current,
                                              field)
        
    
class ChannelData:
    """A class for raw data from an individual channel.
    
    On __init__, parameters are found from the parent Shot and from
    shot_params.py for the desired channel. The raw data from the
    channel is then read in using
    read_ultrasound_new.read_ultrasound().  Transformations from the
    measurement depth to the measurement location in cylindrical
    coordinates are also done."""
    
    def __init__(self, shot, channel_num):
        '''Initialize a ChannelData object.

        Note that shot is a Shot object, which must be created
        before. Ideally, this function is only run from
        Shot.add_channel_data().'''

        if(not(shot.channels_used.__contains__(channel_num))):
            raise ValueError("Shot %d does not use channel %d" % (shot.number,
                                                                  channel_num))

        #Get a pointer back to our parent Shot.
        self.shot = shot
        
        #Read in the data from the UDV file
        if(not(os.path.exists(shot.filename))):
            raise ValueError('Data file %s does not exist.' % self.filename)

        data = rudv.read_ultrasound(shot.filename, channel_num,
                                    verbose=0)

        self.velocity = data['velocity']
        self.echo = data['echo']
        self.energy = data['energy']
        self.depth = data['depth']
        self.time = data['time']
        self.channel = data['channel']
        self.maxvelocity = data['maxvelocity']
        

        #Now grab the shot parameters from the database.
        params = sp.shot_params[shot.number]
        
        if(params.__contains__('trouble_flag')):
            print "Shot %d has trouble_flag set. Check notebook." % shot.number

        #Pick out the transducer mounting parameters to correspond to this
        #channel
        channel_idx = params['channels'].index(channel_num)
        
        self.A = params['As'][channel_idx]
        self.B = params['Bs'][channel_idx]
        self.offset = params['offsets'][channel_idx]
        self.port = params['ports'][channel_idx]

        
        self.time_points = self.time.size
        self.spatial_points = self.depth.size

        #Now run some routines to unwrap the aliased velocity, and to find
        #the location of each measurement.        
        self.calculate_radius()
        self.calculate_azimuth()
        self.calculate_height()
        self.unwrap_velocity()

    def unwrap_velocity(self, threshold=1.5):
        '''Adds the unwrapped velocity to the channel information using
        the specified threshold.'''
        #Add the unwrapped velocity to the channel information
        self.unwrapped_velocity = np.zeros(self.velocity.shape)
        self.unwrap_threshold = threshold
    
        maxvelocity = self.maxvelocity
    
        for j in range(0, self.time_points):
            #Define an array describing the number of cumulative phase shifts
            #from the face of the transducer to the current radius. Iterate
            #along, adding one when we jump 2\pi, and subtracting one when
            #we go back the other way.
            #We don't start counting until after a radius of 19.5cm, to avoid
            #problems with noise near the outer cylinder.
            wraps = np.zeros(self.spatial_points)
            first_idx = self.get_index_near_radius(19.5)
            for i in range(first_idx, self.spatial_points):
                if (self.velocity[j, i] -
                    self.velocity[j, i-1]) < -threshold*maxvelocity:
                    wraps[i] = wraps[i-1] + 1
                elif (self.velocity[j, i] -
                      self.velocity[j, i-1]) > threshold*maxvelocity:
                    wraps[i] = wraps[i-1] -1
                else:
                    wraps[i] = wraps[i-1]
            #Every 2\pi phase shift corresponds to a shift in the velocity
            #of 2*maxvelocity. So calculate and apply the appropriate
            #velocity correction based on the number of 2\pi phase shifts
            #at each radius.
            v_correction = wraps*2.0*maxvelocity
            self.unwrapped_velocity[j,:] = self.velocity[j,:] + v_correction
    
    def calculate_radius(self):
        '''Calculate the radial location of the measured points'''
        d = self.depth - self.offset
        self.r = np.zeros(self.depth.size)

        sinA = math.sin(degstorads(self.A))
        cosA = math.cos(degstorads(self.A))
        sinB = math.sin(degstorads(self.B))
        for i in range(0,d.size):
            self.r[i] = math.sqrt((d[i]*sinA*sinB)**2 + (r2 - d[i]*cosA)**2)
    
    def calculate_azimuth(self):
        '''Calculate the azimuthal location of the measured points'''
        d = self.depth - self.offset
        self.azimuth = np.zeros(self.depth.size)
        azimuthoffset = sp.ports[self.port]['theta']

        sinA = math.sin(degstorads(self.A))
        cosA = math.cos(degstorads(self.A))
        sinB = math.sin(degstorads(self.B))
        
        for i in range(0,d.size):
            self.azimuth[i] = math.asin(d[i]*sinA*sinB/
                                        math.sqrt((d[i]*sinA*sinB)**2 +
                                                  (r2 - d[i]*cosA)**2))
            self.azimuth[i] = wrap_phase(self.azimuth[i] + azimuthoffset)    
    
    def calculate_height(self):
        '''Calculate the height of the measured points'''
        d = self.depth - self.offset
        self.z = np.zeros(self.depth.size)
        
        zoffset = sp.ports[self.port]['z']
        
        sinA = math.sin(degstorads(self.A))
        cosA = math.cos(degstorads(self.A))
        sinB = math.sin(degstorads(self.B))
        cosB = math.cos(degstorads(self.B))
        
        for i in range(0,d.size):
            self.z[i] = d[i]*sinA*cosB + zoffset

    def get_index_near_time(self, time):
        '''Find index in time_array of the element closest to the
        specified time'''
        return abs(self.time - time).argmin()

    def get_index_near_radius(self, radius):
        '''Find index in radius array of the element closest to the
        specified radius'''
        return abs(self.r - radius).argmin()

    def mean_t(self, t_start, t_end):
        """Find the mean over the specified time interval

        Returns a dictionary containing r, azimuth, z, depth,
        velocity, unwrapped_velocity, echo, and energy, where the
        value at each radius is the mean value over the specified time
        interval."""

        start_idx = self.get_index_near_time(t_start)
        end_idx = self.get_index_near_time(t_end)
        
        r = self.r.copy()
        azimuth = self.azimuth.copy()
        z = self.z.copy()
        depth = self.depth.copy()
        velocity = np.mean(self.velocity[start_idx:end_idx, :], axis=0)
        unwrapped_velocity = np.mean(self.unwrapped_velocity[start_idx:end_idx, :], axis=0)
        echo = np.mean(self.echo[start_idx:end_idx, :], axis=0)
        energy = np.mean(self.energy[start_idx:end_idx, :], axis=0)
        
        return {'r': r, 'azimuth': azimuth, 'z': z, 'depth': depth,
                'velocity': velocity,
                'unwrapped_velocity': unwrapped_velocity, 'echo': echo,
                'energy': energy}

    def median_t(self, t_start, t_end):
        """Find the median over the specified time interval

        Returns a dictionary containing r, azimuth, z, depth,
        velocity, unwrapped_velocity, echo, and energy, where the
        value at each radius is the median value over the specified
        time interval."""

        start_idx = self.get_index_near_time(t_start)
        end_idx = self.get_index_near_time(t_end)
        
        r = self.r.copy()
        azimuth = self.azimuth.copy()
        z = self.z.copy()
        depth = self.depth.copy()
        velocity = np.median(self.velocity[start_idx:end_idx, :], axis=0)
        unwrapped_velocity = np.median(self.unwrapped_velocity[start_idx:end_idx, :], axis=0)
        echo = np.median(self.echo[start_idx:end_idx, :], axis=0)
        energy = np.median(self.energy[start_idx:end_idx, :], axis=0)
        
        return {'r': r, 'azimuth': azimuth, 'z': z, 'depth': depth,
                'velocity': velocity,
                'unwrapped_velocity': unwrapped_velocity, 'echo': echo,
                'energy': energy}

    def list_params(self):
        '''Lists information about the channel'''
        print "Shot: %d, Channel: %d, Port: %d" % (self.shot.number,
                                                   self.channel,
                                                   self.port)
        print "A = %g, B = %g, offset = %gmm" % (self.A,
                                                 self.B,
                                                 self.offset)
        print "UDV delay: %gs, Data-taking time: %gs" % (self.shot.udv_delay,
                                                         self.time[-1])

    def duplicate(self):
        dup_chan = ChannelData(self.shot, self.channel)
        return dup_chan


class Velocity():
    """A class for processed velocity measurements.

    These are distinct from the velocities in the Channel class
    because the velocities here are processed and presented in the
    v_r, v_theta, and v_z components.  __init__() tries to be smart
    about which generation routine to call based on the number of
    channels presented."""
    def __init__(self, shot, channel_nums, m=0, period=0):
        """Creates a Velocity object

        Creates a new Velocity object based on the channel numbers
        specified in the list channel_nums. Tries to be smart about
        selecting generation methods, based on the number of channels
        required and whether or not a non-zero m has been
        specified."""

        self.shot = shot
        self.progenitors = []

        #Make sure we've been given a reasonable number of channels.
        if (len(channel_nums) < 1) or (len(channel_nums) > 3):
            raise ValueError("Can't generate velocity from %d measurements" % len(channel_nums))


        #Make sure period is cast right, and make sure it is in
        #reasonable bounds.
        period = float(period)
        if (m != 0) and (period <= 0):
            raise ValueError("In call to Velocity.__init__(), period must be > 0 if m!=0")
        
        #Put all of the channel objects in the progenitors list.
        for channel_num in channel_nums:
            try:
                channel = self.shot.get_channel(channel_num)
            except:
                raise
            self.progenitors.append(channel)

        #Now call the correct generation method for each situation.
        if len(channel_nums) == 1:
            if (m==0):
                self.m = 0
                self.period = 0
                self.gen_velocity_one_transducer(self.progenitors[0])
            else:
                self.m = m
                self.period = period
                self.gen_velocity_one_transducer_nonaxi(self.progenitors[0])
        elif len(channel_nums) == 2:
            if (m==0):
                self.m = 0
                self.period = 0
                self.gen_velocity_two_transducers(self.progenitors[0],
                                                  self.progenitors[1])
            else:
                self.m = m
                self.period = period
                self.gen_velocity_two_transducers_nonaxi(self.progenitors[0],
                                                         self.progenitors[1])
        elif len(channel_nums) == 3:
            self.m = 0
            self.period = 0
            self.gen_velocity_three_transducers(self.progenitors[0],
                                                self.progenitors[1],
                                                self.progenitors[2])
        else:
            raise ValueError("Can't generate velocity from %d measurements" % len(channel_nums))


    def gen_velocity_one_transducer(self, channel):
        '''Generate velocity from a single transducer.

        If it is purely radial or purely vertical, a purely radial or
        vertical velocity is created.  Otherwise, the velocity is
        assumed to be in the azimuthal direction, and the appropriate
        angle corrections are applied to the velocity.'''
        
        self.time = channel.time.copy()
        self.r = channel.r.copy()
        self.azimuth = channel.azimuth.copy()
        self.z = channel.z.copy()
        

        if (((channel.B == 0) or (channel.B == -180) or (channel.B == 180)) and
            (channel.A == 90)):
            #This thing is just pointed vertically, so just use the unwrapped
            #velocity and the the position from the original channel
            self.vr = np.ones(channel.unwrapped_velocity.shape)*np.nan
            self.vtheta = np.ones(channel.unwrapped_velocity.shape)*np.nan
            self.vz = (channel.unwrapped_velocity/
                       math.cos(degstorads(channel.B)))
        elif (channel.A == 0):
            #In the unlikely event that we got this dead on in the radial
            #direction
            self.vr = -1.0*channel.unwrapped_velocity
            self.vtheta = np.ones(channel.unwrapped_velocity.shape)*np.nan
            self.vz = np.ones(channel.unwrapped_velocity.shape)*np.nan
        else:
            #Otherwise, just assume the velocity is in the azimuthal direction
            self.vr = np.ones(channel.unwrapped_velocity.shape)*np.nan
            self.vtheta = np.zeros(channel.unwrapped_velocity.shape)
            self.vz = np.ones(channel.unwrapped_velocity.shape)*np.nan

            sinA = math.sin(degstorads(channel.A))
            cosA = math.cos(degstorads(channel.A))
            sinB = math.sin(degstorads(channel.B))
            cosB = math.cos(degstorads(channel.B))
            d = channel.depth - channel.offset

            #Calculate the the correction factor needed at each radius
            anglefactor = np.zeros(self.r.size)
            
            for i in range(0, self.r.size):
                anglefactor[i] = (math.sqrt(1-sinA**2*cosB**2)*
                                  math.sin(math.atan(sinA*sinB/cosA) +
                                           math.asin(d[i]*sinA*sinB/
                                                     self.r[i])))
                
            #Now iterate over every time, applying the correction factor
            #and also adding offset due to the transducer motion to find
            #the velocity in the lab frame.
            for i in range(0, self.time.size):
                self.vtheta[i,:] = ((channel.unwrapped_velocity[i,:]/
                                     anglefactor) +
                                    self.r*rpmtorads(self.shot.OCspeed))
        #Now before we leave, reverse these arrays so that they're in
        #smallest-radius-first order, since this matches better with what
        #we do everywhere else.
        self.r = self.r[::-1]
        self.azimuth = self.azimuth[::-1]
        self.z = self.z[::-1]
        self.vr = self.vr[:,::-1]
        self.vtheta = self.vtheta[:,::-1]
        self.vz = self.vz[:,::-1]

    def gen_velocity_one_transducer_nonaxi(self, channel, knotsperperiod=6):
        '''Generate nonaxisymmetric velocity from a single transducer

        Find the velocity fields using one transducer, assuming a
        nonaxisymmetric velocity distribution, with m and period
        provided in the call to __init__() (and probably to the call
        to Shot.get_velocity(). Assumes that we are only dealing with
        azimuthal velocities for now. Note that this method
        essentially corrects for the azimuthal offset along a
        measurement chord, making each measurement appear to be made
        at theta=0.'''
        #Create a copy of the original channel object. We're going to make
        #changes to the data in this thing to pass to
        #gen_velocity_one_transducers(), but we of course don't want to
        #modify the original channel.
        tempchannel = deepcopy(channel)

        #Due to the shifted azimuthal location of each measurement, each
        #measurement at the same time along the UDV beam is at a different
        #phase of the wave, phase = k\cdotx - \omega t. But we want to
        #transform everything to a system where it is as if we had made
        #each measurement at the same time and at the same azimuthal location.
        #To find the required time shift in the signal for that to happen,
        #we equate the phase of the measurement made, with the desired result
        #m(\theta + \theta_offset) - \omega t = m \theta - \omega(t+t_shift)
        #So we must offset the time by an amount -m\theta_shift*period/(2*pi).
        #The maximum amount that the time base will have to be shifted in
        #either direction is m*period/2, so we'll trim that amount from
        #each of the time arrays to make sure that we'll always be
        #interpolating between measured points.
        
        #Also, choose a dt such that m*period/dt = 200. We're upsampling
        #here so that when we go to plot this on the r-theta plane,
        #we have an easier time of it.
        dt = self.m*self.period/200.0
        time_buffer = self.m*self.period/2.0
        tempchannel.time = np.arange(tempchannel.time[0] + time_buffer,
                                     tempchannel.time[-1] - time_buffer, dt)

        #Now reset the velocity structures in each temp channel to zeros
        #of the appropriate size: Same number of spatial points, shorter
        #time base.
        tempchannel.velocity = np.zeros([len(tempchannel.time),
                                         len(tempchannel.depth)])
        tempchannel.unwrapped_velocity = np.zeros([len(tempchannel.time),
                                                   len(tempchannel.depth)])

        #Now go through each position of each of these velocity structures,
        #make a fit, and interpolate onto the new time structure. We use
        #explicit knots, with the number set by knotsperperiod, to get
        #an appropriate amount of smoothing.


        for i in range(0, len(tempchannel.depth)):
            toffset = self.m*channel.azimuth[i]*self.period/(2*math.pi)
            knots = np.linspace(channel.time[1] - toffset,
                                channel.time[-2] - toffset,
                                num=knotsperperiod*int((channel.time[-2] -
                                                        channel.time[1]) /
                                                       self.period))
            
            f = LSQUnivariateSpline((channel.time - toffset),
                                    channel.velocity[:, i],
                                    knots, k=3)
            tempchannel.velocity[:,i] = f(tempchannel.time)

            f = LSQUnivariateSpline((channel.time - toffset),
                                    channel.unwrapped_velocity[:, i],
                                    knots, k=3)
            tempchannel.unwrapped_velocity[:,i] = f(tempchannel.time)
        
        
        #Just for good form, reset the azimuth in both cases to zero, since
        #we have effectively put every measurement at the same azimuth.
        tempchannel.azimuth = np.zeros(len(tempchannel.depth))
        
        #Okay, pass the channel to gen_velocity_one_transducer().
        self.gen_velocity_one_transducer(tempchannel)
        #We're done with the fake channel, so get rid of it.
        del(tempchannel)

    def gen_velocity_two_transducers(self, ch1, ch2, radialknots=30):
        '''Generate velocity from two transducers.

        Currently assumes we are just getting contributions from v_r
        and v_theta'''
                
        #Find the index of the deepest point (smallest radius)
        ch1_last_idx = ch1.r.argmin()
        ch2_last_idx = ch2.r.argmin()
        
        #First find out which has the least radial penetration, and use that
        #as the definitive radial coordinate. This avoids radii where only
        #one channel has information
        #Also reverse the array, so smaller radii are first.
        if (ch1.r.min() > ch2.r.min()):
            use_ch1_r = True
            self.r = ch1.r[0:ch1_last_idx][::-1]
        else:
            use_ch1_r = False
            self.r = ch2.r[0:ch2_last_idx][::-1]
        
        self.time = ch1.time.copy()
        
        #With two transducers, it's less clear what the z and azimuth
        #coordinates should be. Just make them nans.
        self.z = np.ones(self.r.size)*np.nan
        self.azimuth = np.ones(self.r.size)*np.nan

        
        self.vr = np.zeros((self.time.size, self.r.size))
        self.vtheta = np.zeros((self.time.size, self.r.size))
        self.vz = np.ones((self.time.size, self.r.size))*np.nan

        #Set up some temporary arrays to store the velocities
        ch1_v = np.zeros((self.time.size, self.r.size))
        ch2_v = np.zeros((self.time.size, self.r.size))

        #Now interpolate and resample the velocity onto the same radial grid,
        #again keeping in mind that we need to reverse these arrays as inputs
        #into the interpolation routines, so that smaller measured radii
        #are first. Now everything in ch1_v, ch2_v and self.r will
        #be stored from smaller radii to larger.
        for i in range (0, self.time.size):
            if(use_ch1_r):
                knots = np.linspace(ch2.r[ch2_last_idx-2], ch2.r[1],
                                    num=radialknots)
                ch1_v[i,:] = ch1.unwrapped_velocity[i,0:ch1_last_idx][::-1]
                f = LSQUnivariateSpline(ch2.r[0:ch2_last_idx][::-1],
                                        ch2.unwrapped_velocity[i,0:ch2_last_idx][::-1],
                                        knots, k=3)
                ch2_v[i,:] = f(self.r)
            else:
                knots = np.linspace(ch1.r[ch1_last_idx-2], ch1.r[1],
                                    num=radialknots)
                ch2_v[i,:] = ch2.unwrapped_velocity[i,0:ch2_last_idx][::-1]
                f = LSQUnivariateSpline(ch1.r[0:ch1_last_idx][::-1],
                                        ch1.unwrapped_velocity[i,0:ch1_last_idx][::-1],
                                        knots, k=3)
                ch1_v[i,:] = f(self.r)

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
        sinA1 = math.sin(degstorads(ch1.A))
        cosA1 = math.cos(degstorads(ch1.A))
        sinB1 = math.sin(degstorads(ch1.B))
        cosB1 = math.cos(degstorads(ch1.B))
        sinA2 = math.sin(degstorads(ch2.A))
        cosA2 = math.cos(degstorads(ch2.A))
        sinB2 = math.sin(degstorads(ch2.B))
        cosB2 = math.cos(degstorads(ch2.B))

        alpha1 = math.atan(sinA1*sinB1/cosA1)
        alpha2 = math.atan(sinA2*sinB2/cosA2)

        T = np.zeros([2,2])

        for i in range(0, self.r.size):
            r = self.r[i]
            #Set up the transformation matrix
            d1 = ((r2*cosA1 - math.sqrt(r**2*(sinA1**2*sinB1**2 + cosA1**2) -
                                        r2**2*sinA1**2*sinB1**2)) /
                  (sinA1**2*sinB1**2 + cosA1**2))
            d2 = ((r2*cosA2 - math.sqrt(r**2*(sinA2**2*sinB2**2 + cosA2**2) -
                                        r2**2*sinA2**2*sinB2**2)) /
                  (sinA2**2*sinB2**2 + cosA2**2))
            theta1 = math.asin(d1*sinA1*sinB1/r)
            theta2 = math.asin(d2*sinA2*sinB2/r)
            xi1 = alpha1 + theta1
            xi2 = alpha2 + theta2

            T[0,0] = -math.sqrt(1 - sinA1**2*cosB1**2)*math.cos(xi1)
            T[0,1] = math.sqrt(1 - sinA1**2*cosB1**2)*math.sin(xi1)
            T[1,0] = -math.sqrt(1 - sinA2**2*cosB2**2)*math.cos(xi2)
            T[1,1] = math.sqrt(1 - sinA2**2*cosB2**2)*math.sin(xi2)

            #Now invert the matrix so we can apply it to the measured
            #velocities
            Tinv = np.linalg.inv(T)

            #Now cycle through every time point at this radius,
            #and dot the inverted transformation matrix into the
            #measurements to find v_r and v_theta
            for j in range(0, self.time.size):
                [self.vr[j,i], self.vtheta[j,i]] = np.dot(Tinv,
                                                          [ch1_v[j,i],
                                                           ch2_v[j,i]])
                #Add the azimuthal velocity offset due to the transducer
                #motion to find the velocity in the lab frame.
                self.vtheta[j,i] = (self.vtheta[j,i] +
                                    rpmtorads(self.shot.OCspeed)*r)

    def gen_velocity_two_transducers_nonaxi(self, ch1, ch2, knotsperperiod=6):
        '''Generate nonaxisymmetric velocity using two transducers

        Find the velocity fields using two transducers, assuming a
        nonaxisymmetric velocity distribution, with m and period
        provided in the call to __init__() (and probably to the call
        to Shot.get_velocity(). Decomposes only into v_r and v_theta.'''
        
        #Create copies of the original channel objects. We're going to make
        #changes to the data in these things to pass to
        #gen_velocity_two_transducers(), but we of course don't want to
        #modify the original channels.
        tempch1 = deepcopy(ch1)
        tempch2 = deepcopy(ch2)
        
        #Due to the shifted azimuthal location of each measurement, each
        #measurement at the same time along the UDV beam is at a different
        #phase of the wave, phase = k\cdotx - \omega t. But we want to
        #transform everything to a system where it is as if we had made
        #each measurement at the same time and at the same azimuthal location.
        #To find the required time shift in the signal for that to happen,
        #we equate the phase of the measurement made, with the desired result
        #m(\theta + \theta_offset) - \omega t = m \theta - \omega(t+t_shift)
        #So we must offset the time by an amount -m\theta_shift*period/(2*pi).
        #The maximum amount that the time base will have to be shifted in
        #either direction is m*period/2, so we'll trim that amount from
        #each of the time arrays to make sure that we'll always be
        #interpolating between measured points.

        #Also, choose a dt such that m*period/dt = 200. We're upsampling
        #here so that when we go to plot this on the r-theta plane,
        #we have an easier time of it.
        
        #Use a common time base for both channels
        dt = abs(self.m)*self.period/200.0
        time_buffer = abs(self.m)*self.period/2.0
        tempch1.time = np.arange(tempch1.time[0] + time_buffer,
                                 tempch1.time[-1] - time_buffer, dt)
        tempch2.time = tempch1.time.copy()

        #Now reset the velocity structures in each temp channel to zeros
        #of the appropriate size: Same number of spatial points, shorter
        #time base.
        tempch1.velocity = np.zeros([len(tempch1.time), len(tempch1.depth)])
        tempch2.velocity = np.zeros([len(tempch2.time), len(tempch2.depth)])
        tempch1.unwrapped_velocity = np.zeros([len(tempch1.time),
                                               len(tempch1.depth)])
        tempch2.unwrapped_velocity = np.zeros([len(tempch2.time),
                                               len(tempch2.depth)])

        #Now go through each position of each of these velocity structures,
        #make a fit, and interpolate onto the new time structure. We use
        #explicit knots, with the number set by knotsperperiod, to get
        #an appropriate amount of smoothing.

        for i in range(0, len(tempch1.depth)):
            toffset = self.m*ch1.azimuth[i]*self.period/(2*math.pi)
            knots = np.linspace(ch1.time[1] - toffset,
                                ch1.time[-2] - toffset,
                                num=knotsperperiod*int((ch1.time[-2] -
                                                        ch1.time[1]) /
                                                       self.period))

            f = LSQUnivariateSpline((ch1.time - toffset),
                                    ch1.velocity[:, i],
                                    knots, k=3)
            tempch1.velocity[:,i] = f(tempch1.time)

            f = LSQUnivariateSpline((ch1.time - toffset),
                                    ch1.unwrapped_velocity[:, i],
                                    knots, k=3)
            tempch1.unwrapped_velocity[:,i] = f(tempch1.time)
        
        
        for i in range(0, len(tempch2.depth)):
            toffset = self.m*ch2.azimuth[i]*self.period/(2*math.pi)
            knots = np.linspace(ch2.time[1] - toffset,
                                ch2.time[-2] - toffset,
                                num=knotsperperiod*int((ch2.time[-2] -
                                                        ch2.time[1]) /
                                                       self.period))

            f = LSQUnivariateSpline((ch2.time - toffset),
                                    ch2.velocity[:, i],
                                    knots, k=3)
            tempch2.velocity[:,i] = f(tempch2.time)

            f = LSQUnivariateSpline((ch2.time - toffset),
                                    ch2.unwrapped_velocity[:, i],
                                    knots, k=3)
            tempch2.unwrapped_velocity[:,i] = f(tempch2.time)

        
        #Just for good form, reset the azimuth in both cases to zero, since
        #we have effectively put every measurement at the same azimuth.
        tempch1.azimuth = np.zeros(len(tempch1.depth))
        tempch2.azimuth = np.zeros(len(tempch2.depth))
        
        #Okay, pass these channels to gen_velocity_two_transducers().
        self.gen_velocity_two_transducers(tempch1, tempch2)
        #We're done with our fake channels, so get rid of them.
        del(tempch1)
        del(tempch2)

    def get_index_near_time(self, time):
        '''Find index in the time_array of element closest to the 
        specified time'''
        return abs(self.time - time).argmin()
                  
    def get_index_near_radius(self, radius):
        '''Find index in radius array of the element closest to the
        specified radius'''
        return abs(self.r - radius).argmin()

    def mean_t(self, t_start, t_end):
        """Find the mean velocities over the specified time interval

        Returns a dictionary containing r, z, azimuth, vr, vtheta, and
        vz, where the value of the velocity at each radius is the mean
        value over the specified time interval."""

        start_idx = self.get_index_near_time(t_start)
        end_idx = self.get_index_near_time(t_end)
        
        r = self.r.copy()
        azimuth = self.azimuth.copy()
        z = self.z.copy()
        vr = np.mean(self.vr[start_idx:end_idx, :], axis=0)
        vtheta = np.mean(self.vtheta[start_idx:end_idx, :], axis=0)
        vz = np.mean(self.vz[start_idx:end_idx, :], axis=0)
        
        return {'r': r, 'azimuth': azimuth, 'z': z, 'vr': vr,
                'vtheta': vtheta, 'vz': vz}

    def median_t(self, t_start, t_end):
        """Find the median velocities over the specified time interval

        Returns a dictionary containing r, z, azimuth, vr, vtheta, and
        vz, where the value of the velocity at each radius is the
        median value over the specified time interval."""

        start_idx = self.get_index_near_time(t_start)
        end_idx = self.get_index_near_time(t_end)
        
        r = self.r.copy()
        azimuth = self.azimuth.copy()
        z = self.z.copy()
        vr = np.median(self.vr[start_idx:end_idx, :], axis=0)
        vtheta = np.median(self.vtheta[start_idx:end_idx, :], axis=0)
        vz = np.median(self.vz[start_idx:end_idx, :], axis=0)
        
        return {'r': r, 'azimuth': azimuth, 'z': z, 'vr': vr,
                'vtheta': vtheta, 'vz': vz}
    
    def list_progenitor_params(self):
        '''List information about the channels that were combined to
        create a Velocity object.'''
        num_progenitors = len(self.progenitors)
        print "Derived from %d progenitor(s)" % num_progenitors
        for i in range(0, num_progenitors):
            progenitor = self.progenitors[i]
            print "%d: A=%g, B=%g, port=%d" % (i,
                                               progenitor.A,
                                               progenitor.B,
                                               progenitor.port)

    def get_progenitor_channels(self):
        """Return a list of the channel numbers used to make a
        Velocity object."""
        
        progenitor_channels = []
        for progenitor in self.progenitors:
            progenitor_channels.append(progenitor.channel)
        progenitor_channels.sort()
        return progenitor_channels
    
    def used_channel(self, channel_num):
        """Boolean function that evaluates whether a specified
        channel_num was used to form this velocity."""

        #Check to see if this channel is present in our progenitors
        if self.get_progenitor_channels().__contains__(channel_num):
            return True
        else:
            return False

class CouetteProfile():
    """A simple class used to calculate and store the ideal Couette profile
    for the parameters in a Shot object."""
    
    def __init__(self, shot):
        self.shot = shot
        self.r = np.linspace(r1, r2, 200)
        self.vtheta = np.zeros(self.r.size)
        v1 = rpmtorads(shot.ICspeed)*r1
        v2 = rpmtorads(shot.OCspeed)*r2
        self.a = (v1*r1 - v2*r2)/(r1**2 - r2**2)
        self.b = (v1*r1 - self.a*r1**2)

        for i in range(0, self.vtheta.size):
            self.vtheta[i] = self.a*self.r[i] + self.b/self.r[i]


class ShotList():
    """A class for managing groups of Shots.

    Maintains a list of processed Shots. Normally, only the get_shot()
    method should be required to access this list. But shots can also be
    removed with the del_shot() method."""
    
    def __init__(self):
        self.shots = []

    def get_shot(self, shot_num):
        """Returns a Shot object for the specified shot number."""

        #Check to see if we've created this shot before, and, if so,
        #return it
        for shot in self.shots:
            if (shot.number == shot_num):
                return shot

        #Looks like we don't have it yet, so let's add it.
        return self.add_shot(shot_num)

    def add_shot(self, shot_num):
        """Adds and returns a Shot object for the specified shot number."""
        
        #Try to create this shot, checking to make sure that Shot.__init__
        #doesn't return False.
        try:
            shot=Shot(shot_num)
        except ValueError as e:
            print "Error adding shot to list."
            print e
            return None
        
        self.shots.append(shot)
        return shot
    
    def del_shot(self, shot_num):
        """Deletes Shot object from the list for the specified shot number."""
        
        for shot in self.shots:
            if (shot.number == shot_num):
                self.shots.remove(shot)


def update_shot_params():
    """Update the shot_params database after changes to the database."""
    reload(sp)


def wrap_phase(angle):
    """Make phase fit in the range -pi to pi."""
    while (angle > math.pi):
        angle = angle - 2.0*math.pi

    while (angle < -math.pi):
        angle = angle + 2.0*math.pi

    return angle
