#!/usr/bin/env python

import sys
sys.path.append('../05-hartree_fock')

### ANCHOR: imports
import numpy as np
from scipy.sparse import csc_matrix, eye, kron
from scipy.sparse.linalg import eigsh
from functools import reduce
from itertools import combinations
from hartree_fock import HartreeFock
### ANCHOR_END: imports

### ANCHOR: one_site_operators
SIGMA_0 = np.array([[1, 0], [0, 1]])
SIGMA_Z = np.array([[1, 0], [0, -1]])
SIGMA_P = np.array([[0, 1], [0, 0]])  # annihilation operator
SIGMA_M = np.array([[0, 0], [1, 0]])  # creation operator
### ANCHOR_END: one_site_operators


### ANCHOR: csc_kron
def csc_kron(a, b):
    return csc_matrix(kron(a, b, format='csc'))
### ANCHOR_END: csc_kron


### ANCHOR: ci_class
### ANCHOR: ci_declaration
class ConfigurationInteraction(HartreeFock):
### ANCHOR_END: ci_declaration

    ### ANCHOR: ci_initialise
    def initialise(self):
        super().initialise()
        self.nsite = 2 * len(self.mol.basisfunctions)
        self.ndim = 2**self.nsite
        self.vacuum = eye(self.ndim, 1, format='csc')
        self.get_fermionic_operators()
    ### ANCHOR_END: ci_initialise
    
    ### ANCHOR: ci_get_fermionic_operators
    def get_fermionic_operators(self):
        self.creators = []
        for i in range(0, self.nsite):
            one_site_creators = (
                [SIGMA_Z] * i 
                + [SIGMA_M] 
                + [SIGMA_0] * (self.nsite - i - 1)
            )
            self.creators.append(reduce(csc_kron, one_site_creators))
        self.annihilators = [creator.getH() for creator in self.creators]
    ### ANCHOR_END: ci_get_fermionic_operators

    ### ANCHOR: ci_get_hamiltonian
    def get_hamiltonian(self, coeffs=None):
        if coeffs is None:
            if not hasattr(self, 'mo_coeff'):
                self.run_hf(threshold=1e-8, verbose=0)
                coeffs = self.mo_coeff
        else:
            coeffs = np.array(coeffs)
        
        h = np.einsum(
            'ij,ip,jq->pq', 
            self.mol.T + self.mol.Ven, 
            coeffs, coeffs,
            optimize=True,
        )
        g = np.einsum(
            'ijkl,ip,jq,kr,ls->pqrs', 
            self.mol.twoel, 
            coeffs, coeffs, coeffs, coeffs,
            optimize=True,
        )

        hamiltonian = csc_matrix((self.ndim, self.ndim), dtype=float)
        for i in range(0, self.nsite):
            for j in range(0, self.nsite):
                ij = (i % 2 == j % 2)
                hamiltonian +=  ij * h[i//2, j//2] \
                    * (self.creators[i] @ self.annihilators[j])
                for k in range(self.nsite):
                    for l in range(self.nsite):
                        kl = (k % 2 == l % 2)
                        hamiltonian += 0.5 * ij * kl \
                            * g[i//2, j//2, k//2, l//2] \
                            * (self.creators[i] @ self.creators[k] @
                               self.annihilators[l] @ self.annihilators[j])
        
        return hamiltonian
    ### ANCHOR_END: ci_get_hamiltonian

    ### ANCHOR: ci_get_n_electron_subspace
    def get_n_electron_subspace(self, n):
        n_electron_creators = combinations(self.creators, n)
        projector = csc_matrix((self.ndim, self.ndim), dtype=float)
        for ops in n_electron_creators:
            creator = reduce(lambda x, y: x @ y, ops)
            ket = creator @ self.vacuum
            bra = ket.T
            projector += ket @ bra
        return projector
    ### ANCHOR_END: ci_get_n_electron_subspace
    
    ### ANCHOR: ci_get_nuclear_repulsion
    def get_nuclear_repulsion(self):
        e_nuc = 0.0
        for i, ai in enumerate(self.mol.atomlist):
            for j, aj in enumerate(self.mol.atomlist[:i]):
                rij = np.linalg.norm(ai.coord - aj.coord)
                e_nuc += ai.atnum * aj.atnum / rij
        print(e_nuc)
        return e_nuc
    ### ANCHOR_END: ci_get_nuclear_repulsion

    ### ANCHOR: ci_run_ci
    def run_ci(self, nstate, projector=None):
        hamiltonian = self.get_hamiltonian()
        if projector is not None:
            # orthogonal projectors are symmetric
            hamiltonian = projector @ hamiltonian @ projector
        eigvals, eigvecs = eigsh(hamiltonian, k=nstate, which='SA')
        eigvals += self.get_nuclear_repulsion()

        print('CI:')
        for state in range(0, nstate):
            print(f'State {state:3d}: E = {eigvals[state]:12.8f} a.u.')
            for i, c in enumerate(eigvecs[:, state]):
                contribution = np.abs(c)**2
                if np.abs(c) > 0.1:
                    state_str = f'|{i:0{self.nsite}b}>'
                    print(f'  {state_str}: {c:12.8f} '
                          f'({100.0 * contribution:.1f} %)')
            print()

        return eigvals, eigvecs
    ### ANCHOR_END: ci_run_ci
### ANCHOR_END: ci_class

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    sys.path.append('../03-molecular_integrals')
    
    ### ANCHOR: h4_molecule
    from atom import Atom
    from molecule import Molecule
    
    # Coordinates are in the unit of Angstrom.
    r = 1.0 / 2.0
    h1 = Atom('H', [ r,  r, 0.0], unit='A')
    h2 = Atom('H', [-r,  r, 0.0], unit='A')
    h3 = Atom('H', [-r, -r, 0.0], unit='A')
    h4 = Atom('H', [ r, -r, 0.0], unit='A')
    
    mol = Molecule()
    mol.set_atomlist([h1, h2, h3, h4])
    mol.get_basis('sto-3g')
    ### ANCHOR_END: h4_molecule

    ### ANCHOR: ci_no_projector
    ci = ConfigurationInteraction(mol)
    ci.initialise()
    eigvals, eigvecs = ci.run_ci(20)
    ### ANCHOR_END: ci_no_projector
    
    ### ANCHOR: ci_projector
    ci = ConfigurationInteraction(mol)
    ci.initialise()
    projector = ci.get_n_electron_subspace(4)
    eigvals, eigvecs = ci.run_ci(20, projector=projector)
    ### ANCHOR_END: ci_projector
    
