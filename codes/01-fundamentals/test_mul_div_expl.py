#!/usr/bin/env python

### ANCHOR: import
from multiplication import mul
from division import div
### ANCHOR_END: import

### ANCHOR: example_test
def test_mul_example():
    assert mul(3, 8) == 24

def test_div_example():
    assert div(17, 3) == 5
### ANCHOR_END: example_test

### ANCHOR: parametrized_example_test
import pytest

@pytest.mark.parametrize(
    'a, b, expected', 
    [(3, 8, 24), (7, 4, 28), (14, 11, 154), (8, 53, 424)],
)
def test_mul_param_example(a, b, expected):
    assert mul(a, b) == expected

@pytest.mark.parametrize(
    'a, b, expected', 
    [(17, 3, 5), (21, 7, 3), (31, 2, 15), (6, 12, 0)],
)
def test_div_param_example(a, b, expected):
    assert div(a, b) == expected
### ANCHOR_END: parametrized_example_test

### ANCHOR: random_example_test
from random import randrange

N = 50

def test_mul_random_example():
    for _ in range(0, N):
        a = randrange(1_000)
        b = randrange(1_000)
        assert mul(a, b) == a * b

def test_div_random_example():
    for _ in range(0, N):
        a = randrange(1_000)
        b = randrange(1_000)
        assert div(a, b) == a // b
### ANCHOR_END: random_example_test

