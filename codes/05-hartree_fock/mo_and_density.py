#!/usr/bin/env python

import sys
sys.path.append(
    '../03-molecular_integrals'
)

import numpy as np
from mayavi import mlab

### ANCHOR: imports
from atom import Atom
from molecule import Molecule
from hartree_fock import HartreeFock
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

rhf = HartreeFock(mol)
rhf.initialize()
e_scf = rhf.run_hf(verbose=0)
### ANCHOR_END: water_hf

### ANCHOR: construct_grid
XLIM, YLIM, ZLIM = (-5.0, 5.0), (-5.0, 5.0), (-5.0, 5.0)
NX, NY, NZ = 80, 80, 80

grid = build_grid(XLIM, YLIM, ZLIM, NX, NY, NZ)
mo_grid = evaluate_mo_grid(mol, grid, rhf.mo_energy, rhf.mo_coeff)
### ANCHOR_END: construct_grid

### ANCHOR: water_mo
ISOSURFACE_COLORS = [(1, 0, 0), (0, 0, 1)]
ORBITAL_ISOVALUES = [0.05, -0.05]

ihomo = (rhf.nocc - 1) * 2
ilumo = rhf.nocc * 2

fig_homo = mlab.figure()
p_homo = visualize_cube(mol, grid, mo_grid[ihomo], ORBITAL_ISOVALUES, 
                        ISOSURFACE_COLORS, fig_homo)

fig_lumo = mlab.figure()
p_lumo = visualize_cube(mol, grid, mo_grid[ilumo], ORBITAL_ISOVALUES, 
                        ISOSURFACE_COLORS, fig_lumo)
### ANCHOR_END: water_mo

mlab.savefig('../../assets/figures/05-hartree_fock/water_homo.png', figure=fig_homo)
mlab.savefig('../../assets/figures/05-hartree_fock/water_lumo.png', figure=fig_lumo)

### ANCHOR: mlab_show
mlab.show()
### ANCHOR_END: mlab_show

### ANCHOR: water_density
DENSITY_COLORS = [(0.3, 0.3, 0.3)]
DENSITY_ISOVALUES = [0.05]

density_grid = np.zeros((NX, NY, NZ))
for d in mo_grid[:rhf.nocc * 2]:
    density_grid += np.abs(d)**2

fig_density = mlab.figure()
visualize_cube(mol, grid, density_grid, DENSITY_ISOVALUES,
               DENSITY_COLORS, fig_density, opacity=0.5)
### ANCHOR_END: water_density

mlab.savefig('../../assets/figures/05-hartree_fock/water_density.png', figure=fig_density)

mlab.show()

