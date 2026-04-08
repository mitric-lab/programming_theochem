#!/usr/bin/env python

import sys
sys.path.append('../../03-molecular_integrals')
sys.path.append('../../05-hartree_fock')
sys.path.append('../../06-configuration_interaction')

### ANCHOR: imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import sqrtm

from atom import Atom
from molecule import Molecule
from configuration_interaction import ConfigurationInteraction
### ANCHOR_END: imports

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

### ANCHOR: loewdin_orthogonalisation
ci = ConfigurationInteraction(mol)
ci.initialise()
coeffs = np.linalg.inv(sqrtm(ci.mol.S))
projector = ci.get_n_electron_subspace(4)
print('Loewdin orthogonalisation')
e, v = ci.run_ci(6, coeffs=coeffs, projector=projector)
print()
### ANCHOR_END: loewdin_orthogonalisation

### ANCHOR: cholesky_decomposition
ci = ConfigurationInteraction(mol)
ci.initialise()
coeffs = np.linalg.inv(np.linalg.cholesky(ci.mol.S).T)
projector = ci.get_n_electron_subspace(4)
print('Cholesky decomposition')
e, v = ci.run_ci(6, coeffs=coeffs, projector=projector)

