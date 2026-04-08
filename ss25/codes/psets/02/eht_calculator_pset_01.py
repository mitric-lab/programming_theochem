#!/usr/bin/env python

import numpy as np

### Constants
HARTREE_TO_EV = 27.211386245988

### EHT parameters
# Number of valence electrons
Z_DICT = {
    1: 1,
    6: 4,
    7: 5,
    8: 6,
}

# Number of valence orbitals
N_DICT = {
    1: 1,
    6: 4,
    7: 4,
    8: 4,
}

ENERGY_DICT = {
    1: [-13.6 / HARTREE_TO_EV],
    6: [-21.4 / HARTREE_TO_EV, -11.4 / HARTREE_TO_EV],
    7: [-26.0 / HARTREE_TO_EV, -13.4 / HARTREE_TO_EV],
    8: [-32.3 / HARTREE_TO_EV, -14.8 / HARTREE_TO_EV],
}

K_DICT = {
    1: [0.66836],
    6: [0.88266, 0.58621],
    7: [0.75747, 0.68272],
    8: [0.84677, 0.76529],
}


class ExtendedHuckelCalculator(object):
    
    def __init__(self, molecule):
        self.molecule = molecule
        self.molecule.get_S()
        self.natom = self.molecule.natom
        self.atomlist = self.molecule.atomlist
        self.overlap = self.molecule.S
        self.norb = len(self.overlap)
        self.nelec = sum([Z_DICT[at.atnum] for at in self.atomlist])
        assert self.nelec % 2 == 0, 'Only closed-shell molecules are supported!'
        self.nocc = self.nelec // 2

        self.iorb_to_atom = []
        self.iorb_to_l = []
        for at in self.atomlist:
            at_norb = N_DICT[at.atnum]
            self.iorb_to_atom.extend([at.atnum] * at_norb)
            if at_norb == 1:
                self.iorb_to_l.append(0)
            elif at_norb == 4:
                self.iorb_to_l.extend([0, 1, 1, 1])
            else:
                raise ValueError('Invalid angular momentum!')
        assert len(self.iorb_to_atom) == self.norb
        assert len(self.iorb_to_l) == self.norb

    def get_hamiltonian(self):
        self.hamiltonian = np.zeros_like(self.overlap)

        # Diagonal elements
        for i in range(0, self.norb):
            at_i = self.iorb_to_atom[i]
            l_i = self.iorb_to_l[i]
            self.hamiltonian[i, i] = ENERGY_DICT[at_i][l_i]
        # Off-diagonal elements
        for i in range(0, self.norb):
            at_i = self.iorb_to_atom[i]
            l_i = self.iorb_to_l[i]
            for j in range(i + 1, self.norb):
                at_j = self.iorb_to_atom[j]
                l_j = self.iorb_to_l[j]
                
                h_ij = K_DICT[at_i][l_i] * K_DICT[at_j][l_j] \
                        * (ENERGY_DICT[at_i][l_i] + ENERGY_DICT[at_j][l_j]) \
                        * self.overlap[i, j]
                
                if i == 4 and j == 5:
                    f1 = K_DICT[at_i][l_i]
                    f2 = K_DICT[at_j][l_j]
                    f3 = (ENERGY_DICT[at_i][l_i] + ENERGY_DICT[at_j][l_j])
                    f4 = self.overlap[i, j]

                self.hamiltonian[i, j] = h_ij
                self.hamiltonian[j, i] = h_ij

    def get_orbital_energies(self):
        if not hasattr(self, 'hamiltonian'):
            self.get_hamiltonian()
        e_orbs, _ = np.linalg.eigh(self.hamiltonian)
        return e_orbs

    def get_electronic_energy(self):
        if not hasattr(self, 'hamiltonian'):
            self.get_hamiltonian()
        e_orbs, _ = np.linalg.eigh(self.hamiltonian)
        e_elec = 2.0 * sum(e_orbs[:self.nocc])
        return e_elec

    def get_electronic_repulsion_energy(self):
        raise NotImplementedError
    
    def get_nuclear_repulsion_energy(self):
        raise NotImplementedError

    def get_total_energy(self):
        raise NotImplementedError
    
