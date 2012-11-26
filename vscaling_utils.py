"""Get average measurements at a point

Used for finding the normalized, scaled velocities at a point. Uses
motor speed state and current measurements to properly do the normalizing
and scaling with errorbars, so we can't get these measurements from
the UDV data alone."""

import sys
sys.path.append("/u/aroach/udv-scripts")
import numpy
import motor_data
import mag_filter

motor_data.datapath="/p/mri/data/"

class AvgPointMeasurement:
    def __init__(self, velocity, r, t_start, t_end, daq_turnon_time=120):
        """Get one average point measurement

        Note that t_start and t_end are given in terms of the UDV time
        base. It is assumed that the magnetics time base begins 120 seconds
        into the shot. If this is not correct, daq_turnon_time must be
        must be adjusted."""
        
        self.r = r
        self.velocity = velocity
        self.shot = velocity.shot
        self.t_start = t_start
        self.t_end = t_end

        magdatapath = "/p/mri/data/%04i/" % self.shot.number
        t_upper, current_upper = \
                 mag_filter.get_timeseries(magdatapath,
                                           "Upper Current Sensor",
                                           t_final=10000)
        t_lower, current_lower = \
                 mag_filter.get_timeseries(magdatapath,
                                           "Upper Current Sensor",
                                           t_final=10000)
        
        upper_start_idx = abs(t_upper -
                              (t_start + self.shot.udv_delay -
                               daq_turnon_time)).argmin()
        upper_end_idx = abs(t_upper -
                            (t_end + self.shot.udv_delay -
                             daq_turnon_time)).argmin()
        lower_start_idx = abs(t_lower -
                              (t_start + self.shot.udv_delay -
                               daq_turnon_time)).argmin()
        lower_end_idx = abs(t_lower -
                            (t_end + self.shot.udv_delay -
                             daq_turnon_time)).argmin()
        self.currentavg = (current_upper[upper_start_idx:
                                         upper_end_idx].mean() +
                           current_lower[lower_start_idx:
                                         lower_end_idx].mean())
        self.currentstd = (current_upper[upper_start_idx:
                                         upper_end_idx].std() +
                           current_lower[lower_start_idx:
                                         lower_end_idx].std())
        
        self.vaavg = self.currentavg*2.8669/numpy.sqrt(4*numpy.pi*6.36)
        self.vastd = self.currentstd*2.8669/numpy.sqrt(4*numpy.pi*6.36)
        
        #Grab the motor data
        md = motor_data.MotorData(self.shot.number)

        #Average the inner cylinder speeds over the total length of the
        #the applied field.
        
        self.ICspeedavg = md.time_avg(self.shot.field_delay,
                                      (self.shot.field_delay +
                                       self.shot.field_length))['ICspeed']

        self.ICspeedstd = md.time_std(self.shot.field_delay,
                                      (self.shot.field_delay +
                                       self.shot.field_length))['ICspeed']

        self.vicavg = self.ICspeedavg*2*numpy.pi*7.06/60
        self.vicstd = self.ICspeedstd*2*numpy.pi*7.06/60

        #Average the outer cylinder speed over the time of the average
        #UDV measurement.
        #It turns out that the OC encoder sometimes has problems, so
        #use the OR encoder since the speeds are locked.

        self.OCspeedavg = md.time_avg((self.shot.udv_delay +
                                       t_start),
                                      (self.shot.udv_delay +
                                       t_end))['ORspeed']
        self.OCspeedstd = md.time_std((self.shot.udv_delay +
                                       t_start),
                                      (self.shot.udv_delay +
                                       t_end))['ORspeed']

        #Get the velocity measurements
        startidx = self.velocity.get_index_near_time(t_start)
        endidx = self.velocity.get_index_near_time(t_end)
        ridx = self.velocity.get_index_near_radius(r)

        self.vravg = self.velocity.vr[startidx:endidx, ridx].mean()
        self.vrstd = self.velocity.vr[startidx:endidx, ridx].std()
        self.vtavg = self.velocity.vtheta[startidx:endidx, ridx].mean() 
        self.vtstd = self.velocity.vtheta[startidx:endidx, ridx].std()

        #This is the amount of the required offset in the determined
        #azimuthal velocity due to variances in the OC speed from the assumed
        #value when calculating the velocities.

        self.OCspeedoffset = (self.OCspeedavg -
                              self.shot.OCspeed)*2*numpy.pi*self.r/60
        self.OCspeedoffsetstd = self.OCspeedstd*2*numpy.pi*self.r/60

        self.vtavg = self.vtavg + self.OCspeedoffset
        self.vtstd = numpy.sqrt(self.vtstd**2 +
                                self.OCspeedoffsetstd**2)

        #Now do the normalized quantities vt/vic
        self.vtnorm = self.vtavg/self.vicavg
        self.vtnormstd = self.vtnorm*numpy.sqrt(self.vtstd**2/self.vtavg**2 +
                                                self.vicstd**2/self.vicavg**2)
        self.vrnorm = self.vravg/self.vicavg
        self.vrnormstd = self.vrnorm*numpy.sqrt(self.vrstd**2/self.vravg**2 +
                                                self.vicstd**2/self.vicavg**2)

        #And the normalized alfven speed
        if (self.vaavg == 0):
            self.vanorm = 0
            self.vanormstd = 0
        else:
            self.vanorm = self.vaavg/self.vicavg
            self.vanormstd = (self.vanorm *
                              numpy.sqrt(self.vastd**2/self.vaavg**2 +
                                         self.vicstd**2/self.vicavg**2))

