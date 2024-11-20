#входные данные по варианту
methane = 0.845993
ethane = 0.065381
propane = 0.020317
i_butane = 0
n_butane = 0.002795
neo_pentane = 0
i_pentane = 0
n_pentane = 0.000753
neo_hexane = 0
n_hexane = 0.000793
heptane = 0
nitrogen = 0.049954
carbon_dioxide = 0.009623
helium = 0.000407
hydrogen = 0
pressure = 18 
temperature = 3

ri = [
    methane, ethane, propane, i_butane, n_butane, 
    neo_pentane, i_pentane, n_pentane, neo_hexane, 
    n_hexane, heptane, nitrogen, carbon_dioxide, helium, hydrogen
]

Ki = [
    0.4619255, 0.5279209, 0.583749, 0.6406937, 0.6341423,
    0.6738577, 0.6738577, 0.6798307, 0.7175118, 0.7175118,
    0.7175118, 0.4479153, 0.4557489, 0.3589888, 0.3514916
]

Kij = [
        [1, 1, 1.007619, 1, 0.997596, 1, 1, 1.002529, 1, 0.982962, 0.982962, 1.00363, 0.995933, 1, 1.02326],
        [1, 1, 0.986893, 1, 1, 1, 1, 1, 1, 1, 1, 1.00796, 1.00851, 1, 1.02034],
        [1.007619, 0.986893, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0.997596, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1.002529, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0.982962, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.910183, 1, 1],
        [0.982962, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1.00363, 1.00796, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.982361, 0.982361, 1.03227],
        [0.995933, 1.00851, 1, 1, 1, 1, 1, 1, 1, 0.910183, 1, 0.982361, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.982361, 1, 1, 1],
        [1.02326, 1.02034, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.03227, 1, 1, 1]
    ]
a = [
    0.1538326,
    1.341953,
    -2.998583,
    -0.04831228,
    0.3757965,
    -1.589575,
    -0.05358847,
    0.88659463,
    -0.71023704,
    -1.471722,
    1.32185035,
    -0.78665925,
    0.00000000229129,
    0.1576724,
    -0.4363864,
    -0.04408159,
    -0.003433888,
    0.03205905,
    0.02487355,
    0.07332279,
    -0.001600573,
    0.6424706,
    -0.4162601,
    -0.06689957,
    0.2791795,
    -0.6966051,
    -0.002860589,
    -0.008098836,
    3.150547,
    0.007224479,
    -0.7057529,
    0.5349792,
    -0.07931491,
    -1.418465,
    -5.99905*10**(-17),
    0.1058402,
    0.03431729,
    -0.007022847,
    0.02495587,
    0.04296818,
    0.7465453,
    -0.2919613,
    7.294616,
    -9.936757,
    -0.005399808,
    -0.2432567,
    0.04987016,
    0.003733797,
    1.874951,
    0.002168144,
    -0.6587164,
    0.000205518,
    0.009776195,
    -0.02048708,
    0.01557322,
    0.006862415,
    -0.001226752,
    0.002850908
    ]
a = [
    0.1538326,
    1.341953,
    -2.998583,
    -0.04831228,
    0.3757965,
    -1.589575,
    -0.05358847,
    0.88659463,
    -0.71023704,
    -1.471722,
    1.32185035,
    -0.78665925,
    0.00000000229129,
    0.1576724,
    -0.4363864,
    -0.04408159,
    -0.003433888,
    0.03205905,
    0.02487355,
    0.07332279,
    -0.001600573,
    0.6424706,
    -0.4162601,
    -0.06689957,
    0.2791795,
    -0.6966051,
    -0.002860589,
    -0.008098836,
    3.150547,
    0.007224479,
    -0.7057529,
    0.5349792,
    -0.07931491,
    -1.418465,
    -5.99905*10**(-17),
    0.1058402,
    0.03431729,
    -0.007022847,
    0.02495587,
    0.04296818,
    0.7465453,
    -0.2919613,
    7.294616,
    -9.936757,
    -0.005399808,
    -0.2432567,
    0.04987016,
    0.003733797,
    1.874951,
    0.002168144,
    -0.6587164,
    0.000205518,
    0.009776195,
    -0.02048708,
    0.01557322,
    0.006862415,
    -0.001226752,
    0.002850908
    ]
