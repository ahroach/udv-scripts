from numpy import *
from pylab import *
numshots = 91

#Example commands
#UDV_helpers.plot_power_spectrum("1099.BDD", 2, 40, 28, 33.5, freqband_min=1.0, freqband_max=1.5)
#UDV_helpers.fit_frequency("1099.BDD", 2, 40, 28, 33.5, start_frequency=1.40, start_amplitude=14)


shot = zeros(numshots)
speed = zeros(numshots)
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

i = 0
shot[i] = 939
speed[i] = 400
current[i] = 600
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 70
saturatedshear[i] = -1.5527

i = 1
shot[i] = 943
speed[i] = 400
current[i] = 400
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 70
saturatedshear[i] = -1.14272

i = 2
shot[i] = 944
speed[i] = 400
current[i] = 700
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 70
saturatedshear[i] = -1.631213

i = 3
shot[i] = 945
speed[i] = 400
current[i] = 900
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 70
saturatedshear[i] = -2.18107

#Should only do from 24, to ~40 seconds.  Dies away after that.c
i = 4
shot[i] = 946
speed[i] = 400
current[i] = 1100
saturatedfrequency[i] = 0.987
saturatedfrequencyerr[i] = 0.030
freqband_min[i] = 0.8
freqband_max[i] = 1.25
saturatedpower[i] = 25.4145
timefieldon[i] = 20
timesaturated[i] = 24
timefieldoff[i] = 55
saturatedshear[i] = -2.467

i = 5
shot[i] = 947 
speed[i] = 400
current[i] = 1200
saturatedfrequency[i] = 0.95
saturatedfrequencyerr[i] = 0.05
freqband_min[i] = 0.75
freqband_max[i] = 1.30
saturatedpower[i] = 47.5379
timefieldon[i] = 20
timesaturated[i] = 24
timefieldoff[i] = 50
saturatedshear[i] = -2.61587

i = 6
shot[i] = 948
speed[i] = 400
current[i] = 1300
saturatedfrequency[i] = 0.997
saturatedfrequencyerr[i] = 0.005
freqband_min[i] = 0.75
freqband_max[i] = 1.30
saturatedpower[i] = 178.73433
timefieldon[i] = 20
timesaturated[i] = 25
timefieldoff[i] = 45
saturatedshear[i] = -2.336486

i = 7
shot[i] = 949
speed[i] = 400
current[i] = 1400
saturatedfrequency[i] = 1.13
saturatedfrequencyerr[i] = 0.05
freqband_min[i] = 0.75
freqband_max[i] = 1.30
saturatedpower[i] = 124.149
timefieldon[i] = 20
timesaturated[i] = 25
timefieldoff[i] = 40
saturatedshear[i] = -2.61616

i = 8
shot[i] = 950
speed[i] = 400
current[i] = 1500
saturatedfrequency[i] = 1.17
saturatedfrequencyerr[i] = 0.02
freqband_min[i] = 1.0
freqband_max[i] = 1.35
saturatedpower[i] = 153.633
timefieldon[i] = 20
timesaturated[i] = 24
timefieldoff[i] = 35
saturatedshear[i] = -2.5007305

i = 9
shot[i] = 951
speed[i] = 400
current[i] = 1600
saturatedfrequency[i] = 1.04
saturatedfrequencyerr[i] = 0.04
freqband_min[i] = 0.85
freqband_max[i] = 1.15
saturatedpower[i] = 279.92
timefieldon[i] = 20
timesaturated[i] = 25
timefieldoff[i] = 35
saturatedshear[i] = -2.10557

i = 10
shot[i] = 953
speed[i] = 400
current[i] = 1400
saturatedfrequency[i] = 1.02
saturatedfrequencyerr[i] = 0.02
freqband_min[i] = 0.85
freqband_max[i] = 1.15
saturatedpower[i] = 166.144
timefieldon[i] = 20
timesaturated[i] = 24
timefieldoff[i] = 40
saturatedshear[i] = -2.4494

#Only did spectrum from 24 to 30 seconds.  Weirdness after that.
i = 11
shot[i] = 954
speed[i] = 600
current[i] = 1400
saturatedfrequency[i] =1.55
saturatedfrequencyerr[i] = 0.1
freqband_min[i] = 1.0
freqband_max[i] = 1.9
saturatedpower[i] = 103.033
timefieldon[i] = 20
timesaturated[i] = 24
timefieldoff[i] = 40
saturatedshear[i] = -3.77453

i = 12
shot[i] = 955
speed[i] = 600
current[i] = 1200
saturatedfrequency[i] = 1.01
saturatedfrequencyerr[i] = 0.04
freqband_min[i] = 0.85
freqband_max[i] = 1.15
saturatedpower[i] = 10.953
timefieldon[i] = 20
timesaturated[i] =25
timefieldoff[i] = 50
saturatedshear[i] = -3.47629

