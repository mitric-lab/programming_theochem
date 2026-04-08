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
### ANCHOR_END: imports

### ANCHOR: atoms_in_water
# Coordinates are in the unit of Angstrom.
o1 = Atom('O', [ 0.000,  0.000,  0.000], unit='A')
h1 = Atom('H', [ 1.000,  0.000,  0.000], unit='A')
h2 = Atom('H', [ 0.000,  1.000,  0.000], unit='A')
### ANCHOR_END: atoms_in_water

### ANCHOR: water_overlap
water = Molecule()
water.set_atomlist([o1, h1, h2])
water.get_basis('vsto-3g')
water.get_S()

np.set_printoptions(precision=4, suppress=True, floatmode='fixed')
print('Overlap matrix:')
print(water.S)
### ANCHOR_END: water_overlap
print()

### ANCHOR: water_iorb_mapping
NORB_DICT = {1: 1, 6: 4, 7: 4, 8: 4}
norb = len(water.S)

iorb_to_atom = []
iorb_to_l = []
for at in water.atomlist:
    at_norb = NORB_DICT[at.atnum]
    iorb_to_atom.extend([at.atnum] * at_norb)
    if at_norb == 1:
        iorb_to_l.extend([0])
    elif at_norb == 4:
        iorb_to_l.extend([0, 1, 1, 1])
    else:
        raise ValueError('Currently only supports s and p orbitals.')

# Check dimensions
assert len(iorb_to_atom) == norb
assert len(iorb_to_l) == norb
### ANCHOR_END: water_iorb_mapping

### ANCHOR: water_hamiltonian
# Define constants
HARTREE_TO_EV = 27.211386245988
ALPHA_DICT = {
    1: [-13.6 / HARTREE_TO_EV],
    6: [-21.4 / HARTREE_TO_EV, -11.4 / HARTREE_TO_EV],
    7: [-26.0 / HARTREE_TO_EV, -13.4 / HARTREE_TO_EV],
    8: [-32.3 / HARTREE_TO_EV, -14.8 / HARTREE_TO_EV],
}
K_DICT = {
    1: [0.66836],
    6: [0.88266, 0.58621],
    7: [0.75747, 0.68272],
    8: [0.84677, 0.76529],
}

hamiltonian = np.zeros((norb, norb))

# Diagonal elements
for i in range(0, norb):
    at_i = iorb_to_atom[i]
    l_i = iorb_to_l[i]
    hamiltonian[i, i] = ALPHA_DICT[at_i][l_i]

# Off-diagonal elements
for i in range(0, norb):
    at_i = iorb_to_atom[i]
    l_i = iorb_to_l[i]
    for j in range(i + 1, norb):
        at_j = iorb_to_atom[j]
        l_j = iorb_to_l[j]
                
        h_ij = K_DICT[at_i][l_i] * K_DICT[at_j][l_j] \
                * (ALPHA_DICT[at_i][l_i] + ALPHA_DICT[at_j][l_j]) \
                * water.S[i, j]
        hamiltonian[i, j] = h_ij
        hamiltonian[j, i] = h_ij

np.set_printoptions(precision=4, suppress=True, floatmode='fixed')
print('Hamiltonian:')
print(hamiltonian)
### ANCHOR_END: water_hamiltonian
print()

### ANCHOR: water_orbital_energies
e_orbs, _ = np.linalg.eigh(hamiltonian)

np.set_printoptions(precision=4, suppress=True, floatmode='fixed')
print('Orbital energies:')
print(e_orbs)
### ANCHOR_END: water_orbital_energies
print()

### ANCHOR: water_nocc
Z_DICT = {1: 1, 6: 4, 7: 5, 8: 6}

nelec = sum([Z_DICT[at.atnum] for at in water.atomlist])
assert nelec % 2 == 0, 'Only closed-shell molecules are supported!'
nocc = nelec // 2
### ANCHOR_END: water_nocc

### ANCHOR: water_electronic_energy
e_elec = 2.0 * sum(e_orbs[:nocc])
print(f'E^{{elec}} = {e_elec:.4f}')
### ANCHOR_END: water_electronic_energy

