#!/usr/bin/env python

from hypothesis import given
import hypothesis.strategies as st

### ANCHOR: bad_mul
def bad_mul(a, b):
    if a > 10 and b > 20:
        return 0
    else:
        return a * b
### ANCHOR_END: bad_mul

### ANCHOR: test_bad_mul
@given(st.integers(), st.integers())
def test_bad_mul(a, b):
    assert bad_mul(a, b) == a * b
### ANCHOR_END: test_bad_mul

