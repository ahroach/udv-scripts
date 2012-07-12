from numpy import *
from pylab import *
numshots = 30

shot = zeros(numshots)
speed = zeros(numshots)
current = zeros(numshots)
saturatedfrequency = zeros(numshots)
saturatedfrequencyerr = zeros(numshots)
saturatedpower = zeros(numshots)
saturatedintervalstart = zeros(numshots)
saturatedintervalstop = zeros(numshots)
timefieldon = zeros(numshots)
timesaturated = zeros(numshots)
timefieldoff = zeros(numshots)
freqband_min = zeros(numshots)
freqband_max = zeros(numshots)
#Shear measurements taken from 12 to 16 cm.
saturatedshear = zeros(numshots)
beginningshear = zeros(numshots)


#For MRI-Zed shots.  Ring-speed ratio at 10%: 400, 220, 53, 53
#Measurements taken at r=19.2 cm
i = 0
shot[i] = 1036
speed[i] = 400
current[i] = 800
saturatedfrequency[i] = 0.25
saturatedfrequencyerr[i] = 0.03
freqband_min[i] = 0.20
freqband_max[i] = 0.35
saturatedpower[i] = 11.637
saturatedintervalstart[i] = 50 
saturatedintervalstop[i] = 69
timefieldon[i] = 20
timesaturated[i] = 50
timefieldoff[i] = 70
saturatedshear[i] = -1.26525

i = 1
shot[i] = 926
speed[i] = 400
current[i] = 1000
saturatedfrequency[i] = 0.40
saturatedfrequencyerr[i] = 0.02
freqband_min[i] = 0.28
freqband_max[i] = 0.58
saturatedpower[i] = 25.728
saturatedintervalstart[i] = 32  
saturatedintervalstop[i] = 59
timefieldon[i] = 20
timesaturated[i] = 32
timefieldoff[i] = 60
saturatedshear[i] = -1.48177

i = 2
shot[i] = 927
speed[i] = 400
current[i] = 1200 
saturatedfrequency[i] = 0.44
saturatedfrequencyerr[i] = 0.02
freqband_min[i] = 0.23
freqband_max[i] = 0.67
saturatedpower[i] = 73.902
saturatedintervalstart[i] = 32  
saturatedintervalstop[i] = 49
timefieldon[i] = 20
timesaturated[i] = 32
timefieldoff[i] = 50
saturatedshear[i] = -1.411973

i = 3
shot[i] = 1044
speed[i] = 400
current[i] = 1400
saturatedfrequency[i] = 0.45
saturatedfrequencyerr[i] = 0.05
freqband_min[i] = 0.35
freqband_max[i] = 0.60
saturatedpower[i] = 71.254
saturatedintervalstart[i] = 32  
saturatedintervalstop[i] = 39
timefieldon[i] = 20
timesaturated[i] = 32
timefieldoff[i] = 40
saturatedshear[i] = -1.007015


i = 4
shot[i] = 854
speed[i] = 800
current[i] = 1200
saturatedfrequency[i] = 0.59
saturatedfrequencyerr[i] = 0.10
freqband_min[i] = 0.50
freqband_max[i] = 0.80
saturatedpower[i] = 16.627
saturatedintervalstart[i] = 135  
saturatedintervalstop[i] = 154
timefieldon[i] = 125
timesaturated[i] = 135
timefieldoff[i] = 155
saturatedshear[i] = -2.88058

i = 5
shot[i] = 856
speed[i] = 1200
current[i] = 1200
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
saturatedintervalstart[i] = nan  
saturatedintervalstop[i] = nan
timefieldon[i] = 125
timesaturated[i] = nan
timefieldoff[i] = 155
saturatedshear[i] = -3.935047


i = 6
shot[i] = 858
speed[i] = 1600
current[i] = 1200
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
saturatedintervalstart[i] = nan  
saturatedintervalstop[i] = nan
timefieldon[i] = 125
timesaturated[i] = nan
timefieldoff[i] = 155
saturatedshear[i] = -5.0827

