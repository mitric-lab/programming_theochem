#!/usr/bin/env python

import sympy as sp
from sympy.abc import x, y

### ANCHOR: limit
x = sp.symbols('x')
f = sp.sin(x) / x
lim = sp.limit(f, x, 0)
assert lim == sp.sympify(1)
### ANCHOR_END: limit

### ANCHOR: one_side_limit
f = sp.sympify(1) / x
rlim = sp.limit(f, x, 0, '+')
assert rlim == sp.oo

llim = sp.limit(f, x, 0, '-')
assert llim == -sp.oo
### ANCHOR_END: one_side_limit

### ANCHOR: first_derivative
x, y = sp.symbols('x y')
f = x**3 + y**3 + sp.cos(x * y) + sp.exp(x**2 + y**2)
f1 = sp.diff(f, x)
### ANCHOR_END: first_derivative

### ANCHOR: 2_3_derivative
f2 = sp.diff(f, x, x)
f3 = sp.diff(f, (x, 3))
### ANCHOR_END: 2_3_derivative

### ANCHOR: x_y_derivative
f4 = sp.diff(f, x, y)
### ANCHOR_END: x_y_derivative


### ANCHOR: substitution
f = x**3 + y**3 + sp.cos(x*y) + sp.exp(x**2 + y**2)
f3 = sp.diff(f, (x, 3))
g = f3.subs(y, 0)
h = f3.subs(y, x)
i = f3.subs(y, sp.exp(x))
j = f3.subs([(x, 1), (y, 0)])
### ANCHOR_END: substitution

### ANCHOR: indefinit_integral
f = sp.exp(-x)
f_int = sp.integrate(f, x)
### ANCHOR_END: indefinit_integral

### ANCHOR: definit_integral
f = sp.exp(-x)
f_dint = sp.integrate(f, (x, 0, sp.oo))
assert f_dint == sp.sympify(1)
### ANCHOR_END: definit_integral

### ANCHOR: multivariable_integral
f = sp.exp(-x**2 - y**2)
f_dint = sp.integrate(f, (x, -sp.oo, sp.oo), (y, -sp.oo, sp.oo))
assert f_dint == sp.pi
### ANCHOR_END: multivariable_integral

