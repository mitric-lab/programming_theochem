## Configuration Interaction Singles

The configuration interaction singles (CIS) method applies a truncated CI 
wavefunction up to single excitations to a reference determinant, usually 
the Hartree-Fock determinant:
$$
  \ket{\Psi^n_{\mathrm{CIS}}} = c_0^n \ket{\Phi_0} 
    + \sum_{ia} c_{ia}^n \ket{\Phi_i^a}\,.
$$
The CIS matrix thus takes the form
$$
  \bm{H} =
  \left(
  \begin{array}{c|c}
    \braket{\Phi_0 | \hat{H} | \Phi_0} 
      & \hspace{4em} \braket{\Phi_0 | \hat{H} | \Phi_i^a} \hspace{4em} \\ 
    \hline
    \\
    \\
    \\
    \\
    \\
    \braket{\Phi_i^a | \hat{H} | \Phi_0} & \braket{\Phi_i^a | \hat{H} | \Phi_j^b}
    \\
    \\
    \\
    \\
    \\
    \\
  \end{array}
  \right)\,.
$$

### Theoretical Background

We shall assume for simplicity that the reference determinant is the 
Hartree-Fock determinant. This makes our calculation easier, because 
the Brillouin condition is satisfied and the reference determinant does 
not interact with singly excited determinants, i.e. 
$\langle \Phi_0 | \hat{H} | \Phi_i^a \rangle = 0$. This makes our CIS 
matrix block diagonal. Since the first block is just the Hartree-Fock 
energy, we only have to calculate the second block: 
$\langle \Phi_i^a | \hat{H} | \Phi_j^b \rangle$ explicitly. 

After some algebraical magic, we arrive at 
$$
\langle \Phi_i^a | \hat{H} | \Phi_j^b \rangle = 
  (E_0 + \epsilon_a - \epsilon_i) \delta_{ij} \delta_{ab} + 
  (jb|ai) - (ji|ab)
$$

It should be noted that the two-electron integrals are required in the 
MO basis, so we have to transform them from the AO basis:
$$
(pq|rs) = \sum_{\mu \nu \sigma \lambda} 
  C_{\mu p}^* C_{\nu q} C_{\sigma r}^* 
  C_{\lambda s} (\mu \nu | \sigma \lambda)
$$
where $C_{\mu p}$ is the $\mu$-th AO coefficient of the 
$p$-th MO. 

For computational efficiency, this transformation is usually done
in 4 steps, with one summation performed at each step. This reduces
the computational complexity from $O(N^8)$ for a direct transformation
to $O(N^5)$.

### Implementation

We can now implement the CIS method. Since we need several quantities from 
the Hartree-Fock calculation, it is convenient to let the `CIS` class inherit 
from the `HartreeFock` class. 
```python
{{#include ../codes/06-configuration_interaction/cis.py:imports_and_constants}}
```
```python
{{#include ../codes/06-configuration_interaction/cis.py:cis_class}}
```

The method `get_cis_hamiltonian` is the centerpiece of the CIS class. It 
ar first transforms the ERIs to the MO basis, spin-blocks them, and the 
enumerates all singly excited determinants. The CIS Hamiltonian is then 
constructed from the transformed ERIs and the MO energies. 
 
The spin-blocking is useful, since we can obtain excited states with all 
possible spin multiplicities. Although it is not necessary for CIS, since 
only singlets and triplets are obtainable from a singlet reference, it 
will become very useful when higher excitations are included.

```admonish note
Although spin-blocking will ease the implementation of higher 
excitations, it makes our algorithm less efficient. First of all, each 
dimension of the spin-blocked ERIs is twice as large as the original 
one, which makes it 16 times as big. Secondly, since states with different 
spin multiplicities are orthogonal in the absence of spin-orbit coupling, 
we only have to include some determinants (actually some carefully chosen 
linear combinations of determinants called configuration state functions) 
in the CI expansion. This will reduced the size of the CI matrix greatly 
when higher excitations are present.
```

The method `run_cis` takes the CIS hamiltonian and diagonalizes it. The 
eigenvalues are the excitation energies, and the eigenvectors are the 
coefficients of the excited determinants in the CIS wavefunction. This method 
also prints details about the loewest excited states.

Now we can test our implementation on the water molecule. 
```python
{{#shiftinclude -4:../codes/06-configuration_interaction/cis.py:cis_water}}
```
A section of the console output is shown below:
```txt
Excited State   1: E_exc =    11.0619 eV
4a   -> 5a      -0.707107 (50.0 %)
4b   -> 5b       0.707107 (50.0 %)

Excited State   2: E_exc =    11.0619 eV
4a   -> 5b      -0.997462 (99.5 %)

Excited State   3: E_exc =    11.0619 eV
4b   -> 5a       0.997462 (99.5 %)

Excited State   4: E_exc =    13.1605 eV
4a   -> 5a      -0.707107 (50.0 %)
4b   -> 5b      -0.707107 (50.0 %)
```

It can be seen that the first three excited states are degenerate, 
and their orbital contributions indicate that they are all
triplet states with $S_z = 0, -1, +1$. The fourth state is a singlet state
built from an equal mixture of 2 singly excited determinants.

We could again plot the density here for the excited states. Since the 
Slater determinants are orthogonal, the total (one-electron) density is 
just the sum of the densities of the individual determinants. 

But with excited states, we can plot something more interesting: the 
transition density. Its definition is strongly motivated by the 
spin-free one-electron density:
$$
  \rho_{fi}(r) = \int \Psi_f^{*}(x, x_2, \cdots, x_N)\ \Psi_i(x, x_2, \cdots, x_N) 
    \ \mathrm{d}\sigma \mathrm{d}x_2 \cdots \mathrm{d}x_N
$$
So we have two different wavefunctions in the integral, one for the 
initial state $\Psi_i$ and one for the final state $\Psi_f$, instead 
of just one in the case of the density. This makes the transition density 
technically not a density, since it is not positive definite. 

For a transition density from the ground state to a singly excited state, 
we can simplify the expression to
$$
  \rho_{fi}(r) = \sum_{i,a} c_{ia} \int \phi_a^{*}(x) \phi_i(x)\ \mathrm{d}\sigma
$$

Using the functions we have written in section [5.1.1](ch04-01a-plot_grid_data.md), 
we can calculate and visualize the transition 
density of water:
```python
{{#include ../codes/06-configuration_interaction/transition_density.py:construct_grid}}
```
```python
{{#include ../codes/06-configuration_interaction/transition_density.py:water_td}}
```
Since our $\alpha$ orbitals have even indices and $\beta$ orbitals 
have odd indices, the if statement ensures that we only include orbital 
pairs with the same spin. The resulting figure is shown below. 

<p style="text-align:center">
  <img src="../assets/figures/06-configuration_interaction/water_transition_density.png" alt="water transition density">
</p>

Despite the word "density" in its name, the transition density is not
a density in the usual sense, because it can be negative, as we can
see from the blue isosurface.

