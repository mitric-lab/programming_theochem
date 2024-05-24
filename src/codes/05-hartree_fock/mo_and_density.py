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
from hartree_fock import HartreeFock
### ANCHOR_END: imports

from isosurface import build_grid, evaluate_mo_grid, visualize_cube

### ANCHOR: water_hf
# Coordinates are in the unit of Angstrom.
o1 = Atom('O', [ 0.000,  0.000,  0.000], unit='A')
h1 = Atom('H', [ 0.758,  0.587,  0.000], unit='A')
h2 = Atom('H', [-0.758,  0.587,  0.000], unit='A')

mol = HartreeFock()
mol.set_atomlist([o1, h1, h2])
mol.get_basis('sto-3g')

mol.initialize()
e_scf = mol.run_hf(verbose=0)
### ANCHOR_END: water_hf

### ANCHOR: construct_grid
XLIM, YLIM, ZLIM = (-5.0, 5.0), (-5.0, 5.0), (-5.0, 5.0)
NX, NY, NZ = 80, 80, 80

grid = build_grid(XLIM, YLIM, ZLIM, NX, NY, NZ)
mo_grid = evaluate_mo_grid(mol, grid)
### ANCHOR_END: construct_grid

### ANCHOR: water_mo
ISOSURFACE_COLORS = [(1, 0, 0), (0, 0, 1)]
ORBITAL_ISOVALUES = [0.05, -0.05]

ihomo = (mol.nocc - 1) * 2
ilumo = mol.nocc * 2

fig_homo = mlab.figure()
visualize_cube(mol, grid, mo_grid[ihomo], ORBITAL_ISOVALUES, 
               ISOSURFACE_COLORS, fig_homo)

fig_lumo = mlab.figure()
visualize_cube(mol, grid, mo_grid[ilumo], ORBITAL_ISOVALUES, 
               ISOSURFACE_COLORS, fig_lumo)

# Remove this line if you are using Jupyter notebook
mlab.show()
### ANCHOR_END: water_mo

### ANCHOR: water_density
DENSITY_COLORS = [(0.3, 0.3, 0.3)]
DENSITY_ISOVALUES = [0.05]

density_grid = np.zeros((NX, NY, NZ))
for d in mo_grid[:mol.nocc * 2]:
    density_grid += np.abs(d)**2

fig_density = mlab.figure()
visualize_cube(mol, grid, density_grid, DENSITY_ISOVALUES,
               DENSITY_COLORS, fig_density, opacity=0.5)

# Remove this line if you are using Jupyter notebook
mlab.show()
### ANCHOR_END: water_density

