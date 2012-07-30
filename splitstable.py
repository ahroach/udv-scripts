import numpy
numshots = 43

#Example commands
#UDV_helpers.plot_power_spectrum("1099.BDD", 2, 40, 28, 33.5, freqband_min=1.0, freqband_max=1.5)
#UDV_helpers.fit_frequency("1099.BDD", 2, 40, 28, 33.5, start_frequency=1.40, start_amplitude=14)


shot = numpy.zeros(numshots)
omega1 = numpy.zeros(numshots)
omega2 = numpy.zeros(numshots)
current = numpy.zeros(numshots)
saturatedfrequency = numpy.zeros(numshots)
saturatedfrequencyerr = numpy.zeros(numshots)
saturatedpower = numpy.zeros(numshots)
saturatedintervalstart = numpy.zeros(numshots)
saturatedintervalstop = numpy.zeros(numshots)
timefieldon = numpy.zeros(numshots)
timesaturated = numpy.zeros(numshots)
timefieldoff = numpy.zeros(numshots)
freqband_min = numpy.zeros(numshots)
freqband_max = numpy.zeros(numshots)


i = 0
shot[i] = 1248
omega1[i] = 110
omega2[i] = 100
current[i] = 0
saturatedfrequency[i] = 0.025
saturatedfrequencyerr[i] = 0.005
freqband_min[i] = 0.02
freqband_max[i] = 0.03
saturatedpower[i] = 0.138
saturatedintervalstart[i] = 120
saturatedintervalstop[i] = 480
timefieldon[i] = numpy.nan
timesaturated[i] = 120
timefieldoff[i] = numpy.nan

i = 1
shot[i] = 1249
omega1[i] = 110
omega2[i] = 100
current[i] = 400
saturatedfrequency[i] = 0.02
saturatedfrequencyerr[i] = 0.005
freqband_min[i] = 0.015
freqband_max[i] = 0.025
saturatedpower[i] = 0.0825
saturatedintervalstart[i] = 140
saturatedintervalstop[i] = 395
timefieldon[i] = 125
timesaturated[i] = 140
timefieldoff[i] = 395


i = 2
shot[i] = 1250
omega1[i] = 110
omega2[i] = 100
current[i] = 0
saturatedfrequency[i] = 0.020
saturatedfrequencyerr[i] = 0.005
freqband_min[i] = 0.015
freqband_max[i] = 0.025
saturatedpower[i] = 0.0933
saturatedintervalstart[i] = 0
saturatedintervalstop[i] = 485
timefieldon[i] = numpy.nan
timesaturated[i] = 0
timefieldoff[i] = numpy.nan


i = 3
shot[i] = 1251
omega1[i] = 110
omega2[i] = 100
current[i] = 0
saturatedfrequency[i] = 0.015
saturatedfrequencyerr[i] = 0.005
freqband_min[i] = 0.010
freqband_max[i] = 0.020
saturatedpower[i] = 0.0371
saturatedintervalstart[i] = 120
saturatedintervalstop[i] = 1575
timefieldon[i] = numpy.nan
timesaturated[i] = 120
timefieldoff[i] = numpy.nan


i = 4
shot[i] = 1252
omega1[i] = 110
omega2[i] = 100
current[i] = 400
saturatedfrequency[i] = 0.02
saturatedfrequencyerr[i] = 0.005
freqband_min[i] = 0.015
freqband_max[i] = 0.025
saturatedpower[i] = 0.0387
saturatedintervalstart[i] = 0
saturatedintervalstop[i] = 470
timefieldon[i] = 200
timesaturated[i] = 0
timefieldoff[i] = 500


i = 5
shot[i] = 1253
omega1[i] = 110
omega2[i] = 100
current[i] = 600
saturatedfrequency[i] = 0.021
saturatedfrequencyerr[i] = 0.005
freqband_min[i] = 0.016
freqband_max[i] = 0.026
saturatedpower[i] = 0.0691
saturatedintervalstart[i] = 0
saturatedintervalstop[i] = 475
timefieldon[i] = 400
timesaturated[i] = 0
timefieldoff[i] = 480


