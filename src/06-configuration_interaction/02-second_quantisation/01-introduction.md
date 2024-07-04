### Introduction

Quantum states of the first quantisation live in the Hilbert space, where the
number of particles is conserved. Because we want to have a description that
allows for the creation and annihilation of particles, we need to move to a
larger vector space, the Fock space. In this section, we will introduce the
Fock space and the operators that act on vectors in it.

#### The Fock Space
We already know that a first quantisation state with $N$ particles lives in 
the Hilbert space $\hat{A} \mathcal{H}^{\otimes N}$, where $\hat{A}$ 
is the antisymmetrisation operator and $\mathcal{H}$ is a single-particle 
Hilbert space. The notation $\mathcal{H}^{\otimes N}$ means that we 
take the tensor product of $\mathcal{H}$ with itself $N$ times, i.e. 
$$
  \mathcal{H}^{\otimes N} = 
  \underbrace{\mathcal{H} \otimes \cdots \otimes \mathcal{H}}_{n\ \text{times}}
$$

Since we want to allow an arbitrary number of particles in second 
quantisation, we must enter a larger space, the so-called *Fock space*. 
The Fock space is defined as the direct sum of all $N$-particle 
Hilbert spaces:
$$
  \mathcal{F} = \bigoplus_{N=0}^\infty \mathcal{H}^{\otimes N}
$$
We also include the $N=0$ case, which only contains the vacuum state 
$| \mathrm{vac} \rangle$. A determinant is represented by an 
occupation-number (ON) vector $\vec{k}$, 
$$
  | k \rangle = | k_1, k_2, \cdots, k_M \rangle, \quad k_p \in \{0, 1\}
$$
with $M$ single-particle states. The occupation numbers $k_p$ 
can either be 0 (empty) or 1 (occupied) due to the Pauli exclusion principle. 
The single-particle state is also called a *site* and can e.g. be an 
orbital.

Because we do not want to do difficult calculations with state vectors 
(except for the vacuum state), we must represent states by some 
(combination of) operators, something that generate all possible states 
in the Fock space from the vacuum state. 

#### Creation and Annihilation Operators
We want to define a creation operator $a_p^{\dagger}$ that 
creates a particle at site $p$. It should also take care of Pauli 
exclusion, i.e. it should destroy the state if site $p$ is already 
occupied. This leads to the following definition:
$$
\begin{align}
  a_p^{\dagger} | k_1, \cdots, 0_p, \cdots, k_M \rangle &= 
  \Gamma_p^{\vec{k}} | k_1, \cdots, 1_p, \cdots, k_M \rangle \\
  a_p^{\dagger} | k_1, \cdots, 1_p, \cdots, k_M \rangle &= 0
\end{align}
$$
where the phase factor $\Gamma_p^{\vec{k}}$ is defined as
$$
  \Gamma_p^{\vec{k}} = \prod_{q=1}^{p-1} (-1)^{k_q}
$$
So for every already occupied site $q$ before site $p$, we 
have to multiply the state with $-1$. This is necessary to ensure 
antisymmetry.

These two equations can be combined into a single one:
$$
  a_p^{\dagger} | \vec{k} \rangle = 
    \delta_{k_p, 0} \Gamma_p^{\vec{k}} | k_1, \cdots, 1_p, \cdots, k_M \rangle
$$
From the definition, it trivially follows that 
$$
  a_p^{\dagger} a_p^{\dagger} | \vec{k} \rangle = 0
$$

For two different creation operators $a_p^{\dagger}$ and 
$a_q^{\dagger}$, we can show the following:
$$
  (a_p^{\dagger} a_q^{\dagger} + a_q^{\dagger} a_p^{\dagger}) | \vec{k} \rangle = 0
$$