i = 13
shot[i] = 956
speed[i] = 600
current[i] = 1000
saturatedfrequency[i] = 1.37
saturatedfrequencyerr[i] = 0.03
freqband_min[i] = 1.30
freqband_max[i] = 1.50
saturatedpower[i] = 2.10825
timefieldon[i] = 20
timesaturated[i] = 25
timefieldoff[i] = 60
saturatedshear[i] = -2.887623

i = 14
shot[i] = 957
speed[i] = 400
current[i] = 1000
saturatedfrequency[i] = 0.60
saturatedfrequencyerr[i] = 0.05
freqband_min[i] = 0.40
freqband_max[i] = 0.80
saturatedpower[i] = 2.91633
timefieldon[i] = 20
timesaturated[i] = 30
timefieldoff[i] = 60
saturatedshear[i] = -2.337136

i = 15
shot[i] = 958
speed[i] = 600
current[i] = 1100
saturatedfrequency[i] = 1.15
saturatedfrequencyerr[i] = 0.15
freqband_min[i] = 1.0
freqband_max[i] = 1.40
saturatedpower[i] = 2.8197
timefieldon[i] = 20
timesaturated[i] = 30
timefieldoff[i] = 55
saturatedshear[i] = -3.112143

i = 16
shot[i] = 959
speed[i] = 200
current[i] = 1100
saturatedfrequency[i] = 0.54
saturatedfrequencyerr[i] = 0.02
freqband_min[i] = 0.38
freqband_max[i] = 0.69
saturatedpower[i] = 65.915
timefieldon[i] = 20
timesaturated[i] = 25
timefieldoff[i] = 55
saturatedshear[i] = -1.15038

i = 17
shot[i] = 960
speed[i] = 200
current[i] = 1000
saturatedfrequency[i] = 0.535
saturatedfrequencyerr[i] = 0.015
freqband_min[i] = 0.36
freqband_max[i] = 0.66
saturatedpower[i] = 67.812
timefieldon[i] = 20
timesaturated[i] = 27
timefieldoff[i] = 60
saturatedshear[i] = -1.156337

i = 18
shot[i] = 961
speed[i] = 200
current[i] = 900
saturatedfrequency[i] = 0.47
saturatedfrequencyerr[i] = 0.01
freqband_min[i] = 0.34
freqband_max[i] = 0.56
saturatedpower[i] = 33.984
timefieldon[i] = 20
timesaturated[i] = 27
timefieldoff[i] = 65
saturatedshear[i] = -1.3113414

i = 19
shot[i] = 962
speed[i] = 200
current[i] = 800
saturatedfrequency[i] = 0.40
saturatedfrequencyerr[i] = 0.02
freqband_min[i] = 0.30
freqband_max[i] = 0.50
saturatedpower[i] = 15.2418
timefieldon[i] = 20
timesaturated[i] = 37
timefieldoff[i] = 70
saturatedshear[i] = -1.3340047

i = 20
shot[i] = 963
speed[i] = 200
current[i] = 700
saturatedfrequency[i] = 0.30
saturatedfrequencyerr[i] = 0.03
freqband_min[i] = 0.20
freqband_max[i] = 0.50
saturatedpower[i] = 5.264
timefieldon[i] = 20
timesaturated[i] = 32
timefieldoff[i] = 70
saturatedshear[i] = -1.220107

i = 21
shot[i] = 964
speed[i] = 200
current[i] = 600
saturatedfrequency[i] = 0.25
saturatedfrequencyerr[i] = 0.03
freqband_min[i] = 0.15
freqband_max[i] = 0.35
saturatedpower[i] = 1.18654
timefieldon[i] = 20
timesaturated[i] = 45
timefieldoff[i] = 70
saturatedshear[i] = -1.067340

i = 22
shot[i] = 965
speed[i] = 200
current[i] = 500
saturatedfrequency[i] = 0.26
saturatedfrequencyerr[i] = 0.03
freqband_min[i] = 0.15
freqband_max[i] = 0.30
saturatedpower[i] = 0.17965
timefieldon[i] = 20
timesaturated[i] = 35
timefieldoff[i] = 70
saturatedshear[i] = -0.932147

i = 23
shot[i] = 966
speed[i] = 200
current[i] = 400
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 70
saturatedshear[i] = -0.75823

i = 24
shot[i] = 967
speed[i] = 100
current[i] = 400 
saturatedfrequency[i] = 0.195
saturatedfrequencyerr[i] = 0.01
freqband_min[i] = 0.15
freqband_max[i] = 0.30
saturatedpower[i] = 0.64628
timefieldon[i] = 20
timesaturated[i] = 35
timefieldoff[i] = 70
saturatedshear[i] = -0.5139

