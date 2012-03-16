from numpy import *
from pylab import *
numshots = 50

shot = zeros(numshots)
speed = zeros(numshots)
irspeed = zeros(numshots)
current = zeros(numshots)
saturatedfrequency = zeros(numshots)
saturatedfrequencyerr = zeros(numshots)
saturatedpower = zeros(numshots)
timefieldon = zeros(numshots)
timesaturated = zeros(numshots)
timefieldoff = zeros(numshots)
freqband_min = zeros(numshots)
freqband_max = zeros(numshots)
#Shear measurements taken from 12 to 16 cm.
saturatedshear = zeros(numshots)
beginningshear = zeros(numshots)


#From scan of MRI 10% profiles: 400, irspeed, 53, 53
#Measurements taken at r=19.2 cm (location 40 channel 2)
i=0
shot[i] = 926
speed[i] = 400
irspeed[i] = 220
current[i] = 1000
saturatedfrequency[i] = 0.39
saturatedfrequencyerr[i] = 0.02
freqband_min[i] = 0.28
freqband_max[i] = 0.58
saturatedpower[i] = 13.4408
timefieldon[i] = 20
timesaturated[i] = 32
timefieldoff[i] = 60
saturatedshear[i] = -1.481773

i=1
shot[i] = 927
speed[i] = 400
irspeed[i] = 220
current[i] = 1200
saturatedfrequency[i] = 0.450
saturatedfrequencyerr[i] = 0.01
freqband_min[i] = 0.23
freqband_max[i] = 0.67
saturatedpower[i] = 37.813
timefieldon[i] = 20
timesaturated[i] = 32
timefieldoff[i] = 50
saturatedshear[i] = -1.411973

i=2
shot[i] = 909
speed[i] = 400
irspeed[i] = 220
current[i] = 700
saturatedfrequency[i] = 0.48
saturatedfrequencyerr[i] = 0.10
freqband_min[i] = 0.39
freqband_max[i] = 0.63
saturatedpower[i] = 0.06465
timefieldon[i] = 20
timesaturated[i] = 50
timefieldoff[i] = 75
saturatedshear[i] =-1.4061952

i=3
shot[i] = 1034
speed[i] = 400
irspeed[i] = 300
current[i] = 800
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 70
saturatedshear[i] = -1.39684

i=4
shot[i] = 1035
speed[i] = 400
irspeed[i] = 120
current[i] = 800
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 70
saturatedshear[i] = -0.9170165

i=5
shot[i] = 1036
speed[i] = 400
irspeed[i] = 220
current[i] = 800
saturatedfrequency[i] = 0.277
saturatedfrequencyerr[i] = 0.02
freqband_min[i] = 0.20
freqband_max[i] = 0.35
saturatedpower[i] = 5.41325
timefieldon[i] = 20
timesaturated[i] = 50
timefieldoff[i] = 70
saturatedshear[i] = -1.26525

i=6
shot[i] = 1037
speed[i] = 400
irspeed[i] = 140
current[i] = 800
saturatedfrequency[i] = 0.257
saturatedfrequencyerr[i] = 0.02
freqband_min[i] = 0.22
freqband_max[i] = 0.32
saturatedpower[i] = 0.3334
timefieldon[i] = 20
timesaturated[i] = 55
timefieldoff[i] = 70
saturatedshear[i] = -1.0121

i=7
shot[i] = 1038
speed[i] = 400
irspeed[i] = 300
current[i] = 1000
saturatedfrequency[i] = 0.465
saturatedfrequencyerr[i] = 0.005
freqband_min[i] = 0.40
freqband_max[i] = 0.50
saturatedpower[i] = 13.62497
timefieldon[i] = 20
timesaturated[i] = 40
timefieldoff[i] = 60
saturatedshear[i] = -1.66045

#Some weirdness after 55s, so only use interval from 40 to 55s.
i=8
shot[i] = 1039
speed[i] = 400
irspeed[i] = 140
current[i] = 1000
saturatedfrequency[i] = 0.31
saturatedfrequencyerr[i] = 0.01
freqband_min[i] = 0.30
freqband_max[i] = 0.40
saturatedpower[i] = 1.2151
timefieldon[i] = 20
timesaturated[i] = 40
timefieldoff[i] = 60
saturatedshear[i] = -0.971887

i=9
shot[i] = 1040
speed[i] = 400
irspeed[i] = 300
current[i] = 1200
saturatedfrequency[i] = 0.62
saturatedfrequencyerr[i] = 0.01
freqband_min[i] = 0.55
freqband_max[i] = 0.70
saturatedpower[i] = 66.8109
timefieldon[i] = 20
timesaturated[i] = 35
timefieldoff[i] = 50
saturatedshear[i] = -1.54702

i=10
shot[i] = 1041
speed[i] = 400
irspeed[i] = 140
current[i] = 1200
saturatedfrequency[i] = 0.30
saturatedfrequencyerr[i] = 0.01
freqband_min[i] = 0.25
freqband_max[i] = 0.35
saturatedpower[i] = 2.3233
timefieldon[i] = 20
timesaturated[i] = 30
timefieldoff[i] = 50
saturatedshear[i] = -0.788796