```admonish proof title="Proof" collapsible=true
Without loss of generality, we can assume $p < q$. It follows that
$$
\begin{align}
    a_p^\dagger a_q^\dagger | \cdots, k_p, \cdots, k_q, \cdots \rangle &= 
      a_p^\dagger \delta_{k_q 0} \Gamma_q^{\vec{k}} 
      |\cdots, k_p, \cdots, 1_q, \cdots \rangle \\
    &= \delta_{k_p 0} \delta_{k_q 0} \Gamma_p^{\vec{k}} \Gamma_q^{\vec{k}} 
      |\cdots, 1_p, \cdots, 1_q, \cdots \rangle
\end{align}
$$
since the phase factor $\Gamma_p^{\vec{k}}$ is not affected by the 
application of $a_q^\dagger$. Reversing the order of both operators, 
we obtain
$$
\begin{align}
    a_q^\dagger a_p^\dagger \cdots, k_p, \cdots, k_q, \cdots \rangle
      &= a_q^\dagger \delta_{k_p 0} \Gamma_p^{\vec{k}} 
      |\cdots, 1_p, \cdots, k_q, \cdots \rangle \\
    &= \delta_{k_p 0} \delta_{k_q 0} \Gamma_p^{\vec{k}} (-\Gamma_q^{\vec{k}}) 
      |\cdots, 1_p, \cdots, 1_q, \cdots \rangle
\end{align}
$$

This time, an extra factor of $-1$ appears since the application of 
$a_p^\dagger$ changes the parity for $a_q^\dagger$. Combining 
the two equations above, we can write
$$
    (a_p^\dagger a_q^\dagger + a_q^\dagger a_p^\dagger) |\vec{k}\rangle = 0
$$
which also holds for the case $p = q$.
```

The action of Hermitian adjoints $a_p$ on $|\vec{k} \rangle$ can be 
understood by inserting the identity
$$
a_p \ket{\vec{k}} = 
  \sum_{\vec{m}} \ket{\vec{m}} \braket{\vec{m} | a_p | \vec{k}}\,.
$$

The matrix element that has occured can be evaluated as
$$
\braket{\vec{m} | a_p | \vec{k}} = 
  \braket{\vec{k} | a_p^\dagger | \vec{m}}^* = 
  \delta_{m_p 0} \Gamma_p^{\vec{m}} \braket{\vec{k} | m_1, \cdots, 1_p, \cdots m_M}^*\,.
$$

The overlap $\langle \vec{k} | m_1, \cdots, 1_p, \cdots \rangle$ is 
nonzero if and only if both vectors are identical, which is the case when 
$]\vec{k} \rangle$ and $| \vec{m} \rangle$ only differ at position 
$p$, where $k_p = 1$ and $m_p = 0$. Therefore, this matrix element 
can also be written as

$$
\begin{align}
  \braket{\vec{m} | a_p | \vec{k}}
    &= \delta_{m_p 0} \delta_{k_p 1} \Gamma_p^{\vec{m}}
      \braket{ k_1, \cdots, 0_p, \cdots k_M | m_1, \cdots, 1_p, \cdots m_M}^* \\
    &= \delta_{m_p 0} \delta_{k_p 1} \Gamma_p^{\vec{m}}
      \braket{ m_1, \cdots, 1_p, \cdots m_M | k_1, \cdots, 1_p, \cdots k_M} \\
    &= \delta_{m_p 0} \delta_{k_p 1} \Gamma_p^{\vec{m}}
      \braket{ m_1, \cdots, 0_p, \cdots m_M | k_1, \cdots, 0_p, \cdots k_M} \\
    &= \delta_{k_p 1} \Gamma_p^{\vec{m}}
      \braket{ \vec{m} | k_1, \cdots, 0_p, \cdots k_M } \\
    &= \delta_{k_p 1} \Gamma_p^{\vec{k}} 
      \braket{ \vec{m} | k_1, \cdots, 0_p, \cdots k_M }\,,
\end{align}
$$
where we used the fact $\Gamma_p^{\vec{k}} = \Gamma_p^{\vec{m}}$, which 
follows directly from its definition. Therefore, only one term in the sum 
survives and we can conclude
$$
a_p |\vec{k} \rangle = 
  \delta_{k_p 1} \Gamma_p^{\vec{k}} | k_1, \cdots, 0_p, \cdots k_M \rangle\,.
$$

The operator $a_p$ removes the occupation at $p$ if occupied and 
returns zero if unoccupied. Therefore, we shall call it 
*annihilation* operator. A special case of the equation above is
$$
a_p |\mathrm{vac} \rangle = 0\,,
$$
which states that the annihilation operator destroys the vacuum state.

Since the annihilation operator is the Hermitian adjoint of the creation 
operator, we can follow
$$
  (a_p a_q + a_q a_p) | \vec{k} \rangle = 0\,.
$$

