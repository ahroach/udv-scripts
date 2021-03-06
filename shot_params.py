#Creates a dictionary of shots with shot parameters
#Transducer parameters (port number, alpha, beta, offset)
#Component speeds are in RPM.

#The key 'trouble_flag' indicates that there was something wrong with the
#shot. Consult lab notebook for more details.

#Port numbering scheme:
#9   10  11  12
#5   6   7   8
#1   2   3   4

#shot_params[num]['channels'].__contains__(4)
#shot_params[num]['channels'].index(channel_num)

from math import pi
from numpy import nan

#Port locations
ports = {}
ports[1] = {'r': 20.3, 'theta': 0.0, 'z': 3.01625}
ports[2] = {'r': 20.3, 'theta': pi/2, 'z': 3.01625}
ports[3] = {'r': 20.3, 'theta': pi, 'z': 3.01625}
ports[4] = {'r': 20.3, 'theta': 3*pi/2, 'z': 3.01625}
ports[5] = {'r': 20.3, 'theta': 0.0, 'z': 14.44625}
ports[6] = {'r': 20.3, 'theta': pi/2, 'z': 14.44625}
ports[7] = {'r': 20.3, 'theta': pi, 'z': 14.44625}
ports[8] = {'r': 20.3, 'theta': 3*pi/2, 'z': 14.44625}
ports[9] = {'r': 20.3, 'theta': 0.0, 'z': 25.87625}
ports[10] = {'r': 20.3, 'theta': pi/2, 'z': 25.87625}
ports[11] = {'r': 20.3, 'theta': pi, 'z': 25.87625}
ports[12] = {'r': 20.3, 'theta': 3*pi/2, 'z': 25.87625}


shot_params = {}