i = 25
shot[i] = 968
speed[i] = 100
current[i] = 500
saturatedfrequency[i] = 0.19
saturatedfrequencyerr[i] = 0.03
freqband_min[i] = 0.10
freqband_max[i] = 0.30
saturatedpower[i] = 3.557823
timefieldon[i] = 20 
timesaturated[i] = 33
timefieldoff[i] = 70
saturatedshear[i] = -0.60290

i = 26
shot[i] = 969
speed[i] = 100
current[i] = 600
saturatedfrequency[i] = 0.240
saturatedfrequencyerr[i] = 0.015
freqband_min[i] = 0.15
freqband_max[i] = 0.35
saturatedpower[i] = 7.95912
timefieldon[i] = 20
timesaturated[i] = 35
timefieldoff[i] = 70
saturatedshear[i] = -0.637253

i = 27
shot[i] = 970
speed[i] = 100
current[i] = 300
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 70
saturatedshear[i] = -0.410969

i = 28
shot[i] = 971
speed[i] = 50
current[i] = 300
saturatedfrequency[i] = 0.100
saturatedfrequencyerr[i] = 0.015
freqband_min[i] = 0.05
freqband_max[i] = 0.15
saturatedpower[i] = 0.40512
timefieldon[i] = 20
timesaturated[i] = 33
timefieldoff[i] = 70
saturatedshear[i] = -0.25822

i = 29
shot[i] = 972
speed[i] = 50
current[i] = 400
saturatedfrequency[i] = 0.125
saturatedfrequencyerr[i] = 0.006
freqband_min[i] = 0.075
freqband_max[i] = 0.19
saturatedpower[i] = 1.719408
timefieldon[i] = 20
timesaturated[i] = 36
timefieldoff[i] = 70
saturatedshear[i] = -0.29219

i = 30
shot[i] = 973
speed[i] = 50
current[i] = 500
saturatedfrequency[i] = 0.132
saturatedfrequencyerr[i] = 0.005
freqband_min[i] = 0.05
freqband_max[i] = 0.23
saturatedpower[i] = 4.4797
timefieldon[i] = 20
timesaturated[i] = 36
timefieldoff[i] = 70
saturatedshear[i] = -0.27019

i = 31
shot[i] = 974
speed[i] = 50
current[i] = 200
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 70
saturatedshear[i] = -0.19413

#Used channel 3 on this one: clearer signal
i = 32
shot[i] = 975
speed[i] = 50
current[i] = 1600
saturatedfrequency[i] = 0.113
saturatedfrequencyerr[i] = 0.01
freqband_min[i] = 0.10
freqband_max[i] = 0.60
saturatedpower[i] = 1.372
timefieldon[i] = 20
timesaturated[i] = 29
timefieldoff[i] = 35
saturatedshear[i] = -0.292567

i = 33
shot[i] = 976
speed[i] = 700
current[i] = 1200
saturatedfrequency[i] = 1.28
saturatedfrequencyerr[i] = 0.07
freqband_min[i] = 1.05
freqband_max[i] = 1.70
saturatedpower[i] = 8.04103
timefieldon[i] = 20
timesaturated[i] = 30
timefieldoff[i] = 50
saturatedshear[i] = -3.69716

i = 34
shot[i] = 977
speed[i] = 700
current[i] = 1300
saturatedfrequency[i] = 1.13
saturatedfrequencyerr[i] = 0.06
freqband_min[i] = 0.80
freqband_max[i] = 1.40
saturatedpower[i] = 8.4940
timefieldon[i] = 20
timesaturated[i] = 30
timefieldoff[i] = 45 
saturatedshear[i] = -3.8889103

i = 35
shot[i] = 978
speed[i] = 700
current[i] = 1400
saturatedfrequency[i] = 1.22
saturatedfrequencyerr[i] = 0.05
freqband_min[i] = 1.0
freqband_max[i] = 1.5
saturatedpower[i] = 23.4955
timefieldon[i] = 20
timesaturated[i] = 27
timefieldoff[i] = 40
saturatedshear[i] = -3.95703

#Only did interval from 26 to 29 seconds.  Field droop at end?
i = 36
shot[i] = 979
speed[i] = 700
current[i] = 1600
saturatedfrequency[i] = 1.55
saturatedfrequencyerr[i] = 0.05
freqband_min[i] = 1.2
freqband_max[i] = 2.2
saturatedpower[i] = 226.118
timefieldon[i] = 20
timesaturated[i] = 26
timefieldoff[i] = 35 
saturatedshear[i] = -4.627321

i = 37
shot[i] = 980
speed[i] = 200
current[i] = 1600
saturatedfrequency[i] = 0.532
saturatedfrequencyerr[i] = 0.001
freqband_min[i] = 0.50
freqband_max[i] = 0.70
saturatedpower[i] = 66.1434
timefieldon[i] = 20
timesaturated[i] = 27
timefieldoff[i] = 35
saturatedshear[i] = -1.13171