class AvgPointMeasurement_group():
    """A group of AvgPointMeasurements"""
    def __init__(self, *measurements, **params):
        """Get a group of average point measurements

        *measurements is any number of tuples where the first item is a
        velocity object, the second item is the start time, and the
        third item is the end time.

        Legal **params are 'r' (default 14),
        and 'daq_turnon_time' (default 120)
        """

        self.r = params.pop('r', 14)
        self.daq_turnon_time = params.pop('daq_turnon_time', 120)

        self.avgpointmeasurements = []
        for measurement in measurements:
            apm = AvgPointMeasurement(measurement[0], self.r,
                                      measurement[1], measurement[2],
                                      daq_turnon_time=self.daq_turnon_time)    
            self.avgpointmeasurements.append(apm)
        
        self.vanorms = numpy.zeros(len(self.avgpointmeasurements))
        self.vanormstds = numpy.zeros(len(self.avgpointmeasurements))
        self.vrnorms = numpy.zeros(len(self.avgpointmeasurements))
        self.vrnormstds = numpy.zeros(len(self.avgpointmeasurements))
        self.vtnorms = numpy.zeros(len(self.avgpointmeasurements))
        self.vtnormstds = numpy.zeros(len(self.avgpointmeasurements))
        self.vravgs = numpy.zeros(len(self.avgpointmeasurements))
        self.vrstds = numpy.zeros(len(self.avgpointmeasurements))
        self.vtavgs = numpy.zeros(len(self.avgpointmeasurements))
        self.vtstds = numpy.zeros(len(self.avgpointmeasurements))
        self.vocavgs = numpy.zeros(len(self.avgpointmeasurements))
        self.vocstds = numpy.zeros(len(self.avgpointmeasurements))
        self.vicavgs = numpy.zeros(len(self.avgpointmeasurements))
        self.vicstds = numpy.zeros(len(self.avgpointmeasurements))
        self.currentavgs = numpy.zeros(len(self.avgpointmeasurements))
        self.currentstds = numpy.zeros(len(self.avgpointmeasurements))

        for i in range(0, len(self.avgpointmeasurements)):
            self.vanorms[i] = self.avgpointmeasurements[i].vanorm
            self.vanormstds[i] = self.avgpointmeasurements[i].vanormstd
            self.vrnorms[i] = self.avgpointmeasurements[i].vrnorm
            self.vrnormstds[i] = self.avgpointmeasurements[i].vrnormstd
            self.vtnorms[i] = self.avgpointmeasurements[i].vtnorm
            self.vtnormstds[i] = self.avgpointmeasurements[i].vtnormstd
            self.vravgs[i] = self.avgpointmeasurements[i].vravg
            self.vrstds[i] = self.avgpointmeasurements[i].vrstd
            self.vtavgs[i] = self.avgpointmeasurements[i].vtavg
            self.vtstds[i] = self.avgpointmeasurements[i].vtstd
            self.vocavgs[i] = self.avgpointmeasurements[i].OCspeedavg
            self.vocstds[i] = self.avgpointmeasurements[i].OCspeedstd
            self.vicavgs[i] = self.avgpointmeasurements[i].vicavg
            self.vicstds[i] = self.avgpointmeasurements[i].vicstd
            self.currentavgs[i] = self.avgpointmeasurements[i].currentavg
            self.currentstds[i] = self.avgpointmeasurements[i].currentstd