i = 7
shot[i] = 860
speed[i] = 1800
current[i] = 1200
saturatedfrequency[i] = nan 
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
saturatedintervalstart[i] = nan  
saturatedintervalstop[i] = nan
timefieldon[i] = 5
timesaturated[i] = nan
timefieldoff[i] = 35
saturatedshear[i] = -5.8765

i = 8
shot[i] = 894
speed[i] = 800
current[i] = 600
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
saturatedintervalstart[i] = nan  
saturatedintervalstop[i] = nan 
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 80
saturatedshear[i] = nan

i = 9
shot[i] = 898
speed[i] = 800
current[i] = 1000
saturatedfrequency[i] = 0.94
saturatedfrequencyerr[i] = 0.08
freqband_min[i] = 0.8
freqband_max[i] = 1.1
saturatedpower[i] = 0.5202
saturatedintervalstart[i] = 40  
saturatedintervalstop[i] = 59
timefieldon[i] = 20
timesaturated[i] = 40
timefieldoff[i] = 60
saturatedshear[i] = nan

i = 10
shot[i] = 900
speed[i] = 800
current[i] = 1400
saturatedfrequency[i] = 0.70
saturatedfrequencyerr[i] = 0.05
freqband_min[i] = 0.40
freqband_max[i] = 1.0
saturatedpower[i] = 89.774
saturatedintervalstart[i] = 30  
saturatedintervalstop[i] = 39
timefieldon[i] = 20
timesaturated[i] = 30
timefieldoff[i] = 40
saturatedshear[i] = nan