i = 38
shot[i] = 981
speed[i] = 100
current[i] = 1600
saturatedfrequency[i] = 0.246
saturatedfrequencyerr[i] = 0.002
freqband_min[i] = 0.10
freqband_max[i] = 0.60
saturatedpower[i] = 33.888
timefieldon[i] = 20
timesaturated[i] = 29
timefieldoff[i] = 35
saturatedshear[i] = -0.4422470

i = 39
shot[i] = 982
speed[i] = 700
current[i] = 1500
saturatedfrequency[i] = 1.48
saturatedfrequencyerr[i] = 0.12
freqband_min[i] = 1.30
freqband_max[i] = 1.80
saturatedpower[i] = 44.789
timefieldon[i] = 20
timesaturated[i] = 25
timefieldoff[i] = 35
saturatedshear[i] = -4.54313

i = 40
shot[i] = 983
speed[i] = 700
current[i] = 100
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 70
saturatedshear[i] = -1.79223

i = 41
shot[i] = 984
speed[i] = 700
current[i] = 250
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 70
saturatedshear[i] = -1.93907

i = 42
shot[i] = 985
speed[i] = 700
current[i] = 300
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 70
saturatedshear[i] = -2.02837

i = 43
shot[i] = 986
speed[i] = 700
current[i] = 400
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 70
saturatedshear[i] = -2.06967

i = 44
shot[i] = 987
speed[i] = 700
current[i] = 500
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 70
saturatedshear[i] = -1.98387

i = 45
shot[i] = 988
speed[i] = 700
current[i] = 600
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 70
saturatedshear[i] = -2.003006

i = 46
shot[i] = 989
speed[i] = 700
current[i] = 700
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 70
saturatedshear[i] = -2.26845

i = 47
shot[i] = 990
speed[i] = 700
current[i] = 800
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 70
saturatedshear[i] = -2.678014

i = 48
shot[i] = 991
speed[i] = 700
current[i] = 900
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 65
saturatedshear[i] = -2.80618

i = 49
shot[i] = 992
speed[i] = 700
current[i] = 1000
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 65
saturatedshear[i] = -2.93815

i = 50
shot[i] = 993
speed[i] = 700
current[i] = 1100
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 55
saturatedshear[i] = -3.177322

i = 51
shot[i] = 1007
speed[i] = 25
current[i] = 1200
saturatedfrequency[i] = .045
saturatedfrequencyerr[i] = .005
freqband_min[i] = .00001
freqband_max[i] = .035
saturatedpower[i] = 0.75242
timefieldon[i] = 20
timesaturated[i] = 40
timefieldoff[i] = 50
saturatedshear[i] = nan


i = 52
shot[i] = 1008
speed[i] = 25
current[i] = 600
saturatedfrequency[i] = 0.065
saturatedfrequencyerr[i] = 0.005
freqband_min[i] = .03
freqband_max[i] = .09
saturatedpower[i] = 1.8726
timefieldon[i] = 20
timesaturated[i] = 64
timefieldoff[i] = 140
saturatedshear[i] = nan


i = 53
shot[i] = 1009
speed[i] = 25
current[i] = 200
saturatedfrequency[i] = 0.035
saturatedfrequencyerr[i] = 0.010
freqband_min[i] = .02
freqband_max[i] = .08
saturatedpower[i] = 0.009405
timefieldon[i] = 20
timesaturated[i] = 140
timefieldoff[i] = 260
saturatedshear[i] = nan


i = 54
shot[i] = 1010
speed[i] = 25
current[i] = 400
saturatedfrequency[i] = 0.0695
saturatedfrequencyerr[i] = 0.0002 
freqband_min[i] = 0.055
freqband_max[i] = 0.080
saturatedpower[i] = 1.6305
timefieldon[i] = 20
timesaturated[i] = 80
timefieldoff[i] = 260
saturatedshear[i] = nan


i = 55
shot[i] = 1011
speed[i] = 25
current[i] = 100
saturatedfrequency[i] = nan 
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 260
saturatedshear[i] = nan

#Just do to 43 seconds to avoid noisy wrap-arounds
i = 56
shot[i] = 1089
speed[i] = 800
current[i] = 1200
saturatedfrequency[i] = 1.15
saturatedfrequencyerr[i] = 0.20
freqband_min[i] = 1.0
freqband_max[i] = 1.25
saturatedpower[i] = 3.187
timefieldon[i] = 20
timesaturated[i] = 32
timefieldoff[i] = 50
saturatedshear[i] = nan


#Cut off after 33.5, because there's weirdness.
i = 57
shot[i] = 1099
speed[i] = 600
current[i] = 1600
saturatedfrequency[i] = 1.39
saturatedfrequencyerr[i] = 0.02
freqband_min[i] = 1.0
freqband_max[i] = 1.5
saturatedpower[i] = 188.6
timefieldon[i] = 20
timesaturated[i] = 28
timefieldoff[i] = 35
saturatedshear[i] = nan

