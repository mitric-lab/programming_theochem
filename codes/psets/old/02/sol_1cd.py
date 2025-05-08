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
from basis_set import Gaussian as OldGaussian
import T
import S
### ANCHOR_END: imports


class Gaussian(OldGaussian):
    ### ANCHOR: gaussian_t
    def T(self, other):
        t_x = np.array([
            T.t_ij(self.ijk[0], other.ijk[0], alphai, alphaj, 
                   self.A[0], other.A[0])
            * S.s_ij(self.ijk[1], other.ijk[1], alphai, alphaj, 
                     self.A[1], other.A[1])
            * S.s_ij(self.ijk[2], other.ijk[2], alphai, alphaj, 
                     self.A[2], other.A[2])
            * ci * cj * normi * normj
            for ci, alphai, normi in zip(self.coefs, self.exps, self.norm_const)
            for cj, alphaj, normj in zip(other.coefs, other.exps, other.norm_const)
        ]).sum()
        t_y = np.array([
            S.s_ij(self.ijk[0], other.ijk[0], alphai, alphaj, 
                   self.A[0], other.A[0])
            * T.t_ij(self.ijk[1], other.ijk[1], alphai, alphaj, 
                     self.A[1], other.A[1])
            * S.s_ij(self.ijk[2], other.ijk[2], alphai, alphaj, 
                     self.A[2], other.A[2])
            * ci * cj * normi * normj
            for ci, alphai, normi in zip(self.coefs, self.exps, self.norm_const)
            for cj, alphaj, normj in zip(other.coefs, other.exps, other.norm_const)
        ]).sum()
        t_z = np.array([
            S.s_ij(self.ijk[0], other.ijk[0], alphai, alphaj, 
                   self.A[0], other.A[0])
            * S.s_ij(self.ijk[1], other.ijk[1], alphai, alphaj, 
                     self.A[1], other.A[1])
            * T.t_ij(self.ijk[2], other.ijk[2], alphai, alphaj, 
                     self.A[2], other.A[2])
            * ci * cj * normi * normj
            for ci, alphai, normi in zip(self.coefs, self.exps, self.norm_const)
            for cj, alphaj, normj in zip(other.coefs, other.exps, other.norm_const)
        ]).sum()
        return t_x + t_y + t_z
    ### ANCHOR_END: gaussian_t

OldMolecule.get_basis.__globals__['BasisSet'].get_basisfunctions.__globals__['Gaussian'] = Gaussian

class Molecule(OldMolecule):
    ### ANCHOR: molecule_get_t
    def get_T(self) -> None:
        nbf = len(self.basisfunctions)
        self.T = np.zeros((nbf, nbf))
        for i in np.arange(0, nbf):
            for j in np.arange(i, nbf):
                self.T[i,j] = self.basisfunctions[i].T(self.basisfunctions[j])
                self.T[j,i] = self.T[i,j]
    ### ANCHOR_END: molecule_get_t

### ANCHOR: atoms_in_water
# Coordinates are in the unit of Angstrom.
o1 = Atom('O', [ 0.000,  0.000,  0.000], unit='A')
h1 = Atom('H', [ 1.000,  0.000,  0.000], unit='A')
h2 = Atom('H', [ 0.000,  1.000,  0.000], unit='A')
### ANCHOR_END: atoms_in_water

### ANCHOR: water_kinetics
water = Molecule()
water.set_atomlist([o1, h1, h2])
water.get_basis('sto-3g')
water.get_T()

np.set_printoptions(precision=4, linewidth=200, suppress=True)
print(water.T)
### ANCHOR_END: water_kinetics

