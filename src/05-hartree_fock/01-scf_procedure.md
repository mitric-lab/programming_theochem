## The SCF Procedure

Because the Fock operator itself depends on its solutions, the
Hartree-Fock equation, or rather the Rothaan-Hall equation, cannot
be solved using conventional eigenvalue solvers. 

### Summary of the Procedure

The SCF procedure in the (restricted) Hartree-Fock approximation can be 
summarised as follows:

1. Specify a molecule and a basis set.
2. Calculate all required molecular integrals 
   (overlap integrals $\bm{S}$, 
   kinetic energy integrals $\bm{T}$,
   nuclear attraction integrals $\bm{V}_\mathrm{ne}$,
   electron repulsion integrals $(\mu\nu|\sigma\lambda)$.
3. Calculate the transformation matrix $\bm{X} = \bm{S}^{-1/2}$.
4. Obtain a guess for the density matrix $\bm{P}$.
5. Calculate the matrix $\bm{G}$ from the density matrix using 
   $G_{\mu\nu} = \sum_{\lambda\sigma} P_{\lambda\sigma} [ (\mu\nu|\sigma\lambda) - \frac{1}{2} (\mu\lambda|\sigma\nu) ]$.
6. Obtain the Fock matrix $\bm{F} = \bm{H^{\mathrm{core}}} + \bm{G}$, where 
   $\bm{H^{\mathrm{core}}} = \bm{T} + \bm{V}_\mathrm{ne}$.
7. Calculate the transformed Fock matrix $\bm{F}' = \bm{X}^\dagger \bm{F} \bm{X}$
8. Diagonalize the transformed Fock matrix $\bm{F}'$ to obtain the 
   orbital energies $\varepsilon\_i$ and the transformed MO coefficients 
   $\bm{C}'$.
9. Transform the MO coefficients back to the original basis set 
   $\bm{C} = \bm{X} \bm{C}'$.
10. Form a new density matrix $\bm{P}$ from $\bm{C}$
    using $P_{\mu\nu} = 2 \sum_{i=1}^{n_{\mathrm{occ}}} C_{\mu i} C_{\nu i}$.
11. Check for convergence. If not, return to step 5 with the new density matrix.
12. If the procedure has converged, calculate the quantities of interest 
    (e.g. total energy, dipole moment, etc.) from the converged solution.

### Implementation

We can implement the Hartree-Fock procedure in a Python class. Since we want 
to access lots of properties of the molecule, it is convenient to pass the
molecule object to the constructor of the `HartreeFock` class.
```python
{{#include ../codes/05-hartree_fock/hartree_fock.py:hartree_fock_class}}
```
The convergence criterion is chosen as the absolute difference between the
total SCF energy of two consecutive iterations. The total SCF energy is
given by
$$
  E_{\mathrm{SCF}} = \frac{1}{2} \sum_{\mu\nu} (H_{\mu\nu}^{\mathrm{core}} + F_{\mu\nu}) P_{\nu\mu}\,.
$$

Now we test our HF implementation on the water molecule using the STO-3G basis set.
```python
{{#shiftinclude -4:../codes/05-hartree_fock/hartree_fock.py:hartree_fock_water}}
```
We get the final (electronic) energy of $E_\mathrm{SCF} = -84.143659\ \mathrm{a.u.}$ 
To obtain the total HF energy, the nuclear repulsion energy $E_\mathrm{ne}$ 
has to be added to it.