#Just do to 33.5 seconds again.  Field droop?
i = 58
shot[i] = 1100
speed[i] = 800
current[i] = 1600
saturatedfrequency[i] = 1.46
saturatedfrequencyerr[i] = 0.03
freqband_min[i] = 1.25
freqband_max[i] = 1.75
saturatedpower[i] = 143.59
timefieldon[i] = 20
timesaturated[i] = 28
timefieldoff[i] = 35
saturatedshear[i] = nan

i = 59
shot[i] = 1101
speed[i] = 800
current[i] = 1200
saturatedfrequency[i] = 1.07
saturatedfrequencyerr[i] = 0.2
freqband_min[i] = 0.9
freqband_max[i] = 1.2
saturatedpower[i] = 4.33
timefieldon[i] = 20
timesaturated[i] = 30
timefieldoff[i] = 50
saturatedshear[i] = nan


i = 60
shot[i] = 1106
speed[i] = 800
current[i] = 900
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 65
saturatedshear[i] = nan


i = 61
shot[i] = 1188
speed[i] = 10
current[i] = 400
saturatedfrequency[i] = 0.023
saturatedfrequencyerr[i] = 0.01
freqband_min[i] = 0.008
freqband_max[i] = 0.0306
saturatedpower[i] = 0.2146
timefieldon[i] = 20
timesaturated[i] = 115
timefieldoff[i] = 260
saturatedshear[i] = nan

i = 62
shot[i] = 1189
speed[i] = 5
current[i] = 400 
saturatedfrequency[i] = 0.01
saturatedfrequencyerr[i] = 0.01
freqband_min[i] = 0.0057
freqband_max[i] = 0.020
saturatedpower[i] = 0.071
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 260
saturatedshear[i] = nan

i = 63
shot[i] = 1190
speed[i] = 3
current[i] = 300 
saturatedfrequency[i] = 0.00645
saturatedfrequencyerr[i] = 0.0020
freqband_min[i] = 0.00242
freqband_max[i] = 0.0121
saturatedpower[i] = 0.0371
timefieldon[i] = 20 
timesaturated[i] = 150
timefieldoff[i] = 440
saturatedshear[i] = nan

i = 64
shot[i] = 1191
speed[i] = 3
current[i] = 50 
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 20
timesaturated[i] = nan
timefieldoff[i] = 1220
saturatedshear[i] = nan

i = 65
shot[i] =  1192
speed[i] = 3
current[i] = 100 
saturatedfrequency[i] = 0.0073
saturatedfrequencyerr[i] = 0.001
freqband_min[i] = 0.00565
freqband_max[i] = 0.00887
saturatedpower[i] = 0.00246
timefieldon[i] = 20
timesaturated[i] = 350
timefieldoff[i] = 1220
saturatedshear[i] = nan

i = 66
shot[i] = 1193
speed[i] = 1
current[i] = 100 
saturatedfrequency[i] = 0.0021
saturatedfrequencyerr[i] = 0.0005
freqband_min[i] = 0.0015
freqband_max[i] = 0.0030
saturatedpower[i] = 0.002101
timefieldon[i] = 125
timesaturated[i] = 1030
timefieldoff[i] = 3725
saturatedshear[i] = nan

i = 67
shot[i] = 1194
speed[i] = 1
current[i] = 30 
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 125
timesaturated[i] = nan
timefieldoff[i] = 3725
saturatedshear[i] = nan

i = 68
shot[i] = 1198
speed[i] = 0.5
current[i] = 45
saturatedfrequency[i] = 0.00242 
saturatedfrequencyerr[i] = 0.0005
freqband_min[i] = 0.0018
freqband_max[i] = 0.0032
saturatedpower[i] = 6.263e-5
timefieldon[i] = 125
timesaturated[i] = 2310
timefieldoff[i] = 5525
saturatedshear[i] = nan

i = 69
shot[i] = 1199
speed[i] = 0.5
current[i] = 25
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 125
timesaturated[i] = nan
timefieldoff[i] = 3725
saturatedshear[i] = nan

#Many m numbers during shot, unclear what to do with spectrum
i = 70
shot[i] = 1200
speed[i] = 0.5
current[i] = 250
saturatedfrequency[i] = 0.00516/3
saturatedfrequencyerr[i] = 0.0055/3
freqband_min[i] = 0.004
freqband_max[i] = 0.0056
saturatedpower[i] = 0.0002138
timefieldon[i] = 125
timesaturated[i] = 1000
timefieldoff[i] = 3725
saturatedshear[i] = nan

i = 71
shot[i] = 1206
speed[i] = 0.5
current[i] = 100
saturatedfrequency[i] = 0.00091
saturatedfrequencyerr[i] = 0.00030
freqband_min[i] = 0.000645
freqband_max[i] = 0.00161
saturatedpower[i] = 0.000401
timefieldon[i] = 125 
timesaturated[i] = 1500
timefieldoff[i] = 3725
saturatedshear[i] = nan

