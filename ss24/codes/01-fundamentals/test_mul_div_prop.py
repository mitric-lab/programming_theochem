#!/usr/bin/env python

from multiplication import mul
from division import div

### ANCHOR: import
from hypothesis import given
import hypothesis.strategies as st
### ANCHOR_END: import

### ANCHOR: test_mul
@given(st.integers(), st.integers())
def test_mul_property(a, b):
    assert mul(a, b) == a * b
### ANCHOR_END: test_mul

### ANCHOR: test_mul_non_neg
@given(st.integers(min_value=0), st.integers(min_value=0))
def test_mul_property_non_neg(a, b):
    assert mul(a, b) == a * b
### ANCHOR_END: test_mul_non_neg

### ANCHOR: test_div
@given(st.integers(), st.integers())
def test_div_property(a, b):
    assert div(a, b) == a // b
### ANCHOR_END: test_div

### ANCHOR: test_div_non_neg
@given(st.integers(min_value=0), st.integers(min_value=1))
def test_div_property_no_zero(a, b):
    assert div(a, b) == a // b
### ANCHOR_END: test_div_non_neg
