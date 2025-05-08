#!/usr/bin/env python

### ANCHOR: imports
import sympy as sp
from sympy.physics.quantum import TensorProduct
### ANCHOR_END: imports

### ANCHOR: define_ladder_operators
a_dag = sp.Matrix([[0, 0], [1, 0]])
a = sp.Matrix([[0, 1], [0, 0]])
### ANCHOR_END: define_ladder_operators

### ANCHOR: anticommutator_one_site
print('Anticommutator of a_dag and a:')
print('{a_dag, a}:', a_dag * a + a * a_dag)
### ANCHOR_END: anticommutator_one_site

### ANCHOR: two_site_basis
s_0 = sp.Matrix([[1], [0]])
s_1 = sp.Matrix([[0], [1]])

s_00 = TensorProduct(s_0, s_0)
s_01 = TensorProduct(s_0, s_1)
s_10 = TensorProduct(s_1, s_0)
s_11 = TensorProduct(s_1, s_1)

print('Basis states:')
print('|00>:', s_00)
print('|01>:', s_01)
print('|10>:', s_10)
print('|11>:', s_11)
### ANCHOR_END: two_site_basis

### ANCHOR: ladder_operators_two_sites_naive
a_dag_1_p = TensorProduct(a_dag, sp.eye(2))
a_dag_2_p = TensorProduct(sp.eye(2), a_dag)
a_1_p = TensorProduct(a, sp.eye(2))
a_2_p = TensorProduct(sp.eye(2), a)
### ANCHOR_END: ladder_operators_two_sites_naive

### ANCHOR: anticommutator_two_sites_naive
print('Anticommutator of a_dag_i_p and a_i_p:')
print('{a_dag_1, a_1}:', a_dag_1_p * a_1_p + a_1_p * a_dag_1_p)
print('{a_dag_2, a_2}:', a_dag_2_p * a_2_p + a_2_p * a_dag_2_p)
### ANCHOR_END: anticommutator_two_sites_naive

### ANCHOR: ladder_operators_two_sites
sigma_z = sp.Matrix([[1, 0], [0, -1]])

a_dag_1 = TensorProduct(a_dag, sp.eye(2))
a_dag_2 = TensorProduct(sigma_z, a_dag)
a_1 = TensorProduct(a, sp.eye(2))
a_2 = TensorProduct(sigma_z, a)
### ANCHOR_END: ladder_operators_two_sites

### ANCHOR: anticommutator_two_sites
print('Anticommutator of a_(dag)_i and a_(dag)_j:')
print('{a_dag_1, a_1}:', a_dag_1 * a_1 + a_1 * a_dag_1)
print('{a_dag_2, a_2}:', a_dag_2 * a_2 + a_2 * a_dag_2)
print('{a_dag_1, a_2}:', a_dag_1 * a_2 + a_2 * a_dag_1)
print('{a_dag_2, a_1}:', a_dag_2 * a_1 + a_1 * a_dag_2)
print('{a_dag_1, a_dag_2}:', a_dag_1 * a_dag_1 + a_dag_1 * a_dag_1)
print('{a_1, a_2}:', a_1 * a_2 + a_2 * a_1)
### ANCHOR_END: anticommutator_two_sites

