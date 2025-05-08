#!/usr/bin/env python

import sys
sys.path.append('../../03-molecular_integrals')
sys.path.append('../../05-hartree_fock')
sys.path.append('../../06-configuration_interaction')

### ANCHOR: imports
import numpy as np
import matplotlib.pyplot as plt

from atom import Atom
from molecule import Molecule
from configuration_interaction import ConfigurationInteraction
### ANCHOR_END: imports

### ANCHOR: d4h_h4_function
def make_d4h_h4(r_hh, basis='sto-3g'):
    h1 = Atom('H', [ 0.5*r_hh,  0.5*r_hh,  0.0], unit='A')
    h2 = Atom('H', [-0.5*r_hh,  0.5*r_hh,  0.0], unit='A')
    h3 = Atom('H', [-0.5*r_hh, -0.5*r_hh,  0.0], unit='A')
    h4 = Atom('H', [ 0.5*r_hh, -0.5*r_hh,  0.0], unit='A')

    mol = Molecule()
    mol.set_atomlist([h1, h2, h3, h4])
    mol.get_basis(basis)

    return mol
### ANCHOR_END: d4h_h4_function

NSTATES = 8
R_HH_MIN, R_HH_MAX = 0.6, 2.5
NPOINTS = 20

r_hh_array = np.linspace(R_HH_MIN, R_HH_MAX, NPOINTS)
print(r_hh_array)
d4h_ci_energies = np.zeros((NSTATES, NPOINTS))

for i, r_hh in enumerate(r_hh_array):
    mol = make_d4h_h4(r_hh)
    ci = ConfigurationInteraction(mol)
    ci.initialise()
    projector = ci.get_n_electron_subspace(4)
    e, v = ci.run_ci(NSTATES, projector=projector, verbose=0)
    d4h_ci_energies[:, i] = e


### ANCHOR: make_d2h_h4
def make_d2h_h4(r_x, r_y, basis='sto-3g'):
    h1 = Atom('H', [ 0.5*r_x,  0.5*r_y,  0.0], unit='A')
    h2 = Atom('H', [-0.5*r_x,  0.5*r_y,  0.0], unit='A')
    h3 = Atom('H', [-0.5*r_x, -0.5*r_y,  0.0], unit='A')
    h4 = Atom('H', [ 0.5*r_x, -0.5*r_y,  0.0], unit='A')

    mol = Molecule()
    mol.set_atomlist([h1, h2, h3, h4])
    mol.get_basis(basis)

    return mol
### ANCHOR_END: make_d2h_h4

NSTATES = 12
R_X_MIN, R_X_MAX = 0.4, 2.5
RY = 1.4
NPOINTS = 22

r_x_array = np.linspace(R_X_MIN, R_X_MAX, NPOINTS)
print(r_x_array)
d2h_ci_energies = np.zeros((NSTATES, NPOINTS))

for i, r_x in enumerate(r_x_array):
    mol = make_d2h_h4(r_x, RY)
    ci = ConfigurationInteraction(mol)
    ci.initialise()
    projector = ci.get_n_electron_subspace(4)
    e, v = ci.run_ci(NSTATES, projector=projector, verbose=0)
    d2h_ci_energies[:, i] = e


fig, axs = plt.subplots(1, 2, figsize=(8, 5))

for i, e in enumerate(d4h_ci_energies):
    axs[0].plot(r_hh_array, e, label=f'state {i}')

axs[0].set_title(r'$\mathrm{D_{4h}}$ $\mathrm{H_4}$')
axs[0].set_xlabel(r'$r_{\mathrm{H-H}}$ / $\mathrm{\AA}$')
axs[0].set_ylabel('energy / a.u.')
axs[0].legend()

for i, e in enumerate(d2h_ci_energies):
    axs[1].plot(r_x_array, e, label=f'state {i}')

axs[1].set_title(r'$\mathrm{D_{2h}}$ $\mathrm{H_4}$ ($r_y = 1.4\ \mathrm{\AA}$)')
axs[1].set_xlabel(r'$r_x$ / $\mathrm{\AA}$')
axs[1].set_ylabel('energy / a.u.')
axs[1].legend()

fig.tight_layout()

plt.show()

fig.savefig('../../../assets/figures/psets/04/h4_d4h_d2h_scan.svg')