i = 11
shot[i] = 902
speed[i] = 1200
current[i] = 1400
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
saturatedintervalstart[i] = nan  
saturatedintervalstop[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 40
saturatedshear[i] = nan

i = 12
shot[i] = 904
speed[i] = 1200
current[i] = 1600
saturatedfrequency[i] = 0.90
saturatedfrequencyerr[i] = 0.10
freqband_min[i] = 0.50
freqband_max[i] = 1.27
saturatedpower[i] = 37.93
saturatedintervalstart[i] = 27.5  
saturatedintervalstop[i] = 34
timefieldon[i] = 20
timesaturated[i] = 27.5
timefieldoff[i] = 35


i = 13
shot[i] = 909
speed[i] = 400
current[i] = 700
saturatedfrequency[i] = 0.48
saturatedfrequencyerr[i] = 0.03
freqband_min[i] = 0.39
freqband_max[i] = 0.63
saturatedpower[i] = 0.12453
saturatedintervalstart[i] = 50  
saturatedintervalstop[i] = 74
timefieldon[i] = 20
timesaturated[i] = 50
timefieldoff[i] = 75


i = 14
shot[i] = 911
speed[i] = 200
current[i] = 500
saturatedfrequency[i] = 0.132
saturatedfrequencyerr[i] = 0.02
freqband_min[i] = 0.11
freqband_max[i] = 0.16
saturatedpower[i] = 0.1837
saturatedintervalstart[i] = 50  
saturatedintervalstop[i] = 79
timefieldon[i] = 20
timesaturated[i] = 50
timefieldoff[i] = 80


i = 15
shot[i] = 913
speed[i] = 200
current[i] = 600
saturatedfrequency[i] = 0.20
saturatedfrequencyerr[i] = 0.015
freqband_min[i] = 0.11
freqband_max[i] = 0.27
saturatedpower[i] = 2.2813
saturatedintervalstart[i] = 33  
saturatedintervalstop[i] = 79
timefieldon[i] = 20
timesaturated[i] = 33
timefieldoff[i] = 80


i = 16
shot[i] = 914
speed[i] = 200
current[i] = 700
saturatedfrequency[i] = 0.24
saturatedfrequencyerr[i] = 0.01
freqband_min[i] = 0.17
freqband_max[i] = 0.32
saturatedpower[i] = 5.8443
saturatedintervalstart[i] = 34  
saturatedintervalstop[i] = 74
timefieldon[i] = 20
timesaturated[i] = 34
timefieldoff[i] = 75


i = 17
shot[i] = 915
speed[i] = 200
current[i] = 1600
saturatedfrequency[i] = 0.25
saturatedfrequencyerr[i] = 0.03
freqband_min[i] = 0.12
freqband_max[i] = 0.40
saturatedpower[i] = 21.138
saturatedintervalstart[i] = 27  
saturatedintervalstop[i] = 34
timefieldon[i] = 20
timesaturated[i] = 27
timefieldoff[i] = 35


i = 18
shot[i] = 916
speed[i] = 600
current[i] = 900
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
saturatedintervalstart[i] = nan  
saturatedintervalstop[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 65


i = 19
shot[i] = 917
speed[i] = 600
current[i] = 1000
saturatedfrequency[i] = 0.36
saturatedfrequencyerr[i] = 0.05
freqband_min[i] = 0.29
freqband_max[i] = 0.50
saturatedpower[i] = 1.6104
saturatedintervalstart[i] = 43  
saturatedintervalstop[i] = 59
timefieldon[i] = 20
timesaturated[i] = 43
timefieldoff[i] = 60


i = 20
shot[i] = 918
speed[i] = 600
current[i] = 1100
saturatedfrequency[i] = 0.40
saturatedfrequencyerr[i] = 0.03
freqband_min[i] = 0.25
freqband_max[i] = 0.60
saturatedpower[i] = 13.94
saturatedintervalstart[i] = 41  
saturatedintervalstop[i] = 54
timefieldon[i] = 20
timesaturated[i] = 41
timefieldoff[i] = 55


i = 21
shot[i] = 919
speed[i] = 800
current[i] = 1100
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
saturatedintervalstart[i] = nan  
saturatedintervalstop[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 55


i = 22
shot[i] = 920
speed[i] = 600
current[i] = 1300
saturatedfrequency[i] = 0.63
saturatedfrequencyerr[i] = 0.03
freqband_min[i] = 0.40
freqband_max[i] = 0.80
saturatedpower[i] = 74.017
saturatedintervalstart[i] = 32  
saturatedintervalstop[i] = 44
timefieldon[i] = 20
timesaturated[i] = 32
timefieldoff[i] = 45


i = 23
shot[i] = 921
speed[i] = 1000
current[i] = 1300
saturatedfrequency[i] = 0.56
saturatedfrequencyerr[i] = 0.05
freqband_min[i] = 0.50
freqband_max[i] = 0.70
saturatedpower[i] = 2.9412
saturatedintervalstart[i] = 32  
saturatedintervalstop[i] = 44
timefieldon[i] = 20
timesaturated[i] = 32
timefieldoff[i] = 45


i = 24
shot[i] = 922
speed[i] = 1000
current[i] = 1400
saturatedfrequency[i] = 0.72
saturatedfrequencyerr[i] = 0.03
freqband_min[i] = 0.50
freqband_max[i] = 1.0
saturatedpower[i] = 7.9399
saturatedintervalstart[i] = 30  
saturatedintervalstop[i] = 39
timefieldon[i] = 20
timesaturated[i] = 30
timefieldoff[i] = 40


i = 25
shot[i] = 931
speed[i] = 100
current[i] = 1600
saturatedfrequency[i] = 0.20
saturatedfrequencyerr[i] = 0.15
freqband_min[i] = 0.2
freqband_max[i] = 0.4
saturatedpower[i] = 1.455
saturatedintervalstart[i] = 25  
saturatedintervalstop[i] = 34
timefieldon[i] = 20
timesaturated[i] = 25
timefieldoff[i] = 35

i = 26
shot[i] = 932
speed[i] = 100
current[i] = 800
saturatedfrequency[i] = 0.125
saturatedfrequencyerr[i] = 0.01
freqband_min[i] = 0.075
freqband_max[i] = 0.175
saturatedpower[i] = 6.1972
saturatedintervalstart[i] = 38  
saturatedintervalstop[i] = 69
timefieldon[i] = 20
timesaturated[i] = 38
timefieldoff[i] = 70


i = 27
shot[i] = 933
speed[i] = 100
current[i] = 500
saturatedfrequency[i] = 0.126
saturatedfrequencyerr[i] = 0.01
freqband_min[i] = 0.10
freqband_max[i] = 0.16
saturatedpower[i] = 2.9229
saturatedintervalstart[i] = 40  
saturatedintervalstop[i] = 79
timefieldon[i] = 20
timesaturated[i] = 40
timefieldoff[i] = 80


i = 28
shot[i] = 934
speed[i] = 100
current[i] = 400
saturatedfrequency[i] = 0.20
saturatedfrequencyerr[i] = 0.015
freqband_min[i] = 0.12
freqband_max[i] = 0.30
saturatedpower[i] = 1.9822
saturatedintervalstart[i] = 45  
saturatedintervalstop[i] = 79
timefieldon[i] = 20
timesaturated[i] = 45
timefieldoff[i] = 80


i = 29
shot[i] = 935
speed[i] = 100
current[i] = 300
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
saturatedintervalstart[i] = nan  
saturatedintervalstop[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 80




def get_data():
    mrized_data = {'shot': shot, 'speed': speed, 'current': current, 'saturatedfrequency': saturatedfrequency, 'saturatedfrequencyerr': saturatedfrequencyerr, 'saturatedpower': saturatedpower, 'timefieldon': timefieldon, 'timesaturated': timesaturated, 'timefieldoff': timefieldoff, 'saturatedshear': saturatedshear}
    return mrized_data

rho = 6.36 #Density of GaInSn in gm/cm^3
eta = 2.57e3 #Magnetic diffusivity in cm^2/sec

def plot_amplitudes(elsasser = 1):
    mrized_data = get_data()
    scatter(mrized_data['speed']*2*pi/60, mrized_data['current']*2.8669, mrized_data['saturatedpower']*1000000/(mrized_data['speed']*mrized_data['speed']), label='_nolegend_')
    #also plot the xs.
    nan_idx = isnan(mrized_data['saturatedpower'])
    plot(mrized_data['speed'][nan_idx]*2*pi/60, mrized_data['current'][nan_idx]*2.8669, 'x', color='black', label='_nolegend_')
            
    xlabel("IC Speed [rad/sec]")
    ylabel("B [Gauss]")
    title("$P_{fundamental}/\Omega_{IC}^2$")
    #Now plot line for Elsasser number constant
    #Defined as v_A^2/(eta*Omega)
    Omega = linspace(0,1200, 100)
    Omega = Omega*2*pi/60
    B_crit = sqrt(4*pi*rho*eta*Omega*elsasser)
    labelstring = "$\Lambda = $" + str(elsasser)
    axes = axis()
    plot(Omega, B_crit, color='k', label=labelstring)
    axis(axes)
    legend(loc='lower right')
    

def plot_frequencies():
    mrized_data = get_data()
    scatter(mrized_data['speed'], mrized_data['current'], (mrized_data['saturatedfrequency'] + mrized_data['speed']*53/(60*400))*100000/mrized_data['speed'])
    xlabel("IC Speed [RPM]")
    ylabel("Coil Current [A]")
    
def plot_quantity_at_speed(quantity, speed):
    mrized_data = get_data()

    count = 0
    for i in range(0, mrized_data['speed'].size):
        if (mrized_data['speed'][i] == speed):
            count = count + 1

    quantity_array = zeros(count)
    current_array = zeros(count)

    index = 0
    for i in range(0, mrized_data['speed'].size):
        if (mrized_data['speed'][i] == speed):
            quantity_array[index] = mrized_data[quantity][i]
            current_array[index] = mrized_data['current'][i]
            index = index + 1

    plot(current_array, quantity_array, 'o')
    xlabel("Current [A]")
    ylabel(quantity)
    title("MRI-Zed oscillations")