b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9, 9]
c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1]
u = [0, 0.5, 1, 3.5, -0.5, 4.5, 0.5, 7.5, 9.5, 6, 12, 12.5, -6, 2, 3, 2, 2, 11, -0.5, 0.5, 0, 4, 6, 21, 23, 22, -1, -0.5, 7, -1, 6, 4, 1, 9, -13, 21, 8, -0.5, 0, 2, 7, 9, 22, 23, 1, 9, 3, 8, 23, 1.5, 5, -0.5, 4, 7, 3, 0, 1, 0]
k = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 2, 2, 4, 4, 0, 0, 2, 2, 2, 4, 4, 4, 4, 0, 1, 1, 2, 2, 3, 3, 4, 4, 4, 0, 0, 2, 2, 2, 4, 4, 0, 2, 2, 4, 4, 0, 2, 0, 2, 1, 2, 2, 2, 2]
g = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]
q = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1]
f = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
s = [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
w = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Gi = [
    0,
    0.0793,
    0.141239,
    0.256692,
    0.281835,
    0.332267,
    0.332267,
    0.366911,0.289731,
    0.289731,
    0.289731,
    0.027815,
    0.189065,
    0,
    0.034369
    ]
Gij = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.807653, 1, 1.95731],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.370296, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.982746, 1, 1],
    [0.807653, 0.370296, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.982746, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1.95731, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
Qi = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.69, 0, 0]
Fi = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
Ei = [
    151.3183,
    244.1667,
    298.1183,
    324.0689,
    337.6389,
    365.5999,
    365.5999,
    370.6823,402.636293,
    402.636293,
    402.636293,
    99.73778,
    241.9606,
    2.610111,
    26.95794
    ]
Eij = [
    [1, 1, 0.994635, 1.01953, 0.989844, 1, 1.00235, 0.999268, 1, 1.107274, 1.107274, 0.97164, 0.960644, 1, 1.17052],
    [1, 1, 1.02256, 1, 1.01306, 1, 1, 1.00532, 1, 1, 1, 0.97012, 0.925053, 1, 1.16446],
    [0.994635, 1.02256, 1, 1, 1.0049, 1, 1, 1, 1, 1, 1, 0.945939, 0.960237, 1, 1.034787],
    [1.01953, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.946914, 0.906849, 1, 1.3],
    [0.989844, 1.01306, 1.0049, 1, 1, 1, 1, 1, 1, 1, 1, 0.973384, 0.897362, 1, 1.3],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1.00235, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.95934, 0.726255, 1, 1],
    [0.999268, 1.00532, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.94552, 0.859764, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1.107274, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.855134, 1, 1],
    [1.107274, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.855134, 1, 1],
    [0.97164, 0.97012, 0.945939, 0.946914, 0.973384, 1, 0.95934, 0.94552, 1, 1, 1, 1, 1.02274, 1, 1.08632],
    [0.960644, 0.925053, 0.960237, 0.906849, 0.897362, 1, 0.726255, 0.859764, 1, 0.855134, 0.855134, 1.02274, 1, 1, 1.28179],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1.17052, 1.16446, 1.034787, 1.3, 1.3, 1, 1, 1, 1, 1, 1, 1.08632, 1.28179, 1, 1]
    ]
Vij = [
    [1, 1, 0.990877, 1, 0.992291, 1, 1, 1.00367, 1, 1.302576, 1.302576, 0.886106, 0.963827, 1, 1.15639],
    [1, 1, 1.065173, 1.25, 1.25, 1, 1.25, 1.25, 1, 1, 1, 0.816431, 0.96987, 1, 1.61666],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.915502, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.993556, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.066638, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.066638, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.835058, 1, 0.408838],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
