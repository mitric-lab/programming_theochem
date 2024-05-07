# Molecular Integrals

<!-- ch0 -->

In quantum chemistry, the very well-known Hartree-Fock (HF) method is used to 
approximate the ground-state electronic structure of a molecule. The method 
involves solving the HF equation, which is given by
$$
\hat{f} | \varphi_i \rangle = \epsilon_i | \varphi_i \rangle
$$
where $\hat{f}$ is the Fock operator, $| \varphi_i \rangle $ is 
the $i$-th eigenfunction, $\epsilon_i$ is the corresponding eigenvalue. 
We identify the eigenfunction with canonical molecular orbitals and the 
eigenvalues with orbital energies.

The Fock operator is defined as
$$
\hat{f} = \hat{h}^{\mathrm{core}} + \sum_{j=1}^{N} \left( \hat{J}_j - \hat{K}_j \right)
$$
with the one-electron Hamiltonian $\hat{h}^{\mathrm{core}}$, the Coulomb 
operator $\hat{J}_j$ and the exchange operator $\hat{K}_j$, and $N$ 
stands for the number of electrons.

Since $\hat{h}^{\mathrm{core}}$ contains differential operators and 
$\hat{J}_j$ and $\hat{K}_j$ have integrals in them, the HF equation 
is an integro-differential equation, for which a closed-form solution is 
extremely difficult to obtain and analytical solutions are only known for 
the simplest cases. 

Therefore, we utilize numerical methods to solve the HF equation. 
Though popular in other fields, discretisation is very impractical here. 
Considering the rapid change of electronic density from nuclei to bonds and 
bond lengths of roughly 1 Å, at least 4 points per Å should be used for a 
crude representation of the wavefunction. Also, we should add a boundary to 
properly describe the fall-off of the wavefunction. For a medium-sized molecule, 
e.g. porphin, which is around 10 Å across, a box of the dimension 
15 Å × 15 Å × 5 Å would be appropriate, which translates to 60 × 60 × 20 = 72000 
grid points. This is far from practical. If we wish for a finer granulated grid or 
calculations for larger molecules, discretization will become infeasible rather quickly.

So, the spatial grid is a very inefficient basis for the HF equation. Because 
the molecule consists of atoms, it should be possible to represent the 
molecular orbitals with some sort of combination of atomic orbitals. The simplest 
combination is the linear combination. In this case, our basis is 
*atom-centered wavefunctions* $\chi_\mu$, and the molecular orbitals can be 
expressed as
$$
| \varphi_i \rangle = \sum_{\mu} c_{\mu i} \chi_\mu
$$
where $\mu$ indexes the atomic basis functions.

Inserting this Ansatz into the HF equation and projecting both sides 
onto $\langle \chi_\nu|$, we obtain
$$
\begin{align}
  \langle \chi_\nu | \hat{f} | \sum_{\mu} c_{\mu i} \chi_\mu \rangle &= \epsilon_i  \langle \chi_\nu | \sum_{\mu} c_{\mu i} \chi_\mu \rangle \\
  \sum_{\mu} \langle \chi_\nu | \hat{f} | \chi_\mu \rangle c_{\mu i} &= \sum_{\mu} \langle \chi_\nu | \chi_\mu \rangle c_{\mu i} \epsilon_i \\
  \mathbf{F}\vec{c}_i &= \mathbf{S}\vec{c}_i\epsilon_i
\end{align}
$$
where $\mathbf{F}$ is the Fock matrix, 
$\vec{c}_i$ is the coefficient vector of the $i$-th molecular orbital, 
$\mathbf{S}$ is the overlap matrix, 
and $\epsilon_i$ is the energy of the $i$-th molecular orbital.

The new equation is called the Roothaan-Hall equation, where the difficult 
derivatives and integrals of the unknown molecular orbitals are reduced to 
derivatives and integrals of known basis functions. After evaluating these 
integrals in $\mathbf{F}$ and $\mathbf{S}$, the actual solving step 
is easily done using some linear algebra.

A closer inspection of the matrices $\mathbf{F}$ and $\mathbf{S}$
reveals that four types of molecular integrals exist:
- Overlap integrals: $\langle \chi_\mu | \chi_\nu \rangle$
- Kinetic energy integrals: $\langle \chi_\mu | -\frac{1}{2} \nabla^2 | \chi_\nu \rangle$
- nuclear attraction integrals: $\langle \chi_\mu | -Z_{\mathrm{nuc}}/R_{\mathrm{nuc}} | \chi_\nu \rangle$
- electron repulsion integrals: $\langle \mu \nu | \lambda \sigma \rangle$

In this chapter, some basic concepts of basis functions will be introduced, 
followed by symbolic calculation of closed-form expressions for molecular 
integrals. In the end, we will use these expressions to generate a module, 
which performs all these integrals.
