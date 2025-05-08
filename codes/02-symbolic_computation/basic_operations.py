#!/usr/bin/env python

import sympy as sp

### ANCHOR: expression
x, y = sp.symbols('x y')
f = x + 2 * y
### ANCHOR_END: expression

### ANCHOR: f_times_x
g = x * f
### ANCHOR_END: f_times_x

### ANCHOR: expand
g_expanded = sp.expand(g)
### ANCHOR_END: expand

### ANCHOR: factor
g_factorized = sp.factor(g_expanded)
### ANCHOR_END: factor

### ANCHOR: complicated_expression
t, omega = sp.symbols('t omega')
f = sp.sqrt(2) / sp.sympify(2) * sp.exp(-t) * sp.cos(omega*t)
### ANCHOR_END: complicated_expression

### ANCHOR: function_one_arg
f_func1 = sp.Lambda(t, f)
### ANCHOR_END: function_one_arg

### ANCHOR: function_two_args
f_func2 = sp.Lambda((t, omega), f)
### ANCHOR_END: function_two_args

### ANCHOR: function_call_one
f_func1(1)
### ANCHOR_END: function_call_one

### ANCHOR: function_call_two
f_func2(sp.Rational(1, 2), 1)
### ANCHOR_END: function_call_two

### ANCHOR: numeric_function
import math
f_num = sp.lambdify((t, omega), f)
assert math.isclose(f_num(0, 1), math.sqrt(2)/2)
### ANCHOR_END: numberic_function

### ANCHOR: expression_to_python_float
f_01_expr = f.subs([(t, 0), (omega, 1)])
f_01_expr_num = float(f_01_expr)
assert math.isclose(f_01_expr_num, math.sqrt(2)/2)
### ANCHOR_END: expression_to_python_float

### ANCHOR: expression_to_sympy_float
f_01_expr = f.subs([(t, 0), (omega, 1)])
f_01_expr_num = f_01_expr.evalf()
f_01_expr_num2 = f_01_expr.evalf(50)
### ANCHOR_END: expression_to_sympy_float

