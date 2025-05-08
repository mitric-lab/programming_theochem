#!/usr/bin/env python

import sys
sys.path.append( 
    '/Users/xmiao/WORK/teaching/Programmierkurs_Master_SS23/'
    'python-course-master/code/ch03'
)

### ANCHOR: imports
import sympy as sp
from sympy.printing.numpy import NumPyPrinter, \
    _known_functions_numpy, _known_constants_numpy
import os
from hermite_expansion import get_ckn
### ANCHOR_END: imports

### ANCHOR: define_symbols
# Initialisation of symbolic variables
alpha, beta = sp.symbols('alpha beta', real=True, positive=True)
AX, BX = sp.symbols('A_x B_x', real=True)
### ANCHOR_END: define_symbols

### ANCHOR: define_s00
# Overlap for l_a = l_b = 0
S_00 = sp.sqrt(sp.pi / (alpha + beta)) * sp.exp(
    -((alpha * beta) / (alpha + beta)) * (AX**2 - 2 * AX * BX + BX**2)
)
### ANCHOR_END: define_s00

### ANCHOR: hermite_overlap_function
def generate_hermite_overlaps(lmax):
    hermite_overlaps = {}
    for k in range(0, lmax + 1):
        for l in range(0, lmax + 1):
            ho_kl = sp.simplify(sp.diff(sp.diff(S_00, AX, k), BX, l))
            hermite_overlaps[(k, l)] = ho_kl
    
    return hermite_overlaps
### ANCHOR_END: hermite_overlap_function

### ANCHOR: single_overlap_function
def get_single_overlap(i, j, hermite_overlaps):
    if i < 0 or j < 0:
        return 0

    overlap = 0
    for k in range(0, i + 1):
        cki = get_ckn(k, i, alpha)
        for l in range(0, j + 1):
            clj = get_ckn(l, j, beta)
            overlap += cki * clj * hermite_overlaps[(k, l)]
    overlap = sp.factor_terms(overlap)
    
    return overlap
### ANCHOR_END: single_overlap_function

### ANCHOR: generate_kinetics_function
def generate_kinetics(lmax):
    hermite_overlaps = generate_hermite_overlaps(lmax + 2)

    kinetics = {}
    # Loop through all combinations of Gaussian functions up to order lmax
    for i in range(lmax + 1):
        for j in range(lmax + 1):
            print(i, j)
            # Store the kinetic integral in the dictionary with the key (i, j)
            kinetic_integral = \
                -2.0 * beta**2 * get_single_overlap(i, j + 2, hermite_overlaps) \
                + beta * (2 * j + 1) * get_single_overlap(i, j, hermite_overlaps) \
                - 0.5 * j * (j - 1) * get_single_overlap(i, j - 2, hermite_overlaps)
            kinetics[(i, j)] = sp.factor_terms(kinetic_integral)

    # Return the dictionary containing the kinetic energy integrals
    return kinetics
### ANCHOR_END: generate_kinetics_function

### ANCHOR: define_lmax
LMAX = 1
### ANCHOR_END: define_lmax

### ANCHOR: substitute_repeated_expressions
# Substitute repeated expressions
X_AB, X_AB_SQ, P, Q = sp.symbols(
    'ab_diff ab_diff_squared ab_sum ab_product', 
    real=True,
)
subsdict = {
    AX - BX: X_AB,         
    AX**2 - 2 * AX * BX + BX**2: X_AB_SQ,
    alpha + beta: P, 
    alpha * beta: Q,
}

t_ij = generate_kinetics(LMAX)
t_ij = {k: v.subs(subsdict) for (k, v) in t_ij.items()}
### ANCHOR_END: substitute_repeated_expressions

### ANCHOR: write_kinetics_function
def write_kinetics_py(kinetics, printer, path=''):
    with open(os.path.join(path, 'T.py'), 'w') as f:
        f.write('import numpy as np\n')
        f.write('def t_ij(i, j, alpha, beta, ax, bx):\n')
        # Calculate repeated expressions
        f.write('    ab_diff = ax - bx\n')
        f.write('    ab_diff_squared = ab_diff**2\n')
        f.write('    ab_sum = alpha + beta\n')
        f.write('    ab_product = alpha * beta\n')
        f.write('\n')
        # Write integrals for different cases
        
        for i, (key, value) in enumerate(kinetics.items()):
            if i == 0:
                if_str = 'if'
            else:
                if_str = 'elif'
            
            ia, ib = key
            code = printer.doprint(value)
            f.write(f'    {if_str} (i, j) == ({ia}, {ib}):\n')
            f.write(f'        return {code}\n')
        f.write('    else:\n')
        f.write('        raise NotImplementedError\n')
### ANCHOR_END: write_kinetics_function

### ANCHOR: setup_printer
_numpy_known_functions = {k: f'np.{v}' for k, v 
                          in _known_functions_numpy.items()}
_numpy_known_constants = {k: f'np.{v}' for k, v 
                          in _known_constants_numpy.items()}

printer = NumPyPrinter()
printer._module = 'np'
printer.known_functions = _numpy_known_functions
printer.known_constants = _numpy_known_constants
### ANCHOR_END: setup_printer

### ANCHOR: write_kinetics
MY_PATH = '.'
write_kinetics_py(t_ij, printer, path=MY_PATH)
### ANCHOR_END: write_kinetics

