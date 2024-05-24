#!/usr/bin/env python

import sys
sys.path.append( 
    '/Users/xmiao/WORK/teaching/Programmierkurs_Master_SS23/'
    'python-course-master/code/ch03'
)

### ANCHOR: imports
import numpy as np

from atom import Atom
from molecule import Molecule
from basis_set import Gaussian, BasisSet
## ANCHOR_END: imports

# import from sol_1 while suppressing print output
import io
import sys

suppress_text = io.StringIO()
sys.stdout = suppress_text 
from sol_1 import Z_DICT, water, e_elec
sys.stdout = sys.__stdout__

### ANCHOR: constants
BOHR_TO_ANGS = 0.529177210903
A_DICT = {1: 0.70485, 6: 0.64786, 7: 0.60722, 8: 0.64781}
B_DICT = {1: 0.83541, 6: 0.94928, 7: 1.0975, 8: 1.0510}
C_DICT = {1: 0.29684, 6: 0.71224, 7: 2.0093, 8: 3.0455}
D_DICT = {1: 3.8163, 6: 1.1130, 7: 2.1880, 8: 2.2954}
E_DICT = {1: 1.2612, 6: 3.7686, 7: 2.5854, 8: 1.2897}
### ANCHOR_END: constants

### ANCHOR: v_rep_elec_function
def v_rep_elec(at1, at2):
    atnum1, atnum2 = at1.atnum, at2.atnum
    v0 = BOHR_TO_ANGS
    r12 = np.linalg.norm(at1.coord - at2.coord) * BOHR_TO_ANGS
    v_rep_ev = v0 * Z_DICT[atnum1] * Z_DICT[atnum2] \
            * (1.0 / (r12 + C_DICT[atnum1] + C_DICT[atnum2])) \
            * np.exp(-(A_DICT[atnum1] + A_DICT[atnum2]) 
                     * r12**(B_DICT[atnum1] + B_DICT[atnum2]))
    return v_rep_ev
### ANCHOR_END: v_rep_elec_function

### ANCHOR: water_v_rep_elec
e_rep_elec = 0.0
for i in range(0, water.natom):
    for j in range(i + 1, water.natom):
        e_rep_elec += v_rep_elec(water.atomlist[i], water.atomlist[j])
print(f'E_{{rep}}^{{elec}} = {e_rep_elec:.4f}')
### ANCHOR_END: water_v_rep_elec

### ANCHOR: v_rep_nuc_function
def v_rep_nuc(at1, at2):
    atnum1, atnum2 = at1.atnum, at2.atnum
    v0 = BOHR_TO_ANGS
    r12 = np.linalg.norm(at1.coord - at2.coord) * BOHR_TO_ANGS
    v_rep_ev = v0 * Z_DICT[atnum1] * Z_DICT[atnum2] \
        * (1.0 / r12) \
        * np.exp(-(D_DICT[atnum1] + D_DICT[atnum2]) 
        * r12**(E_DICT[atnum1] + E_DICT[atnum2]))
    return v_rep_ev
### ANCHOR_END: v_rep_nuc_function

### ANCHOR: water_v_rep_nuc
e_rep_nuc = 0.0
for i in range(0, water.natom):
    for j in range(i + 1, water.natom):
        e_rep_nuc += v_rep_nuc(water.atomlist[i], water.atomlist[j])
print(f'E_{{rep}}^{{nuc}} = {e_rep_nuc:.4f}')
### ANCHOR_END: water_v_rep_nuc

### ANCHOR: water_total_energy
e_tot = e_elec + e_rep_elec + e_rep_nuc
print(f'E^{{tot}} = {e_tot:.4f}')
### ANCHOR_END: water_total_energy

