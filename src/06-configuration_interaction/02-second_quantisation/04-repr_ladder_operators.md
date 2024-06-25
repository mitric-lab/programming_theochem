### Representation of Ladder Operators

Although it is very elegant to perform calculations by hand with ladders 
operators as abstract objects, it is not very practical to implement 
numerical calculations with them. In order to do so, we need to find a 
representation of the ladder operators in terms of matrices. 

```admonish note
The representation presented here is called the 
*Jordan-Wigner representation*. There are other equally valid 
representations as well.
```

#### Representation for one site
Consider a system with just one site. This can only have two possible 
states, $\ket{0}$ and $\ket{1}$. Because these states should 
be orthonormal, one of the most natural representations is the following:
$$
\ket{0} \rightarrow \begin{pmatrix} 1 \\ 0 \end{pmatrix} \quad
\ket{1} \rightarrow \begin{pmatrix} 0 \\ 1 \end{pmatrix}
$$

You can check that this representation is indeed orthonormal with respect 
to the standard inner product. 

How can we represent the ladder operators in this basis? We can use the 
properties of the creation operator:
$$
a^\dagger \ket{0} = \ket{1} \quad \text{and} \quad
a^\dagger \ket{1} = 0
$$

We can construct the matrix representation by applying the operator to 
an arbitrary state vector $|k\rangle$ and exploiting the linearity:
$$
\begin{aligned}
  a^\dagger \ket{k}
  &= a^\dagger \left( \lambda_0 \ket{0} + \lambda_1 \ket{1} \right) 
    \rightarrow a^\dagger \begin{pmatrix} \lambda_0 \\ \lambda_1 \end{pmatrix} \\
  &= \lambda_0 a^\dagger \ket{0} + \lambda_1 a^\dagger \ket{1} \\
  &= \lambda_0 \ket{1} + 0 \\
  &= \lambda_0 \ket{1} + 0 \ket{0} \\ 
  &\rightarrow \lambda_0 \begin{pmatrix} 0 \\ 1 \end{pmatrix} + 
    0 \begin{pmatrix} 1 \\ 0 \end{pmatrix} \\
  &= \begin{pmatrix} 0 + 0 \\ \lambda_0 + 0 \end{pmatrix} \\
  &= \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} 
    \begin{pmatrix} \lambda_0 \\ \lambda_1 \end{pmatrix}
\end{aligned}
$$
Hence,
$$
a^\dagger \rightarrow \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}
$$
And for the annihilation operator, its Hermitian conjugate:
$$
a \rightarrow \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}
$$

Since we know that a successive application of two creation or two 
annihihilation operators will certainly destroy the state vector, the 
corresponding matrices must be zero, i.e.:
$$
(a^\dagger)^2 = a^2 = 0
$$
where $0$ stands for the null matrix. You can check that this is 
indeed the case by explicitly squaring the matrices above. Square matrices, 
whose $k$-th power is zero, are called *nilpotent* matrices. So our 
representation matrices of the ladder operators are nilpotent (with an 
index of 2).

Therefore, two anti-commutation relations
$$
\{a^\dagger, a^\dagger\} = \{a, a\} = 0
$$
are automatically satisfied. 

We can check the last relation by explicit calculation. Although it can 
be done relatively easily by hand, it will become more and more tedious 
as the number of sites increases. Therefore, we will use SymPy for this.

After importing SymPy, we can define the ladder operators as matrices:
```python
{{#include ../../codes/06-configuration_interaction/repr_sq.py:imports}}
```
```python
{{#include ../../codes/06-configuration_interaction/repr_sq.py:define_ladder_operators}}
```

Addition and Multiplication of SymPy matrices can be done with the ordinary 
operators `+` and `*`, so we can calculate the anti-commutator as follows:
```python
{{#include ../../codes/06-configuration_interaction/repr_sq.py:anticommutator_one_site}}
```

This should give us the identity matrix $\identity_2$, which is the 
representation of one in this basis.

#### Representation for two sites
Now let's consider a system with two sites. The basis states are now 
tensor products of the basis states of the one-site system:
$$
|k_1 k_2\rangle = |k_1\rangle \otimes |k_2\rangle
$$
Using the representation of the one-site system, we find out
$$
\ket{0 0} \rightarrow \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} \quad
\ket{0 1} \rightarrow \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} \quad
\ket{1 0} \rightarrow \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix} \quad
\ket{1 1} \rightarrow \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}
$$
We can verify this using SymPy:
```python
{{#include ../../codes/06-configuration_interaction/repr_sq.py:two_site_basis}}
```

```admonish tip title="Relation to Binary Numbers"
The abstract state vector ($\ket{k_1, \cdots, k_M}$) is represented by
the occupation number of each sites. Since every site can be either
unoccupied (0) or occupied (1) for a pure state, this abstract vector 
can be treated as a
binary number, e.g. $\ket{00} \rightarrow 00_2 = 0_{10}$, 
$\ket{10} \rightarrow 10_2 = 2_{10}$, etc.

The column vectors of pure states in this representation are
standard basis vectors of the tensor product space, i.e. they have a
single one and all other entries are zero. If we take a closer look at the
(zero-based) index of the one in the column vector, we can see that it 
corresponds to the binary number of the abstract state vector.

Therefore, to retrieve the abstract state vector from the column vector,
we can simply convert the index of the one to a binary number.
```