class AvgProfile:
    def __init__(self, velocity, t_start, t_end, daq_turnon_time=120):
        """Get one average point measurement
        
        Note that t_start and t_end are given in terms of the UDV time
        base. It is assumed that the magnetics time base begins 120 seconds
        into the shot. If this is not correct, daq_turnon_time must be
        must be adjusted."""
        
        self.r = velocity.r
        self.velocity = velocity
        self.shot = velocity.shot
        self.t_start = t_start
        self.t_end = t_end

        magdatapath = "/p/mri/data/%04i/" % self.shot.number
        t_upper, current_upper = mag_filter.get_timeseries(magdatapath,
                                                           "Upper Current Sensor",
                                                           t_final=10000)
        t_lower, current_lower = mag_filter.get_timeseries(magdatapath,
                                                           "Upper Current Sensor",
                                                           t_final=10000)
    
        upper_start_idx = abs(t_upper -
                              (t_start + self.shot.udv_delay -
                               daq_turnon_time)).argmin()
        upper_end_idx = abs(t_upper -
                            (t_end + self.shot.udv_delay -
                             daq_turnon_time)).argmin()
        lower_start_idx = abs(t_lower -
                              (t_start + self.shot.udv_delay -
                               daq_turnon_time)).argmin()
        lower_end_idx = abs(t_lower -
                            (t_end + self.shot.udv_delay -
                             daq_turnon_time)).argmin()
        self.currentavg = (current_upper[upper_start_idx:
                                         upper_end_idx].mean() +
                           current_lower[lower_start_idx:
                                         lower_end_idx].mean())
        self.currentstd = (current_upper[upper_start_idx:
                                         upper_end_idx].std() +
                           current_lower[lower_start_idx:
                                         lower_end_idx].std())
        
        self.vaavg = self.currentavg*2.8669/numpy.sqrt(4*numpy.pi*6.36)
        self.vastd = self.currentstd*2.8669/numpy.sqrt(4*numpy.pi*6.36)
        
        #Grab the motor data
        md = motor_data.MotorData(self.shot.number)

        #Average the inner cylinder speeds over the total length of the
        #the applied field.
        
        self.ICspeedavg = md.time_avg(self.shot.field_delay,
                                      (self.shot.field_delay +
                                       self.shot.field_length))['ICspeed']

        self.ICspeedstd = md.time_std(self.shot.field_delay,
                                      (self.shot.field_delay +
                                       self.shot.field_length))['ICspeed']

        self.vicavg = self.ICspeedavg*2*numpy.pi*7.06/60
        self.vicstd = self.ICspeedstd*2*numpy.pi*7.06/60

        #Average the outer cylinder speed over the time of the average
        #UDV measurement.
        #It turns out that the OC encoder sometimes has problems, so
        #use the OR encoder since the speeds are locked.

        self.OCspeedavg = md.time_avg((self.shot.udv_delay +
                                       t_start),
                                      (self.shot.udv_delay +
                                       t_end))['ORspeed']
        self.OCspeedstd = md.time_std((self.shot.udv_delay +
                                       t_start),
                                      (self.shot.udv_delay +
                                       t_end))['ORspeed']

        #Get the velocity measurements
        startidx = self.velocity.get_index_near_time(t_start)
        endidx = self.velocity.get_index_near_time(t_end)
        ridx = self.velocity.get_index_near_radius(r)

        self.vravg = self.velocity.vr[startidx:endidx].mean(axis=0)
        self.vrstd = self.velocity.vr[startidx:endidx].std(axis=0)
        self.vtavg = self.velocity.vtheta[startidx:endidx].mean(axis=0) 
        self.vtstd = self.velocity.vtheta[startidx:endidx].std(axis=0)

        #This is the amount of the required offset in the determined
        #azimuthal velocity due to variances in the OC speed from the assumed
        #value when calculating the velocities.

        self.OCspeedoffset = (self.OCspeedavg -
                              self.shot.OCspeed)*2*numpy.pi*self.r/60
        self.OCspeedoffsetstd = self.OCspeedstd*2*numpy.pi*self.r/60

        self.vtavg = self.vtavg + self.OCspeedoffset
        self.vtstd = numpy.sqrt(self.vtstd**2 +
                                self.OCspeedoffsetstd**2)

        #Now do the normalized quantities vt/vic
        self.vtnorm = self.vtavg/self.vicavg
        self.vtnormstd = self.vtnorm*numpy.sqrt(self.vtstd**2/self.vtavg**2 +
                                                self.vicstd**2/self.vicavg**2)
        self.vrnorm = self.vravg/self.vicavg
        self.vrnormstd = self.vrnorm*numpy.sqrt(self.vrstd**2/self.vravg**2 +
                                                self.vicstd**2/self.vicavg**2)

        #And the normalized alfven speed
        if (self.vaavg == 0):
            self.vanorm = 0
            self.vanormstd = 0
        else:
            self.vanorm = self.vaavg/self.vicavg
            self.vanormstd = (self.vanorm *
                              numpy.sqrt(self.vastd**2/self.vaavg**2 +
                                         self.vicstd**2/self.vicavg**2))


