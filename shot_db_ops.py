import shot_params as sp
from numpy import nan,isnan

def sanity_check(shot):
    #for key in shot_params.shot_params.keys():
    #    shot_db_ops.sanity_check(key)
        
    params = sp.shot_params[shot]

    if (params['current'] != 0 and
        (isnan(params['field_delay']) or isnan(params['t_field']))):
        print "Warning on shot " + str(shot) + ": Current specified but time value(s) are nans."

    if (params['current'] == 0 and
        (not(isnan(params['field_delay'])) or not(isnan(params['t_field'])))):
        print "Warning on shot " + str(shot) + ": No current, but field timing values are given."

    if (params['current'] != 0 and
        (params['field_delay'] + params['t_field']) !=
        (params['shot_length'] - 5)):
        print "Suspicious shot and field timing on shot " + str(shot)

    if params['udv_delay'] >= params['shot_length']:
        print "Suspicious UDV delay on shot " + str(shot)

    if (len(params['channels']) != len(params['alphas']) or
        len(params['channels']) != len(params['betas']) or
        len(params['channels']) != len(params['offsets']) or
        len(params['channels']) != len(params['ports'])):
        print "Length mismatch between UDV probe parameter arrays"

    if (not(is_ekman(shot)) and not(is_split(shot)) and
        not(is_solid_body(shot)) and not(is_mri_z(shot)) and
        not(is_mri_mango(shot)) and not(is_mri(shot)) and
        not(is_mri_new(shot))):
        print "Suspicious component speeds in shot " + str(shot)

    if shot != params['shot_num']:
        print "Index number and shot_num mismatch in shot " + str(shot)



def is_set_trouble_flag(shot):
    if sp.shot_params[shot].__contains__('trouble_flag'):
        print '\033[91m'+"Warning: trouble_flag set on shot "+str(shot)+'\033[0m'
        return True
    return False


def is_solid_body(shot):
    IC = sp.shot_params[shot]['ICspeed']
    IR = sp.shot_params[shot]['IRspeed']
    OR = sp.shot_params[shot]['ORspeed']
    OC = sp.shot_params[shot]['OCspeed']
    if IC == IR and IC == OR and IC == OC:
        return True
    return False


def is_split(shot):
    IC = sp.shot_params[shot]['ICspeed']
    IR = sp.shot_params[shot]['IRspeed']
    OR = sp.shot_params[shot]['ORspeed']
    OC = sp.shot_params[shot]['OCspeed']
    if IC == IR and OC == OR and IC != OC:
        return True
    return False


def is_split_unstable(shot):
    IC = sp.shot_params[shot]['ICspeed']
    IR = sp.shot_params[shot]['IRspeed']
    OR = sp.shot_params[shot]['ORspeed']
    OC = sp.shot_params[shot]['OCspeed']
    if IC == IR and OR == 0 and OC == 0 and IC != 0:
        return True
    return False


def is_split_cyclonic(shot):
    IC = sp.shot_params[shot]['ICspeed']
    IR = sp.shot_params[shot]['IRspeed']
    OR = sp.shot_params[shot]['ORspeed']
    OC = sp.shot_params[shot]['OCspeed']
    if OC == OR and IR == 0 and IC == 0 and OC != 0:
        return True
    return False


def is_ekman(shot):
    IC = sp.shot_params[shot]['ICspeed']
    IR = sp.shot_params[shot]['IRspeed']
    OR = sp.shot_params[shot]['ORspeed']
    OC = sp.shot_params[shot]['OCspeed']
    if IC != 0 and IC != IR and IR == OR and IR == OC:
        return True
    return False


def is_mri_z(shot):
    IC = sp.shot_params[shot]['ICspeed']
    IR = sp.shot_params[shot]['IRspeed']
    OR = sp.shot_params[shot]['ORspeed']
    OC = sp.shot_params[shot]['OCspeed']

    IRrat = float(IC)/float(IR)
    ORrat = float(IC)/float(OR)
    OCrat = float(IC)/float(OC)

    in_range = lambda x, y: abs(1.0 - x/y) < 0.01

    if (OC != 0 and OR != 0 and IR != 0 and in_range(IRrat, 1.818) and
        in_range(ORrat, 7.547) and in_range(OCrat, 7.547)):
        return True
    return False


def is_mri_new(shot):
    IC = sp.shot_params[shot]['ICspeed']
    IR = sp.shot_params[shot]['IRspeed']
    OR = sp.shot_params[shot]['ORspeed']
    OC = sp.shot_params[shot]['OCspeed']

    IRrat = float(IC)/float(IR)
    ORrat = float(IC)/float(OR)
    OCrat = float(IC)/float(OC)

    in_range = lambda x, y: abs(1.0 - x/y) < 0.01

    if (OC != 0 and OR != 0 and IR != 0 and in_range(IRrat, 2.0) and
        in_range(ORrat, 6.061) and in_range(OCrat, 7.547)):
        return True
    return False




def is_mri_mango(shot):
    IC = sp.shot_params[shot]['ICspeed']
    IR = sp.shot_params[shot]['IRspeed']
    OR = sp.shot_params[shot]['ORspeed']
    OC = sp.shot_params[shot]['OCspeed']

    IRrat = float(IC)/float(IR)
    ORrat = float(IC)/float(OR)
    OCrat = float(IC)/float(OC)

    in_range = lambda x, y: abs(1.0 - x/y) < 0.01

    if (OC != 0 and OR != 0 and IR != 0 and in_range(IRrat, 1.481) and
        in_range(ORrat, 7.547) and in_range(OCrat, 7.547)):
        return True
    return False