i = 72
shot[i] = 1207
speed[i] = 0.5
current[i] = 60
saturatedfrequency[i] = 0.00184 
saturatedfrequencyerr[i] = 0.0007
freqband_min[i] = 0.00108
freqband_max[i] = 0.0025
saturatedpower[i] = 0.0001543
timefieldon[i] = 125
timesaturated[i] = 2100
timefieldoff[i] = 3725
saturatedshear[i] = nan

i = 73
shot[i] = 1208
speed[i] = 0.5
current[i] = 80
saturatedfrequency[i] = 0.001 
saturatedfrequencyerr[i] = 0.005
freqband_min[i] = 0.0005
freqband_max[i] = 0.0018
saturatedpower[i] = 0.000381567
timefieldon[i] = 125
timesaturated[i] = 1700
timefieldoff[i] = 3725
saturatedshear[i] = nan

#m=2 for 2/3rds of shot
i = 74
shot[i] = 1209
speed[i] = 0.5
current[i] = 150
saturatedfrequency[i] = 0.0009
saturatedfrequencyerr[i] = 0.0003
freqband_min[i] = 0.0006
freqband_max[i] = 0.0012
saturatedpower[i] = 0.000375
timefieldon[i] = 125
timesaturated[i] = 2660
timefieldoff[i] = 3725
saturatedshear[i] = nan

#Dominant frequency here is m=2. Complicated behavior abounds.
i = 75
shot[i] = 1210
speed[i] = 0.5
current[i] = 200
saturatedfrequency[i] = 2.78e-3/2
saturatedfrequencyerr[i] = 3.0e-4/2
freqband_min[i] = 2.5e-3
freqband_max[i] = 3.2e-3
saturatedpower[i] = 4.664e-4
timefieldon[i] = 125
timesaturated[i] = 850
timefieldoff[i] = 3725
saturatedshear[i] = nan

#Short shot, complicated mode structure, much uncertainty
i = 76
shot[i] = 1214
speed[i] = 0.5
current[i] = 300
saturatedfrequency[i] = 6.665e-3/3
saturatedfrequencyerr[i] = 3e-3/3
freqband_min[i] = 3.2e-3
freqband_max[i] = 1e-2
saturatedpower[i] = 1.51e-4
timefieldon[i] = 125
timesaturated[i] = 500
timefieldoff[i] = 800
saturatedshear[i] = nan

#Very complicated. Lots of harmonics. Picking dominant one, m=2?
i = 77
shot[i] = 1215
speed[i] = 1
current[i] = 250 
saturatedfrequency[i] = 2.83e-3
saturatedfrequencyerr[i] = 3.0e-4
freqband_min[i] = 2.2e-3
freqband_max[i] = 3.4e-3
saturatedpower[i] = 8.967e-4
timefieldon[i] = 125
timesaturated[i] = 900
timefieldoff[i] = 3725
saturatedshear[i] = nan


#Not a clean spectrum at all.  Icky.  Not sure what's going on.
i = 78
shot[i] = 1216
speed[i] = 1
current[i] = 60 
saturatedfrequency[i] = 4.5e-3
saturatedfrequencyerr[i] = 1.5e-3
freqband_min[i] = 3e-3
freqband_max[i] = 6e-3
saturatedpower[i] = 1.202e-4
timefieldon[i] = 125
timesaturated[i] = 500
timefieldoff[i] = 3725
saturatedshear[i] = nan

i = 79
shot[i] = 1221
speed[i] = 1
current[i] = 45
saturatedfrequency[i] = 4.8e-3
saturatedfrequencyerr[i] = 4e-4
freqband_min[i] = 4.4e-3
freqband_max[i] = 5.6e-3
saturatedpower[i] = 5.82e-6
timefieldon[i] = 125
timesaturated[i] = 2500
timefieldoff[i] = 3725
saturatedshear[i] = nan

i = 80
shot[i] = 1218
speed[i] = 0.5
current[i] = 40
saturatedfrequency[i] = 2.26e-3 
saturatedfrequencyerr[i] = 7e-4
freqband_min[i] = 8e-4
freqband_max[i] = 3.3e-3
saturatedpower[i] = 4.317e-5
timefieldon[i] = 0
timesaturated[i] = 1500
timefieldoff[i] = 3580
saturatedshear[i] = nan

i = 81
shot[i] = 1219
speed[i] = 0.5
current[i] = 32
saturatedfrequency[i] = 1.2e-3
saturatedfrequencyerr[i] = 4.0e-4
freqband_min[i] = 0.6e-3
freqband_max[i] = 2.0e-3
saturatedpower[i] = 7.398e-6
timefieldon[i] = 125
timesaturated[i] = 2200
timefieldoff[i] = 3725
saturatedshear[i] = nan


