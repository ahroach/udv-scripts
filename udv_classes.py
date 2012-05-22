import read_ultrasound_new as rudv
from scipy.interpolate import UnivariateSpline
from copy import deepcopy
import shot_params as sp
import shot_db_ops as sdo
from numpy import *

'''Provides Shot, Channel, and Velocity objects to be used in processing
UDV data. Also provides get_shot() (and the associated add_shot()) and
del_shot() functions for managing a list of already-processed shots.'''

r1 = 7.06
r2 = 20.30
rpmtorads = lambda x: x*2.0*pi/60.0
degstorads = lambda x: x*pi/180.0

class Shot:
    def __init__(self, shot_num):
        '''Creates a new Shot object, looks up and adds shot parameters
        to the object, and runs add_channel_data() for all channels'''
        if(not(sp.shot_params.has_key(shot_num))):
            print "Error: Shot %d not in database." % shot_num
            return False
        
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
    
    def add_channel(self, channel_num):
        '''Adds and returns a ChannelData object corresponding to channel_num
        for this Shot.'''
        #Make sure this channel exists
        if(not(self.channels_used.__contains__(channel_num))):
            print "Error: Shot %d doesn't use channel %d." % (self.number,
                                                              channel_num)
            return False

        #And create it, adding the object to the channels dictionary
        self.channels[channel_num] = ChannelData(self, channel_num)
        return self.channels[channel_num]
    
    def get_velocity(self, channel_nums, m=0, period=0):
        '''Returns a Velocity object produced using the specified
        channel_nums for this Shot.'''
        channel_nums = self.sanitize_channel_nums_for_velocities(channel_nums)

        #Check to see if we've processed this velocity data before, and, if so,
        #return it

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
                return velocity

        #Otherwise add this new velocity set and return that.
        return self.add_velocity(channel_nums, m=m, period=period)

    def add_velocity(self, channel_nums, m=0, period=0):
        '''Adds and returns a Velocity object produced using channel_nums
        for this Shot.'''
        channel_nums = self.sanitize_channel_nums_for_velocities(channel_nums)
        
        #Make sure we actually have all of these channels.
        for channel_num in channel_nums:
            if(not(self.channels_used.__contains__(channel_num))):
                print "Error: Shot %d doesn't use channel %d." % (self.number,
                                                                  channel_num)
                return False

        
        self.velocities.append(Velocity(self, channel_nums, m, period))
        return self.velocities[-1]
    
    def del_velocity(self, channel_nums, m=0, period=0):
        '''Removes a Velocity object from a shot matching the specified
        parameters.'''
        channel_nums = self.sanitize_channel_nums_for_velocities(channel_nums)

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
            print "Error: Shot %d doesn't use channel %d" % (shot.number,
                                                             channel_num)
            return False

        #Get a pointer back to our parent Shot.
        self.shot = shot
        
        #Read in the data from the UDV file
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
        self.unwrap_velocity()
        self.calculate_radius()
        self.calculate_azimuth()
        self.calculate_height()

    def unwrap_velocity(self, threshold=1.5):
        '''Adds the unwrapped velocity to the channel information using
        the specified threshold.'''
        #Add the unwrapped velocity to the channel information
        self.unwrapped_velocity = zeros(self.velocity.shape)
        self.unwrap_threshold = threshold
    
        maxvelocity = self.maxvelocity
    
        for j in range(0, self.time_points):
            #Define an array describing the number of cumulative phase shifts
            #from the face of the transducer to the current radius. Iterate
            #along, adding one when we jump 2\pi, and subtracting one when
            #we go back the other way.
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
            #Every 2\pi phase shift corresponds to a shift in the velocity
            #of 2*maxvelocity. So calculate and apply the appropriate
            #velocity correction based on the number of 2\pi phase shifts
            #at each radius.
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

    def get_index_near_time(self, time):
        '''Find the index in the time_array of the element closest to the
        specified time'''
        return abs(self.time - time).argmin()

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

    def duplicate(self):
        dup_chan = ChannelData(self.shot, self.channel)
        return dup_chan