i = 6
shot[i] = 1254
omega1[i] = 120
omega2[i] = 100
current[i] = 600
saturatedfrequency[i] = 0.062
saturatedfrequencyerr[i] = 0.006
freqband_min[i] = 0.056
freqband_max[i] = 0.068
saturatedpower[i] = 1.331
saturatedintervalstart[i] = 0
saturatedintervalstop[i] = 480
timefieldon[i] = 360
timesaturated[i] = 0
timefieldoff[i] = 480


i = 7
shot[i] = 1255
omega1[i] = 120
omega2[i] = 100
current[i] = 800
saturatedfrequency[i] = 0.06
saturatedfrequencyerr[i] = 0.005
freqband_min[i] = 0.055
freqband_max[i] = 0.065
saturatedpower[i] = 1.122
saturatedintervalstart[i] = 115
saturatedintervalstop[i] = 430
timefieldon[i] = 360
timesaturated[i] = 115
timefieldoff[i] = 430


i = 8
shot[i] = 1256
omega1[i] = 120
omega2[i] = 100
current[i] = 1000
saturatedfrequency[i] = 0.06
saturatedfrequencyerr[i] = 0.005
freqband_min[i] = 0.055
freqband_max[i] = 0.065
saturatedpower[i] = 1.217
saturatedintervalstart[i] = 100
saturatedintervalstop[i] = 400
timefieldon[i] = 360
timesaturated[i] = 100
timefieldoff[i] = 405


i = 9
shot[i] = 1257
omega1[i] = 120
omega2[i] = 100
current[i] = 1400
saturatedfrequency[i] = 0.065
saturatedfrequencyerr[i] = 0.006
freqband_min[i] = 0.060
freqband_max[i] = 0.070
saturatedpower[i] = 1.120
saturatedintervalstart[i] = 100
saturatedintervalstop[i] = 380
timefieldon[i] = 360
timesaturated[i] = 100 
timefieldoff[i] = 383


i = 10
shot[i] = 1258
omega1[i] = 170
omega2[i] = 100
current[i] = 0
saturatedfrequency[i] = 0.18
saturatedfrequencyerr[i] = 0.01
freqband_min[i] = 0.17
freqband_max[i] = 0.19
saturatedpower[i] = 11.37
saturatedintervalstart[i] = 55
saturatedintervalstop[i] = 235
timefieldon[i] = numpy.nan
timesaturated[i] = 55
timefieldoff[i] = numpy.nan


i = 11
shot[i] = 1259
omega1[i] = 220
omega2[i] = 100
current[i] = 0
saturatedfrequency[i] = 0.30
saturatedfrequencyerr[i] = 0.03
freqband_min[i] = 0.27
freqband_max[i] = 0.33
saturatedpower[i] = 30.23
saturatedintervalstart[i] = 35
saturatedintervalstop[i] = 120
timefieldon[i] = numpy.nan
timesaturated[i] = 35
timefieldoff[i] = numpy.nan


i = 12
shot[i] = 1260
omega1[i] = 250
omega2[i] = 100
current[i] = 0
saturatedfrequency[i] = 0.42
saturatedfrequencyerr[i] = 0.05
freqband_min[i] = 0.37
freqband_max[i] = 0.47
saturatedpower[i] = 57.1
saturatedintervalstart[i] = 33
saturatedintervalstop[i] = 120
timefieldon[i] = numpy.nan
timesaturated[i] = 33
timefieldoff[i] = numpy.nan


i = 13
shot[i] = 1261
omega1[i] = 315
omega2[i] = 100
current[i] = 0
saturatedfrequency[i] = 0.55
saturatedfrequencyerr[i] = 0.05
freqband_min[i] = 0.50
freqband_max[i] = 0.60
saturatedpower[i] = 49.8
saturatedintervalstart[i] = 0
saturatedintervalstop[i] = 60
timefieldon[i] = numpy.nan
timesaturated[i] = 0
timefieldoff[i] = numpy.nan


