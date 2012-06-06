import UDV_helpers as udvh
from copy import deepcopy
import scipy.optimize
import scipy.interpolate
from pylab import *

def global_optimize_transducer_angle(shot1, shot2, channelnum1, channelnum2,
                                     start_time, end_time):
    #Get copies of the real channels
    sh1ch1 = deepcopy(shot1.get_channel(channelnum1))
    sh1ch2 = deepcopy(shot1.get_channel(channelnum2))
    sh2ch1 = deepcopy(shot2.get_channel(channelnum1))
    sh2ch2 = deepcopy(shot2.get_channel(channelnum2))

    #Now get some dummy combined velocity things.
    vel1 = deepcopy(shot1.get_velocity(channelnum1, channelnum2))
    vel2 = deepcopy(shot2.get_velocity(channelnum1, channelnum2))
    
    start_idx = vel1.get_index_near_time(start_time)
    end_idx = vel1.get_index_near_time(end_time)

    figure()
    udvh.plot_two_component_avg_velocities(vel1, start_idx, end_idx)
    udvh.plot_two_component_avg_velocities(vel2, start_idx, end_idx)

    #Find how far to go from the outside to get to the inner and outer
    #points of interest
    indx_in = vel1.r.size - vel1.get_index_near_radius(11.0)
    indx_out = vel1.r.size - vel2.get_index_near_radius(19.0)
    nindx = indx_in-indx_out

    def err_func(As):
        print "Running with A1 = %0.8g, A2 = %0.8g" % (As[0], As[1])
        #First modify the As in the relevant dummy channels.
        sh1ch1.A = As[0]
        sh2ch1.A = As[0]
        sh1ch2.A = As[1]
        sh2ch2.A = As[1]

        #Need to update the radius vectors, too
        sh1ch1.calculate_radius()
        sh1ch2.calculate_radius()
        sh2ch1.calculate_radius()
        sh2ch2.calculate_radius()

        #Now reprocess the dummy velocities.
        vel1.gen_velocity_two_transducers(sh1ch1, sh1ch2)
        vel2.gen_velocity_two_transducers(sh2ch1, sh2ch2)
        print "In index: %d, Out index %d, Velocity size: %d" % (indx_in,
                                                                 indx_out,
                                                                 vel1.r.size)

        #And calculate the error vector. We multiply the vr difference by
        #10 assuming the vr ~ 0.10*vtheta
        error = zeros(2*nindx)
        for i in range(0, nindx):
            error[i] = (vel1.vtheta[start_idx:end_idx, -(i+indx_out)].mean() +
                        vel2.vtheta[start_idx:end_idx, -(i+indx_out)].mean())
        for i in range(nindx, 2*nindx):
            n = i-nindx
            error[i] = 10*(vel1.vr[start_idx:end_idx, -(n+indx_out)].mean() -
                            vel2.vr[start_idx:end_idx, -(n+indx_out)].mean())
        return error

    A0 = [sh1ch1.A, sh1ch2.A]

    Alsq = scipy.optimize.leastsq(err_func, A0, full_output=1)
    
    #Make sure we have the updated As
    A1 = Alsq[0][0]
    A2 = Alsq[0][1]
    sh1ch1.A = A1
    sh2ch1.A = A1
    sh1ch2.A = A2
    sh2ch2.A = A2
    #Now reprocess the dummy velocities.
    vel1.gen_velocity_two_transducers(sh1ch1, sh1ch2)
    vel2.gen_velocity_two_transducers(sh2ch1, sh2ch2)


    #And let's take a look at what we generated.
    print "Optimized parameters: A1 = %0.3g, A2 = %0.3g" % (A1, A2)


    figure()
    udvh.plot_two_component_avg_velocities(vel1, start_idx, end_idx)
    udvh.plot_two_component_avg_velocities(vel2, start_idx, end_idx)


