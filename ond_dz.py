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
Mi =[
    16.043, 30.07, 44.097, 58.123, 58.123, 
    72.15, 72.15, 72.15, 86.177, 86.177, 
    100.204, 28.0135, 44.01, 4.0026, 2.0159
]

#Подсчет xi по формуле (18)
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
print('Kx=', Kx)

#Подсчет давления нормировки p0m по формуле (4)
R = 8.31451
Lt = 1      
p0m = 10**-3 * Kx**-3 * R * Lt
print(p0m)

#Подсчет молярной массы Mm по формуле (19) 
Nc = len(Mi)
Mm = sum(Mi[i] * xi[i] for i in range(Nc))
print(Mm)

#Подсчет Gij по формуле (17) 
N = len(Gi)
G_ij = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        G_ij[i, j] = Gij[i][j] * 0.5 * (Gi[i] + Gi[j]) 
print('Gij',G_ij)

Ei = [
    151.3183,
    244.1667,
    298.1183,
    324.0689,
    337.6389,
    365.5999,
    365.5999,
    370.6823,
    402.636293,
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

#Подсчет Eij по формуле (16) 
Ei = np.array(Ei)
Eij = np.array(Eij)
N = len(Ei)
E_ij = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        E_ij[i, j] = Eij[i, j] * np.sqrt(Ei[i] * Ei[j])
print('Eij', E_ij)

Gi = [
    0,
    0.0793,
    0.141239,
    0.256692,
    0.281835,
    0.332267,
    0.332267,
    0.366911,
    0.289731,
    0.289731,
    0.289731,
    0.027815,
    0.189065,
    0,
    0.034369
]

Gij = np.array([
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
])


g = np.array([0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0])
Qi = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.69, 0, 0])
q = np.array([0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1])
Fi = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
f = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
w = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
Si = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
Wi = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

#Подсчет Bnij по формуле (15) 
N = len(Gi)
B_nij = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        B_nij[i, j] = (Gij[i, j] + 1 - g[i] ) * (Qi[i] * Qi[j] + 1 - q[i]) * (np.sqrt(Fi[i] * Fi[j] + 1 - f[i])) * (Si[i] * Si[j] + 1 - Si[i]) * (Wi[i] * Wi[j] + 1 - w[i])
print('Bij', B_nij)

import numpy as np

xi = np.array([8.48648771e-01, 6.59895488e-02, 2.06854346e-02, 0.00000000e+00,
               2.89036045e-03, 0.00000000e+00, 0.00000000e+00, 7.97808098e-04,
               0.00000000e+00, 8.63958632e-04, 0.00000000e+00, 5.00306160e-02,
               9.68620464e-03, 4.07298292e-04, 0.00000000e+00])

Ei = np.array([
    151.3183,
    244.1667,
    298.1183,
    324.0689,
    337.6389,
    365.5999,
    365.5999,
    370.6823,
    402.636293,
    402.636293,
    402.636293,
    99.73778,
    241.9606,
    2.610111,
    26.95794
])

Eij = np.array([
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
])

Vij = np.array([
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
])

#Подсчет параметра V по формуле (14)
Nc = len(xi)
term1 = np.sum(xi * Ei**(5/2))**2
term2 = 0
for i in range(Nc - 1):
    for j in range(i + 1, Nc):
        term2 += xi[i] * xi[j] * (Vij[i, j]**5 - 1) * (Ei[i] * Ei[j])**(5/2)
V = (term1 + 2 * term2)**(1/5)
print(f"V = {V}")

#Подсчет параметра F по формуле (13)
F = 0
for i in range(len(xi)):
    F += xi[i]**2 * Fi[i]
print(f"F = {F}")

#Подсчет параметра Q по формуле (12)
Q = 0
for i in range(len(xi)):
    Q += xi[i] * Qi[i]
print(f"Q = {Q}")


xi = np.array([
    0.8486487705378545, 0.06598954882315745, 0.020685434562408678, 0.0, 
    0.0028903604523203012, 0.0, 0.0, 0.0007978080977642223, 0.0, 
    0.0008639586324170732, 0.0, 0.05003061595948862, 0.00968620464280331, 
    0.0004072982917858287, 0.0
])

