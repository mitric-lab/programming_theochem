#!/usr/bin/env python

import sys
sys.path.append('../../03-molecular_integrals')
sys.path.append('../../05-hartree_fock')
sys.path.append('../../06-configuration_interaction')

### ANCHOR: imports
import numpy as np
import matplotlib.pyplot as plt
from mayavi import mlab

from atom import Atom
from molecule import Molecule
from cis import CIS
from isosurface import build_grid, evaluate_mo_grid, visualize_cube
### ANCHOR_END: imports

### ANCHOR: h6_molecule
h1 = Atom('H', [-2.500, -0.350,  0.000], unit='A')
h2 = Atom('H', [-2.500,  0.350,  0.000], unit='A')
h3 = Atom('H', [-0.350,  0.000,  0.000], unit='A')
h4 = Atom('H', [ 0.350,  0.000,  0.000], unit='A')
h5 = Atom('H', [ 2.500, -0.350,  0.000], unit='A')
h6 = Atom('H', [ 2.500,  0.350,  0.000], unit='A')
### ANCHOR_END: h6_molecule

mol = Molecule()
mol.set_atomlist([h1, h2, h3, h4, h5, h6])
mol.get_basis('sto-3g')

cis = CIS(mol)
cis.initialize()
cis.run_cis(nprint=20)

### ANCHOR: plot_mo
XLIM, YLIM, ZLIM = (-8.0, 8.0), (-5.0, 5.0), (-5.0, 5.0)
NX, NY, NZ = 80, 80, 80

ISOSURFACE_COLORS = [(1, 0, 0), (0, 0, 1)]
ORBITAL_ISOVALUES = [0.05, -0.05]

grid = build_grid(XLIM, YLIM, ZLIM, NX, NY, NZ)
mo_grid = evaluate_mo_grid(mol, grid, cis.mo_energy, cis.mo_coeff)

fig_mo2 = mlab.figure()
p_mo2 = visualize_cube(mol, grid, mo_grid[4], ORBITAL_ISOVALUES, 
                       ISOSURFACE_COLORS, fig_mo2)
mlab.savefig('../../../assets/figures/psets/03/h6_mo2.png')

fig_mo5 = mlab.figure()
p_mo5 = visualize_cube(mol, grid, mo_grid[10], ORBITAL_ISOVALUES, 
                       ISOSURFACE_COLORS, fig_mo5)
mlab.savefig('../../../assets/figures/psets/03/h6_mo5.png')
### ANCHOR_END: plot_mo

### ANCHOR: get_tdm
ISTATE = 11
tdm = cis.cis_states[:, ISTATE].reshape(2 * cis.nocc, -1)
### ANCHOR_END: get_tdm

fig, ax = plt.subplots(figsize=(4, 4))
ax.set_ylabel('occupied MOs')
ax.set_xlabel('virtual MOs')
ax.xaxis.set_ticks_position('top')

ax.matshow(tdm**2)

fig.savefig('../../../assets/figures/psets/03/h6_tdm_12.svg')

### ANCHOR: calculate_nto
u, s, vh = np.linalg.svd(tdm)
print(s)

mo_occ_grid = mo_grid[:6]
mo_virt_grid = mo_grid[6:]
nto_occ_grid = np.einsum('ixyz,ij->jxyz', mo_occ_grid, u)
nto_virt_grid = np.einsum('axyz,ab->bxyz', mo_virt_grid, vh.T)
### ANCHOR_END: calculate_nto

### ANCHOR: plot_nto
fig_nto_occ0 = mlab.figure()
p_nto_occ0 = visualize_cube(mol, grid, nto_occ_grid[0], ORBITAL_ISOVALUES, 
                            ISOSURFACE_COLORS, fig_nto_occ0)
mlab.savefig('../../../assets/figures/psets/03/h6_nto_occ0.png')

fig_nto_virt0 = mlab.figure()
p_nto_virt0 = visualize_cube(mol, grid, nto_virt_grid[0], ORBITAL_ISOVALUES,
                             ISOSURFACE_COLORS, fig_nto_virt0)
mlab.savefig('../../../assets/figures/psets/03/h6_nto_virt0.png')
### ANCHOR_END: plot_nto

mlab.show()