Since the ladder operators 
for different sites (anti-)commute, i.e. they do not affect the other site, 
one may come up with the idea to represent the ladder operators using 
a tensor product of the identity matrix and the representation for one-site 
systems, i.e.
$$
a_1^{(\dagger)} \rightarrow a^{(\dagger)} \otimes \identity_2 \quad 
a_2^{(\dagger)} \rightarrow \identity_2 \otimes a^{(\dagger)}
$$
or in SymPy:
```python
{{#include ../../codes/06-configuration_interaction/repr_sq.py:ladder_operators_two_sites_naive}}
```
You can play around with the representations and check that they manipulate 
the basis states correctly. 

Using the mixed-product property of the tensor product, i.e. 
$ (\mathbf{A} \otimes \mathbf{B}) (\mathbf{C} \otimes \mathbf{D}) = 
(\mathbf{A} \mathbf{C}) \otimes (\mathbf{B} \mathbf{D}) $, we can 
see 
$$
\begin{aligned}
  (a_1^{(\dagger)})^2 &= (a^{(\dagger)})^2 \otimes (\identity_2)^2 = 0 \\ 
  (a_2^{(\dagger)})^2 &= (\identity_2)^2 \otimes (a^{(\dagger)})^2 = 0
\end{aligned}
$$
because the nilpotency of the one-site ladder operators. 

So, the anticommuation relations 
$$
\{a_p^\dagger, a_p^\dagger\} = \{a_p, a_p\} = 0\quad \text{for } p = 1, 2
$$
are again automatically satisfied. We can also verify the anti-commutation 
relation
$$
\{a_p^\dagger, a_p\} = 1\quad \text{for } p = 1, 2
$$
```python
{{#include ../../codes/06-configuration_interaction/repr_sq.py:anticommutator_two_sites_naive}}
```
However, the excitement is short-lived, because the anticommuation relations 
on different sites are not satisfied:
$$
\{a_1^\dagger, a_2^\dagger\} \neq 0 \quad \{a_1, a_2\} \neq 0 \quad
\{a_1^\dagger, a_2\} \neq 0 \quad \{a_1, a_2^\dagger\} \neq 0
$$
However, if we take the commutator instead of the anticommutor, we find 
that they are zero. Therefore, we have obtained a representation of the 
ladder operators for hard-core bosons, i.e. bosons with the property that 
there can be at most one boson per site. This might be of some interest 
but we are looking for a representation for fermions. So we must modify 
our representation a bit.

Let us examine the defining equation of the creation operator:
$$
  a_p^{\dagger} | \vec{k} \rangle = 
    \delta_{k_p, 0} \Gamma_p^{\vec{k}} | k_1, \cdots, 1_p, \cdots, k_M \rangle
$$
with
$$
  \Gamma_p^{\vec{k}} = \prod_{q=1}^{p-1} (-1)^{k_q}
$$
So, the creation operator at site $p$ should count the number of 
particles on previous sites and collect a factor of $1$ or $-1$ 
for unoccupied or occupied sites, respectively. Therefore, we cannot use the 
identity matrix for the tensor product, since it only returns $1$. 

We now define the matrix
$$
\sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$
Apply it of $\ket{0}$ and $\ket{1}$, we can see that it gives 
us $1$ and $-1$, respectively, exactly what we want. Since the ladder operator
should not affect the sites after it, the identity matrix should still be 
used for sites after it. This leads to the following representation:
$$
a_1^{(\dagger)} \rightarrow a^{(\dagger)} \otimes \identity_2 \quad
a_2^{(\dagger)} \rightarrow \sigma_z \otimes a^{(\dagger)} \quad
$$
or in SymPy:
```python
{{#include ../../codes/06-configuration_interaction/repr_sq.py:ladder_operators_two_sites}}
```
Feel free to play around with the representation and verify that it 
manupulates the basis states correctly. Note that this time
$$
  a_2^\dagger |1 0\rangle = - |1 1\rangle
$$
where the minus sign correctly reflects $\Gamma_2^{\vec{k}}$.

It can be verified that all anticommuation relations are satisfied 
using the representation;
```python
{{#include ../../codes/06-configuration_interaction/repr_sq.py:anticommutator_two_sites}}
```
The "trivial" anticommutation relations
$$
\{a_p^\dagger, a_p^\dagger\} = \{a_p, a_p\} = 0\quad \text{for } p = 1, 2
$$
are omitted in the code snippet, because they are again automatically 
satisfied due to the nilpotency of the one-site ladder operators.

#### Generalisation to $M$ sites
With the idea of the representation for two sites, we can generalize it 
to $M$ sites. The ladder operators are represented as
$$
a_p^{(\dagger)} \rightarrow \sigma_z^{\otimes (p-1)} \otimes 
  a^{(\dagger)} \otimes \identity_2^{\otimes (M-p)}
$$

In English, the ladder operator at site $p$ is represented as 
the tensor product of $M$ $2 \times 2$ matrices, where the first 
$p-1$ ones are $-\sigma_z$, the $p$-th one is $a^{(\dagger)}$, 
and the last $M-p$ ones are $\identity_2$.


