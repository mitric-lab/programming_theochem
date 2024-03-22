#!/usr/bin/env python

### ANCHOR: imports
import matplotlib.pyplot as plt
from molecule import Molecule
### ANCHOR_END: imports

### ANCHOR: calculate_nuclear_attractions
ethene = Molecule()
ethene.read_from_xyz('ethene.xyz')
ethene.get_basis('sto-3g')
ethene.get_V()
nuclear_attractions = ethene.Ven
### ANCHOR_END: calculate_nuclear_attractions

### ANCHOR: plot_nuclear_attractions
fig, ax = plt.subplots(figsize=(4, 4))
ax.matshow(nuclear_attractions)

fig.tight_layout()
plt.show()
### ANCHOR_END: plot_nuclear_attractions
fig.savefig('../../src/figures/03_molecular_integrals/ethene_kinetic.svg')

### ANCHOR: pyscf_nuclear_attractions
import numpy as np
from pyscf import gto

mol = gto.M(atom='ethene.xyz', basis='sto-3g')
nuclear_attractions_pyscf = mol.intor("int1e_nuc", hermi=1)
print(np.allclose(nuclear_attractions, nuclear_attractions_pyscf))
### ANCHOR_END: pyscf_nuclear_attractions