def brute_force_transducer_angle(shot1, shot2, channelnum1, channelnum2,
                                 start_time, end_time, anglediff=2.0,
                                 A1s=linspace(18,23,30),
                                 A2s=linspace(18,23,30), 
                                 progressive_draw=0,
                                 norm=1):
    """Do a brute force calibration of the transducer angles. Calculate a
    number of positions around the suspected angle for each transducer, and
    plot an error function for all of those points"""
    #Get copies of the real channels
    sh1ch1 = deepcopy(shot1.get_channel(channelnum1))
    sh1ch2 = deepcopy(shot1.get_channel(channelnum2))
    sh2ch1 = deepcopy(shot2.get_channel(channelnum1))
    sh2ch2 = deepcopy(shot2.get_channel(channelnum2))

    #Now get some dummy combined velocity things.
    vel1 = deepcopy(shot1.get_velocity(channelnum1, channelnum2))
    vel2 = deepcopy(shot2.get_velocity(channelnum1, channelnum2))
    
    start_idx = vel1.get_index_near_time(start_time)
    end_idx = vel1.get_index_near_time(end_time)

    def err_func(A1, A2):
        #First modify the As in the relevant dummy channels.
        sh1ch1.A = A1
        sh2ch1.A = A1
        sh1ch2.A = A2
        sh2ch2.A = A2
        
        #Need to update the radius vectors, too
        sh1ch1.calculate_radius()
        sh1ch2.calculate_radius()
        sh2ch1.calculate_radius()
        sh2ch2.calculate_radius()
        
        #Now reprocess the dummy velocities.
        vel1.gen_velocity_two_transducers(sh1ch1, sh1ch2)
        vel2.gen_velocity_two_transducers(sh2ch1, sh2ch2)
        
        #Find indices of radius bounds
        indx_rmin = vel1.get_index_near_radius(11.0)
        indx_rmax = vel1.get_index_near_radius(19.0)
        nindx = indx_rmax - indx_rmin
        
        #And calculate the norm for the differences between the
        #forward and backwards shots, divided by the total number of
        #radial samples. The degree of the norm is specified by the
        #'norm' parameter (1=L1, 2=L2, 3=L3, etc.). We multiply the vr
        #difference by 10 assuming that vr ~ 0.10*vtheta so that we
        #give ~equal weights to both components.

        vt_diff = abs(mean(vel1.vtheta[start_idx:end_idx, indx_rmin:indx_rmax],
                           axis=0) +
                      mean(vel2.vtheta[start_idx:end_idx, indx_rmin:indx_rmax],
                           axis=0))
        
        vr_diff = 10*abs(mean(vel1.vr[start_idx:end_idx, indx_rmin:indx_rmax],
                              axis=0) -
                         mean(vel2.vr[start_idx:end_idx, indx_rmin:indx_rmax],
                              axis=0))
        
        total_err = ((vr_diff**norm).sum() +
                     (vt_diff**norm).sum())**(1.0/norm)/(nindx)
        
        return total_err

    errors = ones([A2s.size, A1s.size])*nan
    fig = figure()

    totalpts = errors.size
    print "Entering loop...."
    for i in range(0, A1s.size):
        for j in range(0, A2s.size):
            errors[j, i] = err_func(A1s[i], A2s[j])
            if(progressive_draw):
                fig.clear()
                ax = fig.add_subplot(111)
                cp = ax.contourf(A1s, A2s, errors, 50)
                fig.colorbar(cp)
                ax.set_xlabel("A for Channel %d" % channelnum1)
                ax.set_ylabel("A for Channel %d" % channelnum2)
                draw()
            sys.stdout.write('\x1b[1A\x1b[2K\x1b[J')
            print "%d of %d positions analyzed" % (i*A2s.size + j + 1,
                                                   totalpts)

    fig.clear()
    ax = fig.add_subplot(111)
    cp = ax.contourf(A1s, A2s, errors, 30)
    fig.colorbar(cp)
    ax.set_xlabel("A for Channel %d" % channelnum1)
    ax.set_ylabel("A for Channel %d" % channelnum2)
    return (A1s, A2s, errors)