shot_params[676] = {'shot_num': 676, 'shot_length': 190,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[677] = {'shot_num': 677, 'shot_length': 190,
                    'ICspeed': 400, 'IRspeed': 146,
                    'ORspeed': 40, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[678] = {'shot_num': 678, 'shot_length': 65,
                    'ICspeed': 0, 'IRspeed': 0,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 400, 'field_delay': 5, 't_field': 60,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[679] = {'shot_num': 679, 'shot_length': 190,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 400, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[681] = {'shot_num': 681, 'shot_length': 190,
                    'ICspeed': 400, 'IRspeed': 146,
                    'ORspeed': 40, 'OCspeed': 53,
                    'current': 400, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[682] = {'shot_num': 682, 'shot_length': 150,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 20,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[683] = {'shot_num': 683, 'shot_length': 155,
                    'ICspeed': 400, 'IRspeed': 146,
                    'ORspeed': 40, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 25,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[684] = {'shot_num': 684, 'shot_length': 165,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 35,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[685] = {'shot_num': 685, 'shot_length': 165,
                    'ICspeed': 400, 'IRspeed': 146,
                    'ORspeed': 40, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 35,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[686] = {'shot_num': 686, 'shot_length': 165,
                    'ICspeed': 106, 'IRspeed': 106,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1200, 'field_delay': 125, 't_field': 35,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[687] = {'shot_num': 687, 'shot_length': 165,
                    'ICspeed': 800, 'IRspeed': 292,
                    'ORspeed': 80, 'OCspeed': 106,
                    'current': 1200, 'field_delay': 125, 't_field': 35,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[688] = {'shot_num': 688, 'shot_length': 165,
                    'ICspeed': 800, 'IRspeed': 292,
                    'ORspeed': 80, 'OCspeed': 106,
                    'current': 1200, 'field_delay': 125, 't_field': 35,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[691] = {'shot_num': 691, 'shot_length': 120,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[692] = {'shot_num': 692, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[693] = {'shot_num': 693, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 400,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[694] = {'shot_num': 694, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 181,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[695] = {'shot_num': 695, 'shot_length': 120,
                    'ICspeed': -53, 'IRspeed': -53,
                    'ORspeed': -53, 'OCspeed': -53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[696] = {'shot_num': 696, 'shot_length': 60,
                    'ICspeed': -400, 'IRspeed': -400,
                    'ORspeed': -53, 'OCspeed': -53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[697] = {'shot_num': 697, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[698] = {'shot_num': 698, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[699] = {'shot_num': 699, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 210,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[700] = {'shot_num': 700, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 210,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[701] = {'shot_num': 701, 'shot_length': 190,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 400, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[702] = {'shot_num': 702, 'shot_length': 190,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 400, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[703] = {'shot_num': 703, 'shot_length': 165,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 35,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[704] = {'shot_num': 704, 'shot_length': 190,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 35,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[707] = {'shot_num': 707, 'shot_length': 190,
                    'ICspeed': 400, 'IRspeed': 400,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 400, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[708] = {'shot_num': 708, 'shot_length': 190,
                    'ICspeed': 400, 'IRspeed': 400,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 400, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[711] = {'shot_num': 711, 'shot_length': 190,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 400, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[713] = {'shot_num': 713, 'shot_length': 180,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 800, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[714] = {'shot_num': 714, 'shot_length': 180,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 800, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 120,
                    'channels': [1],
                    'As': [0.75],
                    'Bs': [-90],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[715] = {'shot_num': 715, 'shot_length': 190,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 400, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 120,
                    'channels': [1],
                    'As': [0.75],
                    'Bs': [-90],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[716] = {'shot_num': 716, 'shot_length': 190,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 400, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 120,
                    'channels': [1],
                    'As': [0.75],
                    'Bs': [-90],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[717] = {'shot_num': 717, 'shot_length': 190,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 600, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 120,
                    'channels': [1],
                    'As': [0.75],
                    'Bs': [-90],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[718] = {'shot_num': 718, 'shot_length': 190,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 600, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 120,
                    'channels': [1],
                    'As': [0.75],
                    'Bs': [-90],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[719] = {'shot_num': 719, 'shot_length': 190,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 600, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[720] = {'shot_num': 720, 'shot_length': 180,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 800, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 120,
                    'channels': [1],
                    'As': [0.75],
                    'Bs': [-90],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[721] = {'shot_num': 721, 'shot_length': 180,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 800, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 120,
                    'channels': [1],
                    'As': [0.75],
                    'Bs': [-90],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[722] = {'shot_num': 722, 'shot_length': 180,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 800, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 120,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[723] = {'shot_num': 723, 'shot_length': 170,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 120,
                    'channels': [1],
                    'As': [0.75],
                    'Bs': [-90],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[724] = {'shot_num': 724, 'shot_length': 170,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 120,
                    'channels': [1],
                    'As': [0.75],
                    'Bs': [-90],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[725] = {'shot_num': 725, 'shot_length': 170,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[726] = {'shot_num': 726, 'shot_length': 160,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 120,
                    'channels': [1],
                    'As': [0.75],
                    'Bs': [-90],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[727] = {'shot_num': 727, 'shot_length': 160,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 120,
                    'channels': [1],
                    'As': [0.75],
                    'Bs': [-90],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[728] = {'shot_num': 728, 'shot_length': 160,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[729] = {'shot_num': 729, 'shot_length': 150,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1400, 'field_delay': 125, 't_field': 20,
                    'udv_delay': 120,
                    'channels': [1],
                    'As': [0.75],
                    'Bs': [-90],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[730] = {'shot_num': 730, 'shot_length': 150,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 1400, 'field_delay': 125, 't_field': 20,
                    'udv_delay': 120,
                    'channels': [1],
                    'As': [0.75],
                    'Bs': [-90],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[731] = {'shot_num': 731, 'shot_length': 150,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 1400, 'field_delay': 125, 't_field': 20,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[732] = {'shot_num': 732, 'shot_length': 145,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1600, 'field_delay': 125, 't_field': 15,
                    'udv_delay': 120,
                    'channels': [1],
                    'As': [0.75],
                    'Bs': [-90],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[733] = {'shot_num': 733, 'shot_length': 145,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 1600, 'field_delay': 125, 't_field': 15,
                    'udv_delay': 120,
                    'channels': [1],
                    'As': [0.75],
                    'Bs': [-90],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[734] = {'shot_num': 734, 'shot_length': 145,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 1600, 'field_delay': 125, 't_field': 15,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[735] = {'shot_num': 735, 'shot_length': 240,
                    'ICspeed': -400, 'IRspeed': -200,
                    'ORspeed': -66, 'OCspeed': -53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[736] = {'shot_num': 736, 'shot_length': 240,
                    'ICspeed': -400, 'IRspeed': -53,
                    'ORspeed': -53, 'OCspeed': -53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[737] = {'shot_num': 737, 'shot_length': 240,
                    'ICspeed': -400, 'IRspeed': -400,
                    'ORspeed': -53, 'OCspeed': -53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[738] = {'shot_num': 738, 'shot_length': 240,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[739] = {'shot_num': 739, 'shot_length': 240,
                    'ICspeed': 400, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[740] = {'shot_num': 740, 'shot_length': 240,
                    'ICspeed': 400, 'IRspeed': 400,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[741] = {'shot_num': 741, 'shot_length': 60,
                    'ICspeed': 800, 'IRspeed': 400,
                    'ORspeed': 132, 'OCspeed': 106,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[742] = {'shot_num': 742, 'shot_length': 170,
                    'ICspeed': 800, 'IRspeed': 400,
                    'ORspeed': 132, 'OCspeed': 106,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[743] = {'shot_num': 743, 'shot_length': 170,
                    'ICspeed': 106, 'IRspeed': 106,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 120,
                    'channels': [1],
                    'As': [0.75],
                    'Bs': [-90],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[744] = {'shot_num': 744, 'shot_length': 170,
                    'ICspeed': 800, 'IRspeed': 400,
                    'ORspeed': 132, 'OCspeed': 106,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 120,
                    'channels': [1],
                    'As': [0.75],
                    'Bs': [-90],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[745] = {'shot_num': 745, 'shot_length': 170,
                    'ICspeed': 400, 'IRspeed': 146,
                    'ORspeed': 40, 'OCspeed': 53,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[763] = {'shot_num': 763, 'shot_length': 170,
                    'ICspeed': 106, 'IRspeed': 106,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 120,
                    'channels': [1],
                    'As': [0.75],
                    'Bs': [-90],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[774] = {'shot_num': 774, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[775] = {'shot_num': 775, 'shot_length': 120,
                    'ICspeed': 106, 'IRspeed': 106,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[785] = {'shot_num': 785, 'shot_length': 70, 'trouble_flag': 1,
                    'ICspeed': 800, 'IRspeed': 400,
                    'ORspeed': 132, 'OCspeed': 106,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[787] = {'shot_num': 787, 'shot_length': 40, 'trouble_flag': 1,
                    'ICspeed': 1200, 'IRspeed': 600,
                    'ORspeed': 198, 'OCspeed': 159,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[788] = {'shot_num': 788, 'shot_length': 40, 'trouble_flag': 1,
                    'ICspeed': 1200, 'IRspeed': 600,
                    'ORspeed': 198, 'OCspeed': 159,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[813] = {'shot_num': 813, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[814] = {'shot_num': 814, 'shot_length': 40, 'trouble_flag': 1,
                    'ICspeed': 800, 'IRspeed': 400,
                    'ORspeed': 132, 'OCspeed': 106,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[815] = {'shot_num': 815, 'shot_length': 10, 'trouble_flag': 1,
                    'ICspeed': 800, 'IRspeed': 292,
                    'ORspeed': 80, 'OCspeed': 106,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[816] = {'shot_num': 816, 'shot_length': 9, 'trouble_flag': 1,
                    'ICspeed': 1200, 'IRspeed': 600,
                    'ORspeed': 198, 'OCspeed': 159,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[818] = {'shot_num': 818, 'shot_length': 40, 'trouble_flag': 1,
                    'ICspeed': 1200, 'IRspeed': 600,
                    'ORspeed': 198, 'OCspeed': 159,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[819] = {'shot_num': 819, 'shot_length': 40, 'trouble_flag': 1,
                    'ICspeed': 1200, 'IRspeed': 600,
                    'ORspeed': 198, 'OCspeed': 159,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[820] = {'shot_num': 820, 'shot_length': 120, 'trouble_flag': 1,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[821] = {'shot_num': 821, 'shot_length': 120, 'trouble_flag': 1,
                    'ICspeed': 400, 'IRspeed': 175,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[822] = {'shot_num': 822, 'shot_length': 120, 'trouble_flag': 1,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[823] = {'shot_num': 823, 'shot_length': 120, 'trouble_flag': 1,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[824] = {'shot_num': 824, 'shot_length': 120, 'trouble_flag': 1,
                    'ICspeed': 400, 'IRspeed': 175,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[825] = {'shot_num': 825, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 175,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[826] = {'shot_num': 826, 'shot_length': 120, 'trouble_flag': 1,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[827] = {'shot_num': 827, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[828] = {'shot_num': 828, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[829] = {'shot_num': 829, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 240,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[830] = {'shot_num': 830, 'shot_length': 185,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 800, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[831] = {'shot_num': 831, 'shot_length': 180,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 800, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 120,
                    'channels': [1],
                    'As': [0.75],
                    'Bs': [-90],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[832] = {'shot_num': 832, 'shot_length': 170,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 120,
                    'channels': [1],
                    'As': [0.75],
                    'Bs': [-90],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[833] = {'shot_num': 833, 'shot_length': 160,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 120,
                    'channels': [1],
                    'As': [0.75],
                    'Bs': [-90],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[834] = {'shot_num': 834, 'shot_length': 150,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1400, 'field_delay': 125, 't_field': 20,
                    'udv_delay': 120,
                    'channels': [1],
                    'As': [0.75],
                    'Bs': [-90],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[836] = {'shot_num': 836, 'shot_length': 160,
                    'ICspeed': 106, 'IRspeed': 106,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[838] = {'shot_num': 838, 'shot_length': 160, 'trouble_flag': 1,
                    'ICspeed': 800, 'IRspeed': 440,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 102.5,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[839] = {'shot_num': 839, 'shot_length': 160,
                    'ICspeed': 159, 'IRspeed': 159,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[840] = {'shot_num': 840, 'shot_length': 160,
                    'ICspeed': 1200, 'IRspeed': 660,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[841] = {'shot_num': 841, 'shot_length': 160,
                    'ICspeed': 212, 'IRspeed': 212,
                    'ORspeed': 212, 'OCspeed': 212,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[842] = {'shot_num': 842, 'shot_length': 160,
                    'ICspeed': 1600, 'IRspeed': 880,
                    'ORspeed': 212, 'OCspeed': 212,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[848] = {'shot_num': 848, 'shot_length': 120,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[849] = {'shot_num': 849, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[850] = {'shot_num': 850, 'shot_length': 160,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[851] = {'shot_num': 851, 'shot_length': 160,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[852] = {'shot_num': 852, 'shot_length': 160,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[853] = {'shot_num': 853, 'shot_length': 160,
                    'ICspeed': 106, 'IRspeed': 106,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[854] = {'shot_num': 854, 'shot_length': 160,
                    'ICspeed': 800, 'IRspeed': 440,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[855] = {'shot_num': 855, 'shot_length': 160,
                    'ICspeed': 159, 'IRspeed': 159,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[856] = {'shot_num': 856, 'shot_length': 160,
                    'ICspeed': 1200, 'IRspeed': 660,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[857] = {'shot_num': 857, 'shot_length': 160,
                    'ICspeed': 212, 'IRspeed': 212,
                    'ORspeed': 212, 'OCspeed': 212,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[858] = {'shot_num': 858, 'shot_length': 160,
                    'ICspeed': 1600, 'IRspeed': 880,
                    'ORspeed': 212, 'OCspeed': 212,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[859] = {'shot_num': 859, 'shot_length': 160,
                    'ICspeed': 239, 'IRspeed': 239,
                    'ORspeed': 239, 'OCspeed': 239,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 120,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[860] = {'shot_num': 860, 'shot_length': 160,
                    'ICspeed': 1800, 'IRspeed': 990,
                    'ORspeed': 239, 'OCspeed': 239,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 120,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[861] = {'shot_num': 861, 'shot_length': 160,
                    'ICspeed': 265, 'IRspeed': 265,
                    'ORspeed': 265, 'OCspeed': 265,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 120,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[864] = {'shot_num': 864, 'shot_length': 160,
                    'ICspeed': 265, 'IRspeed': 265,
                    'ORspeed': 265, 'OCspeed': 265,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 120,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[866] = {'shot_num': 866, 'shot_length': 160,
                    'ICspeed': 1200, 'IRspeed': 800,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 120,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[867] = {'shot_num': 867, 'shot_length': 160,
                    'ICspeed': 1600, 'IRspeed': 1080,
                    'ORspeed': 212, 'OCspeed': 212,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[876] = {'shot_num': 876, 'shot_length': 160,
                    'ICspeed': 1200, 'IRspeed': 810,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[877] = {'shot_num': 877, 'shot_length': 160,
                    'ICspeed': 212, 'IRspeed': 212,
                    'ORspeed': 212, 'OCspeed': 212,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[878] = {'shot_num': 878, 'shot_length': 160,
                    'ICspeed': 1600, 'IRspeed': 1080,
                    'ORspeed': 212, 'OCspeed': 212,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[880] = {'shot_num': 880, 'shot_length': 160,
                    'ICspeed': 1600, 'IRspeed': 940,
                    'ORspeed': 212, 'OCspeed': 212,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[884] = {'shot_num': 884, 'shot_length': 160,
                    'ICspeed': 800, 'IRspeed': 540,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}




shot_params[885] = {'shot_num': 885, 'shot_length': 160,
                    'ICspeed': 800, 'IRspeed': 540,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[886] = {'shot_num': 886, 'shot_length': 160,
                    'ICspeed': 800, 'IRspeed': 440,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[887] = {'shot_num': 887, 'shot_length': 190,
                    'ICspeed': 159, 'IRspeed': 159,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 600, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[888] = {'shot_num': 888, 'shot_length': 190,
                    'ICspeed': 1200, 'IRspeed': 660,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 600, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[894] = {'shot_num': 894, 'shot_length': 190,
                    'ICspeed': 800, 'IRspeed': 440,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 600, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}

shot_params[895] = {'shot_num': 895, 'shot_length': 180,
                    'ICspeed': 106, 'IRspeed': 106,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 800, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[897] = {'shot_num': 897, 'shot_length': 170,
                    'ICspeed': 106, 'IRspeed': 106,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[898] = {'shot_num': 898, 'shot_length': 170,
                    'ICspeed': 800, 'IRspeed': 440,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[899] = {'shot_num': 899, 'shot_length': 150,
                    'ICspeed': 106, 'IRspeed': 106,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1400, 'field_delay': 125, 't_field': 20,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[900] = {'shot_num': 900, 'shot_length': 150,
                    'ICspeed': 800, 'IRspeed': 440,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1400, 'field_delay': 125, 't_field': 20,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[901] = {'shot_num': 901, 'shot_length': 150,
                    'ICspeed': 159, 'IRspeed': 159,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 1400, 'field_delay': 125, 't_field': 20,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[902] = {'shot_num': 902, 'shot_length': 150,
                    'ICspeed': 1200, 'IRspeed': 660,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 1400, 'field_delay': 125, 't_field': 20,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[903] = {'shot_num': 903, 'shot_length': 145,
                    'ICspeed': 159, 'IRspeed': 159,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 1600, 'field_delay': 125, 't_field': 15,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[904] = {'shot_num': 904, 'shot_length': 145,
                    'ICspeed': 1200, 'IRspeed': 660,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 1600, 'field_delay': 125, 't_field': 15,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[909] = {'shot_num': 909, 'shot_length': 185,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 700, 'field_delay': 125, 't_field': 55,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[910] = {'shot_num': 910, 'shot_length': 185,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 700, 'field_delay': 125, 't_field': 55,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}



shot_params[911] = {'shot_num': 911, 'shot_length': 190,
                    'ICspeed': 200, 'IRspeed': 110,
                    'ORspeed': 26.5, 'OCspeed': 26.5,
                    'current': 500, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[912] = {'shot_num': 912, 'shot_length': 190,
                    'ICspeed': 26.5, 'IRspeed': 26.5,
                    'ORspeed': 26.5, 'OCspeed': 26.5,
                    'current': 500, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[913] = {'shot_num': 913, 'shot_length': 190,
                    'ICspeed': 200, 'IRspeed': 110,
                    'ORspeed': 26.5, 'OCspeed': 26.5,
                    'current': 600, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}

shot_params[914] = {'shot_num': 914, 'shot_length': 185,
                    'ICspeed': 200, 'IRspeed': 110,
                    'ORspeed': 26.5, 'OCspeed': 26.5,
                    'current': 700, 'field_delay': 125, 't_field': 55,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[915] = {'shot_num': 915, 'shot_length': 145,
                    'ICspeed': 200, 'IRspeed': 110,
                    'ORspeed': 26.5, 'OCspeed': 26.5,
                    'current': 1600, 'field_delay': 125, 't_field': 15,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[916] = {'shot_num': 916, 'shot_length': 175,
                    'ICspeed': 600, 'IRspeed': 330,
                    'ORspeed': 79.5, 'OCspeed': 79.5,
                    'current': 900, 'field_delay': 125, 't_field': 45,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[917] = {'shot_num': 917, 'shot_length': 170,
                    'ICspeed': 600, 'IRspeed': 330,
                    'ORspeed': 79.5, 'OCspeed': 79.5,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}

shot_params[918] = {'shot_num': 918, 'shot_length': 165,
                    'ICspeed': 600, 'IRspeed': 330,
                    'ORspeed': 79.5, 'OCspeed': 79.5,
                    'current': 1100, 'field_delay': 125, 't_field': 35,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[919] = {'shot_num': 919, 'shot_length': 165,
                    'ICspeed': 800, 'IRspeed': 440,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1100, 'field_delay': 125, 't_field': 35,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[920] = {'shot_num': 920, 'shot_length': 155,
                    'ICspeed': 600, 'IRspeed': 330,
                    'ORspeed': 79.5, 'OCspeed': 79.5,
                    'current': 1300, 'field_delay': 125, 't_field': 25,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[921] = {'shot_num': 921, 'shot_length': 155,
                    'ICspeed': 1000, 'IRspeed': 550,
                    'ORspeed': 132.5, 'OCspeed': 132.5,
                    'current': 1300, 'field_delay': 125, 't_field': 25,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[922] = {'shot_num': 922, 'shot_length': 150,
                    'ICspeed': 1000, 'IRspeed': 550,
                    'ORspeed': 132.5, 'OCspeed': 132.5,
                    'current': 1400, 'field_delay': 125, 't_field': 20,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'As': [0.75, 20.3],
                    'Bs': [-90, 90],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[925] = {'shot_num': 925, 'shot_length': 170, 'trouble_flag': 1,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[926] = {'shot_num': 926, 'shot_length': 170,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[927] = {'shot_num': 927, 'shot_length': 160,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[928] = {'shot_num': 928, 'shot_length': 165,
                    'ICspeed': 600, 'IRspeed': 330,
                    'ORspeed': 79.5, 'OCspeed': 79.5,
                    'current': 1100, 'field_delay': 125, 't_field': 35,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[929] = {'shot_num': 929, 'shot_length': 165,
                    'ICspeed': 800, 'IRspeed': 440,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1100, 'field_delay': 125, 't_field': 35,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[930] = {'shot_num': 930, 'shot_length': 145,
                    'ICspeed': 200, 'IRspeed': 110,
                    'ORspeed': 26.5, 'OCspeed': 26.5,
                    'current': 1600, 'field_delay': 125, 't_field': 15,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[931] = {'shot_num': 931, 'shot_length': 145,
                    'ICspeed': 100, 'IRspeed': 55,
                    'ORspeed': 13.25, 'OCspeed': 13.25,
                    'current': 1600, 'field_delay': 125, 't_field': 15,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[932] = {'shot_num': 932, 'shot_length': 180,
                    'ICspeed': 100, 'IRspeed': 55,
                    'ORspeed': 13.25, 'OCspeed': 13.25,
                    'current': 800, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[933] = {'shot_num': 933, 'shot_length': 190,
                    'ICspeed': 100, 'IRspeed': 55,
                    'ORspeed': 13.25, 'OCspeed': 13.25,
                    'current': 500, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[934] = {'shot_num': 934, 'shot_length': 190,
                    'ICspeed': 100, 'IRspeed': 55,
                    'ORspeed': 13.25, 'OCspeed': 13.25,
                    'current': 400, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[935] = {'shot_num': 935, 'shot_length': 190,
                    'ICspeed': 100, 'IRspeed': 55,
                    'ORspeed': 13.25, 'OCspeed': 13.25,
                    'current': 300, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[936] = {'shot_num': 936, 'shot_length': 160,
                    'ICspeed': 1600, 'IRspeed': 1080,
                    'ORspeed': 212, 'OCspeed': 212,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[939] = {'shot_num': 939, 'shot_length': 180,
                    'ICspeed': 400, 'IRspeed': 400,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 600, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[941] = {'shot_num': 941, 'shot_length': 180, 'trouble_flag': 1,
                    'ICspeed': 400, 'IRspeed': 400,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 800, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[942] = {'shot_num': 942, 'shot_length': 170, 'trouble_flag': 1,
                    'ICspeed': 400, 'IRspeed': 400,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[943] = {'shot_num': 943, 'shot_length': 180,
                    'ICspeed': 400, 'IRspeed': 400,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 400, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[944] = {'shot_num': 944, 'shot_length': 180,
                    'ICspeed': 400, 'IRspeed': 400,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 700, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[945] = {'shot_num': 945, 'shot_length': 180,
                    'ICspeed': 400, 'IRspeed': 400,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 900, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[946] = {'shot_num': 946, 'shot_length': 165,
                    'ICspeed': 400, 'IRspeed': 400,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1100, 'field_delay': 125, 't_field': 35,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[947] = {'shot_num': 947, 'shot_length': 160,
                    'ICspeed': 400, 'IRspeed': 400,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[948] = {'shot_num': 948, 'shot_length': 155,
                    'ICspeed': 400, 'IRspeed': 400,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1300, 'field_delay': 125, 't_field': 25,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[949] = {'shot_num': 949, 'shot_length': 150,
                    'ICspeed': 400, 'IRspeed': 400,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1400, 'field_delay': 125, 't_field': 20,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[950] = {'shot_num': 950, 'shot_length': 145,
                    'ICspeed': 400, 'IRspeed': 400,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1500, 'field_delay': 125, 't_field': 15,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[951] = {'shot_num': 951, 'shot_length': 145,
                    'ICspeed': 400, 'IRspeed': 400,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1600, 'field_delay': 125, 't_field': 15,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[953] = {'shot_num': 953, 'shot_length': 150,
                    'ICspeed': 400, 'IRspeed': 400,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1400, 'field_delay': 125, 't_field': 20,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[954] = {'shot_num': 954, 'shot_length': 150,
                    'ICspeed': 600, 'IRspeed': 600,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1400, 'field_delay': 125, 't_field': 20,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[955] = {'shot_num': 955, 'shot_length': 160,
                    'ICspeed': 600, 'IRspeed': 600,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[956] = {'shot_num': 956, 'shot_length': 170,
                    'ICspeed': 600, 'IRspeed': 600,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[957] = {'shot_num': 957, 'shot_length': 170,
                    'ICspeed': 400, 'IRspeed': 400,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[958] = {'shot_num': 958, 'shot_length': 165,
                    'ICspeed': 600, 'IRspeed': 600,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1100, 'field_delay': 125, 't_field': 35,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[959] = {'shot_num': 959, 'shot_length': 165,
                    'ICspeed': 200, 'IRspeed': 200,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1100, 'field_delay': 125, 't_field': 35,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[960] = {'shot_num': 960, 'shot_length': 170,
                    'ICspeed': 200, 'IRspeed': 200,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[961] = {'shot_num': 961, 'shot_length': 175,
                    'ICspeed': 200, 'IRspeed': 200,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 900, 'field_delay': 125, 't_field': 45,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[962] = {'shot_num': 962, 'shot_length': 180,
                    'ICspeed': 200, 'IRspeed': 200,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 800, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[963] = {'shot_num': 963, 'shot_length': 180,
                    'ICspeed': 200, 'IRspeed': 200,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 700, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[964] = {'shot_num': 964, 'shot_length': 180,
                    'ICspeed': 200, 'IRspeed': 200,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 600, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[965] = {'shot_num': 965, 'shot_length': 180,
                    'ICspeed': 200, 'IRspeed': 200,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 500, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[966] = {'shot_num': 966, 'shot_length': 180,
                    'ICspeed': 200, 'IRspeed': 200,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 400, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[967] = {'shot_num': 967, 'shot_length': 180,
                    'ICspeed': 100, 'IRspeed': 100,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 400, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[968] = {'shot_num': 968, 'shot_length': 180,
                    'ICspeed': 100, 'IRspeed': 100,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 500, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[969] = {'shot_num': 969, 'shot_length': 180, 'trouble_flag': 1,
                    'ICspeed': 100, 'IRspeed': 100,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 600, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[970] = {'shot_num': 970, 'shot_length': 180,
                    'ICspeed': 100, 'IRspeed': 100,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 300, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[971] = {'shot_num': 971, 'shot_length': 180,
                    'ICspeed': 50, 'IRspeed': 50,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 300, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[972] = {'shot_num': 972, 'shot_length': 180,
                    'ICspeed': 50, 'IRspeed': 50,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 400, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[973] = {'shot_num': 973, 'shot_length': 180,
                    'ICspeed': 50, 'IRspeed': 50,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 500, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[974] = {'shot_num': 974, 'shot_length': 180, 'trouble_flag': 1,
                    'ICspeed': 50, 'IRspeed': 50,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 200, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[975] = {'shot_num': 975, 'shot_length': 145,
                    'ICspeed': 50, 'IRspeed': 50,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1600, 'field_delay': 125, 't_field': 15,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[976] = {'shot_num': 976, 'shot_length': 160,
                    'ICspeed': 700, 'IRspeed': 700,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[977] = {'shot_num': 977, 'shot_length': 155,
                    'ICspeed': 700, 'IRspeed': 700,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1300, 'field_delay': 125, 't_field': 25,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[978] = {'shot_num': 978, 'shot_length': 150,
                    'ICspeed': 700, 'IRspeed': 700,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1400, 'field_delay': 125, 't_field': 20,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[979] = {'shot_num': 979, 'shot_length': 145,
                    'ICspeed': 700, 'IRspeed': 700,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1600, 'field_delay': 125, 't_field': 15,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[980] = {'shot_num': 980, 'shot_length': 145,
                    'ICspeed': 200, 'IRspeed': 200,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1600, 'field_delay': 125, 't_field': 15,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[981] = {'shot_num': 981, 'shot_length': 145,
                    'ICspeed': 100, 'IRspeed': 100,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1600, 'field_delay': 125, 't_field': 15,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[982] = {'shot_num': 982, 'shot_length': 145,
                    'ICspeed': 700, 'IRspeed': 700,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1500, 'field_delay': 125, 't_field': 15,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[983] = {'shot_num': 983, 'shot_length': 180, 'trouble_flag': 1,
                    'ICspeed': 700, 'IRspeed': 700,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 180, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[984] = {'shot_num': 984, 'shot_length': 180,
                    'ICspeed': 700, 'IRspeed': 700,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 250, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[985] = {'shot_num': 985, 'shot_length': 180, 'trouble_flag': 1,
                    'ICspeed': 700, 'IRspeed': 700,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 300, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[986] = {'shot_num': 986, 'shot_length': 180,
                    'ICspeed': 700, 'IRspeed': 700,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 400, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[987] = {'shot_num': 987, 'shot_length': 180,
                    'ICspeed': 700, 'IRspeed': 700,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 500, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[988] = {'shot_num': 988, 'shot_length': 180,
                    'ICspeed': 700, 'IRspeed': 700,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 600, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[989] = {'shot_num': 989, 'shot_length': 180,
                    'ICspeed': 700, 'IRspeed': 700,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 700, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[990] = {'shot_num': 990, 'shot_length': 180,
                    'ICspeed': 700, 'IRspeed': 700,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 800, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[991] = {'shot_num': 991, 'shot_length': 175,
                    'ICspeed': 700, 'IRspeed': 700,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 900, 'field_delay': 125, 't_field': 45,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[992] = {'shot_num': 992, 'shot_length': 175,
                    'ICspeed': 700, 'IRspeed': 700,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1000, 'field_delay': 125, 't_field': 45,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[993] = {'shot_num': 993, 'shot_length': 165,
                    'ICspeed': 700, 'IRspeed': 700,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1100, 'field_delay': 125, 't_field': 35,
                    'udv_delay': 105,
                    'channels': [2, 3],
                    'As': [20.3, 20.3],
                    'Bs': [90, 90],
                    'offsets': [0.72, 0.41],
                    'ports': [6, 7]}


shot_params[994] = {'shot_num': 994, 'shot_length': 40,
                    'ICspeed': 0, 'IRspeed': 0,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 1200, 'field_delay': 5, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[995] = {'shot_num': 995, 'shot_length': 160,
                    'ICspeed': 106, 'IRspeed': 106,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[996] = {'shot_num': 996, 'shot_length': 160, 'trouble_flag': 1,
                    'ICspeed': 800, 'IRspeed': 440,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 120,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[997] = {'shot_num': 997, 'shot_length': 160,
                    'ICspeed': 159, 'IRspeed': 159,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[998] = {'shot_num': 998, 'shot_length': 160,
                    'ICspeed': 1200, 'IRspeed': 660,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 105,
                    'channels': [1, 2, 3, 4],
                    'As': [0.75, 20.3, 20.3, 20.3],
                    'Bs': [-90, 90, 90, 90],
                    'offsets': [1.19, 0.72, 0.41, 0.53],
                    'ports': [5, 6, 7, 3]}


shot_params[1000] = {'shot_num': 1000, 'shot_length': 160,
                     'ICspeed': 212, 'IRspeed': 212,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1002] = {'shot_num': 1002, 'shot_length': 160,
                     'ICspeed': 200, 'IRspeed': 26.5,
                     'ORspeed': 26.5, 'OCspeed': 26.5,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1003] = {'shot_num': 1003, 'shot_length': 160,
                     'ICspeed': 400, 'IRspeed': 53,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1004] = {'shot_num': 1004, 'shot_length': 145,
                     'ICspeed': 400, 'IRspeed': 53,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 1600, 'field_delay': 125, 't_field': 15,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1005] = {'shot_num': 1005, 'shot_length': 145,
                     'ICspeed': 200, 'IRspeed': 26.5,
                     'ORspeed': 26.5, 'OCspeed': 26.5,
                     'current': 1600, 'field_delay': 125, 't_field': 15,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1006] = {'shot_num': 1006, 'shot_length': 160,
                     'ICspeed': 200, 'IRspeed': 200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1007] = {'shot_num': 1007, 'shot_length': 160,
                     'ICspeed': 25, 'IRspeed': 25,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1008] = {'shot_num': 1008, 'shot_length': 250, 'trouble_flag': 1,
                     'ICspeed': 25, 'IRspeed': 25,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 600, 'field_delay': 125, 't_field': 120,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1009] = {'shot_num': 1009, 'shot_length': 370,
                     'ICspeed': 25, 'IRspeed': 25,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 200, 'field_delay': 125, 't_field': 240,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1010] = {'shot_num': 1010, 'shot_length': 370,
                     'ICspeed': 25, 'IRspeed': 25,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 400, 'field_delay': 125, 't_field': 240,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1011] = {'shot_num': 1011, 'shot_length': 370,
                     'ICspeed': 25, 'IRspeed': 25,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 100, 'field_delay': 125, 't_field': 240,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1012] = {'shot_num': 1012, 'shot_length': 170,
                     'ICspeed': 0, 'IRspeed': 0,
                     'ORspeed': 106, 'OCspeed': 106,
                     'current': 1000, 'field_delay': 125, 't_field': 40,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1013] = {'shot_num': 1013, 'shot_length': 140,
                     'ICspeed': 0, 'IRspeed': 0,
                     'ORspeed': 106, 'OCspeed': 106,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1014] = {'shot_num': 1014, 'shot_length': 100,
                     'ICspeed': 0, 'IRspeed': 0,
                     'ORspeed': 106, 'OCspeed': 106,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 0,
                     'channels': [1, 2, 3],
                     'As': [0.75, 20.3, 20.3],
                     'Bs': [-90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41],
                     'ports': [5, 6, 7]}


shot_params[1015] = {'shot_num': 1015, 'shot_length': 150,
                     'ICspeed': 0, 'IRspeed': 0,
                     'ORspeed': 106, 'OCspeed': 106,
                     'current': 1400, 'field_delay': 125, 't_field': 20,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1016] = {'shot_num': 1016, 'shot_length': 150,
                     'ICspeed': 0, 'IRspeed': 0,
                     'ORspeed': 26.5, 'OCspeed': 26.5,
                     'current': 1400, 'field_delay': 125, 't_field': 20,
                     'udv_delay': 60,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1017] = {'shot_num': 1017, 'shot_length': 360,
                     'ICspeed': 0, 'IRspeed': 0,
                     'ORspeed': 26.5, 'OCspeed': 26.5,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1018] = {'shot_num': 1018, 'shot_length': 160,
                     'ICspeed': 0, 'IRspeed': 0,
                     'ORspeed': 26.5, 'OCspeed': 26.5,
                     'current': 1400, 'field_delay': 90, 't_field': 20,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1019] = {'shot_num': 1019, 'shot_length': 180, 'trouble_flag': 1,
                     'ICspeed': 200, 'IRspeed': 110,
                     'ORspeed': 26.5, 'OCspeed': 26.5,
                     'current': 600, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1020] = {'shot_num': 1020, 'shot_length': 180, 'trouble_flag': 1,
                     'ICspeed': 200, 'IRspeed': 70,
                     'ORspeed': 26.5, 'OCspeed': 26.5,
                     'current': 600, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1022] = {'shot_num': 1022, 'shot_length': 180, 'trouble_flag': 1,
                     'ICspeed': 400, 'IRspeed': 140,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 600, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1023] = {'shot_num': 1023, 'shot_length': 180, 'trouble_flag': 1,
                     'ICspeed': 400, 'IRspeed': 140,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1024] = {'shot_num': 1024, 'shot_length': 180, 'trouble_flag': 1,
                     'ICspeed': 400, 'IRspeed': 100,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1025] = {'shot_num': 1025, 'shot_length': 180, 'trouble_flag': 1,
                     'ICspeed': 400, 'IRspeed': 220,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1026] = {'shot_num': 1026, 'shot_length': 170, 'trouble_flag': 1,
                     'ICspeed': 400, 'IRspeed': 100,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 1000, 'field_delay': 125, 't_field': 40,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1027] = {'shot_num': 1027, 'shot_length': 160, 'trouble_flag': 1,
                     'ICspeed': 400, 'IRspeed': 100,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1028] = {'shot_num': 1028, 'shot_length': 170, 'trouble_flag': 1,
                     'ICspeed': 400, 'IRspeed': 140,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 1000, 'field_delay': 125, 't_field': 40,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1029] = {'shot_num': 1029, 'shot_length': 160, 'trouble_flag': 1,
                     'ICspeed': 400, 'IRspeed': 140,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1030] = {'shot_num': 1030, 'shot_length': 150, 'trouble_flag': 1,
                     'ICspeed': 400, 'IRspeed': 140,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 1400, 'field_delay': 125, 't_field': 20,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1031] = {'shot_num': 1031, 'shot_length': 150, 'trouble_flag': 1,
                     'ICspeed': 400, 'IRspeed': 220,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 1400, 'field_delay': 125, 't_field': 20,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1032] = {'shot_num': 1032, 'shot_length': 150, 'trouble_flag': 1,
                     'ICspeed': 400, 'IRspeed': 100,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 1400, 'field_delay': 125, 't_field': 20,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1033] = {'shot_num': 1033, 'shot_length': 150, 'trouble_flag': 1,
                     'ICspeed': 400, 'IRspeed': 300,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 1400, 'field_delay': 125, 't_field': 20,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1034] = {'shot_num': 1034, 'shot_length': 180,
                     'ICspeed': 400, 'IRspeed': 300,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1035] = {'shot_num': 1035, 'shot_length': 180,
                     'ICspeed': 400, 'IRspeed': 120,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1036] = {'shot_num': 1036, 'shot_length': 180,
                     'ICspeed': 400, 'IRspeed': 220,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1037] = {'shot_num': 1037, 'shot_length': 180,
                     'ICspeed': 400, 'IRspeed': 140,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1038] = {'shot_num': 1038, 'shot_length': 170,
                     'ICspeed': 400, 'IRspeed': 300,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 1000, 'field_delay': 125, 't_field': 40,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1039] = {'shot_num': 1039, 'shot_length': 170,
                     'ICspeed': 400, 'IRspeed': 140,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 1000, 'field_delay': 125, 't_field': 40,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1040] = {'shot_num': 1040, 'shot_length': 160,
                     'ICspeed': 400, 'IRspeed': 300,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}

shot_params[1041] = {'shot_num': 1041, 'shot_length': 160,
                     'ICspeed': 400, 'IRspeed': 140,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1042] = {'shot_num': 1042, 'shot_length': 150,
                     'ICspeed': 400, 'IRspeed': 300,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 1400, 'field_delay': 125, 't_field': 20,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1043] = {'shot_num': 1043, 'shot_length': 150,
                     'ICspeed': 400, 'IRspeed': 140,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 1400, 'field_delay': 125, 't_field': 20,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1044] = {'shot_num': 1044, 'shot_length': 150,
                     'ICspeed': 400, 'IRspeed': 220,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 1400, 'field_delay': 125, 't_field': 20,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1045] = {'shot_num': 1045, 'shot_length': 160,
                     'ICspeed': 212, 'IRspeed': 212,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1052] = {'shot_num': 1052, 'shot_length': 180,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1053] = {'shot_num': 1053, 'shot_length': 170,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 1000, 'field_delay': 125, 't_field': 40,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1054] = {'shot_num': 1054, 'shot_length': 160,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1055] = {'shot_num': 1055, 'shot_length': 150,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 1400, 'field_delay': 125, 't_field': 20,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1063] = {'shot_num': 1063, 'shot_length': 160,
                     'ICspeed': 400, 'IRspeed': 220,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1064] = {'shot_num': 1064, 'shot_length': 160,
                     'ICspeed': 212, 'IRspeed': 212,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1065] = {'shot_num': 1065, 'shot_length': 160,
                     'ICspeed': 1600, 'IRspeed': 1080,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1066] = {'shot_num': 1066, 'shot_length': 160, 'trouble_flag': 1,
                     'ICspeed': 265, 'IRspeed': 265,
                     'ORspeed': 265, 'OCspeed': 265,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1067] = {'shot_num': 1067, 'shot_length': 165, 'trouble_flag': 1,
                     'ICspeed': 2000, 'IRspeed': 1350,
                     'ORspeed': 265, 'OCspeed': 265,
                     'current': 1200, 'field_delay': 125, 't_field': 35,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1069] = {'shot_num': 1069, 'shot_length': 165,
                     'ICspeed': 159, 'IRspeed': 159,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1070] = {'shot_num': 1070, 'shot_length': 165,
                     'ICspeed': 238, 'IRspeed': 238,
                     'ORspeed': 238, 'OCspeed': 238,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1071] = {'shot_num': 1071, 'shot_length': 165,
                     'ICspeed': 2000, 'IRspeed': 1350,
                     'ORspeed': 265, 'OCspeed': 265,
                     'current': 1200, 'field_delay': 125, 't_field': 35,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1072] = {'shot_num': 1072, 'shot_length': 160,
                     'ICspeed': 1200, 'IRspeed': 810,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1073] = {'shot_num': 1073, 'shot_length': 165,
                     'ICspeed': 238, 'IRspeed': 238,
                     'ORspeed': 238, 'OCspeed': 238,
                     'current': 1200, 'field_delay': 125, 't_field': 35,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1075] = {'shot_num': 1075, 'shot_length': 160,
                     'ICspeed': 238, 'IRspeed': 238,
                     'ORspeed': 238, 'OCspeed': 238,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1077] = {'shot_num': 1077, 'shot_length': 160,
                     'ICspeed': 159, 'IRspeed': 159,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1078] = {'shot_num': 1078, 'shot_length': 160,
                     'ICspeed': 238, 'IRspeed': 238,
                     'ORspeed': 238, 'OCspeed': 238,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1079] = {'shot_num': 1079, 'shot_length': 165,
                     'ICspeed': 2000, 'IRspeed': 1350,
                     'ORspeed': 265, 'OCspeed': 265,
                     'current': 1200, 'field_delay': 125, 't_field': 35,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1080] = {'shot_num': 1080, 'shot_length': 160,
                     'ICspeed': 800, 'IRspeed': 440,
                     'ORspeed': 106, 'OCspeed': 106,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1084] = {'shot_num': 1084, 'shot_length': 160,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1085] = {'shot_num': 1085, 'shot_length': 160,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1086] = {'shot_num': 1086, 'shot_length': 175,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 900, 'field_delay': 125, 't_field': 45,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1087] = {'shot_num': 1087, 'shot_length': 160,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1088] = {'shot_num': 1088, 'shot_length': 160,
                     'ICspeed': 800, 'IRspeed': 800,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1089] = {'shot_num': 1089, 'shot_length': 160,
                     'ICspeed': 800, 'IRspeed': 800,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1090] = {'shot_num': 1090, 'shot_length': 145,
                     'ICspeed': 800, 'IRspeed': 800,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1600, 'field_delay': 125, 't_field': 15,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1091] = {'shot_num': 1091, 'shot_length': 145,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1600, 'field_delay': 125, 't_field': 15,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1093] = {'shot_num': 1093, 'shot_length': 175,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 900, 'field_delay': 125, 't_field': 45,
                     'udv_delay': 105,
                     'channels': [3, 4],
                     'As': [20.3, 20.3],
                     'Bs': [90, 135],
                     'offsets': [0.41, 0.53],
                     'ports': [7, 3]}


shot_params[1094] = {'shot_num': 1094, 'shot_length': 180,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [3, 4],
                     'As': [20.3, 20.3],
                     'Bs': [90, 135],
                     'offsets': [0.41, 0.53],
                     'ports': [7, 3]}


shot_params[1095] = {'shot_num': 1095, 'shot_length': 175,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 900, 'field_delay': 125, 't_field': 45,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1098] = {'shot_num': 1098, 'shot_length': 145,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1600, 'field_delay': 125, 't_field': 15,
                     'udv_delay': 105,
                     'channels': [3, 4],
                     'As': [20.3, 20.3],
                     'Bs': [90, 135],
                     'offsets': [0.41, 0.53],
                     'ports': [7, 3]}


shot_params[1099] = {'shot_num': 1099, 'shot_length': 145,
                     'ICspeed': 600, 'IRspeed': 600,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1600, 'field_delay': 125, 't_field': 15,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1100] = {'shot_num': 1100, 'shot_length': 145,
                     'ICspeed': 800, 'IRspeed': 800,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1600, 'field_delay': 125, 't_field': 15,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1101] = {'shot_num': 1101, 'shot_length': 160,
                     'ICspeed': 800, 'IRspeed': 800,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1102] = {'shot_num': 1102, 'shot_length': 160,
                     'ICspeed': 600, 'IRspeed': 600,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1103] = {'shot_num': 1103, 'shot_length': 160,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1104] = {'shot_num': 1104, 'shot_length': 175,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 900, 'field_delay': 125, 't_field': 45,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1105] = {'shot_num': 1105, 'shot_length': 175,
                     'ICspeed': 600, 'IRspeed': 600,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 900, 'field_delay': 125, 't_field': 45,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1106] = {'shot_num': 1106, 'shot_length': 175,
                     'ICspeed': 800, 'IRspeed': 800,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 900, 'field_delay': 125, 't_field': 45,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1107] = {'shot_num': 1107, 'shot_length': 160,
                     'ICspeed': 212, 'IRspeed': 212,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1108] = {'shot_num': 1108, 'shot_length': 160,
                     'ICspeed': 212, 'IRspeed': 212,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1110] = {'shot_num': 1110, 'shot_length': 160,
                     'ICspeed': 2000, 'IRspeed': 1350,
                     'ORspeed': 265, 'OCspeed': 265,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1112] = {'shot_num': 1112, 'shot_length': 155,
                     'ICspeed': 2000, 'IRspeed': 1350,
                     'ORspeed': 265, 'OCspeed': 265,
                     'current': 1400, 'field_delay': 125, 't_field': 25,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1113] = {'shot_num': 1113, 'shot_length': 148,
                     'ICspeed': 2000, 'IRspeed': 1350,
                     'ORspeed': 265, 'OCspeed': 265,
                     'current': 1600, 'field_delay': 125, 't_field': 18,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1114] = {'shot_num': 1114, 'shot_length': 160,
                     'ICspeed': 2200, 'IRspeed': 1485,
                     'ORspeed': 291.5, 'OCspeed': 291.5,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1115] = {'shot_num': 1115, 'shot_length': 160,
                     'ICspeed': 800, 'IRspeed': 440,
                     'ORspeed': 106, 'OCspeed': 106,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}

shot_params[1116] = {'shot_num': 1116, 'shot_length': 170,
                     'ICspeed': 800, 'IRspeed': 440,
                     'ORspeed': 106, 'OCspeed': 106,
                     'current': 1000, 'field_delay': 125, 't_field': 40,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1117] = {'shot_num': 1117, 'shot_length': 170,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 1000, 'field_delay': 125, 't_field': 40,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1118] = {'shot_num': 1118, 'shot_length': 160,
                     'ICspeed': 1600, 'IRspeed': 880,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1119] = {'shot_num': 1119, 'shot_length': 160,
                     'ICspeed': 2000, 'IRspeed': 1350,
                     'ORspeed': 265, 'OCspeed': 265,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1121] = {'shot_num': 1121, 'shot_length': 190,
                     'ICspeed': 400, 'IRspeed': 220,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 100, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1122] = {'shot_num': 1122, 'shot_length': 190,
                     'ICspeed': 400, 'IRspeed': 220,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 200, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1123] = {'shot_num': 1123, 'shot_length': 190,
                     'ICspeed': 400, 'IRspeed': 220,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 300, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1124] = {'shot_num': 1124, 'shot_length': 190,
                     'ICspeed': 400, 'IRspeed': 220,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 400, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1125] = {'shot_num': 1125, 'shot_length': 190,
                     'ICspeed': 400, 'IRspeed': 220,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 50, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1126] = {'shot_num': 1126, 'shot_length': 190,
                     'ICspeed': 400, 'IRspeed': 220,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 250, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1127] = {'shot_num': 1127, 'shot_length': 160, 'trouble_flag': 1,
                     'ICspeed': 1600, 'IRspeed': 1080,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1128] = {'shot_num': 1128, 'shot_length': 160,
                     'ICspeed': 1600, 'IRspeed': 1200,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1129] = {'shot_num': 1129, 'shot_length': 160,
                     'ICspeed': 2400, 'IRspeed': 1620,
                     'ORspeed': 318, 'OCspeed': 318,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1130] = {'shot_num': 1130, 'shot_length': 160,
                     'ICspeed': 1600, 'IRspeed': 1150,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1132] = {'shot_num': 1132, 'shot_length': 180,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 600, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 180],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 11],
                     'stick_channel': 5,
                     'stick_radius': 13.6}


shot_params[1133] = {'shot_num': 1133, 'shot_length': 180,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 600, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 180],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 11],
                     'stick_channel': 5,
                     'stick_radius': 13.6}


shot_params[1134] = {'shot_num': 1134, 'shot_length': 180,
                     'ICspeed': -400, 'IRspeed': -400,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 600, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 180],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 11],
                     'stick_channel': 5,
                     'stick_radius': 13.6}


shot_params[1135] = {'shot_num': 1135, 'shot_length': 180,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 300, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 180],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 11],
                     'stick_channel': 5,
                     'stick_radius': 13.6}


shot_params[1136] = {'shot_num': 1136, 'shot_length': 160,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 180],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 11],
                     'stick_channel': 5,
                     'stick_radius': 13.6}


shot_params[1137] = {'shot_num': 1137, 'shot_length': 180,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 600, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 180],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 11],
                     'stick_channel': 5,
                     'stick_radius': 12.1}


shot_params[1138] = {'shot_num': 1138, 'shot_length': 180,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 600, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1139] = {'shot_num': 1139, 'shot_length': 180,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1140] = {'shot_num': 1140, 'shot_length': 310,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'supershot_flag': 1, 'current': [200, 400, 600],
                     'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1141] = {'shot_num': 1141, 'shot_length': 170,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 1000, 'field_delay': 125, 't_field': 40,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1142] = {'shot_num': 1142, 'shot_length': 160,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1144] = {'shot_num': 1144, 'shot_length': 150,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 1400, 'field_delay': 125, 't_field': 20,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1145] = {'shot_num': 1145, 'shot_length': 145,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 1600, 'field_delay': 125, 't_field': 15,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1146] = {'shot_num': 1146, 'shot_length': 180,
                     'ICspeed': 1600, 'IRspeed': 880,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1147] = {'shot_num': 1147, 'shot_length': 310,
                     'ICspeed': 1600, 'IRspeed': 880,
                     'ORspeed': 212, 'OCspeed': 212,
                     'supershot_flag': 1, 'current': [200, 400, 600],
                     'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1148] = {'shot_num': 1148, 'shot_length': 170,
                     'ICspeed': 1600, 'IRspeed': 880,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 1000, 'field_delay': 125, 't_field': 40,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1149] = {'shot_num': 1149, 'shot_length': 160,
                     'ICspeed': 1600, 'IRspeed': 880,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1150] = {'shot_num': 1150, 'shot_length': 150,
                     'ICspeed': 1600, 'IRspeed': 880,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 1400, 'field_delay': 125, 't_field': 20,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1151] = {'shot_num': 1151, 'shot_length': 145,
                     'ICspeed': 1600, 'IRspeed': 880,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 1500, 'field_delay': 125, 't_field': 15,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1152] = {'shot_num': 1152, 'shot_length': 180,
                     'ICspeed': 2000, 'IRspeed': 1100,
                     'ORspeed': 265, 'OCspeed': 265,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1153] = {'shot_num': 1153, 'shot_length': 310,
                     'ICspeed': 2000, 'IRspeed': 1100,
                     'ORspeed': 265, 'OCspeed': 265,
                     'supershot_flag': 1, 'current': [200, 400, 600],
                     'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1154] = {'shot_num': 1154, 'shot_length': 170,
                     'ICspeed': 2000, 'IRspeed': 1100,
                     'ORspeed': 265, 'OCspeed': 265,
                     'current': 1000, 'field_delay': 125, 't_field': 40,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}



shot_params[1155] = {'shot_num': 1155, 'shot_length': 160,
                     'ICspeed': 2000, 'IRspeed': 1100,
                     'ORspeed': 265, 'OCspeed': 265,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1156] = {'shot_num': 1156, 'shot_length': 150,
                     'ICspeed': 2000, 'IRspeed': 1100,
                     'ORspeed': 265, 'OCspeed': 265,
                     'current': 1400, 'field_delay': 125, 't_field': 20,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1157] = {'shot_num': 1157, 'shot_length': 145,
                     'ICspeed': 2000, 'IRspeed': 1100,
                     'ORspeed': 265, 'OCspeed': 265,
                     'current': 1600, 'field_delay': 125, 't_field': 15,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1158] = {'shot_num': 1158, 'shot_length': 180,
                     'ICspeed': 2000, 'IRspeed': 1100,
                     'ORspeed': 265, 'OCspeed': 265,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1161] = {'shot_num': 1161, 'shot_length': 180,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1163] = {'shot_num': 1163, 'shot_length': 180, 'trouble_flag': 1,
                     'ICspeed': 2400, 'IRspeed': 1320,
                     'ORspeed': 318, 'OCspeed': 318,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1164] = {'shot_num': 1164, 'shot_length': 310,
                     'ICspeed': 2400, 'IRspeed': 1320,
                     'ORspeed': 318, 'OCspeed': 318,
                     'supershot_flag': 1, 'current': [200, 400, 600],
                     'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1165] = {'shot_num': 1165, 'shot_length': 180,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1166] = {'shot_num': 1166, 'shot_length': 1000,
                     'ICspeed': 200, 'IRspeed': 200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 120,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 180],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 8],
                     'stick_channel': 5,
                     'stick_radius': 15.0}


shot_params[1167] = {'shot_num': 1167, 'shot_length': 1000,
                     'ICspeed': -200, 'IRspeed': -200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 120,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 180],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 8],
                     'stick_channel': 5,
                     'stick_radius': 15.0}


shot_params[1168] = {'shot_num': 1168, 'shot_length': 190,
                     'ICspeed': 200, 'IRspeed': 200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 400, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 180],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 8],
                     'stick_channel': 5,
                     'stick_radius': 15.0}


shot_params[1169] = {'shot_num': 1169, 'shot_length': 170,
                     'ICspeed': 200, 'IRspeed': 200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1000, 'field_delay': 125, 't_field': 40,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 180],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 8],
                     'stick_channel': 5,
                     'stick_radius': 15.0}


shot_params[1170] = {'shot_num': 1170, 'shot_length': 1000,
                     'ICspeed': -200, 'IRspeed': -200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 120,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 8],
                     'stick_channel': 5,
                     'stick_radius': 15.0}


shot_params[1171] = {'shot_num': 1171, 'shot_length': 1000,
                     'ICspeed': 200, 'IRspeed': 200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 120,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 8],
                     'stick_channel': 5,
                     'stick_radius': 15.0}


shot_params[1172] = {'shot_num': 1172, 'shot_length': 190,
                     'ICspeed': 200, 'IRspeed': 200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 400, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 8],
                     'stick_channel': 5,
                     'stick_radius': 15.0}


shot_params[1173] = {'shot_num': 1173, 'shot_length': 170,
                     'ICspeed': 200, 'IRspeed': 200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1000, 'field_delay': 125, 't_field': 40,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 8],
                     'stick_channel': 5,
                     'stick_radius': 15.0}


shot_params[1174] = {'shot_num': 1174, 'shot_length': 180,
                     'ICspeed': 200, 'IRspeed': 200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 700, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 8],
                     'stick_channel': 5,
                     'stick_radius': 15.0}


shot_params[1175] = {'shot_num': 1175, 'shot_length': 180,
                     'ICspeed': 200, 'IRspeed': 200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 700, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 8],
                     'stick_channel': 5,
                     'stick_radius': 15.0}


shot_params[1176] = {'shot_num': 1176, 'shot_length': 190,
                     'ICspeed': 200, 'IRspeed': 200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 400, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 8],
                     'stick_channel': 5,
                     'stick_radius': 15.0}


shot_params[1177] = {'shot_num': 1177, 'shot_length': 1000,
                     'ICspeed': 200, 'IRspeed': 200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 120,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 8],
                     'stick_channel': 5,
                     'stick_radius': 11.0}


shot_params[1178] = {'shot_num': 1178, 'shot_length': 1000,
                     'ICspeed': -200, 'IRspeed': -200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 120,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 8],
                     'stick_channel': 5,
                     'stick_radius': 11.0}


shot_params[1179] = {'shot_num': 1179, 'shot_length': 190,
                     'ICspeed': 200, 'IRspeed': 200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 400, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 8],
                     'stick_channel': 5,
                     'stick_radius': 11.0}


shot_params[1180] = {'shot_num': 1180, 'shot_length': 180,
                     'ICspeed': 200, 'IRspeed': 200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 700, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 8],
                     'stick_channel': 5,
                     'stick_radius': 11.0}


shot_params[1181] = {'shot_num': 1181, 'shot_length': 170,
                     'ICspeed': 200, 'IRspeed': 200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1000, 'field_delay': 125, 't_field': 40,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 8],
                     'stick_channel': 5,
                     'stick_radius': 11.0}


shot_params[1182] = {'shot_num': 1182, 'shot_length': 1000,
                     'ICspeed': -200, 'IRspeed': -200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 120,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 8],
                     'stick_channel': 5,
                     'stick_radius': 13.0}


shot_params[1183] = {'shot_num': 1183, 'shot_length': 1000,
                     'ICspeed': 200, 'IRspeed': 200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 120,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 8],
                     'stick_channel': 5,
                     'stick_radius': 13.0}


shot_params[1184] = {'shot_num': 1184, 'shot_length': 190,
                     'ICspeed': 200, 'IRspeed': 200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 400, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 8],
                     'stick_channel': 5,
                     'stick_radius': 13.0}


shot_params[1185] = {'shot_num': 1185, 'shot_length': 180,
                     'ICspeed': 200, 'IRspeed': 200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 700, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 8],
                     'stick_channel': 5,
                     'stick_radius': 13.0}


shot_params[1186] = {'shot_num': 1186, 'shot_length': 170,
                     'ICspeed': 200, 'IRspeed': 200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1000, 'field_delay': 125, 't_field': 40,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 90],
                     'Bs': [-90, 90, 90, 135, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0],
                     'ports': [5, 6, 7, 3, 8],
                     'stick_channel': 5,
                     'stick_radius': 13.0}


shot_params[1187] = {'shot_num': 1187, 'shot_length': 370, 'trouble_flag': 1,
                     'ICspeed': 25, 'IRspeed': 25,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 500, 'field_delay': 125, 't_field': 160,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1188] = {'shot_num': 1188, 'shot_length': 370,
                     'ICspeed': 10, 'IRspeed': 10,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 400, 'field_delay': 125, 't_field': 240,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1189] = {'shot_num': 1189, 'shot_length': 370,
                     'ICspeed': 5, 'IRspeed': 5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 400, 'field_delay': 125, 't_field': 240,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1190] = {'shot_num': 1190, 'shot_length': 550,
                     'ICspeed': 3, 'IRspeed': 3,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 300, 'field_delay': 125, 't_field': 420,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1191] = {'shot_num': 1191, 'shot_length': 1330,
                     'ICspeed': 3, 'IRspeed': 3,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 50, 'field_delay': 125, 't_field': 1200,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1192] = {'shot_num': 1192, 'shot_length': 1330,
                     'ICspeed': 3, 'IRspeed': 3,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 100, 'field_delay': 125, 't_field': 1200,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1193] = {'shot_num': 1193, 'shot_length': 3730,
                     'ICspeed': 1, 'IRspeed': 1,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 100, 'field_delay': 125, 't_field': 3600,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1194] = {'shot_num': 1194, 'shot_length': 3730,
                     'ICspeed': 1, 'IRspeed': 1,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 30, 'field_delay': 125, 't_field': 3600,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1195] = {'shot_num': 1195, 'shot_length': 3600,
                     'ICspeed': 1, 'IRspeed': 1,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1196] = {'shot_num': 1196, 'shot_length': 3600,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1197] = {'shot_num': 1197, 'shot_length': 5530, 'trouble_flag': 1,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 50, 'field_delay': 125, 't_field': 5400,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1198] = {'shot_num': 1198, 'shot_length': 5530, 'trouble_flag': 1,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 42, 'field_delay': 125, 't_field': 5400,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1199] = {'shot_num': 1199, 'shot_length': 3730,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 25, 'field_delay': 125, 't_field': 3600,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1200] = {'shot_num': 1200, 'shot_length': 3730,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 250, 'field_delay': 125, 't_field': 3600,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1201] = {'shot_num': 1201, 'shot_length': 190,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 600, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}

shot_params[1202] = {'shot_num': 1202, 'shot_length': 170,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1000, 'field_delay': 125, 't_field': 40,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1203] = {'shot_num': 1203, 'shot_length': 220,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 500, 'field_delay': 125, 't_field': 90,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1204] = {'shot_num': 1204, 'shot_length': 280,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 500, 'field_delay': 125, 't_field': 150,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1205] = {'shot_num': 1205, 'shot_length': 160,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1206] = {'shot_num': 1206, 'shot_length': 3730,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 100, 'field_delay': 125, 't_field': 3600,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}

shot_params[1207] = {'shot_num': 1207, 'shot_length': 3730,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 60, 'field_delay': 125, 't_field': 3600,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1208] = {'shot_num': 1208, 'shot_length': 3730,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 80, 'field_delay': 125, 't_field': 3600,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1209] = {'shot_num': 1209, 'shot_length': 3730,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 150, 'field_delay': 125, 't_field': 3600,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1210] = {'shot_num': 1210, 'shot_length': 3730,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 200, 'field_delay': 125, 't_field': 3600,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1211] = {'shot_num': 1211, 'shot_length': 700,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 300, 'field_delay': 125, 't_field': 570,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1212] = {'shot_num': 1212, 'shot_length': 700,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 350, 'field_delay': 125, 't_field': 400,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1213] = {'shot_num': 1213, 'shot_length': 500,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 400, 'field_delay': 125, 't_field': 270,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1214] = {'shot_num': 1214, 'shot_length': 800,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 300, 'field_delay': 125, 't_field': 675,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1215] = {'shot_num': 1215, 'shot_length': 3730,
                     'ICspeed': 1, 'IRspeed': 1,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 250, 'field_delay': 125, 't_field': 3600,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1216] = {'shot_num': 1216, 'shot_length': 3730,
                     'ICspeed': 1, 'IRspeed': 1,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 60, 'field_delay': 125, 't_field': 3600,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1217] = {'shot_num': 1217, 'shot_length': 3730, 'trouble_flag': 1,
                     'ICspeed': 1, 'IRspeed': 1,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 45, 'field_delay': 125, 't_field': 3600,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1218] = {'shot_num': 1218, 'shot_length': 3730, 'trouble_flag': 1,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 40, 'field_delay': 125, 't_field': 3600,
                     'udv_delay': 145,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1219] = {'shot_num': 1219, 'shot_length': 3730,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 32, 'field_delay': 125, 't_field': 3600,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1220] = {'shot_num': 1220, 'shot_length': 145,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1600, 'field_delay': 125, 't_field': 15,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1221] = {'shot_num': 1221, 'shot_length': 3730,
                     'ICspeed': 1, 'IRspeed': 1,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 45, 'field_delay': 125, 't_field': 3600,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1222] = {'shot_num': 1222, 'shot_length': 1330,
                     'ICspeed': 3, 'IRspeed': 3,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 80, 'field_delay': 125, 't_field': 1200,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 135],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1223] = {'shot_num': 1223, 'shot_length': 3730,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 240, 'field_delay': 125, 't_field': 3600,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1224] = {'shot_num': 1224, 'shot_length': 3730,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 100, 'field_delay': 125, 't_field': 3600,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1225] = {'shot_num': 1225, 'shot_length': 3730,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 250, 'field_delay': 125, 't_field': 3600,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1226] = {'shot_num': 1226, 'shot_length': 3730,
                     'ICspeed': 0.5, 'IRspeed': 0.5,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 60, 'field_delay': 125, 't_field': 3600,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1227] = {'shot_num': 1227, 'shot_length': 5530,
                     'ICspeed': 0.25, 'IRspeed': 0.25,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 30, 'field_delay': 125, 't_field': 5400,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1228] = {'shot_num': 1228, 'shot_length': 5530,
                     'ICspeed': 0.25, 'IRspeed': 0.25,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 65, 'field_delay': 125, 't_field': 5400,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1229] = {'shot_num': 1229, 'shot_length': 5530,
                     'ICspeed': 0.25, 'IRspeed': 0.25,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 250, 'field_delay': 125, 't_field': 5400,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1230] = {'shot_num': 1230, 'shot_length': 5530,
                     'ICspeed': 0.25, 'IRspeed': 0.25,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 20, 'field_delay': 125, 't_field': 5400,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1231] = {'shot_num': 1231, 'shot_length': 5530,
                     'ICspeed': 0.25, 'IRspeed': 0.25,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 150, 'field_delay': 125, 't_field': 5400,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 0],
                     'Bs': [-90, 90, 90, 90, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0.0],
                     'ports': [5, 6, 7, 3, 8]}


shot_params[1232] = {'shot_num': 1232, 'shot_length': 5530,
                     'ICspeed': 0.25, 'IRspeed': 0.25,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 200, 'field_delay': 125, 't_field': 5400,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 0],
                     'Bs': [-90, 90, 90, 90, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0.0],
                     'ports': [5, 6, 7, 3, 8]}


shot_params[1233] = {'shot_num': 1233, 'shot_length': 5530,
                     'ICspeed': 0.25, 'IRspeed': 0.25,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 100, 'field_delay': 125, 't_field': 5400,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 0],
                     'Bs': [-90, 90, 90, 90, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0.0],
                     'ports': [5, 6, 7, 3, 8]}


shot_params[1234] = {'shot_num': 1234, 'shot_length': 1000, 'trouble_flag': 1,
                     'ICspeed': 0.25, 'IRspeed': 0.25,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 290, 'field_delay': 125, 't_field': 875,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 0],
                     'Bs': [-90, 90, 90, 90, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0.0],
                     'ports': [5, 6, 7, 3, 8]}


shot_params[1235] = {'shot_num': 1235, 'shot_length': 5530,
                     'ICspeed': 0.25, 'IRspeed': 0.25,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 280, 'field_delay': 125, 't_field': 5400,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 0],
                     'Bs': [-90, 90, 90, 90, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0.0],
                     'ports': [5, 6, 7, 3, 8]}


shot_params[1236] = {'shot_num': 1236, 'shot_length': 180,
                     'ICspeed': 200, 'IRspeed': 200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 0],
                     'Bs': [-90, 90, 90, 90, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0.0],
                     'ports': [5, 6, 7, 3, 8]}


shot_params[1237] = {'shot_num': 1237, 'shot_length': 180,
                     'ICspeed': 200, 'IRspeed': 200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 5],
                     'As': [0.75, 20.3, 0],
                     'Bs': [-90, 90, 0],
                     'offsets': [1.19, 0.72, 0.0],
                     'ports': [5, 6, 8]}


shot_params[1238] = {'shot_num': 1238, 'shot_length': 180,
                     'ICspeed': -200, 'IRspeed': -200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 0],
                     'Bs': [-90, 90, 90, 90, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0.0],
                     'ports': [5, 6, 7, 3, 8]}


shot_params[1239] = {'shot_num': 1239, 'shot_length': 190,
                     'ICspeed': -200, 'IRspeed': -200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 300, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 0],
                     'Bs': [-90, 90, 90, 90, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0.0],
                     'ports': [5, 6, 7, 3, 8]}


shot_params[1240] = {'shot_num': 1240, 'shot_length': 190,
                     'ICspeed': 200, 'IRspeed': 200,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 300, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [0.75, 20.3, 20.3, 20.3, 0],
                     'Bs': [-90, 90, 90, 90, 0],
                     'offsets': [1.19, 0.72, 0.41, 0.53, 0.0],
                     'ports': [5, 6, 7, 3, 8]}


shot_params[1241] = {'shot_num': 1241, 'shot_length': 160,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1242] = {'shot_num': 1242, 'shot_length': 160, 'trouble_flag': 1,
                     'ICspeed': 500, 'IRspeed': 220,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1243] = {'shot_num': 1243, 'shot_length': 160,
                     'ICspeed': 1600, 'IRspeed': 880,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1247] = {'shot_num': 1247, 'shot_length': 360,
                     'ICspeed': 110, 'IRspeed': 110,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1248] = {'shot_num': 1248, 'shot_length': 490,
                     'ICspeed': 110, 'IRspeed': 110,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 200, 'field_delay': 125, 't_field': 360,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1249] = {'shot_num': 1249, 'shot_length': 400,
                     'ICspeed': 110, 'IRspeed': 110,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 400, 'field_delay': 125, 't_field': 270,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1250] = {'shot_num': 1250, 'shot_length': 1800,
                     'ICspeed': 110, 'IRspeed': 110,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 1300,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1251] = {'shot_num': 1251, 'shot_length': 1800,
                     'ICspeed': 110, 'IRspeed': 110,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1252] = {'shot_num': 1252, 'shot_length': 900,
                     'ICspeed': 110, 'IRspeed': 110,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 400, 'field_delay': 600, 't_field': 300,
                     'udv_delay': 400,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1253] = {'shot_num': 1253, 'shot_length': 680,
                     'ICspeed': 110, 'IRspeed': 110,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 600, 'field_delay': 600, 't_field': 80,
                     'udv_delay': 200,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1254] = {'shot_num': 1254, 'shot_length': 720,
                     'ICspeed': 120, 'IRspeed': 120,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 600, 'field_delay': 600, 't_field': 120,
                     'udv_delay': 240,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1255] = {'shot_num': 1255, 'shot_length': 430,
                     'ICspeed': 120, 'IRspeed': 120,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 800, 'field_delay': 360, 't_field': 70,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1256] = {'shot_num': 1256, 'shot_length': 405,
                     'ICspeed': 120, 'IRspeed': 120,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 1000, 'field_delay': 360, 't_field': 45,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1257] = {'shot_num': 1257, 'shot_length': 383,
                     'ICspeed': 120, 'IRspeed': 120,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 1400, 'field_delay': 360, 't_field': 23,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1258] = {'shot_num': 1258, 'shot_length': 240,
                     'ICspeed': 170, 'IRspeed': 170,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1259] = {'shot_num': 1259, 'shot_length': 120,
                     'ICspeed': 220, 'IRspeed': 220,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1260] = {'shot_num': 1260, 'shot_length': 120,
                     'ICspeed': 250, 'IRspeed': 250,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1261] = {'shot_num': 1261, 'shot_length': 120,
                     'ICspeed': 315, 'IRspeed': 315,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 60,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1262] = {'shot_num': 1262, 'shot_length': 120,
                     'ICspeed': 365, 'IRspeed': 365,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 60,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1263] = {'shot_num': 1263, 'shot_length': 120,
                     'ICspeed': 335, 'IRspeed': 335,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 60,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1264] = {'shot_num': 1264, 'shot_length': 190,
                     'ICspeed': 335, 'IRspeed': 335,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 200, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 115,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1265] = {'shot_num': 1265, 'shot_length': 190,
                     'ICspeed': 335, 'IRspeed': 335,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 400, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 115,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1266] = {'shot_num': 1266, 'shot_length': 190,
                     'ICspeed': 335, 'IRspeed': 335,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 600, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 115,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1267] = {'shot_num': 1267, 'shot_length': 190,
                     'ICspeed': 335, 'IRspeed': 335,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 800, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 115,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1268] = {'shot_num': 1268, 'shot_length': 175,
                     'ICspeed': 335, 'IRspeed': 335,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 1000, 'field_delay': 125, 't_field': 45,
                     'udv_delay': 115,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1269] = {'shot_num': 1269, 'shot_length': 160,
                     'ICspeed': 335, 'IRspeed': 335,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 115,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1270] = {'shot_num': 1270, 'shot_length': 155,
                     'ICspeed': 335, 'IRspeed': 335,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 1400, 'field_delay': 125, 't_field': 25,
                     'udv_delay': 115,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1271] = {'shot_num': 1271, 'shot_length': 150,
                     'ICspeed': 335, 'IRspeed': 335,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 1600, 'field_delay': 125, 't_field': 20,
                     'udv_delay': 115,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1272] = {'shot_num': 1272, 'shot_length': 190,
                     'ICspeed': 335, 'IRspeed': 335,
                     'ORspeed': 100, 'OCspeed': 100,
                     'current': 700, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 115,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1273] = {'shot_num': 1273, 'shot_length': 150,
                     'ICspeed': 165, 'IRspeed': 165,
                     'ORspeed': 50, 'OCspeed': 50,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1274] = {'shot_num': 1274, 'shot_length': 150,
                     'ICspeed': 170, 'IRspeed': 170,
                     'ORspeed': 50, 'OCspeed': 50,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1275] = {'shot_num': 1275, 'shot_length': 220,
                     'ICspeed': 170, 'IRspeed': 170,
                     'ORspeed': 50, 'OCspeed': 50,
                     'current': 400, 'field_delay': 155, 't_field': 60,
                     'udv_delay': 145,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1276] = {'shot_num': 1276, 'shot_length': 220,
                     'ICspeed': 170, 'IRspeed': 170,
                     'ORspeed': 50, 'OCspeed': 50,
                     'current': 600, 'field_delay': 155, 't_field': 60,
                     'udv_delay': 145,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1277] = {'shot_num': 1277, 'shot_length': 220,
                     'ICspeed': 170, 'IRspeed': 170,
                     'ORspeed': 50, 'OCspeed': 50,
                     'current': 800, 'field_delay': 155, 't_field': 60,
                     'udv_delay': 145,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1278] = {'shot_num': 1278, 'shot_length': 180,
                     'ICspeed': 170, 'IRspeed': 170,
                     'ORspeed': 50, 'OCspeed': 50,
                     'current': 1600, 'field_delay': 155, 't_field': 20,
                     'udv_delay': 145,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1279] = {'shot_num': 1279, 'shot_length': 150,
                     'ICspeed': 520, 'IRspeed': 520,
                     'ORspeed': 150, 'OCspeed': 150,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1280] = {'shot_num': 1280, 'shot_length': 190,
                     'ICspeed': 520, 'IRspeed': 520,
                     'ORspeed': 150, 'OCspeed': 150,
                     'current': 800, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 115,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1281] = {'shot_num': 1281, 'shot_length': 175,
                     'ICspeed': 520, 'IRspeed': 520,
                     'ORspeed': 150, 'OCspeed': 150,
                     'current': 1000, 'field_delay': 125, 't_field': 45,
                     'udv_delay': 115,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1282] = {'shot_num': 1282, 'shot_length': 150,
                     'ICspeed': 520, 'IRspeed': 520,
                     'ORspeed': 150, 'OCspeed': 150,
                     'current': 1600, 'field_delay': 125, 't_field': 20,
                     'udv_delay': 115,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1283] = {'shot_num': 1283, 'shot_length': 150,
                     'ICspeed': 165, 'IRspeed': 165,
                     'ORspeed': 150, 'OCspeed': 150,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1284] = {'shot_num': 1284, 'shot_length': 150,
                     'ICspeed': 710, 'IRspeed': 710,
                     'ORspeed': 200, 'OCspeed': 200,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1285] = {'shot_num': 1285, 'shot_length': 150,
                     'ICspeed': 670, 'IRspeed': 670,
                     'ORspeed': 200, 'OCspeed': 200,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1286] = {'shot_num': 1286, 'shot_length': 175,
                     'ICspeed': 670, 'IRspeed': 670,
                     'ORspeed': 200, 'OCspeed': 200,
                     'current': 1000, 'field_delay': 125, 't_field': 45,
                     'udv_delay': 115,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1287] = {'shot_num': 1287, 'shot_length': 160,
                     'ICspeed': 670, 'IRspeed': 670,
                     'ORspeed': 200, 'OCspeed': 200,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 115,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1288] = {'shot_num': 1288, 'shot_length': 150,
                     'ICspeed': 670, 'IRspeed': 670,
                     'ORspeed': 200, 'OCspeed': 200,
                     'current': 1600, 'field_delay': 125, 't_field': 20,
                     'udv_delay': 115,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1289] = {'shot_num': 1289, 'shot_length': 1800,
                     'ICspeed': 210, 'IRspeed': 210,
                     'ORspeed': 200, 'OCspeed': 200,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 0,
                     'channels': [2],
                     'As': [20.3],
                     'Bs': [90],
                     'offsets': [0.72],
                     'ports': [6]}


shot_params[1290] = {'shot_num': 1290, 'shot_length': 1200,
                     'ICspeed': 210, 'IRspeed': 210,
                     'ORspeed': 200, 'OCspeed': 200,
                     'current': 250, 'field_delay': 0, 't_field': 1200,
                     'udv_delay': 0,
                     'channels': [2],
                     'As': [20.3],
                     'Bs': [90],
                     'offsets': [0.72],
                     'ports': [6]}


shot_params[1291] = {'shot_num': 1291, 'shot_length': 150,
                     'ICspeed': 1040, 'IRspeed': 1040,
                     'ORspeed': 300, 'OCspeed': 300,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 10,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1292] = {'shot_num': 1292, 'shot_length': 150, 'trouble_flag': 1,
                     'ICspeed': 1030, 'IRspeed': 1030,
                     'ORspeed': 300, 'OCspeed': 300,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1293] = {'shot_num': 1293, 'shot_length': 150,
                     'ICspeed': 1018, 'IRspeed': 1018,
                     'ORspeed': 300, 'OCspeed': 300,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1295] = {'shot_num': 1295, 'shot_length': 160, 'trouble_flag': 1,
                     'ICspeed': 2800, 'IRspeed': 371,
                     'ORspeed': 371, 'OCspeed': 371,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1296] = {'shot_num': 1296, 'shot_length': 160,
                     'ICspeed': 2800, 'IRspeed': 371,
                     'ORspeed': 371, 'OCspeed': 371,
                     'current': 800, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1297] = {'shot_num': 1297, 'shot_length': 130,
                     'ICspeed': 2800, 'IRspeed': 371,
                     'ORspeed': 371, 'OCspeed': 371,
                     'current': 1200, 'field_delay': 95, 't_field': 30,
                     'udv_delay': 75,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1298] = {'shot_num': 1298, 'shot_length': 115,
                     'ICspeed': 2800, 'IRspeed': 371,
                     'ORspeed': 371, 'OCspeed': 371,
                     'current': 1500, 'field_delay': 95, 't_field': 15,
                     'udv_delay': 75,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1299] = {'shot_num': 1299, 'shot_length': 130,
                     'ICspeed': 1200, 'IRspeed': 159,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 600, 'field_delay': 95, 't_field': 30,
                     'udv_delay': 75,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1300] = {'shot_num': 1300, 'shot_length': 130,
                     'ICspeed': 1200, 'IRspeed': 159,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 800, 'field_delay': 95, 't_field': 30,
                     'udv_delay': 75,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1301] = {'shot_num': 1301, 'shot_length': 130,
                     'ICspeed': 1200, 'IRspeed': 159,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 1000, 'field_delay': 95, 't_field': 30,
                     'udv_delay': 75,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1302] = {'shot_num': 1302, 'shot_length': 130,
                     'ICspeed': 1200, 'IRspeed': 159,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 1200, 'field_delay': 95, 't_field': 30,
                     'udv_delay': 75,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1303] = {'shot_num': 1303, 'shot_length': 115,
                     'ICspeed': 1200, 'IRspeed': 159,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 1600, 'field_delay': 95, 't_field': 15,
                     'udv_delay': 75,
                     'channels': [1, 2, 3, 4],
                     'As': [0.75, 20.3, 20.3, 20.3],
                     'Bs': [-90, 90, 90, 90],
                     'offsets': [1.19, 0.72, 0.41, 0.53],
                     'ports': [5, 6, 7, 3]}


shot_params[1304] = {'shot_num': 1304, 'shot_length': 190,
                     'ICspeed': 53, 'IRspeed': 53,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 400, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                      'ports': [6, 7, 8, 5, 10]}


shot_params[1305] = {'shot_num': 1305, 'shot_length': 210,
                     'ICspeed': 400, 'IRspeed': 220,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 90,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1306] = {'shot_num': 1306, 'shot_length': 210,
                     'ICspeed': 400, 'IRspeed': 270,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 90,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1307] = {'shot_num': 1307, 'shot_length': 210,
                     'ICspeed': -400, 'IRspeed': -270,
                     'ORspeed': -53, 'OCspeed': -53,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 90,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1308] = {'shot_num': 1308, 'shot_length': 300,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 180,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1309] = {'shot_num': 1309, 'shot_length': 300,
                     'ICspeed': -400, 'IRspeed': -400,
                     'ORspeed': -53, 'OCspeed': -53,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 180,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1310] = {'shot_num': 1310, 'shot_length': 160,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1311] = {'shot_num': 1311, 'shot_length': 70,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1200, 'field_delay': 35, 't_field': 30,
                     'udv_delay': 0,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1312] = {'shot_num': 1312, 'shot_length': 150,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 0, 'OCspeed': 0,
                     'current': 1400, 'field_delay': 125, 't_field': 20,
                     'udv_delay': 120,
                     'channels': [1, 2],
                     'As': [20.3, 20.5],
                     'Bs': [90, -90],
                     'offsets': [1.23, 1.13],
                     'ports': [6, 7]}


shot_params[1313] = {'shot_num': 1313, 'shot_length': 300,
                     'ICspeed': 400, 'IRspeed': 270,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 180,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1314] = {'shot_num': 1314, 'shot_length': 300,
                     'ICspeed': -400, 'IRspeed': -270,
                     'ORspeed': -53, 'OCspeed': -53,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 180,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1315] = {'shot_num': 1315, 'shot_length': 300,
                     'ICspeed': -400, 'IRspeed': -400,
                     'ORspeed': -53, 'OCspeed': -53,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 180,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1316] = {'shot_num': 1316, 'shot_length': 300,
                     'ICspeed': 400, 'IRspeed': 400,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 180,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1317] = {'shot_num': 1317, 'shot_length': 300,
                     'ICspeed': 800, 'IRspeed': 106,
                     'ORspeed': 106, 'OCspeed': 106,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 180,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1318] = {'shot_num': 1318, 'shot_length': 300,
                     'ICspeed': -800, 'IRspeed': -106,
                     'ORspeed': -106, 'OCspeed': -106,
                     'current': 0, 'field_delay': nan, 't_field': nan,
                     'udv_delay': 180,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1319] = {'shot_num': 1319, 'shot_length': 190,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 400, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1321] = {'shot_num': 1321, 'shot_length': 180,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1322] = {'shot_num': 1322, 'shot_length': 160, 'trouble_flag': 1,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1324] = {'shot_num': 1324, 'shot_length': 160,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1325] = {'shot_num': 1325, 'shot_length': 145,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 1600, 'field_delay': 125, 't_field': 15,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1326] = {'shot_num': 1326, 'shot_length': 190,
                     'ICspeed': 1600, 'IRspeed': 880,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 400, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1327] = {'shot_num': 1327, 'shot_length': 180,
                     'ICspeed': 1600, 'IRspeed': 880,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1328] = {'shot_num': 1328, 'shot_length': 160,
                     'ICspeed': 1600, 'IRspeed': 880,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1329] = {'shot_num': 1329, 'shot_length': 145,
                     'ICspeed': 1600, 'IRspeed': 880,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 1600, 'field_delay': 125, 't_field': 15,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1330] = {'shot_num': 1330, 'shot_length': 140, 'trouble_flag': 1,
                     'ICspeed': 2000, 'IRspeed': 1100,
                     'ORspeed': 265, 'OCspeed': 265,
                     'current': 400, 'field_delay': 125, 't_field': 10,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1331] = {'shot_num': 1331, 'shot_length': 190,
                     'ICspeed': 2000, 'IRspeed': 1100,
                     'ORspeed': 265, 'OCspeed': 265,
                     'current': 400, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1332] = {'shot_num': 1332, 'shot_length': 180,
                     'ICspeed': 2000, 'IRspeed': 1100,
                     'ORspeed': 265, 'OCspeed': 265,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1333] = {'shot_num': 1333, 'shot_length': 160,
                     'ICspeed': 2000, 'IRspeed': 1100,
                     'ORspeed': 265, 'OCspeed': 265,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1335] = {'shot_num': 1335, 'shot_length': 145, 'trouble_flag': 1,
                     'ICspeed': 2000, 'IRspeed': 1100,
                     'ORspeed': 265, 'OCspeed': 265,
                     'current': 1600, 'field_delay': 125, 't_field': 15,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1337] = {'shot_num': 1337, 'shot_length': 190,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 400, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1338] = {'shot_num': 1338, 'shot_length': 180,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1339] = {'shot_num': 1339, 'shot_length': 160,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1340] = {'shot_num': 1340, 'shot_length': 145,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 1600, 'field_delay': 125, 't_field': 15,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1342] = {'shot_num': 1342, 'shot_length': 160,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1343] = {'shot_num': 1343, 'shot_length': 160,
                     'ICspeed': 2400, 'IRspeed': 1320,
                     'ORspeed': 318, 'OCspeed': 318,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1344] = {'shot_num': 1344, 'shot_length': 180,
                     'ICspeed': 2400, 'IRspeed': 1320,
                     'ORspeed': 318, 'OCspeed': 318,
                     'current': 800, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1345] = {'shot_num': 1345, 'shot_length': 145,
                     'ICspeed': 2400, 'IRspeed': 1320,
                     'ORspeed': 318, 'OCspeed': 318,
                     'current': 1600, 'field_delay': 125, 't_field': 15,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1346] = {'shot_num': 1346, 'shot_length': 190,
                     'ICspeed': 2400, 'IRspeed': 1320,
                     'ORspeed': 318, 'OCspeed': 318,
                     'current': 400, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1347] = {'shot_num': 1347, 'shot_length': 135, 'trouble_flag': 1,
                     'ICspeed': 2400, 'IRspeed': 1320,
                     'ORspeed': 318, 'OCspeed': 318,
                     'current': 2400, 'field_delay': 125, 't_field': 5,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1348] = {'shot_num': 1348, 'shot_length': 160,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1350] = {'shot_num': 1350, 'shot_length': 160,
                     'ICspeed': 1600, 'IRspeed': 880,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1351] = {'shot_num': 1351, 'shot_length': 160,
                     'ICspeed': 2000, 'IRspeed': 1100,
                     'ORspeed': 265, 'OCspeed': 265,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1352] = {'shot_num': 1352, 'shot_length': 160,
                     'ICspeed': 2400, 'IRspeed': 1320,
                     'ORspeed': 318, 'OCspeed': 318,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1353] = {'shot_num': 1353, 'shot_length': 140, 'trouble_flag': 1,
                     'ICspeed': 2400, 'IRspeed': 1320,
                     'ORspeed': 318, 'OCspeed': 318,
                     'current': 2000, 'field_delay': 125, 't_field': 10,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1354] = {'shot_num': 1354, 'shot_length': 190,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 515, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1355] = {'shot_num': 1355, 'shot_length': 190,
                     'ICspeed': 1600, 'IRspeed': 880,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 685, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1356] = {'shot_num': 1356, 'shot_length': 175,
                     'ICspeed': 2000, 'IRspeed': 1100,
                     'ORspeed': 265, 'OCspeed': 265,
                     'current': 860, 'field_delay': 125, 't_field': 45,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1357] = {'shot_num': 1357, 'shot_length': 170,
                     'ICspeed': 2400, 'IRspeed': 1320,
                     'ORspeed': 318, 'OCspeed': 318,
                     'current': 1030, 'field_delay': 125, 't_field': 40,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1359] = {'shot_num': 1359, 'shot_length': 190,
                     'ICspeed': 400, 'IRspeed': 220,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 171, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1360] = {'shot_num': 1360, 'shot_length': 190,
                     'ICspeed': 600, 'IRspeed': 330,
                     'ORspeed': 79.5, 'OCspeed': 79.5,
                     'current': 257, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1361] = {'shot_num': 1361, 'shot_length': 190,
                     'ICspeed': 800, 'IRspeed': 440,
                     'ORspeed': 106, 'OCspeed': 106,
                     'current': 343, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1362] = {'shot_num': 1362, 'shot_length': 190,
                     'ICspeed': 1000, 'IRspeed': 550,
                     'ORspeed': 132.5, 'OCspeed': 132.5,
                     'current': 429, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1363] = {'shot_num': 1363, 'shot_length': 190,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 514, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1364] = {'shot_num': 1364, 'shot_length': 190,
                     'ICspeed': 1400, 'IRspeed': 770,
                     'ORspeed': 185.5, 'OCspeed': 185.5,
                     'current': 600, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1365] = {'shot_num': 1365, 'shot_length': 190,
                     'ICspeed': 1600, 'IRspeed': 880,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 686, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1366] = {'shot_num': 1366, 'shot_length': 180,
                     'ICspeed': 1800, 'IRspeed': 990,
                     'ORspeed': 238.5, 'OCspeed': 238.5,
                     'current': 771, 'field_delay': 125, 't_field': 50,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1367] = {'shot_num': 1367, 'shot_length': 170,
                     'ICspeed': 2000, 'IRspeed': 1100,
                     'ORspeed': 265, 'OCspeed': 265,
                     'current': 857, 'field_delay': 125, 't_field': 40,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1368] = {'shot_num': 1368, 'shot_length': 170,
                     'ICspeed': 2200, 'IRspeed': 1210,
                     'ORspeed': 291.5, 'OCspeed': 291.5,
                     'current': 943, 'field_delay': 125, 't_field': 40,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1369] = {'shot_num': 1369, 'shot_length': 170,
                     'ICspeed': 2400, 'IRspeed': 1320,
                     'ORspeed': 318, 'OCspeed': 318,
                     'current': 1029, 'field_delay': 125, 't_field': 40,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1370] = {'shot_num': 1370, 'shot_length': 160, 'trouble_flag': 1,
                     'ICspeed': 2600, 'IRspeed': 1430,
                     'ORspeed': 344.5, 'OCspeed': 344.5,
                     'current': 1114, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1371] = {'shot_num': 1371, 'shot_length': 190,
                     'ICspeed': 1600, 'IRspeed': 880,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 1200, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1372] = {'shot_num': 1372, 'shot_length': 160, 'trouble_flag': 1,
                     'ICspeed': 2800, 'IRspeed': 1540,
                     'ORspeed': 371, 'OCspeed': 371,
                     'current': 1200, 'field_delay': 125, 't_field': 30,
                     'udv_delay': 105,
                     'channels': [1, 2, 3, 4, 5],
                     'As': [20.3, 20.5, 20.0, 20.2, 20.3],
                     'Bs': [90, -90, -90, 90, 90],
                     'offsets': [1.23, 1.13, 0.15, 0.41, 0.6],
                     'ports': [6, 7, 8, 5, 10]}


shot_params[1374] = {'shot_num': 1374, 'shot_length': 190,
                     'ICspeed': 400, 'IRspeed': 220,
                     'ORspeed': 53, 'OCspeed': 53,
                     'current': 171, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [2, 3, 4, 5],
                     'As': [20.5, 20.0, 20.2, 20.3],
                     'Bs': [-90, -90, 90, 90],
                     'offsets': [1.13, 0.15, 0.41, 0.6],
                     'ports': [7, 8, 5, 6]}


shot_params[1375] = {'shot_num': 1375, 'shot_length': 190,
                     'ICspeed': 800, 'IRspeed': 440,
                     'ORspeed': 106, 'OCspeed': 106,
                     'current': 343, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [2, 3, 4, 5],
                     'As': [20.5, 20.0, 20.2, 20.3],
                     'Bs': [-90, -90, 90, 90],
                     'offsets': [1.13, 0.15, 0.41, 0.6],
                     'ports': [7, 8, 5, 6]}


shot_params[1376] = {'shot_num': 1376, 'shot_length': 190,
                     'ICspeed': 1200, 'IRspeed': 660,
                     'ORspeed': 159, 'OCspeed': 159,
                     'current': 514, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [2, 3, 4, 5],
                     'As': [20.5, 20.0, 20.2, 20.3],
                     'Bs': [-90, -90, 90, 90],
                     'offsets': [1.13, 0.15, 0.41, 0.6],
                     'ports': [7, 8, 5, 6]}


shot_params[1377] = {'shot_num': 1377, 'shot_length': 190,
                     'ICspeed': 1600, 'IRspeed': 880,
                     'ORspeed': 212, 'OCspeed': 212,
                     'current': 686, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [2, 3, 4, 5],
                     'As': [20.5, 20.0, 20.2, 20.3],
                     'Bs': [-90, -90, 90, 90],
                     'offsets': [1.13, 0.15, 0.41, 0.6],
                     'ports': [7, 8, 5, 6]}


shot_params[1378] = {'shot_num': 1378, 'shot_length': 170,
                     'ICspeed': 2000, 'IRspeed': 1100,
                     'ORspeed': 265, 'OCspeed': 265,
                     'current': 857, 'field_delay': 125, 't_field': 60,
                     'udv_delay': 105,
                     'channels': [2, 3, 4, 5],
                     'As': [20.5, 20.0, 20.2, 20.3],
                     'Bs': [-90, -90, 90, 90],
                     'offsets': [1.13, 0.15, 0.41, 0.6],
                     'ports': [7, 8, 5, 6]}


shot_params[1379] = {'shot_num': 1379, 'shot_length': 170,
                     'ICspeed': 2200, 'IRspeed': 1210,
                     'ORspeed': 291.5, 'OCspeed': 291.5,
                     'current': 943, 'field_delay': 125, 't_field': 40,
                     'udv_delay': 105,
                     'channels': [2, 3, 4, 5],
                     'As': [20.5, 20.0, 20.2, 20.3],
                     'Bs': [-90, -90, 90, 90],
                     'offsets': [1.13, 0.15, 0.41, 0.6],
                     'ports': [7, 8, 5, 6]}


shot_params[1380] = {'shot_num': 1380, 'shot_length': 170, 'trouble_flag': 1,
                     'ICspeed': 2400, 'IRspeed': 1320,
                     'ORspeed': 318, 'OCspeed': 318,
                     'current': 1029, 'field_delay': 125, 't_field': 40,
                     'udv_delay': 105,
                     'channels': [2, 3, 4, 5],
                     'As': [20.5, 20.0, 20.2, 20.3],
                     'Bs': [-90, -90, 90, 90],
                     'offsets': [1.13, 0.15, 0.41, 0.6],
                     'ports': [7, 8, 5, 6]}