Gi = np.array([
    0,
    0.0793,
    0.141239,
    0.256692,
    0.281835,
    0.332267,
    0.332267,
    0.366911,
    0.289731,
    0.289731,
    0.289731,
    0.027815,
    0.189065,
    0,
    0.034369
])

Gij = np.array([
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
])

Gij_corrected = np.array([
    [0, 0.03965, 0.0706195, 0.128346, 0.1409175, 0.1661335, 0.1661335, 0.1834555, 0.1448655, 0.1448655, 0.1448655, 0.0139075, 0.07634946, 0, 0.03363539],
    [0.03965, 0.0793, 0.1102695, 0.167996, 0.1805675, 0.2057835, 0.2057835, 0.2231055, 0.1845155, 0.1845155, 0.1845155, 0.0535575, 0.04968724, 0.03965, 0.0568345],
    [0.0706195, 0.1102695, 0.141239, 0.1989655, 0.211537, 0.236753, 0.236753, 0.254075, 0.215485, 0.215485, 0.215485, 0.084527, 0.165152, 0.0706195, 0.087804],
    [0.128346, 0.167996, 0.1989655, 0.256692, 0.2692635, 0.2944795, 0.2944795, 0.3118015, 0.2732115, 0.2732115, 0.2732115, 0.1422535, 0.2228785, 0.128346, 0.1455305],
    [0.1409175, 0.1805675, 0.211537, 0.2692635, 0.281835, 0.307051, 0.307051, 0.324373, 0.285783, 0.285783, 0.285783, 0.154825, 0.23545, 0.1409175, 0.158102],
    [0.1661335, 0.2057835, 0.236753, 0.2944795, 0.307051, 0.332267, 0.332267, 0.349589, 0.310999, 0.310999, 0.310999, 0.180041, 0.260666, 0.1661335, 0.183318],
    [0.1661335, 0.2057835, 0.236753, 0.2944795, 0.307051, 0.332267, 0.332267, 0.349589, 0.310999, 0.310999, 0.310999, 0.180041, 0.260666, 0.1661335, 0.183318],
    [0.1834555, 0.2231055, 0.254075, 0.3118015, 0.324373, 0.349589, 0.349589, 0.366911, 0.328321, 0.328321, 0.328321, 0.197363, 0.277988, 0.1834555, 0.20064],
    [0.1448655, 0.1845155, 0.215485, 0.2732115, 0.285783, 0.310999, 0.310999, 0.328321, 0.289731, 0.289731, 0.289731, 0.158773, 0.239398, 0.1448655, 0.16205],
    [0.1448655, 0.1845155, 0.215485, 0.2732115, 0.285783, 0.310999, 0.310999, 0.328321, 0.289731, 0.289731, 0.289731, 0.158773, 0.239398, 0.1448655, 0.16205],
    [0.1448655, 0.1845155, 0.215485, 0.2732115, 0.285783, 0.310999, 0.310999, 0.328321, 0.289731, 0.289731, 0.289731, 0.158773, 0.239398, 0.1448655, 0.16205],
    [0.0139075, 0.0535575, 0.084527, 0.1422535, 0.154825, 0.180041, 0.180041, 0.197363, 0.158773, 0.158773, 0.158773, 0.027815, 0.10656898, 0.0139075, 0.031092],
    [0.07634946, 0.04968724, 0.165152, 0.2228785, 0.23545, 0.260666, 0.260666, 0.277988, 0.239398, 0.239398, 0.239398, 0.10656898, 0.189065, 0.0945325, 0.111717],
    [0, 0.03965, 0.0706195, 0.128346, 0.1409175, 0.1661335, 0.1661335, 0.1834555, 0.1448655, 0.1448655, 0.1448655, 0.0139075, 0.0945325, 0, 0.0171845],
    [0.03363539, 0.0568345, 0.087804, 0.1455305, 0.158102, 0.183318, 0.183318, 0.20064, 0.16205, 0.16205, 0.16205, 0.031092, 0.111717, 0.0171845, 0.034369]
])

#Подсчет параметра G по формуле (11)
Nc = len(xi)
term1 = np.sum(xi * Gi)
term2 = 0
for i in range(Nc - 1):
    for j in range(i + 1, Nc):
        term2 += xi[i] * xi[j] * (Gij_corrected[i, j] -1) * (Gi[i] + Gi[j])