def plot_calibrated_result(shot1, shot2, channelnum1, channelnum2,
                           start_time, end_time, A1, A2):
    #Get copies of the real channels
    sh1ch1 = deepcopy(shot1.get_channel(channelnum1))
    sh1ch2 = deepcopy(shot1.get_channel(channelnum2))
    sh2ch1 = deepcopy(shot2.get_channel(channelnum1))
    sh2ch2 = deepcopy(shot2.get_channel(channelnum2))

    #Now get some dummy combined velocity things.
    vel1 = deepcopy(shot1.get_velocity(channelnum1, channelnum2))
    vel2 = deepcopy(shot2.get_velocity(channelnum1, channelnum2))
    
    start_idx = vel1.get_index_near_time(start_time)
    end_idx = vel1.get_index_near_time(end_time)

    #First modify the As in the relevant dummy channels.
    sh1ch1.A = A1
    sh2ch1.A = A1
    sh1ch2.A = A2
    sh2ch2.A = A2
    
    #Need to update the radius vectors, too
    sh1ch1.calculate_radius()
    sh1ch2.calculate_radius()
    sh2ch1.calculate_radius()
    sh2ch2.calculate_radius()
    
    #Now reprocess the dummy velocities.
    vel1.gen_velocity_two_transducers(sh1ch1, sh1ch2)
    vel2.gen_velocity_two_transducers(sh2ch1, sh2ch2)
    
    #Now plot these.
    fig = figure()
    ax1=subplot(2,1,1)
    ax1.plot(vel1.r, mean(vel1.vtheta[start_idx:end_idx,:], axis=0), 'b')
    ax1.plot(vel2.r, -mean(vel2.vtheta[start_idx:end_idx,:], axis=0), 'g')

    ax2=subplot(2,1,2)
    ax2.plot(vel1.r, mean(vel1.vr[start_idx:end_idx,:], axis=0), 'b')
    ax2.plot(vel2.r, mean(vel2.vr[start_idx:end_idx,:], axis=0), 'g')



