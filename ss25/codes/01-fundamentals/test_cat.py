#!/usr/bin/env python

import pytest

def cat(a, b):
    assert isinstance(a, str)
    assert isinstance(b, str)
    return a + b

### ANCHOR: example_test
@pytest.mark.parametrize('a, b, expected', [('Hello', 'World', 'HelloWorld')])
def test_cat_example(a, b, expected):
    assert cat(a, b) == expected
### ANCHOR_END: example_test

### ANCHOR: property_test
@pytest.mark.parametrize('a, b', [('Hello', 'World')])
def test_cat_property(a, b):
    out = cat(a, b)
    assert a == out[:len(a)]
    assert b == out[len(a):]
### ANCHOR_END: property_test
