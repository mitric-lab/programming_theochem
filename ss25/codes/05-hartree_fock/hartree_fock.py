#!/usr/bin/env python


### ANCHOR: imports
import numpy as np
### ANCHOR_END: imports


### ANCHOR: hartree_fock_class
class HartreeFock:

    def __init__(self, molecule, charge=0):
        self.mol = molecule
        self.charge = charge

    def initialise(self):
        self.nel = np.array([
            atom.atnum for atom in self.mol.atomlist
        ]).sum() - self.charge

        # Only restricted Hartree-Fock is implemented
        assert self.nel % 2 == 0, \
            "Only even number of electrons is supported!"
        self.nocc = self.nel // 2
        
        # precalculate integrals 
        self.mol.get_S()
        self.mol.get_T()
        self.mol.get_V()
        self.mol.get_twoel()
        
        # orthogonalise AO
        eigval, eigvec = np.linalg.eigh(self.mol.S)
        self.X = eigvec @ np.diag(1.0 / np.sqrt(eigval))

        # core hamiltonian + initialise density matrix
        self.hcore = self.mol.T + self.mol.Ven
        orb_en, orb = np.linalg.eigh(self.hcore)
        
        c = orb[:, :self.nocc]
        self.p = 2.0 * c @ c.T
    
    def get_fock(self, p):
        g = np.einsum(
            'kl, ijkl -> ij', p, 
            self.mol.twoel - 0.5 * self.mol.twoel.transpose(0, 2, 1, 3),
        )
        return self.hcore + g
    
    def run_hf(self, max_iter=100, threshold=1e-6, verbose=5):
        energy_last_iteration = 0.0
        self.p_old = np.copy(self.p)
        for iteration in range(max_iter):
            # calculate Fock-matrix
            f = self.get_fock(self.p)
            # orthogonalise Fock-Matrix
            f_ortho = self.X.T @ f @ self.X
            # diagonalise Fock-Matrix
            eigvals, eigvecs = np.linalg.eigh(f_ortho)
            # get new density matrix 
            c = eigvecs[:, :self.nocc]
            self.p = 2.0 * c @ c.T
            self.p = self.X @ self.p @ self.X.T
            # calculate energy 
            energy = 0.5 * np.trace((self.hcore + f) @ self.p)
            
            if verbose > 0:
                print(f"Iteration {iteration}, Energy = {energy} Hartree")
            if verbose > 1:
                print(f"MO energies: {eigvals}")
            
            if np.abs(energy - energy_last_iteration) < threshold:
                break
            energy_last_iteration = energy
        
        self.mo_energy = eigvals
        self.mo_coeff = self.X @ eigvecs
        self.energy = energy

        return energy
### ANCHOR_END: hartree_fock_class


if __name__ == '__main__':
    import sys
    
    sys.path.append( 
        '../03-molecular_integrals'
    )

    ### ANCHOR: hartree_fock_water
    from atom import Atom
    from molecule import Molecule
    
    # Coordinates are in the unit of Angstrom.
    o1 = Atom('O', [ 0.000,  0.000,  0.000], unit='A')
    h1 = Atom('H', [ 0.758,  0.587,  0.000], unit='A')
    h2 = Atom('H', [-0.758,  0.587,  0.000], unit='A')
    
    water = Molecule()
    water.set_atomlist([o1, h1, h2])
    water.get_basis('sto-3g')
    
    rhf = HartreeFock(water)
    rhf.initialise()
    e_scf = rhf.run_hf()
    print(f"SCF energy: {e_scf} Hartree")
    ### ANCHOR_END: hartree_fock_water
    
