#!/usr/bin/env python

### ANCHOR: import
import sympy as sp
from sympy.abc import x, m, omega, n, z
### ANCHOR_END: import

### ANCHOR: energy
def energy(n):
    e = omega * (n + sp.Rational(1, 2))
    return e

e_5 = energy(5)
### ANCHOR_END: energy

### ANCHOR: hermite_definition
def hermite_direct(n):
    h_n = (-1)**n * sp.exp(z**2) * sp.diff(sp.exp(-z**2), (z, n))
    h_n = sp.simplify(h_n)
    return h_n
### ANCHOR_END: hermite_definition

### ANCHOR: hermite_recursive
def hermite_recursive(n):
    if n == 0:
        return sp.sympify(1)
    else:
        return sp.simplify(
            2 * x * hermite_recursive(n - 1) \
            - sp.diff(hermite_recursive(n - 1), x)
        )
### ANCHOR_END: hermite_recursive

### ANCHOR: wave_function
def wfn(n):
    nf = (1/sp.sqrt(2**n * sp.factorial(n))) \
         * ((m*omega)/sp.pi)**sp.Rational(1, 4)
    expf = sp.exp(-(m*omega*x**2)/2)
    hp = hermite_direct(n).subs(z, sp.sqrt(m*omega)*x)
    psi_n = sp.simplify(nf * expf * hp)

    return psi_n

psi_5 = wfn(5)
### ANCHOR_END: wave_function

### ANCHOR: wave_function_param
psi_5_param = psi_5.subs([(m, 1), (omega, 1)])
### ANCHOR_END: wave_function_param

### ANCHOR: wave_function_param_plot
import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(-5, 5, 100)

fig, ax = plt.subplots(1, 1, figsize=(8, 5))
ax.set_xlabel('$x$')

ax.plot(x_values, 0.5 * x_values**2, c='k', lw=2)
for i in range(5):
    psi_param = wfn(i).subs([(m, 1), (omega, 1)])
    psi_numpy = sp.lambdify(x, psi_param)
    ax.plot(x_values, psi_numpy(x_values) + (0.5 + i), label=f'n = {i}')

ax.set_xlim(-4, 4)
ax.set_ylim(-0.1, 6.1)
ax.legend()

plt.show()
### ANCHOR_END: wave_function_param_plot
fig.savefig('../../src/figures/02_symbolic_computation/harm_osc.svg')

### ANCHOR: numpy_printer
from sympy.printing.numpy import NumPyPrinter
printer = NumPyPrinter()
code = printer.doprint(psi_5_param)
code = code.replace('numpy', 'np')
print(code)
### ANCHOR_END: numpy_printer