i = 14
shot[i] = 1262
omega1[i] = 365
omega2[i] = 100
current[i] = 0
saturatedfrequency[i] = numpy.nan 
saturatedfrequencyerr[i] = numpy.nan
freqband_min[i] = numpy.nan
freqband_max[i] = numpy.nan
saturatedpower[i] = numpy.nan
saturatedintervalstart[i] = numpy.nan
saturatedintervalstop[i] = numpy.nan
timefieldon[i] = numpy.nan
timesaturated[i] = numpy.nan
timefieldoff[i] = numpy.nan


i = 15
shot[i] = 1263
omega1[i] = 335
omega2[i] = 100
current[i] = 0
saturatedfrequency[i] = numpy.nan
saturatedfrequencyerr[i] = numpy.nan
freqband_min[i] = numpy.nan
freqband_max[i] = numpy.nan
saturatedpower[i] = numpy.nan
saturatedintervalstart[i] = numpy.nan
saturatedintervalstop[i] = numpy.nan
timefieldon[i] = numpy.nan
timesaturated[i] = numpy.nan
timefieldoff[i] = numpy.nan


i = 16
shot[i] = 1264
omega1[i] = 335
omega2[i] = 100
current[i] = 200
saturatedfrequency[i] = numpy.nan
saturatedfrequencyerr[i] = numpy.nan
freqband_min[i] = numpy.nan
freqband_max[i] = numpy.nan
saturatedpower[i] = numpy.nan
saturatedintervalstart[i] = numpy.nan
saturatedintervalstop[i] = numpy.nan
timefieldon[i] = 10
timesaturated[i] = numpy.nan
timefieldoff[i] = 70


i = 17
shot[i] = 1265
omega1[i] = 335
omega2[i] = 100
current[i] = 400
saturatedfrequency[i] = numpy.nan
saturatedfrequencyerr[i] = numpy.nan 
freqband_min[i] = numpy.nan
freqband_max[i] = numpy.nan
saturatedpower[i] = numpy.nan
saturatedintervalstart[i] = numpy.nan
saturatedintervalstop[i] = numpy.nan
timefieldon[i] = 10
timesaturated[i] = numpy.nan
timefieldoff[i] = 70


i = 18
shot[i] = 1266
omega1[i] = 335
omega2[i] = 100
current[i] = 600
saturatedfrequency[i] = numpy.nan
saturatedfrequencyerr[i] = numpy.nan 
freqband_min[i] = numpy.nan
freqband_max[i] = numpy.nan
saturatedpower[i] = numpy.nan
saturatedintervalstart[i] = numpy.nan
saturatedintervalstop[i] = numpy.nan
timefieldon[i] = 10
timesaturated[i] = numpy.nan
timefieldoff[i] = 70


i = 19
shot[i] = 1267
omega1[i] = 335
omega2[i] = 100
current[i] = 800
saturatedfrequency[i] = 0.57
saturatedfrequencyerr[i] = 0.05
freqband_min[i] = 0.52
freqband_max[i] = 0.62
saturatedpower[i] = 119.3
saturatedintervalstart[i] = 35
saturatedintervalstop[i] = 75
timefieldon[i] = 10
timesaturated[i] = 35
timefieldoff[i] = 70


i = 20
shot[i] = 1268
omega1[i] = 335
omega2[i] = 100
current[i] = 1000
saturatedfrequency[i] = 0.57
saturatedfrequencyerr[i] = 0.03
freqband_min[i] = 0.54
freqband_max[i] = 0.60
saturatedpower[i] = 156.6
saturatedintervalstart[i] = 20
saturatedintervalstop[i] = 55
timefieldon[i] = 10
timesaturated[i] = 20
timefieldoff[i] = 55


