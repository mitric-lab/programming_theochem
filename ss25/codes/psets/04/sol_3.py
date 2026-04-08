#!/usr/bin/env python

import sys
sys.path.append('../../03-molecular_integrals')
sys.path.append('../../05-hartree_fock')
sys.path.append('../../06-configuration_interaction')

### ANCHOR: imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import csc_matrix
from functools import reduce
from itertools import combinations

from atom import Atom
from molecule import Molecule
from configuration_interaction import ConfigurationInteraction \
    as ConfigurationInteractionOld
### ANCHOR_END: imports


class ConfigurationInteraction(ConfigurationInteractionOld):
    
    def get_n_excitation_subspace(self, ns):
        n_electron_creators = combinations(self.creators, self.nel)
        n_electron_indices = combinations(range(0, self.nsite), self.nel)
        occupied_indices = set(range(0, self.nel))
        projector = csc_matrix((self.ndim, self.ndim), dtype=float)
        for indices, ops in zip(n_electron_indices, n_electron_creators):
            occ_intersection = set(indices) & occupied_indices
            n_holes = self.nel - len(occ_intersection)
            if n_holes in ns:
                creator = reduce(lambda x, y: x @ y, ops)
                ket = creator @ self.vacuum
                bra = ket.T
                projector += ket @ bra
        return projector
    
    def get_xas_subspace(self, exc_indices):
        n_electron_creators = combinations(self.creators, self.nel)
        n_electron_indices = combinations(range(0, self.nsite), self.nel)
        projector = csc_matrix((self.ndim, self.ndim), dtype=float)
        for indices, ops in zip(n_electron_indices, n_electron_creators):
            xas_intersection = set(indices) & set(exc_indices)
            if set(indices) == set(range(0, self.nel)) \
                or len(xas_intersection) == len(exc_indices) - 1:
                creator = reduce(lambda x, y: x @ y, ops)
                ket = creator @ self.vacuum
                bra = ket.T
                if indices[0] in exc_indices:
                    projector += ket @ bra
        return projector


### ANCHOR: h4_molecule
r = 1.0 / 2.0
h1 = Atom('H', [ r,  r,  0.0], unit='A')
h2 = Atom('H', [-r,  r,  0.0], unit='A')
h3 = Atom('H', [-r, -r,  0.0], unit='A')
h4 = Atom('H', [ r, -r,  0.0], unit='A')
### ANCHOR_END: h4_molecule

mol = Molecule()
mol.set_atomlist([h1, h2, h3, h4])
mol.get_basis('sto-3g')

### ANCHOR: ground_state_calculation
# FCI
ci = ConfigurationInteraction(mol)
ci.initialise()
projector = ci.get_n_electron_subspace(4)
e, v = ci.run_ci(6, projector=projector, verbose=0)
print('FCI:', e[0])

# CISD
ci = ConfigurationInteraction(mol)
ci.initialise()
projector = ci.get_n_excitation_subspace([0, 1, 2])
e, v = ci.run_ci(6, projector=projector, verbose=0)
print('CISD:', e[0])

# CID
ci = ConfigurationInteraction(mol)
ci.initialise()
projector = ci.get_n_excitation_subspace([0, 2])
e, v = ci.run_ci(6, projector=projector, verbose=0)
print('CID:', e[0])

# CIS
ci = ConfigurationInteraction(mol)
ci.initialise()
projector = ci.get_n_excitation_subspace([0, 1])
e, v = ci.run_ci(6, projector=projector, verbose=0)
print('CIS:', e[0])
### ANCHOR_END: ground_state_calculation

### ANCHOR: excited_state_calculation
HARTREE_TO_EV = 27.211386245988

# FCI
ci = ConfigurationInteraction(mol)
ci.initialise()
projector = ci.get_n_electron_subspace(4)
e, v = ci.run_ci(6, projector=projector, verbose=0)
print('FCI (e_exc):', (e[1:] - e[0]) * HARTREE_TO_EV)

# CISD
ci = ConfigurationInteraction(mol)
ci.initialise()
projector = ci.get_n_excitation_subspace([0, 1, 2])
e, v = ci.run_ci(6, projector=projector, verbose=0)
print('CISD (e_exc):', (e[1:] - e[0]) * HARTREE_TO_EV)

# CISDT
ci = ConfigurationInteraction(mol)
ci.initialise()
projector = ci.get_n_excitation_subspace([0, 1, 2, 3])
e, v = ci.run_ci(6, projector=projector, verbose=0)
print('CISDT (e_exc):', (e[1:] - e[0]) * HARTREE_TO_EV)
### ANCHOR_END: excited_state_calculation

### ANCHOR: lih_molecule
li = Atom('Li', [0.000, 0.000, 0.000], unit='A')
h1 = Atom( 'H', [0.000, 0.000, 1.595], unit='A')
### ANCHOR_END: lih_molecule

mol = Molecule()
mol.set_atomlist([li, h1])
mol.get_basis('sto-3g')

ci = ConfigurationInteraction(mol)
ci.initialise()
projector = ci.get_xas_subspace([0, 1])
e, v = ci.run_ci(5, projector=projector, verbose=1)
print('XAS:', (e[1:] - e[0]) * HARTREE_TO_EV)

