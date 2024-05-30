#!/usr/bin/env python

import sys
sys.path.append('../05-hartree_fock')

### ANCHOR: imports_and_constants
import numpy as np
from hartree_fock import HartreeFock

HARTREE_TO_EV = 27.211_386_245_988
### ANCHOR_END: imports_and_constants


### ANCHOR: cis_class
class CIS(HartreeFock):

    def initialize(self):
        super().initialize()
        self.run_hf(max_iter=500, threshold=1e-8, verbose=0)
        print(self.energy)
    
    def get_cis_hamiltonian(self):
        # Transform ERIs from AO basis to MO basis
        eri_mo = np.einsum('pQRS, pP -> PQRS',
                 np.einsum('pqRS, qQ -> pQRS',
                 np.einsum('pqrS, rR -> pqRS',
                 np.einsum('pqrs, sS -> pqrS', self.mol.twoel, 
                           self.mo_coeff, optimize=True), 
                           self.mo_coeff, optimize=True), 
                           self.mo_coeff, optimize=True), 
                           self.mo_coeff, optimize=True)
        
        # Transform to spin-orbital basis
        norb = len(self.mo_energy) * 2
        nocc = self.nocc * 2
        nvirt = norb - nocc
        
        eps = np.repeat(self.mo_energy, 2)
        delta = np.zeros((2, 2, 2, 2))
        delta[(0, 0, 0, 0)] = 1
        delta[(0, 0, 1, 1)] = 1
        delta[(1, 1, 0, 0)] = 1
        delta[(1, 1, 1, 1)] = 1
        eri_mo = np.kron(eri_mo, delta)
        
        # Obtain orbital labels
        self.orb_labels = []
        for i in range(0, len(self.mo_energy)):
            self.orb_labels.extend([f'{i}a', f'{i}b'])
        
        # Obtain excitations in spin-orbit basis
        self.excitations = []
        for i in range(0, nocc):
            for a in range(nocc, norb):
                self.excitations.append((i, a))
        
        # Build the Hamiltonian
        hamiltonian = np.zeros((nocc * nvirt, nocc * nvirt))
        for p, left_excitation in enumerate(self.excitations):
            i, a = left_excitation
            for q, right_excitation in enumerate(self.excitations):
                j, b = right_excitation
                hamiltonian[p, q] = (eps[a] - eps[i]) * (i == j) * (a == b) \
                    + eri_mo[j, b, a, i] - eri_mo[j, i, a, b]
        
        return hamiltonian
    
    def run_cis(self, nprint=None):
        h = self.get_cis_hamiltonian()
        eigval, eigvect = np.linalg.eigh(h)
        
        self.cis_energies = eigval
        self.cis_states = eigvect

        e_ev = eigval * HARTREE_TO_EV
        
        # Print detailed information on significant excitations
        print('CIS:')
        if nprint is None:
            nstate = len(self.excitations)
        elif nprint < 0:
            nstate = 0
        else:
            nstate = min(nprint, len(self.excitations))
        for state in range(0, nstate):
            print(f'Excited State {state + 1:3d}: '
                  f'E_exc = {e_ev[state]:10.4f} eV')
            for idx, exc in enumerate(self.excitations):
                coeff = eigvect[idx, state]
                contribution = np.abs(coeff)**2
                if contribution > 0.1:
                    i, a = exc
                    il, al = (self.orb_labels[x] for x in exc)
                    print(f'{il:4s} -> {al:4s} '
                          f'{coeff:12.6f} ({100.0 * contribution:.1f} %)')
            print()

        return eigval
### ANCHOR_END: cis_class

if __name__ == '__main__':
    sys.path.append('../03-molecular_integrals')

    ### ANCHOR: cis_water
    from atom import Atom
    from molecule import Molecule
    
    # Coordinates are in the unit of Angstrom.
    o1 = Atom('O', [ 0.000,  0.000,  0.000], unit='A')
    h1 = Atom('H', [ 0.758,  0.587,  0.000], unit='A')
    h2 = Atom('H', [-0.758,  0.587,  0.000], unit='A')
    
    water = Molecule()
    water.set_atomlist([o1, h1, h2])
    water.get_basis('sto-3g')
    
    cis = CIS(water)
    cis.initialize()

    cis.run_cis(nprint=20)
    ### ANCHOR_END: cis_water

