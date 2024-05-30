#!/usr/bin/env python

### ANCHOR: imports
import numpy as np
from mayavi import mlab
### ANCHOR_END: imports

### ANCHOR: constants
R_VDW = {
    'H': 2.0787,
    'C': 3.2125,
    'N': 2.9291,
    'O': 2.8724,
}

R_COV = {
    'H': 0.6047,
    'C': 1.4173,
    'N': 1.3417,
    'O': 1.1905,
}

ATOM_COLOR = {
    'H': (0.8, 0.8, 0.8),
    'C': (0.0, 1.0, 0.0),
    'N': (0.0, 0.0, 1.0),
    'O': (1.0, 0.0, 0.0),
}
### ANCHOR_END: constants

### ANCHOR: evaluate_gaussian_basis_function
def evaluate_gaussian_basis(g, x, y, z):
    i, j, k = g.ijk
    x0, y0, z0 = g.A
    g_val = 0.0
    for n, d, alpha in zip(g.norm_const, g.coefs, g.exps):
        g_val += n * d * (x - x0)**i * (y - y0)**j * (z - z0)**k \
            * np.exp(-alpha * ((x - x0)**2 + (y - y0)**2 + (z - z0)**2))
    return g_val
### ANCHOR_END: evaluate_gaussian_basis_function


### ANCHOR: build_grid_function
def build_grid(xlim, ylim, zlim, nx, ny, nz):
    x_ = np.linspace(*xlim, nx)
    y_ = np.linspace(*ylim, ny)
    z_ = np.linspace(*zlim, nz)
    x, y, z = np.meshgrid(x_, y_, z_, indexing='ij')
    return x, y, z
### ANCHOR_END: build_grid_function


### ANCHOR: evaluate_mo_grid_function
def evaluate_mo_grid(mol, grid, mo_energy, mo_coeff):
    x, y, z = grid
    
    # Build MO coefficient matrix in spin-orbital basis
    n_spatial_orb = len(mo_energy)
    c_spin = np.zeros((n_spatial_orb * 2, n_spatial_orb * 2))
    c_spin[:n_spatial_orb:, ::2] = mo_coeff
    c_spin[n_spatial_orb:, 1::2] = mo_coeff
    
    # Evaluate AOs on the grid
    ao_grid = np.zeros((n_spatial_orb * 2, 
                        x.shape[0], x.shape[1], x.shape[2]))
    
    for i, g in enumerate(mol.basisfunctions):
        g_grid = evaluate_gaussian_basis(g, x, y, z)
        ao_grid[i] = g_grid
        ao_grid[i + n_spatial_orb] = g_grid
    
    # Transform to MOs
    mo_grid = np.einsum('ij,ixyz->jxyz', c_spin, ao_grid)
    
    return mo_grid
### ANCHOR_END: evaluate_mo_grid_function


### ANCHOR: visualize_cube_function
def visualize_cube(mol, grid, density, isovalues, colors, figure, **kwargs):
    # Draw atoms
    for a in mol.atomlist:
        p = mlab.points3d(
            *a.coord, R_VDW[a.symbol], color=ATOM_COLOR[a.symbol], 
            scale_factor=0.5, figure=figure,
        )
    
    # Draw bonds
    for i, a in enumerate(mol.atomlist):
        ca = a.coord
        sa = a.symbol
        ra = R_COV[sa]
        for b in mol.atomlist[:i]:
            cb = b.coord
            sb = b.symbol
            rb = R_COV[sb]
            
            vab = cb - ca
            rab = np.linalg.norm(vab)
            if rab < (ra + rb) * 1.2:
                mid = ca + vab * (ra / (ra + rb))
                p = mlab.plot3d(*np.vstack((ca, mid)).T, tube_radius=0.2, 
                                color=ATOM_COLOR[sa], figure=figure)
                p = mlab.plot3d(*np.vstack((cb, mid)).T, tube_radius=0.2, 
                                color=ATOM_COLOR[sb], figure=figure)

    # Draw isosurface
    for ival, c in zip(isovalues, colors):
        p = mlab.contour3d(*grid, density, color=c, contours=[ival], 
                           figure=figure, **kwargs)
    
    return p
### ANCHOR_END: visualize_cube_function

