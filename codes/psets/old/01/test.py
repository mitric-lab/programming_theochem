#!/usr/bin/env python

import sys
sys.path.append( 
    '/Users/xmiao/WORK/teaching/Programmierkurs_Master_SS23/'
    'python-course-master/code/ch03'
)

import numpy as np
from scipy.linalg import eigh
from scipy.optimize import minimize
from atom import Atom
from molecule import Molecule
from basis_set import Gaussian, BasisSet

BOHR_TO_ANGS = 0.529177210903
HARTREE_TO_EV = 27.211386245988

# dim a = L^-1
A_DICT = {
    1: 0.70485,
    6: 0.64786,
    7: 0.60722,
    8: 0.64781,
}

# dim b = 1
B_DICT = {
    1: 0.83541,
    6: 0.94928,
    7: 1.0975,
    8: 1.0510,
}

# dim c = L
C_DICT = {
    1: 0.29684,
    6: 0.71224,
    7: 2.0093,
    8: 3.0455,
}

# dim d = L^-1
D_DICT = {
    1: 3.8163,
    6: 1.1130,
    7: 2.1880,
    8: 2.2954,
}

# dim e = 1
E_DICT = {
    1: 1.2612,
    6: 3.7686,
    7: 2.5854,
    8: 1.2897,
}

Z_DICT = {
    1: 1,
    6: 4,
    7: 5,
    8: 6,
}

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


def v_rep_elec(at1, at2):
    atnum1, atnum2 = at1.atnum, at2.atnum
    v0 = BOHR_TO_ANGS
    r12 = np.linalg.norm(at1.coord - at2.coord) * BOHR_TO_ANGS
    v_rep_ev = v0 * Z_DICT[atnum1] * Z_DICT[atnum2] \
            * (1.0 / (r12 + C_DICT[atnum1] + C_DICT[atnum2])) \
            * np.exp(-(A_DICT[atnum1] + A_DICT[atnum2]) 
                     * r12**(B_DICT[atnum1] + B_DICT[atnum2]))
    return v_rep_ev


def v_rep_nuc(at1, at2):
    atnum1, atnum2 = at1.atnum, at2.atnum
    v0 = BOHR_TO_ANGS
    r12 = np.linalg.norm(at1.coord - at2.coord) * BOHR_TO_ANGS
    v_rep_ev = v0 * Z_DICT[atnum1] * Z_DICT[atnum2] \
            * (1.0 / r12) \
            * np.exp(-(D_DICT[atnum1] + D_DICT[atnum2]) 
                     * r12**(E_DICT[atnum1] + E_DICT[atnum2]))
    return v_rep_ev


class ExtendedHuckelCalculator(object):
    
    def __init__(self, molecule):
        self.molecule = molecule
        self.molecule.get_S()
        self.natom = molecule.natom
        self.overlap = self.molecule.S
        self.norb = len(self.overlap)
        self.nelec = sum([Z_DICT[at.atnum] for at in self.molecule.atomlist])
        assert self.nelec % 2 == 0, 'Only closed-shell molecules are supported!'
        self.nocc = self.nelec // 2

        self.iorb_to_atom = []
        self.iorb_to_l = []
        for at in self.molecule.atomlist:
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
                    print(f1, f2, f3, f4)
                    print(h_ij)
                    print(f1 * f2 * f3 * f4)

                self.hamiltonian[i, j] = h_ij
                self.hamiltonian[j, i] = h_ij

    def get_orbital_energies(self):
        if not hasattr(self, 'hamiltonian'):
            self.get_hamiltonian()
        # e_orbs, _ = eigh(self.hamiltonian, self.overlap, type=1)
        e_orbs, _ = np.linalg.eigh(self.hamiltonian)
        return e_orbs

    def get_electronic_energy(self):
        if not hasattr(self, 'hamiltonian'):
            self.get_hamiltonian()
        # e_orbs, _ = eigh(self.hamiltonian, self.overlap, type=1)
        e_orbs, _ = np.linalg.eigh(self.hamiltonian)
        e_elec = 2.0 * sum(e_orbs[:self.nocc])
        return e_elec

    def get_electronic_repulsion_energy(self):
        e_rep_elec = 0.0
        for i in range(0, self.natom):
            for j in range(i + 1, self.natom):
                e_rep_elec += v_rep_elec(self.molecule.atomlist[i],
                                         self.molecule.atomlist[j])
        return e_rep_elec
    
    def get_nuclear_repulsion_energy(self):
        e_rep_nuc = 0.0
        for i in range(0, self.natom):
            for j in range(i + 1, self.natom):
                e_rep_nuc += v_rep_nuc(self.molecule.atomlist[i],
                                        self.molecule.atomlist[j])
        return e_rep_nuc

    def get_total_energy(self):
        e_elec = self.get_electronic_energy()
        e_rep_elec = self.get_electronic_repulsion_energy()
        e_rep_nuc = self.get_nuclear_repulsion_energy()
        return e_elec + e_rep_elec + e_rep_nuc
    

def get_mol_energy(p, mol0):
    coords = p.reshape((-1, 3))
    
    atomlist = []
    for i, at in enumerate(mol0.atomlist):
        atomlist.append(Atom(at.symbol, coords[i], unit='A'))

    mol = Molecule()
    mol.set_atomlist(atomlist)
    mol.get_basis('vsto-3g')

    ehc = ExtendedHuckelCalculator(mol)
    e_tot = ehc.get_electronic_energy()
    e_tot = ehc.get_total_energy()
    return e_tot


mol0 = Molecule()
mol0.read_from_xyz('mol.xyz')
mol0.get_basis('vsto-3g')
mol0.get_S()
print('Overlap:')
print(mol0.S)

ehc = ExtendedHuckelCalculator(mol0)
ehc.get_hamiltonian()
print('Hamiltonian:')
print(ehc.hamiltonian)

e_orbs = ehc.get_orbital_energies()
print('Orbital energies:')
print(e_orbs)

e_elec = ehc.get_electronic_energy()
print('Electronic energy:')
print(e_elec)

e_rep_elec = ehc.get_electronic_repulsion_energy()
print('Electronic repulsion energy:')
print(e_rep_elec)

e_rep_nuc = ehc.get_nuclear_repulsion_energy()
print('Nuclear repulsion energy:')
print(e_rep_nuc)

e_tot = ehc.get_total_energy()
print('Total energx:')
print(e_elec + e_rep_elec + e_rep_nuc)
print(e_tot)

raise SystemExit

p0 = np.array([at.coord for at in mol0.atomlist]).flatten()

res = minimize(get_mol_energy, p0, args=(mol0, ), method='BFGS')
print(res.x)
print(res.message)

new_coords = res.x.reshape((-1, 3))
with open('test.xyz', 'w') as f:
    f.write(f'{mol0.natom}\n')
    f.write('\n')
    for i, at in enumerate(mol0.atomlist):
        f.write('{0} {1[0]:.12f} {1[1]:.12f} {1[2]:.12f}\n'\
            .format(at.symbol, new_coords[i]))


v1 = new_coords[1] - new_coords[0]
v2 = new_coords[2] - new_coords[0]
l1 = np.linalg.norm(v1)
l2 = np.linalg.norm(v2)

n1 = v1 / l1
n2 = v2 / l2
theta = np.arccos(np.dot(n1, n2))

print('Bond length:')
print(l1)
print(l2)
print('Bond angle:')
print(theta * 180.0 / np.pi)

