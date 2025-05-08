#!/usr/bin/env python

import sys
sys.path.append( 
    '/Users/xmiao/WORK/teaching/Programmierkurs_Master_SS23/'
    'python-course-master/code/ch03'
)

### ANCHOR: imports
import numpy as np
from scipy.optimize import minimize
from atom import Atom
from molecule import Molecule
from extended_huckel_calculator import ExtendedHuckelCalculator
### ANCHOR_END: imports


### ANCHOR: get_mol_energy_function
def get_mol_energy(p, mol0):
    coords = p.reshape((-1, 3))
    
    atomlist = []
    for i, at in enumerate(mol0.atomlist):
        atomlist.append(Atom(at.symbol, coords[i], unit='A'))

    mol = Molecule()
    mol.set_atomlist(atomlist)
    mol.get_basis('vsto-3g')

    ehc = ExtendedHuckelCalculator(mol)
    e_tot = ehc.get_electronic_energy()
    e_tot = ehc.get_total_energy()
    return e_tot
### ANCHOR_END: get_mol_energy_function


### ANCHOR: atoms_in_water
# Coordinates are in the unit of Angstrom.
o1 = Atom('O', [ 0.000,  0.000,  0.000], unit='A')
h1 = Atom('H', [ 1.000,  0.000,  0.000], unit='A')
h2 = Atom('H', [ 0.000,  1.000,  0.000], unit='A')
### ANCHOR_END: atoms_in_water

### ANCHOR: reference_molecule
mol0 = Molecule()
mol0.set_atomlist([o1, h1, h2])
mol0.get_basis('vsto-3g')

p0 = np.array([at.coord for at in mol0.atomlist]).flatten()
### ANCHOR_END: reference_molecule

### ANCHOR: optimize
res = minimize(get_mol_energy, p0, args=(mol0, ), method='BFGS')
print(res.x)
print(res.message)
### ANCHOR_END: optimize

new_coords = res.x.reshape((-1, 3))
with open('water_opt.xyz', 'w') as f:
    f.write(f'{mol0.natom}\n')
    f.write('\n')
    for i, at in enumerate(mol0.atomlist):
        f.write('{0} {1[0]:.12f} {1[1]:.12f} {1[2]:.12f}\n'\
            .format(at.symbol, new_coords[i]))

### ANCHOR: bond_length_angle
v1 = new_coords[1] - new_coords[0]
v2 = new_coords[2] - new_coords[0]
l1 = np.linalg.norm(v1)
l2 = np.linalg.norm(v2)

n1 = v1 / l1
n2 = v2 / l2
theta = np.arccos(np.dot(n1, n2))

print('Bond length:')
print(l1)
print(l2)
print('Bond angle:')
print(theta * 180.0 / np.pi)
### ANCHOR_END: bond_length_angle

