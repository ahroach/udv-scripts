import os
from pylab import *
from scipy import *

def read_ultrasound(filename, channel, verbose=1):
    #UDOP constants:
    Data_Type_Velocity = 0
    Data_Type_Echo = 1
    Data_Type_Energy = 2
    Data_Type_Gate_FFT = 3
    Data_Type_Phase = 4
    Data_Type_Vitson = 5
    Data_Type_Frequency = 6
    Data_Type_Frequency_TR1 = 7
    Data_Type_Frequency_TR2 = 8
    Data_Type_Frequency_TR3 = 9
    Data_Type_Echo_TR1 = 10
    Data_Type_Echo_TR2 = 11
    Data_Type_Echo_TR3 = 12
    Data_Type_Energy_TR1 = 13
    Data_Type_Energy_TR2 = 14
    Data_Type_Energy_TR3 = 15
    Data_Type_Velocity_mm_s_10 = 16   # Velocity in mm/s * 10
    Data_Type_Velocity_mm_s = 17      # Velocity in mm/s
    Data_Type_TGC = 28
    Data_Type_IQ = 29
    Data_Type_Depth = 25              #depths [mm*10]

    Nb_Para_Fct = 256;
    FFT_Scale_Pmin = -50              #FFT minimum level [dBm]

    Retard_Flt_50k = 10500            #IQ filter delay
    Retard_Flt_100k = 6300
    Retard_Flt_150k = 3500
    Retard_Flt_200k = 2800
    Retard_Flt_250k = 2100
    Retard_Flt_300k = 1800

    Ofs_Data = 31268  #Offset in file of the first data value

    # Open the file in read-only binary mode
    try:
        fid = open(filename, mode='rb')
    except IOError:
        print 'Cannot open', filename

    # The binary file format begins with an identification block
    DOP3000ID = fromfile( fid, dtype='|S8', count=1)[0]
    if DOP3000ID != "BINUDOPV":
        print 'Error.  File does not seem to be a UDOP binary file.'
    version = fromfile( fid, dtype='|S6', count=1)[0]
    
    #Read the comment block
    fid.seek(16, 0)
    comment = fromfile(fid, dtype='|S510', count=1)[0]
    if(verbose):
        print comment

    #Define the number of used channels
    Mpx_Mode = udv_params(fid, 1, 52)

    Nb_Used_Channels = 1

    #If the multiplexer is enabled
    if Mpx_Mode & 2 > 0:
        multiplexer_mode = 1
        First_Ch = int(Mpx_Mode / 65536) #First channel in the sequence
        if (verbose):
            print "First Channel: " + str(First_Ch)
        jt = 1 << (First_Ch + 3)
        for i in range(1, 10):
            jt = jt << 1
            if jt == 16384:
                jt = 16
            if Mpx_Mode & jt > 0:
                Nb_Used_Channels = Nb_Used_Channels + 1
        #Now verify that the requested channel exists.
        channel_found = 0
        fid.seek(Ofs_Data)
        if (verbose):
            print "Number of channels used: " + str(Nb_Used_Channels)
        for i in range(1, Nb_Used_Channels + 1):
            if Get_No_Channel(fid) == channel:
                channel_found = 1
            N = fromfile(fid, dtype='uint16', count=1)
            fid.seek(N-2, 1)
        if channel_found == 0:
            print "Error.  Requested channel not present."
            return 0
    else:
        #Not multiplexer mode.  Verify that the channel exists
        multiplexer_mode = 0
        fid.seek(Ofs_Data)
        if Get_No_Channel(fid) != channel:
            print "Error.  Requested channel not present."
            print "Try channel " + str(Get_No_Channel(fid))
            return 0

    #Define the parameters for the selected channel
    #Emitting frequency in kHz
    femit = udv_params(fid, channel, 0)

    #PRF in us
    prf = udv_params(fid, channel, 5)

    #Number of gates
    ngates = udv_params(fid, channel, 13)
    
    #Velocity scale factor
    vsf = udv_params(fid, channel, 15)

    #Sound speed in m/s
    cs = udv_params(fid, channel, 19)
    
    #Time of first gate (n*0.166 ns)
    tfg = udv_params(fid, channel, 9)

    #Resolution (n+1)*0.166ns
    res = udv_params(fid, channel, 10)

    #Number of blocks in multiplexer mode
    #For some reason I've gotten inaccurate numbers in multiplexer_mode
    #when looking at udv_params(fid, channel, 53), so I'm just pulling
    #numblocks from the first channel.
    if multiplexer_mode == 1:
        numblocks = udv_params(fid, 1, 53)
    else:
        numblocks = udv_params(fid, channel, 49)

    #Number of gates in multiplexer mode
    if multiplexer_mode == 1:
        numprofilesinblock = udv_params(fid, channel, 51)
    else:
        numprofilesinblock = udv_params(fid, channel, 48)

    #Acquistion rate 0:6 MHz, 1:12 MHz
    #Converted to kHz.
    acqr = udv_params(fid, channel, 29)
    if acqr%256 == 0:
        acqr = 6000
    elif acqr%256 == 1:
        acqr = 12000
    elif acqr%256 == 2:
        acqr = 36000

    
    #Bandwidth definition: convert to flight delay
    bandw = udv_params(fid, channel, 27)
    if bandw == 0:
        retard_flt_ns = Retard_Flt_50k
    if bandw == 1:
        retard_flt_ns = Retard_Flt_100k
    if bandw == 2:
        retard_flt_ns = Retard_Flt_150k
    if bandw == 3:
        retard_flt_ns = Retard_Flt_200k
    if bandw == 4:
        retard_flt_ns = Retard_Flt_250k
    if bandw == 5:
        retard_flt_ns = Retard_Flt_300k
    

    #Compute the measured Depths in cm
    X = zeros(ngates)
    for i in range(0, ngates):
        X[i] = (tfg + (i)*(res + 1))/(2.0*acqr)
        X[i] = 0.1*(X[i] - (retard_flt_ns/2000000.0))*cs

    velocity = zeros([numblocks*numprofilesinblock,ngates])
    echo = zeros([numblocks*numprofilesinblock,ngates])
    energy = zeros([numblocks*numprofilesinblock,ngates])
    time = zeros(numblocks*numprofilesinblock)

    #Find the end of the file
    fid.seek(0, 2)
    endoffile = fid.tell()

    #Seek to the beginning of the data profiles
    fid.seek(Ofs_Data)
    #Profile number minus one to account for the "pseudo profile" containing
    #depth data at the beginning of the file.
    profile_number = -1
    while (fid.tell() < endoffile) & (profile_number < numblocks*numprofilesinblock):
        #Only interested in profiles with the correct channel number
        if Get_No_Channel(fid) == channel:
            fid.seek(2,1)
            #Find the number of bytes of data for the profile
            nb = fromfile(fid, dtype='uint16', count=1)[0]
            while nb != 0:
                data_type = fromfile(fid, dtype='uint8', count=1)[0]
                if (data_type == Data_Type_Velocity) :
                    velocity[profile_number,:] = fromfile(fid, dtype='int8', count=ngates)
                elif (data_type == Data_Type_Echo) :
                    echo[profile_number,:] = fromfile(fid, dtype='uint8', count=ngates)
                elif (data_type == Data_Type_Energy) :
                    energy[profile_number,:] = fromfile(fid, dtype='uint8', count=ngates)
                elif (data_type == Data_Type_Depth) :
                    #Just skip ahead
                    fid.seek(ngates*2, 1)
                else:
                    print "Unhandled data type " + str(data_type)
                    return 0
                
                nb = fromfile(fid, dtype='uint16', count=1)[0]

            time[profile_number] = 1.0e-4*fromfile(fid, dtype='int32', count=1)[0]
            profile_number = profile_number + 1                
            block_number = fromfile(fid, dtype='int16', count=1)[0]
            junk = fromfile(fid, dtype='int8', count=3)[0]
            channel_number = fromfile(fid, dtype='int8', count=1)[0]
            if (channel_number != channel):
                print "Warning! channel_number after read != channel."
            N = fromfile(fid, dtype='uint16', count=1)[0]
        else:
            N = fromfile(fid, dtype='uint16', count=1)[0] #Num of bytes in profile
            fid.seek(N-2,1)
    if(verbose):
        print str(profile_number) + " profiles read"

    #Convert from the Doppler frequency to velocity in cm/s
    
    valuetofreq = 1000.0*(vsf/3142.0)/(256.0*prf)
    valuetovelocity = 100.0*128*valuetofreq*cs/(256.0*femit)

    maxvelocity = 128*valuetovelocity
    
    velocity = velocity*valuetovelocity

    fid.close()
    data = {'velocity': velocity, 'echo': echo, 'energy': energy, 'depth': X, 'time': time, 'channel': channel, 'maxvelocity': maxvelocity, 'filename': filename}
    return data


#Read a parameter from the parameters list
def udv_params(fid, channel, param_num):
    fid.seek(548 + (channel-1)*256*4 + param_num*4)
    value = fromfile(fid, dtype='int32', count=1)[0]
    return value

#Return the number of a channel associated with the next available
#profile in the data
def Get_No_Channel(fid):
    N = fromfile(fid, dtype='uint16', count=1)[0] #Num of bytes in profile
    fid.seek(N-5, 1)
    No_Channel = fromfile(fid, dtype='uint8', count=1)[0]
    fid.seek(-(N-2), 1) #Put the pointer back where it was
    return No_Channel