We can then examine the action of the action of one creation and one 
annihilation operator on a state vector $| \vec{k} \rangle$. 
After several algebraic transformations, it can be shown that
$$
  (a_p^\dagger a_q + a_q a_p^\dagger) | \vec{k} \rangle = \delta_{pq}\,.
$$

```admonish proof title="Proof" collapsible=true
For $p = q$, we have
$$
\begin{align}
  a_p^\dagger a_p \ket{\cdots, k_p, \cdots} 
    &= a_p^\dagger \delta_{k_p 1} \Gamma_p^{\vec{k}} \ket{\cdots, 0_p, \cdots} \\
    &= \delta_{k_p 1} (\Gamma_p^{\vec{k}})^2 \ket{\cdots, 1_p, \cdots} \\
    &= \delta_{k_p 1} \ket{\cdots, 1_p, \cdots} = \delta_{k_p 1} \ket{\vec{k}}
\end{align}
$$
and
$$
\begin{align}
  a_p a_p^\dagger \ket{\cdots, k_p, \cdots} 
    &= a_p \delta_{k_p 0} \Gamma_p^{\vec{k}} \ket{\cdots, 1_p, \cdots} \\
    &= \delta_{k_p 0} \Gamma_p^{\vec{k}} \ket{\cdots, 0_p, \cdots} \\
    &= \delta_{k_p 0} \ket{\cdots, 0_p, \cdots} = \delta_{k_p 0} \ket{\vec{k}}\,.
\end{align}
$$
Adding both equations, we obtain
$$
  (a_p^\dagger a_p + a_p a_p^\dagger) \ket{\vec{k}} 
    = (\delta_{k_p 1} + \delta_{k_p 0}) \ket{\vec{k}}
    = \ket{\vec{k}}\,,
$$
or, because the state vector $\ket{\vec{k}}$ is arbitrary, we can write
$$
  (a_p^\dagger a_p + a_p a_p^\dagger) = 1\,.
$$

For $p < q$, we have
$$
\begin{align}
  a_p^\dagger a_q \ket{\cdots, k_p, \cdots, k_q, \cdots}
   &= a_p^\dagger \delta_{k_q 1} \Gamma_q^{\vec{k}} \ket{\cdots, k_p, \cdots, 0_q, \cdots} \\
   &= \delta_{k_p 0} \delta_{k_q 1} \Gamma_p^{\vec{k}} \Gamma_q^{\vec{k}} \ket{\cdots, 1_p, \cdots, 0_q, \cdots}
\end{align}
$$
and
$$
\begin{align}
  a_q a_p^\dagger \ket{\cdots, k_p, \cdots, k_q, \cdots}
   &= a_q \delta_{k_p 0} \Gamma_p^{\vec{k}} \ket{\cdots, 1_p, \cdots, k_q, \cdots} \\
   &= -\delta_{k_p 1} \delta_{k_q 0} \Gamma_p^{\vec{k}} \Gamma_q^{\vec{k}} \ket{\cdots, 1_p, \cdots, 0_q, \cdots}\,.
\end{align}
$$
The minus sign arises because the application of $a_q$ is affected by
the previous application of $a_p^\dagger$, which changes the occupation
of site $p$ that comes before site $q$. Adding both equations, we obtain
$$
  (a_p^\dagger a_q + a_q a_p^\dagger) \ket{\vec{k}} = 0\,,
$$
or
$$
  (a_p^\dagger a_q + a_q a_p^\dagger) = 0\,.
$$

The case $p > q$ can be obtained by complex conjugation of the case $p < q$ 
and exchanging the dummy indices $p$ and $q$.

Combining all three cases, we obtain
$$
  (a_p^\dagger a_q + a_q a_p^\dagger) = \delta_{pq}\,.
$$
```

We have now worked out the action of two ladder operators (creation or 
annihilation operator) on an arbitrary state vector. Since it works for 
all possible states, we can as well write the equations solely in terms 
of operators:
$$
\begin{align}
  \{a_p^\dagger, a_q^\dagger\} &= 0 \\
  \{a_p, a_q\} &= 0 \\
  \{a_p^\dagger, a_q\} &= \delta_{pq}
\end{align}
$$
where $\{A, B\} = AB + BA$ is the anticommutator. These relations are 
known as the *anticommutation relations* of the ladder operators and can be 
viewed as the defining property of the ladder operators.

