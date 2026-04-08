#!/usr/bin/env python

### ANCHOR: imports
from molecule import Molecule
### ANCHOR_END: imports

### ANCHOR: calculate_nuclear_attractions
ethene = Molecule()
ethene.read_from_xyz('ethene.xyz')
ethene.get_basis('sto-3g')

ethene.get_S()
overlap = ethene.S

ethene.get_T()
kinetic = ethene.T
### ANCHOR_END: calculate_nuclear_attractions

import numpy as np
from pyscf import gto

mol = gto.M(atom='ethene.xyz', basis='sto-3g')
overlap_pyscf = mol.intor("int1e_ovlp")
kinetic_pyscf = mol.intor("int1e_kin")

print('Overlap: ', np.allclose(overlap, overlap_pyscf))
print('Kinetic: ', np.allclose(kinetic, kinetic_pyscf))
### ANCHOR_END: pyscf_nuclear_attractions

