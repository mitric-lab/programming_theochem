#!/usr/bin/env python

### ANCHOR: import
from sympy.functions.special.spherical_harmonics import Ynm
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
### ANCHOR_END: import

### ANCHOR: func
l, m, theta, phi = sp.symbols("l m theta phi")
Ylm_sym = Ynm(l, m, theta, phi).expand(func=True)
Ylm = sp.lambdify((l, m, theta, phi), Ylm_sym) 
### ANCHOR_END: func

### ANCHOR: grid
N = 1000
theta = np.linspace(0, np.pi, N)
phi = np.linspace(0, 2*np.pi, N)
theta, phi = np.meshgrid(theta, phi)
### ANCHOR_END: grid

### ANCHOR: grid_cart
l = 3
m = 1

Ylm_num = Ylm(l, m, theta, phi)
r = np.abs(Ylm_num)

x = r * np.cos(phi) * np.sin(theta)
y = r * np.sin(phi) * np.sin(theta)
z = r * np.cos(theta)
### ANCHOR_END: grid_cart

### ANCHOR: plot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d")

colors = np.angle(Ylm_num)/(2.0*np.pi) + 0.5
ax.plot_surface(x, y, z, facecolors=cm.hsv(colors))

ax.set_xlim([-0.5, 0.5])
ax.set_ylim([-0.5, 0.5])
ax.set_zlim([-0.5, 0.5])

plt.show()
### ANCHOR_END: plot
