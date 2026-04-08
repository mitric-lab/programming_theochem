#!/usr/bin/env python

import sys
sys.path.append('../03-molecular_integrals')
sys.path.append('../04-hartree_fock')

import numpy as np
from mayavi import mlab

### ANCHOR: imports
from atom import Atom
from molecule import Molecule
from cis import CIS
### ANCHOR_END: imports

from isosurface import build_grid, evaluate_mo_grid, visualize_cube

### ANCHOR: water_hf
# Coordinates are in the unit of Angstrom.
o1 = Atom('O', [ 0.000,  0.000,  0.000], unit='A')
h1 = Atom('H', [ 0.758,  0.587,  0.000], unit='A')
h2 = Atom('H', [-0.758,  0.587,  0.000], unit='A')

mol = Molecule()
mol.set_atomlist([o1, h1, h2])
mol.get_basis('sto-3g')

cis = CIS(mol)
cis.initialize()
cis.run_cis(nprint=20)
### ANCHOR_END: water_hf

### ANCHOR: construct_grid
XLIM, YLIM, ZLIM = (-5.0, 5.0), (-5.0, 5.0), (-5.0, 5.0)
NX, NY, NZ = 80, 80, 80

grid = build_grid(XLIM, YLIM, ZLIM, NX, NY, NZ)
mo_grid = evaluate_mo_grid(mol, grid, cis.mo_energy, cis.mo_coeff)
### ANCHOR_END: construct_grid

### ANCHOR: water_td
ISOSURFACE_COLORS = [(1, 0, 0), (0, 0, 1)]
DENSITY_ISOVALUES = [0.01, -0.01]
ISTATE = 3

td_grid = np.zeros((NX, NY, NZ))
for (exc, c_ia) in zip(cis.excitations, cis.cis_states[:, ISTATE]):
    i, a = exc
    if (i % 2) == (a % 2):
        td_grid += c_ia * mo_grid[i] * mo_grid[a]

fig_td = mlab.figure()
visualize_cube(mol, grid, td_grid, DENSITY_ISOVALUES,
               ISOSURFACE_COLORS, fig_td)
### ANCHOR_END: water_td

mlab.savefig('../../assets/figures/06-configuration_interaction/water_transition_density.png', figure=fig_td)

mlab.show()