Now we know how to represent states using operators in second quantisation. 
But how do observables look like? 

#### Operators in Second Quantisation
We shall at first take a look at one-particle operators 
$\hat{O}_1 = \sum_{i} \hat{o}(i)$, where $\hat{o}(i)$ 
is the one-particle operator acting on the $i$-th particle. By inserting 
the identity to the left and right of the operator, we obtain
$$
  \hat{O}_1 = \sum_{i} \hat{o}(i) = \sum_{i} \sum_{\vec{k}, \vec{k}'}
    \ket{\vec{k}} \braket{\vec{k} | \hat{o}(i) | \vec{k}'} \bra{\vec{k}'}
$$

Suppose the $i$-th particle is on the $p$-th site in the state
$\ket{\vec{k}}$ and $q$-th site in the state $\ket{\vec{k}'}$. 
Then we can replace the sum over $i$ by a sum over $p$ and $q$.
Because the operator $\hat{o}(i)$ 
acts only on the $i$-th particle, the matrix element 
$\braket{\vec{k} | \hat{o}(i) | \vec{k}'}$ evaluates to
$$
\braket{\vec{k} | \hat{o}(i) | \vec{k}'} = 
  \braket{\vec{k} \setminus p | \braket{p | \hat{o}(i) | q} | \vec{k}' \setminus q}
  = o_{pq} \braket{\vec{k} \setminus p | \vec{k}' \setminus q}
$$
where $\ket{\vec{k} \setminus p}$ (sloppily) denotes the state 
vector $\ket{\vec{k}}$ with the $p$-th site removed. But we
already know how to (formally) remove a site from a state vector, namely 
by applying the annihilation operator $a_p$. Therefore, we can write 
the overlap as 
$$
  \braket{\vec{k} \setminus p | \vec{k}' \setminus q} 
    = \braket{a_p \vec{k} | a_q \vec{k}'} 
    = \braket{\vec{k} | a_p^\dagger a_q | \vec{k}'}
$$

Putting everything together, we obtain 
$$
  \hat{O}_1 = \sum_{pq} o_{pq} a_p^\dagger a_q
$$

We can see that a one-particle operator is represented by linear combination 
of creation-annihilation pairs weighted by the matrix elements of the 
one-site operator $\hat{o}(i)$.

We can perform the same calculating for two-particle operators by inserting 
a total of four identities and arrive at 
$$
  \hat{O}_2 = \frac{1}{2} \sum_{pqrs} o_{pqrs} a_p^\dagger a_r^\dagger a_s a_q
$$
with 
$$
  o_{pqrs} = (pq | \hat{o}(i, j) | rs)
$$

So, a molecular electronic Hamiltonian in the language of second quantisation 
is given by
$$
\begin{align}
  \hat{H} &= \hat{h} + \hat{g} \\
  &= \sum_{pq} h_{pq} a_p^\dagger a_q + 
    \frac{1}{2} \sum_{pqrs} g_{pqrs} a_p^\dagger a_r^\dagger a_s a_q
\end{align}
$$
where
$$
\begin{align}
  h_{pq} &= \int \phi_p^{*}(x) 
    \left( -\frac{1}{2} \nabla^2 - \sum_{I=1}^{N} \frac{Z_I}{|r - R_I|} \right) 
    \phi_q(x)\ \mathrm{d}x \\
  g_{pqrs} &= \int \phi_p^{*}(x_1) \phi_r^{*}(x_2)
    \frac{1}{|r_1 - r_2|} \phi_q(x_1) \phi_s(x_2)\ \mathrm{d}x_1 \mathrm{d}x_2
\end{align}
$$

Now with the representation of the observables and states in second 
quantisation, we can evaluate matrix elements. Since all states are 
represented by a product of creation operators acting on the vacuum, 
a matrix element of, say, a one-electron operator would look like this:
$$
  \langle \mathrm{vac} | a_{r_1} \cdots a_{r_k} 
    \ (o_{pq} a_p^\dagger a_q)\ 
    a_{s_1}^\dagger \cdots a_{s_l}^\dagger | \mathrm{vac} \rangle
$$
Ignoring the number $o_{pq}$, we have a product of ladder operators 
in the middle, also known as a *string*. For two-electron operators, the 
situation is similar, just with two additional operators. 


