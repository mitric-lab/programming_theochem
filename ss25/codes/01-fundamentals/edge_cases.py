#!/usr/bin/env python

### ANCHOR: zero_division_err
def div_err(a, b):
    if b == 0:
        raise ZeroDivisionError
    ...
### ANCHOR_END: zero_division_err

### ANCHOR: zero_division_none
def div_none(a, b):
    if b == 0:
        return None
    ...
### ANCHOR_END: zero_division_none

### ANCHOR: negative_input_err
def mul_err(a, b):
    if a < 0 or b < 0:
        raise ValueError
    ...
### ANCHOR_END: negative_input_err

### ANCHOR: negative_input_none
def mul_none(a, b):
    if a < 0 or b < 0:
        return None
    ...
### ANCHOR_END: negative_input_none