def local_optimize_transducer_angle(shot1, shot2, channelnum1, channelnum2,
                                    start_time, end_time):
    '''Implements a method to calculate the pair of transducer angles that
    produce two velocity measurements from a set of forward/backward shots.
    A pair of angles is calculated for reach radius of the measurements.
    If all goes well, the calculated angles will be roughly constant
    as a function of radius. Note that we have assumed that cos(B)=0 to make
    the math easier (i.e. the beams are in the r-\theta plane.) Under
    pathological conditions (such as with a small A angle), there may be no
    set of transducer angles which produce a given pair of measurements.'''

    #Note that this is only valid for cos(B) = 0!
    #We don't have to copy these channels as we do for the global method,
    #since we don't need to modify anything.
    
    sh1ch1 = shot1.get_channel(channelnum1)
    sh1ch2 = shot1.get_channel(channelnum2)
    sh2ch1 = shot2.get_channel(channelnum1)
    sh2ch2 = shot2.get_channel(channelnum2)
    
    #We use the r from the assumed angle of the transducer, since this
    #should be pretty close to reality.
    
    #Reimplement the logic from the gen_velocity_two_transducers to get
    #a common radius vector.
    
    #Find the index of the deepest point (smallest radius)
    sh1ch1_last_idx = sh1ch1.r.argmin()
    sh1ch2_last_idx = sh1ch2.r.argmin()
    sh2ch1_last_idx = sh2ch1.r.argmin()
    sh2ch2_last_idx = sh2ch2.r.argmin()
    
    #Find out which channel has the least radial penetration, and use
    #that as the definitive r coordinate.
    r = sh1ch1.r[0:sh1ch1_last_idx][::-1]
    if (sh1ch2.r.min() > r.min()):
        r = sh1ch2.r[0:sh1ch2_last_idx][::-1]
    if (sh2ch1.r.min() > r.min()):
        r = sh2ch1.r[0:sh2ch1_last_idx][::-1]
    if (sh2ch2.r.min() > r.min()):
        r = sh2ch2.r[0:sh2ch2_last_idx][::-1]
    
    #Now resample each of the velocities onto the new radial grid.
    US = scipy.interpolate.UnivariateSpline
    
    #For shot 1 channel 1
    start_idx = sh1ch1.get_index_near_time(start_time)
    end_idx = sh1ch1.get_index_near_time(end_time)
    
    f = US(sh1ch1.r[0:sh1ch1_last_idx][::-1],
           mean(sh1ch1.unwrapped_velocity[start_idx:end_idx,0:sh1ch1_last_idx],
                axis=0)[::-1],
           k=3, s=0)
    v11 = f(r)
    
    #For shot 1 channel 2
    start_idx = sh1ch2.get_index_near_time(start_time)
    end_idx = sh1ch2.get_index_near_time(end_time)
    
    f = US(sh1ch2.r[0:sh1ch2_last_idx][::-1],
           mean(sh1ch2.unwrapped_velocity[start_idx:end_idx,0:sh1ch2_last_idx],
                axis=0)[::-1],
           k=3, s=0)
    v12 = f(r)
    
    
    #For shot 2 channel 1
    start_idx = sh2ch1.get_index_near_time(start_time)
    end_idx = sh2ch1.get_index_near_time(end_time)
    
    f = US(sh2ch1.r[0:sh2ch1_last_idx][::-1],
           mean(sh2ch1.unwrapped_velocity[start_idx:end_idx,0:sh2ch1_last_idx],
                axis=0)[::-1],
           k=3, s=0)
    v21 = f(r)
    
    
    #For shot 2 channel 2
    start_idx = sh2ch2.get_index_near_time(start_time)
    end_idx = sh2ch2.get_index_near_time(end_time)

    f = US(sh2ch2.r[0:sh2ch2_last_idx][::-1],
           mean(sh2ch2.unwrapped_velocity[start_idx:end_idx,0:sh2ch2_last_idx],
                axis=0)[::-1],
           k=3, s=0)
    v22 = f(r)

    plot(r, v11)
    plot(r, v12)
    plot(r, v21)
    plot(r, v22)

    def errfunc(A, B, r, xi, r2=20.3):
        sinA = sin(pi*A/180.0)
        cosA = cos(pi*A/180.0)
        sinB = sin(pi*B/180.0)
        cosB = cos(pi*B/180.0)
        #depth along measurement for a given radius
        d = ((r2*cosA - sqrt(r**2*(sinA**2*sinB**2 + cosA**2) -
                             r2**2*sinA**2*sinB**2)) /
             (sinA**2*sinB**2 + cosA**2))

        #Ideally, \theta + \alpha = \xi. We determined what \xi should
        #be based on our measurements, so to the extent that
        #\theta + \alpha != \xi, it suggests that our assumed geometry
        #is wrong.
        theta = arcsin(d*sinA*sinB/r)
        alpha = arctan(sinA*sinB/cosA)
        err = (alpha + theta - xi)**2
        #print "A = %0.5g, err=%0.5g" % (A, err)
        return err

    B1 = sh1ch1.B
    B2 = sh1ch2.B

    A1s = zeros(r.size)
    A2s = zeros(r.size)
    
    for i in range(0, r.size):
        E = (v12[i] - v22[i])/(v11[i]-v21[i])
        F = -(v12[i] + v22[i])/(v11[i] + v21[i])
        xi1 = arcsin(sqrt((1-F**2)/(E**2 - F**2)))
        xi2 = arcsin(E*sqrt((1-F**2)/(E**2 - F**2)))
        #print "r = %0.2g: E = %0.3g, F = %0.3g, xi1 = %0.3g, xi2 = %0.3g" % (r[i], E, F, xi1, xi2)

        res1 = scipy.optimize.fmin(errfunc, sh1ch1.A,
                                   args=(B1, r[i], xi1), disp=False)        
    
        res2 = scipy.optimize.fmin(errfunc, sh1ch2.A,
                                   args=(B2, r[i], xi2), disp=False)
        #Sometimes (particularly with a small transducer angle), there is
        #no set of angles that can possibly produce the measured velocities
        #If that's the case, the xi angles will be nans, so we cut those out.
        if(isnan(xi1) or isnan(xi2)):
            A1s[i] = nan
            A2s[i] = nan
        else:
            A1s[i] = res1[0]
            A2s[i] = res2[0]

    figure()
    plot(r, A1s)
    plot(r, A2s)
                                           