class Velocity():
    '''A class for processed velocity measurements. These are distinct from
    the velocities in the Channel class because the velocities here are
    processed and presented in the v_r, v_theta, and v_z components.
    __init__() tries to be smart about which generation routine to call based
    on the number of channels presented.'''
    def __init__(self, shot, channel_nums, m=0, period=0):
        '''Tries to be smart about selecting generation methods, based
        on the number of channels required and whether or not a non-zero
        m has been specified.'''
        self.shot = shot
        self.progenitors = []
    
        if size(channel_nums) == 0:
            print "Error: 0 channels presented to Velocity.__init__()."
            return None
        elif size(channel_nums) == 1:
            self.progenitors.append(self.shot.get_channel(channel_nums[0]))
            if (m==0):
                self.m = 0
                self.period = 0
                self.gen_velocity_one_transducer(self.progenitors[0])
            else:
                self.m = m
                self.period = period
                self.gen_velocity_one_transducer_nonaxi(self.progenitors[0])
        elif size(channel_nums) == 2:
            self.progenitors.append(self.shot.get_channel(channel_nums[0]))
            self.progenitors.append(self.shot.get_channel(channel_nums[1]))
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
        elif size(channel_nums) == 3:
            self.progenitors.append(self.shot.get_channel(channel_nums[0]))
            self.progenitors.append(self.shot.get_channel(channel_nums[1]))
            self.progenitors.append(self.shot.get_channel(channel_nums[2]))
            self.m = 0
            self.period = 0
            self.gen_velocity_three_transducers(self.progenitors[0],
                                                self.progenitors[1],
                                                self.progenitors[2])
        else:
            print "Error: Can't generate velocity from %d measurements" % size(channel_nums)
            return None

    def gen_velocity_one_transducer(self, channel):
        '''Generate velocity from a single transducer. If it is purely radial
        or purely vertical, a purely radial or vertical velocity is created.
        Otherwise, the velocity is assumed to be in the azimuthal direction,
        and the appropriate angle corrections are applied to the velocity.'''
        
        self.time = channel.time.copy()
        self.r = channel.r.copy()
        self.azimuth = channel.azimuth.copy()
        self.z = channel.z.copy()
        

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
            d = channel.depth - channel.offset

            #Calculate the the correction factor needed at each radius
            anglefactor = zeros(self.r.size)
            
            for i in range(0, self.r.size):
                anglefactor[i] = (sqrt(1-sinA**2*cosB**2)*
                                  sin(math.atan(sinA*sinB/cosA) +
                                      math.asin(d[i]*sinA*sinB/self.r[i])))
            
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

    def gen_velocity_one_transducer_nonaxi(self, channel):
        '''Find the velocity fields using one transducer, assuming a
        nonaxisymmetric velocity distribution, with m and period provided
        in the call to __init__() (and probably to the call to
        Shot.get_velocity(). Assumes that we are only dealing with azimuthal
        velocities for now. Note that this method essentially corrects
        for the azimuthal offset along a measurement chord, making each
        measurement appear to be made at \theta=0.'''
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
        dt = self.m*self.period/200
        time_buffer = self.m*self.period/2
        tempchannel.time = arange(tempchannel.time[0] + time_buffer,
                                  tempchannel.time[-1] - time_buffer, dt)

        #Now reset the velocity structures in each temp channel to zeros
        #of the appropriate size: Same number of spatial points, shorter
        #time base.
        tempchannel.velocity = zeros([len(tempchannel.time),
                                      len(tempchannel.depth)])
        tempchannel.unwrapped_velocity = zeros([len(tempchannel.time),
                                                len(tempchannel.depth)])

        #Now go through each position of each of these velocity structures,
        #make a fit, and interpolate onto the new time structure.
        
        for i in range(0, len(tempchannel.depth)):
            f = UnivariateSpline((channel.time -
                                  self.m*channel.azimuth[i]*
                                  self.period/(2*pi)),
                                 channel.velocity[:, i],
                                 k=3, s=0)
            tempchannel.velocity[:,i] = f(tempchannel.time)

            f = UnivariateSpline((channel.time -
                                  self.m*channel.azimuth[i]*
                                  self.period/(2*pi)),
                                 channel.unwrapped_velocity[:, i],
                                 k=3, s=0)
            tempchannel.unwrapped_velocity[:,i] = f(tempchannel.time)
        
        
        #Just for good form, reset the azimuth in both cases to zero, since
        #we have effectively put every measurement at the same azimuth.
        tempchannel.azimuth = zeros(len(tempchannel.depth))
        
        #Okay, pass the channel to gen_velocity_one_transducer().
        self.gen_velocity_one_transducer(tempchannel)
        #We're done with the fake channel, so get rid of it.
        del(tempchannel)

    def gen_velocity_two_transducers(self, ch1, ch2):
        '''Generate velocity from two transducers. Currently assumes we are
           just getting contributions from v_r and v_theta'''
                
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
        self.z = ones(self.r.size)*nan
        self.azimuth = ones(self.r.size)*nan

        
        self.vr = zeros((self.time.size, self.r.size))
        self.vtheta = zeros((self.time.size, self.r.size))
        self.vz = ones((self.time.size, self.r.size))*nan

        #Set up some temporary arrays to store the velocities
        ch1_v = zeros((self.time.size, self.r.size))
        ch2_v = zeros((self.time.size, self.r.size))

        #Now interpolate and resample the velocity onto the same radial grid,
        #again keeping in mind that we need to reverse these arrays as inputs
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
            #Set up the transformation matrix
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

            #Now invert the matrix so we can apply it to the measured
            #velocities
            Tinv = linalg.inv(T)

            #Now cycle through every time point at this radius,
            #and dot the inverted transformation matrix into the
            #measurements to find v_r and v_theta
            for j in range(0, self.time.size):
                [self.vr[j,i], self.vtheta[j,i]] = dot(Tinv,
                                                       [ch1_v[j,i],
                                                       ch2_v[j,i]])
                #Add the azimuthal velocity offset due to the transducer
                #motion to find the velocity in the lab frame.
                self.vtheta[j,i] = (self.vtheta[j,i] +
                                    rpmtorads(self.shot.OCspeed)*r)

    def gen_velocity_two_transducers_nonaxi(self, ch1, ch2):
        '''Find the velocity fields using two transducers, assuming a
        nonaxisymmetric velocity distribution, with m and period provided
        in the call to __init__() (and probably to the call to
        Shot.get_velocity(). Decomposes only into v_r and v_theta.'''
        #Create copies of the original channel objects. We're going to make
        #changes to the data in these things to pass to
        #gen_velocity_two_transducers(), but we of course don't want to
        #modify the original channels.
        tempch1 = deepcopy(ch1.duplicate)
        tempch2 = deepcopy(ch2.duplicate)
        
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
        dt = self.m*self.period/200
        time_buffer = self.m*self.period/2
        tempchannel.time = arange(tempchannel.time[0] + time_buffer,
                                  tempchannel.time[-1] - time_buffer, dt)

        #Now reset the velocity structures in each temp channel to zeros
        #of the appropriate size: Same number of spatial points, shorter
        #time base.
        tempch1.velocity = zeros([len(tempch1.time), len(tempch1.depth)])
        tempch2.velocity = zeros([len(tempch2.time), len(tempch2.depth)])
        tempch1.unwrapped_velocity = zeros([len(tempch1.time),
                                            len(tempch1.depth)])
        tempch2.unwrapped_velocity = zeros([len(tempch2.time),
                                            len(tempch2.depth)])

        #Now go through each position of each of these velocity structures,
        #make a fit, and interpolate onto the new time structure.

        for i in range(0, len(tempch1.depth)):
            f = UnivariateSpline((ch1.time -
                                  self.m*ch1.azimuth[i]*
                                  self.period/(2*pi)),
                                 ch1.velocity[:, i],
                                 k=3, s=0)
            tempch1.velocity[:,i] = f(tempch1.time)

            f = UnivariateSpline((ch1.time -
                                  self.m*ch1.azimuth[i]*
                                  self.period/(2*pi)),
                                 ch1.unwrapped_velocity[:, i],
                                 k=3, s=0)
            tempch1.unwrapped_velocity[:,i] = f(tempch1.time)
        
        
        for i in range(0, len(tempch2.depth)):
            f = UnivariateSpline((ch2.time -
                                  self.m*ch2.azimuth[i]*
                                  self.period/(2*pi)),
                                 ch2.velocity[:, i],
                                 k=3, s=0)
            tempch2.velocity[:,i] = f(tempch2.time)

            f = UnivariateSpline((ch2.time -
                                  self.m*ch2.azimuth[i]*
                                  self.period/(2*pi)),
                                 ch2.unwrapped_velocity[:, i],
                                 k=3, s=0)
            tempch2.unwrapped_velocity[:,i] = f(tempch2.time)

        
        #Just for good form, reset the azimuth in both cases to zero, since
        #we have effectively put every measurement at the same azimuth.
        tempch1.azimuth = zeros(len(tempch1.depth))
        tempch2.azimuth = zeros(len(tempch2.depth))
        
        #Okay, pass these channels to gen_velocity_two_transducers().
        self.gen_velocity_two_transducers(tempch1, tempch2)
        #We're done with our fake channels, so get rid of them.
        del(tempch1)
        del(tempch2)

    def get_index_near_time(self, time):
        '''Find the index in the time_array of the element closest to the
        specified time'''
        return abs(self.time - time).argmin()
                  
    def get_index_near_radius(self, radius):
        '''Find the index in the radius array of the element with r
        closest to the specified radius'''
        return abs(self.r - radius).argmin()
    
    def list_progenitors(self):
        '''List information about the channels that were combined to
        create a Velocity object.'''
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
        self.a = (v1*r1 - v2*r2)/(r1**2 - r2**2)
        self.b = (v1*r1 - self.a*r1**2)

        for i in range(0, self.vtheta.size):
            self.vtheta[i] = self.a*self.r[i] + self.b/self.r[i]


shots=[]
    
def get_shot(shot_num):
    '''Returns a Shot object for the specified shot number.'''
    
    #Check to see if we've created this shot before, and, if so,
    #return it
    for shot in shots:
        if (shot.number == shot_num):
            return shot
    
    #I guess we didn't find a shot that fits the bill. So let's add one.
    return add_shot(shot_num)

def add_shot(shot_num):
    '''Adds and returns a Shot object for the specified shot number.'''
    
    #Try to create this shot, checking to make sure that Shot.__init__
    #doesn't return False.
    shot = Shot(shot_num)
    if(shot):
        shots.append(shot)
        return shot

def del_shot(shot_num):
    '''Deletes Shot objects for the specified shot number.'''
    
    for shot in shots:
        if (shot.number == shot_num):
            shots.remove(shot)


def wrap_phase(angle):
    '''Make phase fit in the range -pi to pi.'''
    while (angle > pi):
        angle = angle - 2.0*pi

    while (angle < -pi):
        angle = angle + 2.0*pi

    return angle
