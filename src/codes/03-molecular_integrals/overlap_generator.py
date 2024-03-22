#!/usr/bin/env python

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
    overlap = 0
    for k in range(0, i + 1):
        cki = get_ckn(k, i, alpha)
        for l in range(0, j + 1):
            clj = get_ckn(l, j, beta)
            overlap += cki * clj * hermite_overlaps[(k, l)]
    overlap = sp.factor_terms(overlap)
    
    return overlap
### ANCHOR_END: single_overlap_function

### ANCHOR: generate_overlaps_function
def generate_overlaps(lmax):
    hermite_overlaps = generate_hermite_overlaps(lmax)

    overlaps = {}
    # Loop through all combinations of Gaussian functions up to order lmax
    for i in range(lmax + 1):
        for j in range(lmax + 1):
            print(i, j)
            # Store the overlap integral in the dictionary with the key (i, j)
            overlaps[(i, j)] = get_single_overlap(i, j, hermite_overlaps)

    # Return the dictionary containing the overlap integrals
    return overlaps
### ANCHOR_END: generate_overlaps_function

### ANCHOR: define_lmax
LMAX = 2
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

s_ij = generate_overlaps(LMAX)
s_ij = {k: v.subs(subsdict) for (k, v) in s_ij.items()}
### ANCHOR_END: substitute_repeated_expressions

### ANCHOR: write_overlaps_function
def write_overlaps_py(overlaps, printer, path=''):
    with open(os.path.join(path, 'S.py'), 'w') as f:
        f.write('import numpy as np\n')
        f.write('def s_ij(i, j, alpha, beta, ax, bx):\n')
        # Calculate repeated expressions
        f.write('    ab_diff = ax - bx\n')
        f.write('    ab_diff_squared = ab_diff**2\n')
        f.write('    ab_sum = alpha + beta\n')
        f.write('    ab_product = alpha * beta\n')
        f.write('\n')
        # Write integrals for different cases
        
        for i, (key, value) in enumerate(overlaps.items()):
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
### ANCHOR_END: write_overlaps_function

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

### ANCHOR: write_overlaps
MY_PATH = '.'
write_overlaps_py(s_ij, printer, path=MY_PATH)
### ANCHOR_END: write_overlaps

