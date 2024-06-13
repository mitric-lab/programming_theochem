# The Hartree-Fock Approximation

With the molecular integrals evaluated in the previous section, we are now
able to perform quantum chemical calculations. One of the most basic methods
is the Hartree-Fock approximation, which is the starting point for many
more advanced methods. 

Since you should already be familiar with the Hartree-Fock approximation 
from the bachelor course on theoretical chemistry, we will only briefly 
summarise the algorithm in this lecture. A detailed derivation of the 
Hartree-Fock equation has been or will be covered in the master courses on 
quantum chemistry, and can alternatively be found 
<a href="assets/misc/Derivation_of_the_Hartree_Fock_Equation.pdf" target="_blank">here</a>.

The terms "Hartree-Fock equation" and "Roothaan-Hall equation" are often used
interchangeably, although there is a subtle difference:
```admonish note title="Hartree-Fock vs. Roothaan-Hall Equation"
The Hartree-Fock equation refers to the integro-differential equation
$$
  \hat{f} \varphi_k (x) = \varepsilon_k \varphi_k (x),
$$
where $\varphi_k (x) \in L^2 (\mathbb{R}^3)$ are the molecular orbitals,
and $\hat{f}: L^2 (\mathbb{R}^3) \rightarrow L^2 (\mathbb{R}^3)$ is the 
Fock operator, which operates on the molecular orbitals.

By introducing a approximative, atom-centred basis set, the Hartree-Fock
equation can be transformed into a matrix equation, the Roothaan-Hall equation:
$$
  \bm{F} \vec{c}_k = \varepsilon_k \bm{S} \vec{c}_k,
$$
where $\vec{c}_k \in \mathbb{R}^N$ are the expansion coefficients of the
molecular orbitals in the basis set, with $N$ being the number of basis 
functions, and $\R{N}{N} \ni \bm{F}: \mathbb{R}^N \rightarrow \mathbb{R}^N$
is the matrix representation of the Fock operator in the selected basis set,
which operates on the vector of expansion coefficients. The overlap matrix
$\bm{S} \in \R{N}{N}$ arises due to the non-orthogonality of the 
atom-centred basis functions.

Since computers cannot handle infinite-dimensional spaces, the Hartree-Fock
equation, which involves continuous functions, cannot be solved directly. 
Therefore, the Roothaan-Hall equation is implemented in quantum chemistry
programmes under the name "Hartree-Fock", although it is actually only an
approximation to the true Hartree-Fock equation.
```

