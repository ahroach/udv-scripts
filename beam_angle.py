import UDV_helpers as udvh
from copy import deepcopy
import scipy.optimize
from pylab import *

def optimize_transducer_angles(shot1, shot2, channelnum1, channelnum2,
                               start_time, end_time):
    #Get copies of the real channels
    sh1ch1 = deepcopy(shot1.get_channel(channelnum1))
    sh1ch2 = deepcopy(shot1.get_channel(channelnum2))
    sh2ch1 = deepcopy(shot2.get_channel(channelnum1))
    sh2ch2 = deepcopy(shot2.get_channel(channelnum2))

    #Now get some dummy combined velocity things.
    vel1 = deepcopy(shot1.get_velocity((channelnum1, channelnum2)))
    vel2 = deepcopy(shot2.get_velocity((channelnum1, channelnum2)))
    
    start_idx = vel1.get_index_near_time(start_time)
    end_idx = vel1.get_index_near_time(end_time)

    figure()
    udvh.plot_two_component_avg_velocities(vel1, start_idx, end_idx)
    udvh.plot_two_component_avg_velocities(vel2, start_idx, end_idx)

    #Find how far to go from the outside to get to the inner and outer
    #points of interest
    indx_in = vel1.r.size - vel1.get_index_near_radius(12.0)
    indx_out = vel1.r.size - vel2.get_index_near_radius(20.0)
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

