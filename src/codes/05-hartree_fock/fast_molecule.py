#!/usr/bin/env python

import sys
sys.path.append( 
    '/Users/xmiao/WORK/teaching/Programmierkurs_Master_SS23/'
    'python-course-master/code/ch03'
)

import numpy as np
from molecule import Molecule as OldMolecule

class Molecule(OldMolecule):
    
    def get_twoel(self):
        nbf = len(self.basisfunctions)
        self.twoel = np.zeros((nbf, nbf, nbf, nbf))
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
                            self.twoel[idx] = g_ijkl