i = 21
shot[i] = 1269
omega1[i] = 335
omega2[i] = 100
current[i] = 1200
saturatedfrequency[i] = 0.55
saturatedfrequencyerr[i] = 0.05
freqband_min[i] = 0.50
freqband_max[i] = 0.60
saturatedpower[i] = 155.1
saturatedintervalstart[i] = 15
saturatedintervalstop[i] = 40
timefieldon[i] = 10
timesaturated[i] = 15
timefieldoff[i] = 40


i = 22
shot[i] = 1270
omega1[i] = 335
omega2[i] = 100
current[i] = 1400
saturatedfrequency[i] = 0.55
saturatedfrequencyerr[i] = 0.05
freqband_min[i] = 0.50
freqband_max[i] = 0.60
saturatedpower[i] = 192.47
saturatedintervalstart[i] = 17
saturatedintervalstop[i] = 35
timefieldon[i] = 10
timesaturated[i] = 17
timefieldoff[i] = 35


i = 23
shot[i] = 1271
omega1[i] = 335
omega2[i] = 100
current[i] = 1600
saturatedfrequency[i] = 0.55
saturatedfrequencyerr[i] = 0.05
freqband_min[i] = 0.50
freqband_max[i] = 0.60
saturatedpower[i] = 157.4
saturatedintervalstart[i] = 16
saturatedintervalstop[i] = 30
timefieldon[i] = 10
timesaturated[i] = 16
timefieldoff[i] = 30


i = 24
shot[i] = 1272
omega1[i] = 335
omega2[i] = 100
current[i] = 700
saturatedfrequency[i] = numpy.nan
saturatedfrequencyerr[i] = numpy.nan
freqband_min[i] = numpy.nan
freqband_max[i] = numpy.nan
saturatedpower[i] = numpy.nan
saturatedintervalstart[i] = numpy.nan
saturatedintervalstop[i] = numpy.nan
timefieldon[i] = 10
timesaturated[i] = numpy.nan
timefieldoff[i] = 70


i = 25
shot[i] = 1273
omega1[i] = 165
omega2[i] = 50
current[i] = 0
saturatedfrequency[i] = 0.28
saturatedfrequencyerr[i] = 0.03
freqband_min[i] = 0.25
freqband_max[i] = 0.31
saturatedpower[i] = 31.8
saturatedintervalstart[i] = 55
saturatedintervalstop[i] = 135
timefieldon[i] = numpy.nan
timesaturated[i] = 55
timefieldoff[i] = numpy.nan


i = 26
shot[i] = 1274
omega1[i] = 170
omega2[i] = 50
current[i] = 0
saturatedfrequency[i] = numpy.nan
saturatedfrequencyerr[i] = numpy.nan
freqband_min[i] = numpy.nan
freqband_max[i] = numpy.nan
saturatedpower[i] = numpy.nan
saturatedintervalstart[i] = numpy.nan
saturatedintervalstop[i] = numpy.nan
timefieldon[i] = numpy.nan
timesaturated[i] = numpy.nan
timefieldoff[i] = numpy.nan


i = 27
shot[i] = 1275
omega1[i] = 170
omega2[i] = 50
current[i] = 400
saturatedfrequency[i] = numpy.nan
saturatedfrequencyerr[i] = numpy.nan
freqband_min[i] = numpy.nan
freqband_max[i] = numpy.nan
saturatedpower[i] = numpy.nan
saturatedintervalstart[i] = numpy.nan
saturatedintervalstop[i] = numpy.nan
timefieldon[i] = 10 
timesaturated[i] = numpy.nan
timefieldoff[i] = 70


i = 28
shot[i] = 1276
omega1[i] = 170
omega2[i] = 50
current[i] = 600
saturatedfrequency[i] = 0.28
saturatedfrequencyerr[i] = 0.03
freqband_min[i] = 0.25
freqband_max[i] = 0.31
saturatedpower[i] = 8.90
saturatedintervalstart[i] = 45
saturatedintervalstop[i] = 70
timefieldon[i] = 10
timesaturated[i] = 45
timefieldoff[i] = 70