i = 82
shot[i] = 1222
speed[i] = 3
current[i] = 80
saturatedfrequency[i] = 4.8e-3
saturatedfrequencyerr[i] = 1.0e-3
freqband_min[i] = 2.8e-3
freqband_max[i] = 5.6e-3
saturatedpower[i] = 2.484e-4
timefieldon[i] = 125
timesaturated[i] = 700
timefieldoff[i] = 1325
saturatedshear[i] = nan


i = 83
shot[i] = 1227
speed[i] = 0.25
current[i] = 30
saturatedfrequency[i] = 3.0e-3
saturatedfrequencyerr[i] = 1.5e-3
freqband_min[i] = 2.4e-3
freqband_max[i] = 4.1e-3
saturatedpower[i] = 9.457e-7
timefieldon[i] = 125
timesaturated[i] = 3500
timefieldoff[i] = 5525
saturatedshear[i] = nan

#Note that the primary mode here is m=2
i = 84
shot[i] = 1228
speed[i] = 0.25
current[i] = 65
saturatedfrequency[i] = 1.78e-3/2
saturatedfrequencyerr[i] = 1.0e-4/2
freqband_min[i] = 1.5e-3
freqband_max[i] = 2.0e-3
saturatedpower[i] = 8.315e-5
timefieldon[i] = 125
timesaturated[i] = 1000
timefieldoff[i] = 5525
saturatedshear[i] = nan


#Note that the primary mode here appears to be m=4
i = 85
shot[i] = 1229
speed[i] = 0.25
current[i] = 250
saturatedfrequency[i] = 4.2e-3/4
saturatedfrequencyerr[i] = 3.0e-4/4
freqband_min[i] = 3.6e-3
freqband_max[i] = 4.7e-3
saturatedpower[i] = 1.57e-5
timefieldon[i] = 125
timesaturated[i] = 1500
timefieldoff[i] = 5525
saturatedshear[i] = nan


i = 86
shot[i] = 1230
speed[i] = 0.25
current[i] = 20
saturatedfrequency[i] = nan
saturatedfrequencyerr[i] = nan
freqband_min[i] = nan
freqband_max[i] = nan
saturatedpower[i] = nan
timefieldon[i] = 125
timesaturated[i] = nan
timefieldoff[i] = 5525
saturatedshear[i] = nan

#Note that primary mode here is m=3
i = 87
shot[i] = 1231
speed[i] = 0.25
current[i] = 150
saturatedfrequency[i] = 2.9e-3/3
saturatedfrequencyerr[i] = 3.0e-4/3
freqband_min[i] = 2.4e-3
freqband_max[i] = 3.5e-3
saturatedpower[i] = 6.7514e-5
timefieldon[i] = 125
timesaturated[i] = 1200
timefieldoff[i] = 5525
saturatedshear[i] = nan

#Primarily m=4
i = 88
shot[i] = 1232
speed[i] = 0.25
current[i] = 200
saturatedfrequency[i] = 4.2e-3/4
saturatedfrequencyerr[i] = 3.0e-4/4
freqband_min[i] = 3.63e-3
freqband_max[i] = 4.94e-3
saturatedpower[i] = 2.53e-5
timefieldon[i] = 125
timesaturated[i] = 1500
timefieldoff[i] = 5525
saturatedshear[i] = nan

#primarily m=2
i = 89
shot[i] = 1233
speed[i] = 0.25
current[i] = 100
saturatedfrequency[i] = 1.61e-3/2
saturatedfrequencyerr[i] = 3.0e-4/2
freqband_min[i] = 1.0e-3
freqband_max[i] = 2.5e-3
saturatedpower[i] = 1.3510e-4
timefieldon[i] = 125
timesaturated[i] = 3200
timefieldoff[i] = 5525
saturatedshear[i] = nan

#Possibly m=5?!
i = 90
shot[i] = 1235
speed[i] = 0.25
current[i] = 280
saturatedfrequency[i] = 5.75e-3/5
saturatedfrequencyerr[i] = 3.0e-4/5
freqband_min[i] = 5.2e-3
freqband_max[i] = 6.2e-3
saturatedpower[i] = 4.196e-6
timefieldon[i] = 125
timesaturated[i] = 1000
timefieldoff[i] = 5525
saturatedshear[i] = nan




def get_data():
    su_data = {'shot': shot, 'speed': speed, 'current': current, 'saturatedfrequency': saturatedfrequency, 'saturatedfrequencyerr': saturatedfrequencyerr, 'saturatedpower': saturatedpower, 'timefieldon': timefieldon, 'timesaturated': timesaturated, 'timefieldoff': timefieldoff, 'saturatedshear': saturatedshear}
    return su_data

