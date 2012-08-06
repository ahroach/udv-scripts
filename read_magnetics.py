from csv import reader
from sys import byteorder
from tkFileDialog import askdirectory
from tkSimpleDialog import askinteger
from glob import glob
import datetime
import shelve
import os
import scipy
import numpy

path = os.path

default_path = '/p/mri/data/'

def get_db_path():
    
    db_path = askdirectory(title="MRI shot database path:",
                           initialdir=path.expanduser(default_path) )

    return db_path


def get_shot_dir(shot_num=0, db_path=default_path):

    """Open the shot database"""

    if not os.path.isdir(db_path): print db_path

    if not path.isdir(db_path):
        db_path = get_db_path()
    
    if shot_num == 0:
        shot_num = askinteger( "Shot number", "Choose a shot number:" )

    shot_dir = os.path.join( db_path, str(shot_num).zfill(4) )
    
    return shot_dir



def get_parameter(shot_dir, parameter, db_path=default_path):

    """Get the value of a shot parameter."""

    # Allow the user to simply specify the shot number to use the
    # default shot directory

    if type(shot_dir) != type(''):
        shot_dir = get_shot_dir(shot_num=shot_dir, db_path=db_path)

    # First read in the parameter list from the parameters file
    pfile = os.path.join( shot_dir, 'parameters.txt' )
    if not os.path.isfile(pfile):   
        pfile = os.path.join( shot_dir, 'parameters-2cards.txt' )
    if not os.path.isfile(pfile):   
        pfile = os.path.join( shot_dir, 'parameters-2computers.txt' )

    f_params = open( pfile )
    r = reader( f_params, delimiter='\t' )

    value = []
    for line in r:
        if line[0] == parameter:
            value.append(line[1])

    f_params.close()

    return value    


def get_timestamp(shot_num, db_path=default_path):

    year = int(get_parameter(shot_num, 'Year')[0])
    month = int(get_parameter(shot_num, 'Month')[0])
    day = int(get_parameter(shot_num, 'Day')[0])
    hour = int(get_parameter(shot_num, 'Hour')[0])
    minute = int(get_parameter(shot_num, 'Minute')[0])

    return datetime.datetime(year,month,day,hour,minute).ctime()



def list_channels(shot_dir, **keywords):

    # Allow the user to simply specify the shot number to use the
    # default shot directory

    if type(shot_dir) != type(''):
        if 'db_path' in keywords:
            db_path = keywords['db_path'] 
            shot_dir = get_shot_dir(shot_num=shot_dir, db_path=db_path)
        else: shot_dir = get_shot_dir(shot_num=shot_dir)
 
    return get_parameter( shot_dir, 'InputChannel')

    
def read_notes(shot_dir):

    """Read in the notes for the shot."""

    # Allow the user to simply specify the shot number to use the
    # default shot directory

    if type(shot_dir) != type(''):
        shot_dir = get_shot_dir(shot_num=shot_dir)

    notes_file = os.path.join( shot_dir,
                            get_parameter( shot_dir, 'NotesFile' )[0] )

    if os.path.isfile( notes_file ):
        f_notes = open( os.path.join( shot_dir, notes_file ) )
        notes = f_notes.read()
        f_notes.close()
    else:
        notes = ''

    return notes



def read_time(shot_dir, **keywords):

    """Read in the timestamp array from a shot"""

    # Allow the user to simply specify the shot number to use the
    # default shot directory

    if type(shot_dir) != type(''):
        if 'db_path' in keywords:
            db_path = keywords['db_path'] 
            shot_dir = get_shot_dir(shot_num=shot_dir, db_path=db_path)
        else: shot_dir = get_shot_dir(shot_num=shot_dir)
 
    time_file = os.path.join( shot_dir, 'TIME.dat' )

    if os.path.isfile(time_file):

        f_time = open( time_file, mode='rb' )

        # The time stamps are stored as single-precision floats
        # (4-bytes) so the filesize is the number of points times 4
        n_points = os.path.getsize( f_time.name ) / 4

        time = numpy.fromfile( f_time, dtype='f',
                                               count=n_points )

        # LabView uses big-endian binary so byteswap if we are on a
        # little-endian machine

        swap =  byteorder == 'little'
            
        if swap:
            time = time.byteswap()

    else:
        time = [-1]
    
    return time



