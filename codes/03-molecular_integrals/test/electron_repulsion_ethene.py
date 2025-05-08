#!/usr/bin/env python

### ANCHOR: imports
import numpy as np
from molecule import Molecule
### ANCHOR_END: imports

import time

### ANCHOR: pyscf_imports
from pyscf import gto
### ANCHOR_END: pyscf_imports

### ANCHOR: calculate_electron_repulsions
ethene = Molecule()
ethene.read_from_xyz('ethene.xyz')
ethene.get_basis('sto-3g')

start = time.time()
ethene.get_twoel()
end = time.time()
print('Time to calculate electron repulsions: {} seconds'.format(end - start))
eri = ethene.twoel
### ANCHOR_END: calculate_electron_repulsions

### ANCHOR: calculate_electron_repulsions_pyscf
ethene = gto.M(atom='ethene.xyz', basis='sto-3g')
eri_pyscf = ethene.intor('int2e')
### ANCHOR_END: calculate_electron_repulsions_pyscf

### ANCHOR: compare_eris
print(np.allclose(eri, eri_pyscf))
### ANCHOR_END: compare_eris