Si = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Wi = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
s = [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Wi = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
w = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
B0i = [
    4.00088,
    4.00263,
    4.02939,
    4.06714,
    4.33944,
    4,
    4,
    4,
    4,
    4,
    4,
    3.50031,
    3.50002,
    2.50,
    2.47906
    ]
C0i = [
    0.76315,
    4.33939,
    6.60569,
    8.97575,
    9.44893,
    11.7618,
    11.7618,
    8.95043,
    11.6977,
    11.6977,
    11.6977,
    0.13732,
    2.04452,
    0.00,
    0.95806
    ]
D0i = [
    820.659,
    559.314,
    479.856,
    438.27,
    468.27,
    292.503,
    292.503,
    178.67,
    182.326,
    182.326,
    182.326,
    662.738,
    919.306,
    0.00,
    228.734
    ]
E0i = [
    0.0046,
    1.23722,
    3.197,
    5.25156,
    6.89406,
    20.1101,
    20.1101,
    21.836,
    26.8142,
    26.8142,
    26.8142,
    -0.1466,
    -1.06044,
    0.00,
    0.45444
    ]
F0i = [
    178.41,
    223.284,
    200.893,
    198.018,
    183.636,
    910.237,
    910.237,
    840.538,
    859.207,
    859.207,
    859.207,
    680.562,
    865.07,
    0.00,
    326.843
    ]
G0i = [
    8.74432,
    13.1974,
    19.1921,
    25.1423,
    24.4618,
    33.1688,
    33.1688,
    33.4032,
    38.6164,
    38.6164,
    38.6164,
    0.90066,
    2.03366,
    0.00,
    1.56039
    ]
H0i = [
    1062.82,
    1031.38,
    955.312,
    1905.02,
    1914.1,
    1919.37,
    1919.37,
    1774.25,
    1826.59,
    1826.59,
    1826.59,
    1740.06,
    483.553,
    0.00,
    1651.71
    ]
I0i = [
    -4.46921,
    -6.01989,
    -8.37267,
    16.1388,
    14.7824,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0.01393,
    0.00,
    -1.3756
    ]
J0i = [
    1090.53,
    1071.29,
    1027.29,
    893.765,
    903.185,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    341.109,
    0.00,
    1671.69
    ]
zci = [
    0.9981,
    0.992,
    0.9834,
    0.971,
    0.9682,
    0.953,
    0.953,
    0.945,
    0.919,
    0.919,
    0.919,
    0.9997,
    0.9947,
    1.0005,
    1.0006
    ]

numerators = [r / z for r, z in zip(ri, zci)]
denominator = sum(numerators)
xi = [num / denominator for num in numerators]
print(xi)

Kp1=9.80665*10**(-2)
Kp2=1.33322*10**(-4)
pressure = 18 #исходное абсолютное давление природного газа в МПа
temperature = 3
T=temperature+273.15 #Температура природного газа в К

import numpy as np

# Given data
xi = np.array([
    0.8486487705378545, 0.06598954882315745, 0.020685434562408678, 0.0, 
    0.0028903604523203012, 0.0, 0.0, 0.0007978080977642223, 0.0, 
    0.0008639586324170732, 0.0, 0.05003061595948862, 0.00968620464280331, 
    0.0004072982917858287, 0.0
])

Ki = np.array([
    0.4619255, 0.5279209, 0.583749, 0.6406937, 0.6341423,
    0.6738577, 0.6738577, 0.6798307, 0.7175118, 0.7175118,
    0.7175118, 0.4479153, 0.4557489, 0.3589888, 0.3514916
])

Kij = np.array([
    [1, 1, 1.007619, 1, 0.997596, 1, 1, 1.002529, 1, 0.982962, 0.982962, 1.00363, 0.995933, 1, 1.02326],
    [1, 1, 0.986893, 1, 1, 1, 1, 1, 1, 1, 1, 1.00796, 1.00851, 1, 1.02034],
    [1.007619, 0.986893, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0.997596, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1.002529, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0.982962, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.910183, 1, 1],
    [0.982962, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1.00363, 1.00796, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.982361, 0.982361, 1.03227],
    [0.995933, 1.00851, 1, 1, 1, 1, 1, 1, 1, 0.910183, 1, 0.982361, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.982361, 1, 1, 1],
    [1.02326, 1.02034, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.03227, 1, 1, 1]
])

#Подсчет смесевого параметра Kx по формуле (5)
Nc = len(xi)
sum_xi_Ki_52 = np.sum(xi * Ki**(5/2))
term1 = sum_xi_Ki_52**2
term2 = 0
for i in range(Nc - 1):
    for j in range(i + 1, Nc):
        Kij_52 = (Kij[i, j]**5 - 1) * (Ki[i] * Ki[j])**(5/2)
        term2 += 2 * xi[i] * xi[j] * Kij_52
Kx = (term1 + term2)**(1/5)
print(Kx)