def read_channel(shot_dir, channel, start=0, stop=-1, **keywords):

    """ Read in the .dat file created by L114-DAQ.vi for a channel """

    # Labview uses big-endian binary files so byteswap if we are on a
    # little-endian machine

    swap =  byteorder == 'little'

    # Allow the user to simply specify the shot number to use the
    # default shot directory

    if type(shot_dir) != type(''):
        if 'db_path' in keywords:
            db_path = keywords['db_path'] 
            shot_dir = get_shot_dir(shot_num=shot_dir, db_path=db_path)
        else: shot_dir = get_shot_dir(shot_num=shot_dir)
        
    # Open the file in read-only binary mode

    filename = os.path.join( shot_dir, channel + '.dat' )
    fid = open(filename, mode='rb')

    # The first two entries are the shot number and the number of entries

    shot_num = numpy.fromfile( fid, dtype='f', count=1 )
    n_points = numpy.fromfile( fid, dtype='f', count=1 )

    if swap: 
	shot_num.byteswap(True)
	n_points.byteswap(True)

    # Skip to the start of the desired data sequence and determine the
    # length of the data array to read in
    fid.seek((start+2)*4L)
    if stop != -1: n_points = stop-start+1

    # Next we read in the time series data into a float array
    data = numpy.fromfile( fid, dtype='f', count=n_points )
    fid.close()

    if swap: 
	data = data.byteswap()

    return data



def read_shot(shot_dir):

    """Read in all of the shot data from the database into a dictionary."""

    # Allow the user to simply specify the shot number to use the
    # default shot directory

    if type(shot_dir) != type(''):
        shot_dir = get_shot_dir(shot_num=shot_dir)

    if os.path.isdir(shot_dir):

        shot = { 'shot_dir': shot_dir,
                 'notes': read_notes( shot_dir ),
                 'time': read_time( shot_dir )
               }

        if os.path.isfile( os.path.join( shot_dir, 'motorspeed.txt' ) ):
            shot['motors'] = get_motor_info( shot_dir )

        channels = get_parameter( shot_dir, 'InputChannel')

        for i in channels:
            shot[i] = read_channel(shot_dir,i)
            
    else:
        print shot_dir + ' not found.'
        shot = {}
	
    return shot



def get_flattop_period(shot_num):

    current = float(get_parameter(shot_num,'Perkin Current')[0])
    f_s = float( get_parameter(shot_num,'AIScanRate')[0] )
    f_s = int(f_s)

    if current < 750: flattop = range(12*f_s,40*f_s)
    elif abs(current - 1000) <= 250: flattop = range(12*f_s,30*f_s)
    elif abs(current - 1500.0) <= 250: flattop = range(12*f_s,22*f_s)
    elif abs(current - 2000.0) <= 250: flattop = range(12*f_s,16*f_s)

    return flattop


def shelf_exists(shot_num, filename):
    if os.path.splitext(filename)[1] != '.db': filename += '.db'
    shot_dir = get_shot_dir(shot_num)
    filepath = os.path.join(shot_dir,filename)
    return os.path.isfile(filepath)



def open_shelf(shot_num, filename, flag='c', writeback=False):
    if os.path.splitext(filename)[1] != '.db': filename += '.db'
    shot_dir = get_shot_dir(shot_num)
    filepath = os.path.join(shot_dir,filename)
    d = shelve.open(filepath, flag=flag, writeback=writeback)
    return d



def write_shelf(shot_num, filename, data):
    d = open_shelf(shot_num, filename)
    for i in data.keys():
        d[i] = data[i]
    d.close()



def read_shelf(shot_num, filename=''):
    data = {}
    shot_dir = get_shot_dir(shot_num)
    filepath = os.path.join(shot_dir,filename)

    if os.path.isfile(filepath):
        d = shelve.open(filepath)
        for i in d.keys():
            data[i] = d[i]
        d.close()
    else:
        print "Cannot find ",filepath

    return data



def clear_shelf(shot_num, filename=''):

    t = type(shot_num)
    if t.__name__ == 'list':
        for shot in shot_num:
            clear_shelf(shot)
    elif t.__name__ == 'int':
        shot_dir = get_shot_dir(shot_num)
        filepath = os.path.join(shot_dir,filename)
        if os.path.isfile(filepath): os.remove(filepath)

