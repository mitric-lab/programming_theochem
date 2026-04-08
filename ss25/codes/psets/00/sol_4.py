#!/usr/bin/env python

### ANCHOR: lucas_number
def lucas_number(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas_number(n - 1) + lucas_number(n - 2)
### ANCHOR_END: lucas_number

### ANCHOR: lucas_number_cache
from functools import lru_cache


@lru_cache(maxsize=4)
def lucas_number_cache(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas_number_cache(n - 1) + lucas_number_cache(n - 2)
### ANCHOR_END: lucas_number_cache

from time import perf_counter

### ANCHOR: timeit
def timeit(func, *args, **kwargs):
    start = perf_counter()
    func(*args, **kwargs)
    end = perf_counter()
    return end - start
### ANCHOR_END: timeit

# time three implementations
N = 35
print(timeit(lucas_number, N))
print(timeit(lucas_number_cache, N))


### ANCHOR: hermite_recursive
import sympy as sp


def hermite_recursive(n, z):
    if n == 0:
        return sp.sympify(1)
    elif n == 1:
        return sp.sympify(2) * z
    else:
        return sp.simplify(
            2 * z * hermite_recursive(n - 1, z) \
            - 2 * (n - 1) * hermite_recursive(n - 2, z)
        )
### ANCHOR_END: hermite_recursive

z = sp.Symbol('z')
print(hermite_recursive(4, z))
print(hermite_recursive(5, z))