i=11
shot[i] = 1042
speed[i] = 400
irspeed[i] = 300
current[i] = 1400
saturatedfrequency[i] = 0.71
saturatedfrequencyerr[i] = 0.01
freqband_min[i] = 0.65
freqband_max[i] = 0.80
saturatedpower[i] = 81.261
timefieldon[i] = 20
timesaturated[i] = 30
timefieldoff[i] = 40
saturatedshear[i] = -1.44832

i=12
shot[i] = 1043
speed[i] = 400
irspeed[i] = 140
current[i] = 1400
saturatedfrequency[i] = 0.28
saturatedfrequencyerr[i] = 0.01
freqband_min[i] = 0.20
freqband_max[i] = 0.40
saturatedpower[i] = 5.350
timefieldon[i] = 20
timesaturated[i] = 30
timefieldoff[i] = 40
saturatedshear[i] = -0.74058

i=13
shot[i] = 1044
speed[i] = 400
irspeed[i] = 220
current[i] = 1400
saturatedfrequency[i] = 0.456
saturatedfrequencyerr[i] = 0.01
freqband_min[i] = 0.35
freqband_max[i] = 0.60
saturatedpower[i] = 31.105
timefieldon[i] = 20
timesaturated[i] = 32
timefieldoff[i] = 40
saturatedshear[i] = -1.007015

i=14
shot[i] = 1052
speed[i] = 400
irspeed[i] = 400
current[i] = 800
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 70
saturatedshear[i] = -2.11757

i=15
shot[i] = 1053
speed[i] = 400
irspeed[i] = 400
current[i] = 1000
saturatedfrequency[i] = 0.39
saturatedfrequencyerr[i] = 0.05
freqband_min[i] = 0.35
freqband_max[i] = 0.55
saturatedpower[i] = 3.35407
timefieldon[i] = 20
timesaturated[i] = 40
timefieldoff[i] = 60
saturatedshear[i] = -2.3716

i=16
shot[i] = 1054
speed[i] = 400
irspeed[i] = 400
current[i] = 1200
saturatedfrequency[i] = 0.54
saturatedfrequencyerr[i] = 0.03
freqband_min[i] = 0.45
freqband_max[i] = 0.55
saturatedpower[i] = 18.3904
timefieldon[i] = 20
timesaturated[i] = 40
timefieldoff[i] = 50
saturatedshear[i] = -2.62309

i=17
shot[i] = 1055
speed[i] = 400
irspeed[i] = 400
current[i] = 1400
saturatedfrequency[i] = 0.88
saturatedfrequencyerr[i] = 0.05
freqband_min[i] = 0.70
freqband_max[i] = 1.0
saturatedpower[i] = 84.462
timefieldon[i] = 20
timesaturated[i] = 25
timefieldoff[i] = 40
saturatedshear[i] = -2.0308


i=18
shot[i] = 1003
speed[i] = 400
irspeed[i] = 53
current[i] = 1200
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 50
saturatedshear[i] = -0.145585


i=19
shot[i] = 1004
speed[i] = 400
irspeed[i] = 53
current[i] = 1600
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 35
saturatedshear[i] = -0.3104


def get_data():
    mrized_data = {'shot': shot, 'speed': speed, 'current': current, 'saturatedfrequency': saturatedfrequency, 'saturatedfrequencyerr': saturatedfrequencyerr, 'saturatedpower': saturatedpower, 'timefieldon': timefieldon, 'timesaturated': timesaturated, 'timefieldoff': timefieldoff, 'irspeed':irspeed, 'saturatedshear': saturatedshear}
    return mrized_data

rho = 6.36 #Density of GaInSn in gm/cm^3
eta = 2.43e3 #Magnetic diffusivity in cm^2/sec

def plot_amplitudes():
    mrized_data = get_data()
    scatter(mrized_data['irspeed']*2.0*pi/60, mrized_data['current']*2.8669, mrized_data['saturatedpower']*20, label='_nolegend_')
    xlabel("IR Speed [rad/sec]")
    ylabel("B [Gauss]")
    title("$P_{fundamental}$")
    #also plot the xs.
    nan_idx = isnan(mrized_data['saturatedpower'])
    plot(mrized_data['irspeed'][nan_idx]*2.0*pi/60, mrized_data['current'][nan_idx]*2.8669, 'x', color='black', label='_nolegend_', markersize=10)

def plot_amplitudes_shear():
    mrized_data = get_data()
    scatter(-mrized_data['saturatedshear'], mrized_data['current']*2.8669, mrized_data['saturatedpower']*30, label='_nolegend_')
    xlabel("Saturated shear, 12-16cm [rad/cm*sec]")
    ylabel("B [Gauss]")
    title("$P_{fundamental}$")
    #also plot the xs.
    nan_idx = isnan(mrized_data['saturatedpower'])
    plot(-mrized_data['saturatedshear'][nan_idx], mrized_data['current'][nan_idx]*2.8669, 'x', color='black', label='_nolegend_', markersize=10)

def plot_frequencies():
    mrized_data = get_data()
    errorbar(mrized_data['irspeed'], mrized_data['saturatedfrequency'], yerr=mrized_data['saturatedfrequencyerr'], fmt='o')
    xlabel("IR Speed [RPM]")
    ylabel("Frequency [Hz]")
    title("Stable 10% shear scan")


