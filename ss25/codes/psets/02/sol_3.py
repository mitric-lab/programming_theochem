#!/usr/bin/env python

import sys
sys.path.append( 
    '/Users/xmiao/WORK/teaching/Programmierkurs_Master_SS23/'
    'python-course-master/code/ch03'
)

### ANCHOR: imports
import numpy as np

from atom import Atom
from molecule import Molecule as OldMolecule
### ANCHOR_END: imports



# OldMolecule.get_basis.__globals__['BasisSet'].get_basisfunctions.__globals__['Gaussian'] = Gaussian

class Molecule(OldMolecule):
    ### ANCHOR: molecule_get_twoel_symm
    def get_twoel_symm(self):
        nbf = len(self.basisfunctions)
        self.twoel_symm = np.zeros((nbf, nbf, nbf, nbf))
        for i in np.arange(nbf):
            for j in np.arange(i + 1):
                ij = i * (i + 1) // 2 + j
                for k in np.arange(nbf):
                    for l in np.arange(k + 1):
                        kl = k * (k + 1) // 2 + l
                        if ij < kl:
                            continue
                        g_ijkl = self.basisfunctions[i].twoel(
                            self.basisfunctions[j],
                            self.basisfunctions[k],
                            self.basisfunctions[l]
                        )
                        indices = (
                            (i, j, k, l), (k, l, i, j), 
                            (j, i, l, k), (l, k, j, i), 
                            (j, i, k, l), (l, k, i, j), 
                            (i, j, l, k), (k, l, j, i)
                        )
                        for idx in indices:
                            self.twoel_symm[idx] = g_ijkl
    ### ANCHOR_END: molecule_get_twoel_symm
    
    ### ANCHOR: molecule_get_twoel_screening
    def get_twoel_screening(self, threshold=1e-8):
        nbf = len(self.basisfunctions)
        self.twoel_screening = np.zeros((nbf, nbf, nbf, nbf))

        for i in np.arange(nbf):
            for j in np.arange(nbf):
                self.twoel_screening[i, j, i, j] = (
                    self.basisfunctions[i].twoel(self.basisfunctions[j],
                        self.basisfunctions[i], self.basisfunctions[j],
                    )
                )
        for i in np.arange(nbf):
            for j in np.arange(nbf):
                for k in np.arange(nbf):
                    for l in np.arange(nbf):
                        if i == k and j == l:
                            continue
                        q_ij = np.sqrt(self.twoel_screening[i, j, i, j])
                        q_kl = np.sqrt(self.twoel_screening[k, l, k, l])
                        q_bound = q_ij * q_kl
                        if q_bound > threshold:
                            self.twoel_screening[i, j, k, l] = (
                                self.basisfunctions[i].twoel(
                                    self.basisfunctions[j],
                                    self.basisfunctions[k],
                                    self.basisfunctions[l],
                                )
                            )
    ### ANCHOR_END: molecule_get_twoel_screening

### ANCHOR: water_molecule
# Coordinates are in the unit of Angstrom.
o1 = Atom('O', [ 0.000,  0.000,  0.000], unit='A')
h1 = Atom('H', [ 0.758,  0.587,  0.000], unit='A')
h2 = Atom('H', [-0.758,  0.587,  0.000], unit='A')

water = Molecule()
water.set_atomlist([o1, h1, h2])
water.get_basis('sto-3g')
### ANCHOR_END: water_molecule

### ANCHOR: water_eri_timing
import time

start = time.time()
water.get_twoel()
end = time.time()
print('Time for two-electron integrals: ', end - start)

start = time.time()
water.get_twoel_symm()
end = time.time()
print('Time for symmetrized two-electron integrals: ', end - start)

start = time.time()
water.get_twoel_screening(threshold=0.05)
end = time.time()
print('Time for screened two-electron integrals: ', end - start)

print(np.allclose(water.twoel, water.twoel_symm))
print(np.allclose(water.twoel_symm, water.twoel_screening, atol=0.05))
### ANCHOR_END: water_eri_timing