rho = 6.36 #Density of GaInSn in gm/cm^3
eta = 2.43e3 #Magnetic diffusivity in cm^2/sec

def plot_amplitudes(elsasser = 1, logscale=0, rpm=0, elsasser_y_axis=0,
                    showtitle=1):
    su_data = get_data()
    if(rpm==0):
        xquantity = su_data['speed']*2*pi/60
    else:
        xquantity = su_data['speed']
    ax = subplot(111)
    nan_idx = isnan(su_data['saturatedpower'])
    num_idx= ~nan_idx
    
    elsasser_num = 4.0413e-4*su_data['current']*su_data['current']/su_data['speed']
    
    if(elsasser_y_axis):
        ax.scatter(xquantity[num_idx], elsasser_num[num_idx], su_data['saturatedpower'][num_idx]*300000/(su_data['speed'][num_idx]*su_data['speed'][num_idx]), label='_nolegend_')
        #also plot the xs.
        ax.plot(xquantity[nan_idx], elsasser_num[nan_idx], 'x', color='black', label='_nolegend_')
        ylabel(r'$\Lambda$')
    else:
        ax.scatter(xquantity[num_idx], su_data['current'][num_idx]*2.8669, su_data['saturatedpower'][num_idx]*300000/(su_data['speed'][num_idx]*su_data['speed'][num_idx]), label='_nolegend_')
        #also plot the xs.
        ax.plot(xquantity[nan_idx], su_data['current'][nan_idx]*2.8669, 'x', color='black', label='_nolegend_')
        ylabel("B [Gauss]")
            
    if(logscale==1):
        ax.set_xscale('log')
        ax.set_yscale('log')
    if(rpm==0):
        xlabel("IC Speed [rad/sec]")
    else:
        xlabel("IC Speed [rpm]")
    
    if(showtitle):
        title("$P_{fundamental}/\Omega_{IC}^2$")
    
    #Now plot line for Elsasser number constant
    #Defined as v_A^2/(eta*Omega)
    Omega = linspace(0.001,1200, 5000)
    Omega = Omega*2*pi/60
    B_crit = sqrt(4*pi*rho*eta*Omega*elsasser)
    labelstring = "$\Lambda = $" + str(elsasser)
    axes = axis()
    if(rpm!=0):
        Omega = Omega*60/(2*pi)

    if(elsasser_y_axis==0):
        plot(Omega, B_crit, color='k', label=labelstring)
        
    axis(axes)
    legend(loc='lower right')


def plot_amplitudes_shear(elsasser = 1):
    su_data = get_data()
    scatter(-su_data['saturatedshear'], su_data['current']*2.8669, su_data['saturatedpower']*30000000/(su_data['speed']*su_data['speed']), label='_nolegend_')
    #also plot the xs.
    nan_idx = isnan(su_data['saturatedpower'])
    plot(-su_data['saturatedshear'][nan_idx], su_data['current'][nan_idx]*2.8669, 'x', color='black', label='_nolegend_')
    xlabel("Saturated shear, 12-16cm [rad/cm*sec]")
    ylabel("B [Gauss]")
    title("$P_{fundamental}/(IC\, \mathrm{speed})^2$")
    #Now plot line for Elsasser number constant
    #Defined as v_A^2/(eta*Omega)

    #Omega = linspace(0.0,1200.0, 1000.0)
    #Omega = Omega*2.0*pi/60
    #B_crit = sqrt(4*pi*rho*eta*Omega*elsasser)
    #labelstring = "$\Lambda = $" + str(elsasser)
    #axes = axis()
    #plot(Omega, B_crit, color='k', label=labelstring)
    #axis(axes)
    #legend(loc='lower right')



def plot_quantity_at_speed(quantity, speed):
    su_data = get_data()
    
    count = 0
    for i in range(0, su_data['speed'].size):
        if (su_data['speed'][i] == speed):
            count = count + 1
            
    quantity_array = zeros(count)
    current_array = zeros(count)
    
    index = 0
    for i in range(0, su_data['speed'].size):
        if (su_data['speed'][i] == speed):
            quantity_array[index] = su_data[quantity][i]
            current_array[index] = su_data['current'][i]
            index = index + 1
                
    plot(current_array*2.8669, quantity_array, 'o')
    xlabel("Magnetic Field [G]")
    ylabel(quantity)
    title("Split-unstable oscillations")

    return current_array*2.8669, quantity_array

def plot_frequency_at_speed(speed):
    su_data = get_data()
    
    speed_idx = (su_data['speed'] == speed)

    labelstring = str(speed) + " RPM"
    errorbar(su_data['current'][speed_idx]*2.8669, su_data['saturatedfrequency'][speed_idx], yerr=su_data['saturatedfrequencyerr'][speed_idx], fmt='o', label=labelstring)
    xlabel("Magnetic Field [G]")
    ylabel("Frequency [Hz]")
    title("Split-unstable oscillations")
    
