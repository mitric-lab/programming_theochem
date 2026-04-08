#!/usr/bin/env python

VSTO_1G_DICT = {
    '1s': {
        'exponents': [0.2709498091],
        'coefficients': [1.0],
    },
    '2s': {
        'exponents': [1.012151084],
        'coefficients': [1.0],
    },
    '2p': {
        'exponents': [1.759666885],
        'coefficients': [1.0],
    }
}

VSTO_2G_DICT = {
    '1s': {
        'exponents': [0.8518186635, 0.1516232927],
        'coefficients': [0.4301284983, 0.6789135305],
    },
    '2s': {
        'exponents': [0.1292278611, 0.04908584205],
        'coefficients': [0.7470867124, 0.2855980556],
    },
    '2p': {
        'exponents': [0.4323908358, 0.1069139065],
        'coefficients': [0.4522627513, 0.6713122642],
    }
}

VSTO_3G_DICT = {
    '1s': {
        'exponents': [2.227660584, 0.4057711562, 0.1098175104],
        'coefficients': [0.1543289673, 0.5353281423, 0.4446345422],
    },
    '2s': {
        'exponents': [2.581578398, 0.1567622104, 0.06018332272],
        'coefficients': [-0.0594474934, 0.5960385398, 0.458178629],
    },
    '2p': {
        'exponents': [0.9192379002, 0.259194503, 0.06009805746],
        'coefficients': [0.1623948553 , 0.5661708862, 0.4223071752],
    }
}

ZETA_DICT = {
    1: [1.6230],
    6: [2.3511, 1.7800],
    7: [2.5626, 2.1125],
    8: [3.5724, 2.2539],
}

ORB_DICT = {
    1: ['1s'],
    6: ['2s', '2p'],
    7: ['2s', '2p'],
    8: ['2s', '2p'],
}

ELEMENTS = [1, 6, 7, 8]


def get_sto_dict(element, sto_dict):
    orbs = ORB_DICT[element]
    zetas = ZETA_DICT[element]
    bf_dict = {}
    for orb, zeta in zip(orbs, zetas):
        exponents = [zeta**2 * x for x in sto_dict[orb]['exponents']]
        coefficients = sto_dict[orb]['coefficients']
        bf_dict[orb] = {
            'exponents': exponents,
            'coefficients': coefficients,
        }
    
    return bf_dict


basis_set = {}
for e in ELEMENTS:
    basis_set[e] = get_sto_dict(e, VSTO_3G_DICT)

print(basis_set)

