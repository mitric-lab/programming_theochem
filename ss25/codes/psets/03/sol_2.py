#!/usr/bin/env python

import sys
sys.path.append( 
    '/Users/xmiao/WORK/teaching/Programmierkurs_Master_SS23/'
    'python-course-master/code/ch03'
)

### ANCHOR: imports
import numpy as np
import matplotlib.pyplot as plt

from atom import Atom
from molecule import Molecule as OldMolecule
### ANCHOR_END: imports

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
        self.get_twoel_symm()
        
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
            2.0 * self.twoel_symm - self.twoel_symm.transpose(0, 2, 1, 3),
        )
        return self.hcore + g

    ### ANCHOR: run_hf_modified
    def run_hf(self, max_iter=100, threshold=1e-6, alpha=0.0):
        energy_last_iteration = 0.0
        self.scf_energies = []
        self.niter = 0
        self.p_old = np.copy(self.p)
        for iteration in range(max_iter):
            self.niter += 1
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
            self.p = alpha * self.p_old + (1.0 - alpha) * self.p
            # calculate energy 
            energy = np.trace((self.hcore + f) @ self.p)
            self.scf_energies.append(energy)
            print(f"Iteration {iteration}, Energy = {energy} Hartree")
            print(f"MO energies: {eigvals}")
            if np.abs(energy - energy_last_iteration) < threshold:
                break
            energy_last_iteration = energy
            self.p_old = np.copy(self.p)
    ### ANCHOR_END: run_hf_modified
    ### ANCHOR: reset_hf
    def reset(self):
        orb_en, orb = np.linalg.eigh(self.hcore)
        c = orb[:, :water.nocc]
        self.p = c @ c.T
        self.p_old = np.copy(self.p)
    ### ANCHOR_END: reset_hf


### ANCHOR: stretched_water_molecule
# Coordinates are in the unit of Angstrom.
o1 = Atom('O', [ 0.000    ,  0.000    ,  0.000], unit='A')
h1 = Atom('H', [ 0.758 * 2,  0.587 * 2,  0.000], unit='A')
h2 = Atom('H', [-0.758 * 2,  0.587 * 2,  0.000], unit='A')
### ANCHOR_END: stretched_water_molecule

### ANCHOR: water_initialization
water = HartreeFock()
water.set_atomlist([o1, h1, h2])
water.get_basis('sto-3g')
water.initialize()
### ANCHOR_END: water_initialization

### ANCHOR: no_damping_energy
water.run_hf(max_iter=100, threshold=1e-6, alpha=0.0)
fig1, ax1 = plt.subplots(figsize=(8, 4))
ax1.plot(water.scf_energies)
ax1.set_xlabel('Iteration')
ax1.set_ylabel('Energy / Hartree')

fig1.tight_layout()
plt.show()
### ANCHOR_END: no_damping_energy
fig1.savefig('../../../src/figures/psets/03/energy_no_damping.svg')

### ANCHOR: damping_single_alpha_energy
water.reset()
water.run_hf(max_iter=100, threshold=1e-6, alpha=0.5)
fig2, ax2 = plt.subplots(figsize=(8, 4))
ax2.plot(water.scf_energies)
ax2.set_xlabel('Iteration')
ax2.set_ylabel('Energy / Hartree')

fig2.tight_layout()
plt.show()
### ANCHOR_END: damping_single_alpha_energy
fig2.savefig('../../../src/figures/psets/03/energy_damping_0.5.svg')

### ANCHOR: niter_alpha
niters = []
alphas = np.linspace(0.00, 0.98, 50)
for alpha in alphas:
    water.reset()
    water.run_hf(max_iter=200, threshold=1e-6, alpha=alpha)
    niters.append(water.niter)

fig3, ax3 = plt.subplots(figsize=(8, 4))
ax3.plot(alphas, niters)
ax3.set_xlabel(r'$\alpha$')
ax3.set_ylabel('Number of iterations')

fig3.tight_layout()
plt.show()
### ANCHOR_END: niter_alpha
fig3.savefig('../../../src/figures/psets/03/niter_alpha.svg')