i = 29
shot[i] = 1277
omega1[i] = 170
omega2[i] = 50
current[i] = 800
saturatedfrequency[i] = 0.30
saturatedfrequencyerr[i] = 0.03
freqband_min[i] = 0.27
freqband_max[i] = 0.33
saturatedpower[i] = 47.1
saturatedintervalstart[i] = 20
saturatedintervalstop[i] = 70
timefieldon[i] = 10
timesaturated[i] = 20
timefieldoff[i] = 70


i = 30
shot[i] = 1278
omega1[i] = 170
omega2[i] = 50
current[i] = 1600
saturatedfrequency[i] = 0.29
saturatedfrequencyerr[i] = 0.06
freqband_min[i] = 0.23
freqband_max[i] = 0.35
saturatedpower[i] = 47.0
saturatedintervalstart[i] = 18
saturatedintervalstop[i] = 34
timefieldon[i] = 10
timesaturated[i] = 18
timefieldoff[i] = 30


i = 31
shot[i] = 1279
omega1[i] = 520
omega2[i] = 150
current[i] = 0
saturatedfrequency[i] = numpy.nan
saturatedfrequencyerr[i] = numpy.nan
freqband_min[i] = numpy.nan
freqband_max[i] = numpy.nan
saturatedpower[i] = numpy.nan
saturatedintervalstart[i] = numpy.nan
saturatedintervalstop[i] = numpy.nan
timefieldon[i] = numpy.nan
timesaturated[i] = numpy.nan
timefieldoff[i] = numpy.nan


i = 32
shot[i] = 1280
omega1[i] = 520
omega2[i] = 150
current[i] = 800
saturatedfrequency[i] = numpy.nan
saturatedfrequencyerr[i] = numpy.nan
freqband_min[i] = numpy.nan
freqband_max[i] = numpy.nan
saturatedpower[i] = numpy.nan
saturatedintervalstart[i] = numpy.nan
saturatedintervalstop[i] = numpy.nan
timefieldon[i] = 10 
timesaturated[i] = numpy.nan
timefieldoff[i] = 70


i = 33
shot[i] = 1281
omega1[i] = 520
omega2[i] = 150
current[i] = 1000
saturatedfrequency[i] = 0.85
saturatedfrequencyerr[i] = 0.05
freqband_min[i] = 0.80
freqband_max[i] = 0.90
saturatedpower[i] = 225.1
saturatedintervalstart[i] = 35
saturatedintervalstop[i] = 55
timefieldon[i] = 10
timesaturated[i] = 35
timefieldoff[i] = 55


i = 34
shot[i] = 1282
omega1[i] = 520
omega2[i] = 150
current[i] = 1600
saturatedfrequency[i] = 0.87
saturatedfrequencyerr[i] = 0.05
freqband_min[i] = 0.82
freqband_max[i] = 0.92
saturatedpower[i] = 325.6
saturatedintervalstart[i] = 15
saturatedintervalstop[i] = 30
timefieldon[i] = 10
timesaturated[i] = 15 
timefieldoff[i] = 30


i = 35
shot[i] = 1283
omega1[i] = 165
omega2[i] = 150
current[i] = 0
saturatedfrequency[i] = numpy.nan
saturatedfrequencyerr[i] = numpy.nan
freqband_min[i] = numpy.nan
freqband_max[i] = numpy.nan
saturatedpower[i] = numpy.nan
saturatedintervalstart[i] = numpy.nan
saturatedintervalstop[i] = numpy.nan
timefieldon[i] = numpy.nan
timesaturated[i] = numpy.nan
timefieldoff[i] = numpy.nan


