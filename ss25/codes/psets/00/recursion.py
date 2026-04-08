#!/usr/bin/env python

### ANCHOR: factorial_recursive
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)
### ANCHOR_END: factorial_recursive

### ANCHOR: factorial_iterative
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
### ANCHOR_END: factorial_iterative

### ANCHOR: cache_usage
from functools import lru_cache

@lru_cache(maxsize=4)
def lucas_number(n):
    ...
### ANCHOR_END: cache_usage
