#!/usr/bin/env python

### ANCHOR: imports
import numpy as np
import copy
from atom import Atom
from basis_set import BasisSet

a0 = 0.529177210903  # Bohr radius in angstrom
### ANCHOR_END: imports


### ANCHOR: molecule_base
class Molecule:
    """
    A class representing a molecule.

    Attributes:
        atomlist (list): A list of `atom` objects representing the atoms 
            in the molecule.
        natom (int): The number of atoms in the molecule.
        basisfunctions (list): A list of `Gaussian` objects representing 
            the basis functions of the molecule.
        S (ndarray): A matrix representing the overlap integrals between 
            basis functions.

    Methods:
        __init__(self) -> None: Initializes a new `molecule` object.
        set_atomlist(self,a: list) -> None: Sets the `atomlist` attribute 
            to the given list of `atom` objects.
        read_from_xyz(self,filename: str) -> None: Reads the coordinates of 
            the atoms in the molecule from an XYZ file.
        get_basis(self, name: str = "sto-3g") -> None: Computes the 
            basis functions for the molecule using the specified basis set.
        get_S(self) -> None: Computes the overlap integrals between 
            basis functions and sets the `S` attribute.
    """

    def __init__(self) -> None:
        """
        Initializes a new `Molecule` object.

        Returns:
            None
        """
        self.atomlist = []
        self.natom = len(self.atomlist)
        self.basisfunctions = []
        self.S = None

    def set_atomlist(self, a: list) -> None:
        """
        Sets the `atomlist` attribute to the given list of `Atom` objects.

        Parameters:
            a (list): A list of `Atom` objects representing the atoms 
                in the molecule.

        Returns:
            None
        """
        self.atomlist = []
        for at in a:
            if at.unit == 'A':
                at.coord = at.coord / a0
            elif at.unit == 'B':
                pass
            else:
                raise ValueError('Invalid unit for atom coordinates.')
            self.atomlist.append(at)
        self.natom = len(self.atomlist)

    def read_from_xyz(self, filename: str) -> None:
        """
        Reads the coordinates of the atoms in the molecule from an XYZ file.

        Parameters:
            filename (str): The name of the XYZ file to read.

        Returns:
            None
        """
        with open(filename, "r") as f:
            for line in f:
                tmp = line.split()
                if len(tmp) == 4:
                    symbol = tmp[0]
                    coord = np.array([float(x) for x in tmp[1:]]) / a0
                    at = Atom(symbol, coord)
                    self.atomlist.append(at)
        self.natom = len(self.atomlist)

    def get_basis(self, name: str = "sto-3g") -> None:
        """
        Computes the basis functions for the molecule using the 
        specified basis set.

        Parameters:
            name (str): The name of the basis set to use. Default is "sto-3g".

        Returns:
            None
        """
        self.basisfunctions = []
        # Initialize BasisSet instance
        basis = BasisSet(name=name)
        # Generate unique list of symbols
        elementlist = set([at.symbol for at in self.atomlist])
        # Return basis dictionary
        basis = basis.get_basisfunctions(elementlist)
        for at in self.atomlist:
            bfunctions = basis[at.symbol]
            for bf in bfunctions:
                newbf = copy.deepcopy(bf)
                newbf.set_A(at.coord)
                self.basisfunctions.append(newbf)
### ANCHOR_END: molecule_base
    ### ANCHOR: molecule_overlap
    def get_S(self) -> None:
        """
        Computes the overlap integrals between basis functions and sets 
        the `S` attribute.

        Returns:
            None
        """
        nbf = len(self.basisfunctions)
        self.S = np.zeros((nbf, nbf))
        for i in np.arange(0, nbf):
            for j in np.arange(i, nbf):
                self.S[i,j] = self.basisfunctions[i].S(self.basisfunctions[j])
                self.S[j,i] = self.S[i,j]
    ### ANCHOR_END: molecule_overlap
    ### ANCHOR: molecule_kinetic
    def get_T(self) -> None:
        nbf = len(self.basisfunctions)
        self.T = np.zeros((nbf, nbf))
        for i in np.arange(0, nbf):
            for j in np.arange(i, nbf):
                self.T[i,j] = self.basisfunctions[i].T(self.basisfunctions[j])
                self.T[j,i] = self.T[i,j]
    ### ANCHOR_END: molecule_kinetic
    ### ANCHOR: molecule_nuclear_attraction
    def get_Vij(self, i, j) -> float:
        v_int = 0.0
        for at in self.atomlist:
            v_int -= at.atnum \
                * self.basisfunctions[i].VC(self.basisfunctions[j], at.coord)
        return v_int

    def get_V(self) -> None:
        nbf = len(self.basisfunctions)
        self.Ven = np.zeros((nbf, nbf))
        for i in np.arange(nbf):
            for j in np.arange(i, nbf):
                self.Ven[i, j] = self.get_Vij(i, j)
                self.Ven[j, i] = self.Ven[i, j]
    ### ANCHOR_END: molecule_nuclear_attraction
    ### ANCHOR: molecule_electron_repulsion
    def get_twoel(self):
        nbf = len(self.basisfunctions)
        self.twoel = np.zeros((nbf, nbf, nbf, nbf))
        for i in np.arange(nbf):
            print(f'i: {i+1}/{nbf}...')
            for j in np.arange(nbf):
                print(f'  j: {j+1}/{nbf}...')
                for k in np.arange(nbf):
                    for l in np.arange(nbf):
                        self.twoel[i, j, k, l] \
                            = self.basisfunctions[i].twoel(
                                self.basisfunctions[j],
                                self.basisfunctions[k],
                                self.basisfunctions[l]
                            )   
    ### ANCHOR_END: molecule_electron_repulsion

