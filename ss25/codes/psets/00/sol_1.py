#!/usr/bin/env python

### ANCHOR: naive_div
def naive_div(a, b):
    r = -1
    while a >= 0:
        a -= b
        r += 1
    return r, a + b
### ANCHOR_END: naive_div

### ANCHOR: div
def div(a, b):
    n = a.bit_length()
    tmp = b << n
    r = 0
    for _ in range(0, n + 1):
        r <<= 1
        if tmp <= a:
            a -= tmp
            r += 1
        tmp >>= 1
    return r, a
### ANCHOR_END: div
