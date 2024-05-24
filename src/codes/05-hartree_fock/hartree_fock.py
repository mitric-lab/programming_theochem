#!/usr/bin/env python

import sys
sys.path.append( 
    '/Users/xmiao/WORK/teaching/Programmierkurs_Master_SS23/'
    'python-course-master/code/ch03'
)

### ANCHOR: imports
import numpy as np

from molecule import Molecule
### ANCHOR_END: imports

from fast_molecule import Molecule

### ANCHOR: hartree_fock_class
class HartreeFock(Molecule):

    def initialize(self):
        self.nel = np.array([
            self.atomlist[i].atnum for i in range(0, len(self.atomlist))
        ]).sum()
        self.nocc = self.nel // 2
        
        # precalculate integrals 
        self.get_S()
        self.get_T()
        self.get_V()
        self.get_twoel()
        
        # orthogonalize AO
        eigval, eigvec = np.linalg.eigh(self.S)
        self.X = eigvec @ np.diag(1.0 / np.sqrt(eigval))

        # core hamiltonian + initialize density matrix
        self.hcore = self.T + self.Ven
        orb_en, orb = np.linalg.eigh(self.hcore)
        
        c = orb[:, :self.nocc]
        self.p = c @ c.T
    
    def get_fock(self, p):
        g = np.einsum(
            'kl, ijkl -> ij', p, 
            2.0 * self.twoel - self.twoel.transpose(0, 2, 1, 3),
        )
        return self.hcore + g
    
    def run_hf(self, max_iter=100, threshold=1e-6, verbose=5):
        energy_last_iteration = 0.0
        self.p_old = np.copy(self.p)
        for iteration in range(max_iter):
            # calculate Fock-matrix
            f = self.get_fock(self.p)
            # orthogonalize Fock-Matrix
            f_ortho = self.X.T @ f @ self.X
            # diagonalize Fock-Matrix
            eigvals, eigvect = np.linalg.eigh(f_ortho)
            # get new density matrix 
            c = eigvect[:, :self.nocc]
            self.p = c @ c.T
            self.p = self.X @ self.p @ self.X.T
            # calculate energy 
            energy = np.trace((self.hcore + f) @ self.p)
            
            if verbose > 0:
                print(f"Iteration {iteration}, Energy = {energy} Hartree")
            if verbose > 1:
                print(f"MO energies: {eigvals}")
            
            if np.abs(energy - energy_last_iteration) < threshold:
                break
            energy_last_iteration = energy
        
        self.mo_energy = eigvals
        self.mo_coeff = self.X @ eigvect
        self.energy = energy

        return energy
### ANCHOR_END: hartree_fock_class


if __name__ == '__main__':
    ### ANCHOR: hartree_fock_water
    from atom import Atom
    
    # Coordinates are in the unit of Angstrom.
    o1 = Atom('O', [ 0.000,  0.000,  0.000], unit='A')
    h1 = Atom('H', [ 0.758,  0.587,  0.000], unit='A')
    h2 = Atom('H', [-0.758,  0.587,  0.000], unit='A')
    
    water = HartreeFock()
    water.set_atomlist([o1, h1, h2])
    water.get_basis('sto-3g')
    
    water.initialize()
    e_scf = water.run_hf()
    print(f"SCF energy: {e_scf} Hartree")
    ### ANCHOR_END: hartree_fock_water
    