class AvgProfile_group():
    """A group of AvgProfiles"""
    def __init__(self, *measurements, **params):
        """Get a group of average profiles

        *measurements is any number of tuples where the first item is a
        velocity object, the second item is the start time, and the
        third item is the end time.

        Legal **params are 'r' (default 14),
        and 'daq_turnon_time' (default 120)
        """

        self.daq_turnon_time = params.pop('daq_turnon_time', 120)

        self.avgprofiles = []
        for measurement in measurements:
            avgp = AvgPointMeasurement(measurement[0],
                                       measurement[1], measurement[2],
                                       daq_turnon_time=self.daq_turnon_time)
            self.avgprofiles.append(avgp)
        
        numavgprofiles = len(self.avgprofiles)

        #Assume that all of these use the same r vector!
        #This should be safe if they're all from the same
        #series of measurements.
        self.r = self.avgprofiles[0].r
        rlen = len(self.r)

        self.vanorms = numpy.zeros(numavgprofiles)
        self.vanormstds = numpy.zeros(numavgprofiles)
        self.vrnorms = numpy.zeros((numavgprofiles, rlen))
        self.vrnormstds = numpy.zeros((numavgprofiles, rlen))
        self.vtnorms = numpy.zeros((numavgprofiles, rlen))
        self.vtnormstds = numpy.zeros((numavgprofiles, rlen))
        self.vravgs = numpy.zeros((numavgprofiles, rlen))
        self.vrstds = numpy.zeros((numavgprofiles, rlen))
        self.vtavgs = numpy.zeros((numavgprofiles, rlen))
        self.vtstds = numpy.zeros((numavgprofiles, rlen))
        self.vocavgs = numpy.zeros(numavgprofiles)
        self.vocstds = numpy.zeros(numavgprofiles)
        self.vicavgs = numpy.zeros(numavgprofiles)
        self.vicstds = numpy.zeros(numavgprofiles)
        self.currentavgs = numpy.zeros(numavgprofiles)
        self.currentstds = numpy.zeros(numavgprofiles)

        for i in range(0, len(self.avgprofiles)):
            self.vanorms[i] = self.avgprofiles[i].vanorm
            self.vanormstds[i] = self.avgprofiles[i].vanormstd
            self.vrnorms[i] = self.avgprofiles[i].vrnorm
            self.vrnormstds[i] = self.avgprofiles[i].vrnormstd
            self.vtnorms[i] = self.avgprofiles[i].vtnorm
            self.vtnormstds[i] = self.avgprofiles[i].vtnormstd
            self.vravgs[i] = self.avgprofiles[i].vravg
            self.vrstds[i] = self.avgprofiles[i].vrstd
            self.vtavgs[i] = self.avgprofiles[i].vtavg
            self.vtstds[i] = self.avgprofiles[i].vtstd
            self.vocavgs[i] = self.avgprofiles[i].OCspeedavg
            self.vocstds[i] = self.avgprofiles[i].OCspeedstd
            self.vicavgs[i] = self.avgprofiles[i].vicavg
            self.vicstds[i] = self.avgprofiles[i].vicstd
            self.currentavgs[i] = self.avgprofiles[i].currentavg
            self.currentstds[i] = self.avgprofiles[i].currentstd