G = term1 + term2
print(f"G = {G}")



Bij = np.array([
    [2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 
     2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 
     1.807653, 2.000000, 2.957310],
    [2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 
     2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 
     1.370296, 2.000000, 2.000000],
    [2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 
     2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 
     2.000000, 2.000000, 2.000000],
    [2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 
     2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 
     2.000000, 2.000000, 2.000000],
    [1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 
     1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 
     1.000000, 1.000000, 1.000000],
    [1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 
     1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 
     1.000000, 1.000000, 1.000000],
    [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 
     0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 
     0.000000, 0.000000, 0.000000],
    [2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 
     2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 
     2.000000, 2.000000, 2.000000],
    [2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 
     2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 
     2.000000, 2.000000, 2.000000],
    [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 
     0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 
     0.000000, 0.000000, 0.000000],
    [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 
     0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 
     0.000000, 0.000000, 0.000000],
    [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 
     0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 
     0.000000, 0.000000, 0.000000],
    [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 
     0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 
     0.000000, 0.000000, 0.000000],
    [2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 
     2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 
     2.000000, 2.000000, 2.000000],
    [2.957310, 2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 
     2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 2.000000, 
     2.000000, 2.000000, 2.828427]
])



#Подсчет параметра Bn по формуле (10)
Nc = len(xi)
Bn = 0
for i in range(Nc):
    for j in range(Nc):
        Bn += xi[i] * xi[j] * Bij[i, j] * Eij[i, j] * (Kij[i, j]**(3/2))
print(f"B_n = {Bn}")
#Подсчет параметра Cn по формуле (9)
C_n = (G + 1 - g)**g * (Q**2 + 1 - q)**q * (F + 1 - f)**f * V**u
print('Cn=', C_n)

#Подсчет параметра Dn и Un по формулам (7-8)
D_n = np.zeros_like(C_n)  
D_n[:12] = Bn * Kx**-3
# For 13 <= n <= 18
D_n[12:18] = Bn * Kx**-3 - C_n[12:18]
U_n = np.zeros_like(C_n)  
U_n[12:] = C_n[12:]
print('D_n=', D_n)
print('U_n', U_n)

#Расчет начального значения приведенной плотности по формуле (41)
delta_0=(10**3 * pressure * Kx**3 )/(R*T)
print('delta=',delta_0)

#Расчет значения тау по формуле (3)
tau=T/Lt
print('tau=', tau)

#Расчет значения A0 по формуле (6)
A0 = 0
for n in range(58):
    A0 += a[n] * (delta_0**b[n]) * (tau**(-u[n])) * (D_n[n] + (b[n] - c[n] * k[n]) * U_n[n] * np.exp(-c[n] * k[n]))
print(f"A_0 = {A0}")

#Расчет значения A1 по формуле (23)
A1 = 0
for n in range(58):
    term1 = (b[n] + 1) * b[n] * D_n[n]
    term2 = ((b[n] - c[n] * k[n]) * (delta_0**k[n]) * (b[n] - c[n] * k[n] * (delta_0**k[n]) + 1 - c[n] * (k[n]**2) * (delta_0**k[n])))
    term3 = U_n[n] * np.exp(-c[n] * k[n])
    A1 += a[n] * (delta_0**b[n]) * (tau**(-u[n])) * (term1 + term2 * term3)
print(f"A_1 = {A1}")

A2 = 0
A3 = 0
for n in range(58):
    A2 += a[n] * (delta_0**b[n]) * (tau**(-u[n])) * (1 - u[n]) * (b[n] * D_n[n] + (b[n] - c[n] * k[n]) * (delta_0**k[n]) * U_n[n] * np.exp(-c[n] * k[n]))
    A3 += a[n] * (delta_0**b[n]) * (tau**(-u[n])) * u[n] * (1 - u[n]) * (D_n[n] + U_n[n] * np.exp(-c[n] * k[n]))

print(f"A_2 = {A2}")
print(f"A_3 = {A3}")

#Расчет приведенного давления pi по формуле (2)
pi=pressure/p0m
print('pi=', pi)