i = 36
shot[i] = 1284
omega1[i] = 710
omega2[i] = 200
current[i] = 0
saturatedfrequency[i] = numpy.nan
saturatedfrequencyerr[i] = numpy.nan
freqband_min[i] = numpy.nan
freqband_max[i] = numpy.nan
saturatedpower[i] = numpy.nan
saturatedintervalstart[i] = numpy.nan
saturatedintervalstop[i] = numpy.nan
timefieldon[i] = numpy.nan
timesaturated[i] = numpy.nan
timefieldoff[i] = numpy.nan


i = 37
shot[i] = 1285
omega1[i] = 670
omega2[i] = 200
current[i] = 0
saturatedfrequency[i] = numpy.nan
saturatedfrequencyerr[i] = numpy.nan
freqband_min[i] = numpy.nan
freqband_max[i] = numpy.nan
saturatedpower[i] = numpy.nan
saturatedintervalstart[i] = numpy.nan
saturatedintervalstop[i] = numpy.nan
timefieldon[i] = numpy.nan
timesaturated[i] = numpy.nan
timefieldoff[i] = numpy.nan


i = 38
shot[i] = 1286
omega1[i] = 670
omega2[i] = 200
current[i] = 1000
saturatedfrequency[i] = numpy.nan
saturatedfrequencyerr[i] = numpy.nan
freqband_min[i] = numpy.nan
freqband_max[i] = numpy.nan
saturatedpower[i] = numpy.nan
saturatedintervalstart[i] = numpy.nan
saturatedintervalstop[i] = numpy.nan
timefieldon[i] = 10
timesaturated[i] = numpy.nan
timefieldoff[i] = 55


i = 39
shot[i] = 1287
omega1[i] = 670
omega2[i] = 200
current[i] = 1200
saturatedfrequency[i] = 1.11
saturatedfrequencyerr[i] = 0.05
freqband_min[i] = 1.06
freqband_max[i] = 1.16
saturatedpower[i] = 535
saturatedintervalstart[i] = 21
saturatedintervalstop[i] = 40
timefieldon[i] = 10
timesaturated[i] = 21
timefieldoff[i] = 40


i = 40
shot[i] = 1288
omega1[i] = 670
omega2[i] = 200
current[i] = 1600
saturatedfrequency[i] = 1.1
saturatedfrequencyerr[i] = 0.1
freqband_min[i] = 1.0
freqband_max[i] = 1.2
saturatedpower[i] = 495
saturatedintervalstart[i] = 17
saturatedintervalstop[i] = 30
timefieldon[i] = 10
timesaturated[i] = 17
timefieldoff[i] = 30


i = 41
shot[i] = 1289
omega1[i] = 210
omega2[i] = 200
current[i] = 0
saturatedfrequency[i] = 0.019
saturatedfrequencyerr[i] = 0.001
freqband_min[i] = 0.018
freqband_max[i] = 0.020
saturatedpower[i] = 0.00759
saturatedintervalstart[i] = 150
saturatedintervalstop[i] = 1500
timefieldon[i] = numpy.nan
timesaturated[i] = 150
timefieldoff[i] = numpy.nan


i = 42
shot[i] = 1290
omega1[i] = 210
omega2[i] = 200
current[i] = 250
saturatedfrequency[i] = 0.022
saturatedfrequencyerr[i] = 0.003
freqband_min[i] = 0.019
freqband_max[i] = 0.025
saturatedpower[i] = 0.00774
saturatedintervalstart[i] = 150
saturatedintervalstop[i] = 1150
timefieldon[i] = 0 
timesaturated[i] = 150
timefieldoff[i] = 1200



def get_data():
    ss_data = {'shot': shot, 'omega1': omega1, 'omega2': omega2,
               'current': current, 'saturatedfrequency': saturatedfrequency,
               'saturatedfrequencyerr': saturatedfrequencyerr,
               'saturatedpower': saturatedpower, 'timefieldon': timefieldon,
               'timesaturated': timesaturated, 'timefieldoff': timefieldoff}
    return ss_data
    
