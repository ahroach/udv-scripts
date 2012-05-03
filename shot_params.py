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

from numpy import nan

shot_params = {}

shot_params[676] = {'shot_num': 676, 'shot_length': 190,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[677] = {'shot_num': 677, 'shot_length': 190,
                    'ICspeed': 400, 'IRspeed': 146,
                    'ORspeed': 40, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[678] = {'shot_num': 678, 'shot_length': 65,
                    'ICspeed': 0, 'IRspeed': 0,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 400, 'field_delay': 5, 't_field': 60,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[679] = {'shot_num': 679, 'shot_length': 190,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 400, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[681] = {'shot_num': 681, 'shot_length': 190,
                    'ICspeed': 400, 'IRspeed': 146,
                    'ORspeed': 40, 'OCspeed': 53,
                    'current': 400, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[682] = {'shot_num': 682, 'shot_length': 152,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 20,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[683] = {'shot_num': 683, 'shot_length': 155,
                    'ICspeed': 400, 'IRspeed': 146,
                    'ORspeed': 40, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 25,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[684] = {'shot_num': 684, 'shot_length': 165,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 35,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[685] = {'shot_num': 685, 'shot_length': 165,
                    'ICspeed': 400, 'IRspeed': 146,
                    'ORspeed': 40, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 35,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[686] = {'shot_num': 686, 'shot_length': 165,
                    'ICspeed': 106, 'IRspeed': 106,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1200, 'field_delay': 125, 't_field': 35,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[687] = {'shot_num': 687, 'shot_length': 165,
                    'ICspeed': 800, 'IRspeed': 292,
                    'ORspeed': 80, 'OCspeed': 106,
                    'current': 1200, 'field_delay': 125, 't_field': 35,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[688] = {'shot_num': 687, 'shot_length': 165,
                    'ICspeed': 800, 'IRspeed': 292,
                    'ORspeed': 80, 'OCspeed': 106,
                    'current': 1200, 'field_delay': 125, 't_field': 35,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[691] = {'shot_num': 691, 'shot_length': 120,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[692] = {'shot_num': 692, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[693] = {'shot_num': 693, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 400,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[694] = {'shot_num': 694, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 181,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[695] = {'shot_num': 695, 'shot_length': 120,
                    'ICspeed': -53, 'IRspeed': -53,
                    'ORspeed': -53, 'OCspeed': -53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[696] = {'shot_num': 696, 'shot_length': 60,
                    'ICspeed': -400, 'IRspeed': -400,
                    'ORspeed': -53, 'OCspeed': -53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[697] = {'shot_num': 697, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[698] = {'shot_num': 698, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[699] = {'shot_num': 699, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 210,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[700] = {'shot_num': 700, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 210,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[701] = {'shot_num': 701, 'shot_length': 190,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 400, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[702] = {'shot_num': 702, 'shot_length': 190,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 400, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[703] = {'shot_num': 703, 'shot_length': 165,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 35,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[704] = {'shot_num': 704, 'shot_length': 190,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 35,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[707] = {'shot_num': 707, 'shot_length': 190,
                    'ICspeed': 400, 'IRspeed': 400,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 400, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[708] = {'shot_num': 708, 'shot_length': 190,
                    'ICspeed': 400, 'IRspeed': 400,
                    'ORspeed': 0, 'OCspeed': 0,
                    'current': 400, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[711] = {'shot_num': 711, 'shot_length': 190,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 400, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[713] = {'shot_num': 713, 'shot_length': 180,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 800, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[714] = {'shot_num': 714, 'shot_length': 180,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 800, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 120,
                    'channels': [1],
                    'alphas': [-0.75],
                    'betas': [0],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[715] = {'shot_num': 715, 'shot_length': 190,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 400, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 120,
                    'channels': [1],
                    'alphas': [-0.75],
                    'betas': [0],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[716] = {'shot_num': 716, 'shot_length': 190,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 400, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 120,
                    'channels': [1],
                    'alphas': [-0.75],
                    'betas': [0],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[717] = {'shot_num': 717, 'shot_length': 190,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 600, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 120,
                    'channels': [1],
                    'alphas': [-0.75],
                    'betas': [0],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[718] = {'shot_num': 718, 'shot_length': 190,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 600, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 120,
                    'channels': [1],
                    'alphas': [-0.75],
                    'betas': [0],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[719] = {'shot_num': 719, 'shot_length': 190,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 600, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[720] = {'shot_num': 720, 'shot_length': 180,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 800, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 120,
                    'channels': [1],
                    'alphas': [-0.75],
                    'betas': [0],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[721] = {'shot_num': 721, 'shot_length': 180,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 800, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 120,
                    'channels': [1],
                    'alphas': [-0.75],
                    'betas': [0],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[722] = {'shot_num': 722, 'shot_length': 180,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 800, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 120,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[723] = {'shot_num': 723, 'shot_length': 170,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 120,
                    'channels': [1],
                    'alphas': [-0.75],
                    'betas': [0],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[724] = {'shot_num': 724, 'shot_length': 170,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 120,
                    'channels': [1],
                    'alphas': [-0.75],
                    'betas': [0],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[725] = {'shot_num': 725, 'shot_length': 170,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[726] = {'shot_num': 726, 'shot_length': 160,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 120,
                    'channels': [1],
                    'alphas': [-0.75],
                    'betas': [0],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[727] = {'shot_num': 727, 'shot_length': 160,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 120,
                    'channels': [1],
                    'alphas': [-0.75],
                    'betas': [0],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[728] = {'shot_num': 728, 'shot_length': 160,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[729] = {'shot_num': 729, 'shot_length': 150,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1400, 'field_delay': 125, 't_field': 20,
                    'udv_delay': 120,
                    'channels': [1],
                    'alphas': [-0.75],
                    'betas': [0],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[730] = {'shot_num': 730, 'shot_length': 150,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 1400, 'field_delay': 125, 't_field': 20,
                    'udv_delay': 120,
                    'channels': [1],
                    'alphas': [-0.75],
                    'betas': [0],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[731] = {'shot_num': 731, 'shot_length': 150,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 1400, 'field_delay': 125, 't_field': 20,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[732] = {'shot_num': 732, 'shot_length': 145,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1600, 'field_delay': 125, 't_field': 15,
                    'udv_delay': 120,
                    'channels': [1],
                    'alphas': [-0.75],
                    'betas': [0],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[733] = {'shot_num': 733, 'shot_length': 145,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 1600, 'field_delay': 125, 't_field': 15,
                    'udv_delay': 120,
                    'channels': [1],
                    'alphas': [-0.75],
                    'betas': [0],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[734] = {'shot_num': 734, 'shot_length': 145,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 1600, 'field_delay': 125, 't_field': 15,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[735] = {'shot_num': 735, 'shot_length': 240,
                    'ICspeed': -400, 'IRspeed': -200,
                    'ORspeed': -66, 'OCspeed': -53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[736] = {'shot_num': 736, 'shot_length': 240,
                    'ICspeed': -400, 'IRspeed': -53,
                    'ORspeed': -53, 'OCspeed': -53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[737] = {'shot_num': 737, 'shot_length': 240,
                    'ICspeed': -400, 'IRspeed': -400,
                    'ORspeed': -53, 'OCspeed': -53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[738] = {'shot_num': 738, 'shot_length': 240,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[739] = {'shot_num': 739, 'shot_length': 240,
                    'ICspeed': 400, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[740] = {'shot_num': 740, 'shot_length': 240,
                    'ICspeed': 400, 'IRspeed': 400,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[741] = {'shot_num': 741, 'shot_length': 60,
                    'ICspeed': 800, 'IRspeed': 400,
                    'ORspeed': 132, 'OCspeed': 106,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[742] = {'shot_num': 742, 'shot_length': 170,
                    'ICspeed': 800, 'IRspeed': 400,
                    'ORspeed': 132, 'OCspeed': 106,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[743] = {'shot_num': 743, 'shot_length': 170,
                    'ICspeed': 106, 'IRspeed': 106,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 120,
                    'channels': [1],
                    'alphas': [-0.75],
                    'betas': [0],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[744] = {'shot_num': 744, 'shot_length': 170,
                    'ICspeed': 800, 'IRspeed': 400,
                    'ORspeed': 132, 'OCspeed': 106,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 120,
                    'channels': [1],
                    'alphas': [-0.75],
                    'betas': [0],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[745] = {'shot_num': 745, 'shot_length': 170,
                    'ICspeed': 400, 'IRspeed': 146,
                    'ORspeed': 40, 'OCspeed': 53,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[763] = {'shot_num': 763, 'shot_length': 170,
                    'ICspeed': 106, 'IRspeed': 106,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 120,
                    'channels': [1],
                    'alphas': [-0.75],
                    'betas': [0],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[774] = {'shot_num': 774, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[775] = {'shot_num': 775, 'shot_length': 120,
                    'ICspeed': 106, 'IRspeed': 106,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[785] = {'shot_num': 785, 'shot_length': 70, 'trouble_flag': 1,
                    'ICspeed': 800, 'IRspeed': 400,
                    'ORspeed': 132, 'OCspeed': 106,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[787] = {'shot_num': 787, 'shot_length': 40, 'trouble_flag': 1,
                    'ICspeed': 1200, 'IRspeed': 600,
                    'ORspeed': 198, 'OCspeed': 159,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[788] = {'shot_num': 788, 'shot_length': 40, 'trouble_flag': 1,
                    'ICspeed': 1200, 'IRspeed': 600,
                    'ORspeed': 198, 'OCspeed': 159,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[813] = {'shot_num': 813, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[814] = {'shot_num': 814, 'shot_length': 40, 'trouble_flag': 1,
                    'ICspeed': 800, 'IRspeed': 400,
                    'ORspeed': 132, 'OCspeed': 106,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[815] = {'shot_num': 815, 'shot_length': 10, 'trouble_flag': 1,
                    'ICspeed': 800, 'IRspeed': 292,
                    'ORspeed': 80, 'OCspeed': 106,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[816] = {'shot_num': 816, 'shot_length': 9, 'trouble_flag': 1,
                    'ICspeed': 1200, 'IRspeed': 600,
                    'ORspeed': 198, 'OCspeed': 159,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[818] = {'shot_num': 818, 'shot_length': 40, 'trouble_flag': 1,
                    'ICspeed': 12000, 'IRspeed': 600,
                    'ORspeed': 198, 'OCspeed': 159,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[819] = {'shot_num': 819, 'shot_length': 40, 'trouble_flag': 1,
                    'ICspeed': 1200, 'IRspeed': 600,
                    'ORspeed': 198, 'OCspeed': 159,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[820] = {'shot_num': 820, 'shot_length': 120, 'trouble_flag': 1,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[821] = {'shot_num': 821, 'shot_length': 120, 'trouble_flag': 1,
                    'ICspeed': 400, 'IRspeed': 175,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[822] = {'shot_num': 822, 'shot_length': 120, 'trouble_flag': 1,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[823] = {'shot_num': 823, 'shot_length': 120, 'trouble_flag': 1,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 66, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[824] = {'shot_num': 824, 'shot_length': 120, 'trouble_flag': 1,
                    'ICspeed': 400, 'IRspeed': 175,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[825] = {'shot_num': 825, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 175,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[826] = {'shot_num': 826, 'shot_length': 120, 'trouble_flag': 1,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[827] = {'shot_num': 827, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 200,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[828] = {'shot_num': 828, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[829] = {'shot_num': 829, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 240,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[830] = {'shot_num': 830, 'shot_length': 185,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 800, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0,0],
                    'offsets': [1.19, 0.72],
                    'ports': [5,6]}


shot_params[831] = {'shot_num': 831, 'shot_length': 180,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 800, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 120,
                    'channels': [1],
                    'alphas': [-0.75],
                    'betas': [0],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[832] = {'shot_num': 832, 'shot_length': 170,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 120,
                    'channels': [1],
                    'alphas': [-0.75],
                    'betas': [0],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[833] = {'shot_num': 833, 'shot_length': 160,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 120,
                    'channels': [1],
                    'alphas': [-0.75],
                    'betas': [0],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[834] = {'shot_num': 834, 'shot_length': 150,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1400, 'field_delay': 125, 't_field': 20,
                    'udv_delay': 120,
                    'channels': [1],
                    'alphas': [-0.75],
                    'betas': [0],
                    'offsets': [1.19],
                    'ports': [5]}


shot_params[836] = {'shot_num': 836, 'shot_length': 160,
                    'ICspeed': 106, 'IRspeed': 106,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[838] = {'shot_num': 838, 'shot_length': 160, 'trouble_flag': 1,
                    'ICspeed': 800, 'IRspeed': 440,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 102.5,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[839] = {'shot_num': 839, 'shot_length': 160,
                    'ICspeed': 159, 'IRspeed': 159,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[840] = {'shot_num': 840, 'shot_length': 160,
                    'ICspeed': 1200, 'IRspeed': 660,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[841] = {'shot_num': 841, 'shot_length': 160,
                    'ICspeed': 212, 'IRspeed': 212,
                    'ORspeed': 212, 'OCspeed': 212,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[842] = {'shot_num': 842, 'shot_length': 160,
                    'ICspeed': 1600, 'IRspeed': 880,
                    'ORspeed': 212, 'OCspeed': 212,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[848] = {'shot_num': 848, 'shot_length': 120,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[849] = {'shot_num': 849, 'shot_length': 120,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 0, 'field_delay': nan, 't_field': nan,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[850] = {'shot_num': 850, 'shot_length': 160,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[851] = {'shot_num': 851, 'shot_length': 160,
                    'ICspeed': 53, 'IRspeed': 53,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[852] = {'shot_num': 852, 'shot_length': 160,
                    'ICspeed': 400, 'IRspeed': 220,
                    'ORspeed': 53, 'OCspeed': 53,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[853] = {'shot_num': 853, 'shot_length': 160,
                    'ICspeed': 106, 'IRspeed': 106,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[854] = {'shot_num': 854, 'shot_length': 160,
                    'ICspeed': 800, 'IRspeed': 440,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[855] = {'shot_num': 855, 'shot_length': 160,
                    'ICspeed': 159, 'IRspeed': 159,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[856] = {'shot_num': 856, 'shot_length': 160,
                    'ICspeed': 1200, 'IRspeed': 660,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[857] = {'shot_num': 857, 'shot_length': 160,
                    'ICspeed': 212, 'IRspeed': 212,
                    'ORspeed': 212, 'OCspeed': 212,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[858] = {'shot_num': 858, 'shot_length': 160,
                    'ICspeed': 1600, 'IRspeed': 880,
                    'ORspeed': 212, 'OCspeed': 212,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 0,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[859] = {'shot_num': 859, 'shot_length': 160,
                    'ICspeed': 239, 'IRspeed': 239,
                    'ORspeed': 239, 'OCspeed': 239,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 120,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[860] = {'shot_num': 860, 'shot_length': 160,
                    'ICspeed': 1800, 'IRspeed': 990,
                    'ORspeed': 239, 'OCspeed': 239,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 120,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[861] = {'shot_num': 861, 'shot_length': 160,
                    'ICspeed': 265, 'IRspeed': 265,
                    'ORspeed': 265, 'OCspeed': 265,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 120,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[864] = {'shot_num': 864, 'shot_length': 160,
                    'ICspeed': 265, 'IRspeed': 265,
                    'ORspeed': 265, 'OCspeed': 265,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 120,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[866] = {'shot_num': 866, 'shot_length': 160,
                    'ICspeed': 1200, 'IRspeed': 800,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 120,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[867] = {'shot_num': 867, 'shot_length': 160,
                    'ICspeed': 1600, 'IRspeed': 1080,
                    'ORspeed': 212, 'OCspeed': 212,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[876] = {'shot_num': 876, 'shot_length': 160,
                    'ICspeed': 1200, 'IRspeed': 810,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[877] = {'shot_num': 877, 'shot_length': 160,
                    'ICspeed': 212, 'IRspeed': 212,
                    'ORspeed': 212, 'OCspeed': 212,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[878] = {'shot_num': 878, 'shot_length': 160,
                    'ICspeed': 1600, 'IRspeed': 1080,
                    'ORspeed': 212, 'OCspeed': 212,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[880] = {'shot_num': 880, 'shot_length': 160,
                    'ICspeed': 1600, 'IRspeed': 940,
                    'ORspeed': 212, 'OCspeed': 212,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[884] = {'shot_num': 884, 'shot_length': 160,
                    'ICspeed': 800, 'IRspeed': 540,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}




shot_params[885] = {'shot_num': 885, 'shot_length': 160,
                    'ICspeed': 800, 'IRspeed': 540,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[886] = {'shot_num': 886, 'shot_length': 160,
                    'ICspeed': 800, 'IRspeed': 440,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1200, 'field_delay': 125, 't_field': 30,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[887] = {'shot_num': 887, 'shot_length': 190,
                    'ICspeed': 159, 'IRspeed': 159,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 600, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[888] = {'shot_num': 888, 'shot_length': 190,
                    'ICspeed': 1200, 'IRspeed': 660,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 600, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[894] = {'shot_num': 894, 'shot_length': 190,
                    'ICspeed': 800, 'IRspeed': 440,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 600, 'field_delay': 125, 't_field': 60,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}

shot_params[895] = {'shot_num': 895, 'shot_length': 190,
                    'ICspeed': 106, 'IRspeed': 106,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 800, 'field_delay': 125, 't_field': 50,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[897] = {'shot_num': 897, 'shot_length': 170,
                    'ICspeed': 106, 'IRspeed': 106,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[898] = {'shot_num': 898, 'shot_length': 170,
                    'ICspeed': 800, 'IRspeed': 440,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1000, 'field_delay': 125, 't_field': 40,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[899] = {'shot_num': 899, 'shot_length': 150,
                    'ICspeed': 106, 'IRspeed': 106,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1400, 'field_delay': 125, 't_field': 20,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[900] = {'shot_num': 900, 'shot_length': 150,
                    'ICspeed': 800, 'IRspeed': 440,
                    'ORspeed': 106, 'OCspeed': 106,
                    'current': 1400, 'field_delay': 125, 't_field': 20,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[901] = {'shot_num': 901, 'shot_length': 150,
                    'ICspeed': 159, 'IRspeed': 159,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 1400, 'field_delay': 125, 't_field': 20,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[902] = {'shot_num': 902, 'shot_length': 150,
                    'ICspeed': 1200, 'IRspeed': 660,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 1400, 'field_delay': 125, 't_field': 20,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[903] = {'shot_num': 903, 'shot_length': 145,
                    'ICspeed': 159, 'IRspeed': 159,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 1600, 'field_delay': 125, 't_field': 15,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}


shot_params[904] = {'shot_num': 904, 'shot_length': 145,
                    'ICspeed': 1200, 'IRspeed': 660,
                    'ORspeed': 159, 'OCspeed': 159,
                    'current': 1600, 'field_delay': 125, 't_field': 15,
                    'udv_delay': 105,
                    'channels': [1, 2],
                    'alphas': [-0.75, 20.3],
                    'betas': [0, 0],
                    'offsets': [1.19, 0.72],
                    'ports': [5, 6]}




