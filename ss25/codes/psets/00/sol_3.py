#!/usr/bin/env python

### ANCHOR: import
import sympy as sp
from IPython.display import display

x, z = sp.symbols('x z')
m = sp.Symbol('m', positive=True)
omega = sp.Symbol('omega', positive=True)
n = sp.Symbol('n', integer=True, nonnegative=True)
### ANCHOR_END: import

### ANCHOR: integrate
def integrate(expr):
    return sp.integrate(expr, (x, -sp.oo, sp.oo))
### ANCHOR_END: integrate

### AMCHOR: hermite
def hermite_direct(n):
    h_n = (-1)**n * sp.exp(z**2) * sp.diff(sp.exp(-z**2), (z, n))
    h_n = sp.simplify(h_n)
    return h_n
### ANCHOR_END: hermite

### ANCHOR: wf
def wfn(n):
    nf = (1/sp.sqrt(2**n * sp.factorial(n))) \
         * ((m*omega)/sp.pi)**sp.Rational(1, 4)
    expf = sp.exp(-(m*omega*x**2)/2)
    hp = hermite_direct(n).subs(z, sp.sqrt(m*omega)*x)
    psi_n = sp.simplify(nf * expf * hp)

    return psi_n
### ANCHOR_END: wf

### ANCHOR: get_sigma_x
def get_sigma_x(psi):
    x_mean = integrate(sp.conjugate(psi) * x * psi)
    x_mean = sp.simplify(x_mean)
    x_rms = integrate(sp.conjugate(psi) * x**2 * psi)
    x_rms = sp.simplify(x_rms)
    
    var_x = x_rms - x_mean**2
    sigma_x = sp.sqrt(var_x)
    
    return sigma_x, x_mean, x_rms
### ANCHOR_END: get_sigma_x

### ANCHOR: get_sigma_p
def get_sigma_p(psi):
    p_mean = integrate(sp.conjugate(psi) * (-sp.I) * sp.diff(psi, x))
    p_mean = sp.simplify(p_mean)
    p_rms = integrate(sp.conjugate(psi) * (-sp.I)**2 * sp.diff(psi, x, x))
    p_rms = sp.simplify(p_rms)

    var_p = p_rms - p_mean**2
    sigma_p = sp.sqrt(var_p)
    
    return sigma_p, p_mean, p_rms
### ANCHOR_END: get_sigma_p

### ANCHOR: print
sp.init_printing()

for i in range(0, 5):
    psi = wfn(i)
    
    sigma_x, x_mean, x_rms = get_sigma_x(psi)
    sigma_p, p_mean, p_rms = get_sigma_p(psi)
    product = sp.simplify(sigma_x * sigma_p)
    
    display((i, (x_mean, x_rms, p_mean, p_rms), (sigma_x, sigma_p), product))
### ANCHOR_END: print
