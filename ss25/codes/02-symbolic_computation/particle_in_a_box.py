#!/usr/bin/env python

### ANCHOR: import
import sympy as sp
from sympy.physics.quantum.constants import hbar

x, N = sp.symbols('x N')
a = sp.Symbol('a', positive=True)
n = sp.Symbol('n', integer=True, positive=True)
### ANCHOR_END: import

### ANCHOR: define_integral
def integrate(expr):
    return sp.integrate(expr, (x, 0, a))
### ANCHOR_END: define_integral

### ANCHOR: normalization
wf = N * sp.sin((n*sp.pi/a) * x)
norm = integrate(wf**2)
N_e = sp.solve(sp.Eq(norm, 1), N)[1]
### ANCHOR_END: normalization

### ANCHOR: wave_function
psi = N_e * sp.sin((n*sp.pi/a) * x)
### ANCHOR_END: wave_function

### ANCHOR: sigma_x
x_mean = integrate(sp.conjugate(psi) * x * psi)
x_mean = sp.simplify(x_mean)
x_rms = integrate(sp.conjugate(psi) * x**2 * psi)
x_rms = sp.simplify(x_rms)

var_x = x_rms - x_mean**2
sigma_x = sp.sqrt(var_x)
### ANCHOR_END: sigma_x

### ANCHOR: sigma_p
p_mean = integrate(sp.conjugate(psi) * (-sp.I*hbar) * sp.diff(psi, x))
p_mean = sp.simplify(p_mean)
p_rms = integrate(sp.conjugate(psi) * (-sp.I*hbar)**2 * sp.diff(psi, x, x))
p_rms = sp.simplify(p_rms)

var_p = p_rms - p_mean**2
sigma_p = sp.sqrt(var_p)
### ANCHOR_END: sigma_p

### ANCHOR: product
product = sigma_x * sigma_p
product = sp.simplify(prod)
p1 = prod.subs(n, 1)
### ANCHOR_END: product
