#!/usr/bin/env python

import sys
sys.path.append( 
    '/Users/xmiao/WORK/teaching/Programmierkurs_Master_SS23/'
    'python-course-master/code/ch03'
)

import numpy as np
from mayavi import mlab

### ANCHOR: imports
from atom import Atom
from cis import CIS
### ANCHOR_END: imports

from isosurface import build_grid, evaluate_mo_grid, visualize_cube

### ANCHOR: water_hf
# Coordinates are in the unit of Angstrom.
o1 = Atom('O', [ 0.000,  0.000,  0.000], unit='A')
h1 = Atom('H', [ 0.758,  0.587,  0.000], unit='A')
h2 = Atom('H', [-0.758,  0.587,  0.000], unit='A')

mol = CIS()
mol.set_atomlist([o1, h1, h2])
mol.get_basis('sto-3g')

mol.initialize()
mol.run_cis(nprint=20)
### ANCHOR_END: water_hf

### ANCHOR: construct_grid
XLIM, YLIM, ZLIM = (-5.0, 5.0), (-5.0, 5.0), (-5.0, 5.0)
NX, NY, NZ = 80, 80, 80

grid = build_grid(XLIM, YLIM, ZLIM, NX, NY, NZ)
mo_grid = evaluate_mo_grid(mol, grid)
### ANCHOR_END: construct_grid

### ANCHOR: water_td
ISOSURFACE_COLORS = [(1, 0, 0), (0, 0, 1)]
DENSITY_ISOVALUES = [0.01, -0.01]
ISTATE = 3

td_grid = np.zeros((NX, NY, NZ))
for (exc, c_ia) in zip(mol.excitations, mol.cis_states[:, ISTATE]):
    i, a = exc
    if (i % 2) == (a % 2):
        td_grid += c_ia * mo_grid[i] * mo_grid[a]

fig_td = mlab.figure()
visualize_cube(mol, grid, td_grid, DENSITY_ISOVALUES,
               ISOSURFACE_COLORS, fig_td)

# Remove this line if you are using Jupyter notebook
mlab.show()
### ANCHOR_END: water_td

