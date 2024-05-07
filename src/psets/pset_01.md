## Problem Set 1

The Extended Hückel Theory (EHT) is a semi-empirical method first 
introduced by Roald Hoffmann in 1963[^hoffmann_eht] to obtain (very) 
approximative solutions to the Schrödinger equation and gain an understanding 
of electronic structures and properties. In this problem set, you will at first 
implement a modification of the original EHT with functions and classes 
defined in the lecture. Afterwards, you will extend EHT with a repulsive 
potential, which enables its ability to perform geometry optimization.

We will use a version of the VSTO-3G 
(**V**alence-only **STO-3G**) basis set parametrised for EHT with the aim 
of geometry optimization throughout this problem set. 
This basis is adapted from the STO exponents fitted by 
Dixon and Jurs[^dixon_params] and the GTO expansion coefficients 
found by Stewart[^stewart_expansion]. You can download this basis set 
<a href="../codes/psets/01/vsto-3g.json" download>here</a>.

<span class="comment">
Note: We could in principle also use the "ordinary" STO-3G basis, 
but the other parameters have to be adjusted.
</span>

### Problem 1
The only kind of molecular integral needed by EHT is the overlap integral, 
which makes this method extremely easy to implement. We shall perform an 
exemplary EHT calculation on water:
```python
{{#include ../codes/psets/01/sol_1.py:atoms_in_water}}
```
**(a) Construct a water molecule as an instance of the class `Molecule` 
using these 3 atoms given. Afterwards, calculate the overlap matrix using 
the basis set provided above.** 

Expected result:

|        |        |        |        |        |        |
|--------|--------|--------|--------|--------|--------|
| 1.0000 | 0.0000 | 0.0000 | 0.0000 | 0.2152 | 0.2152 |
| 0.0000 | 1.0000 | 0.0000 | 0.0000 | 0.4014 | 0.0000 |
| 0.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 | 0.4014 |
| 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 |
| 0.2152 | 0.4014 | 0.0000 | 0.0000 | 1.0000 | 0.1515 |
| 0.2152 | 0.0000 | 0.4014 | 0.0000 | 0.1515 | 1.0000 |

---
&nbsp;

The Hamiltonian of our modified EHT is defined as 
$$
H_{ij} := 
\begin{cases}
\alpha_i & i = j\\
k_i k_j (H_{ii} + H_{jj}) S_{ij} & i \neq j
\end{cases}
{{numeq}}{eq:eht_hamiltonian}
$$
where $\alpha_i$ denotes the energy of the $i$-th atomic orbital (AO) 
and $k_i$ AO-dependent parameters. This notation might be misleading. To 
find $\alpha_i$ or $k_i$, you should at first identify the element associated 
with the $i$-th basis function and use $\alpha_{s/p}$ 
or $k_{s/p}$ of that element according to the angular momentum of the 
$i$-th basis function.

For H, C, N, and O, we shall use the following 
parameters:[^dixon_params]<sup>,</sup>[^anderson_alpha]

|              | H       | C       | N       |     O   |
|--------------|---------|---------|---------|---------|
| $\alpha_s$   | -13.6   | -21.4   | -26.0   | -32.3   |
| $\alpha_p$   |         | -11.4   | -13.4   | -14.8   |
| $k_s$        | 0.66836 | 0.88266 | 0.75747 | 0.84677 |
| $k_p$        |         | 0.58621 | 0.68272 | 0.76529 |

The AO energies $\alpha_{s/p}$ are given in the unit of eV.
Because we only use valence orbitals, <nobr>2 $\alpha$'s</nobr> and 
<nobr>2 $k$'s</nobr> are needed for C, N, and O, while H requires just 
<nobr>1 $\alpha$</nobr> and <nobr>1 $k$</nobr>.

```admonish info title="Note on the original EHT" collapsible=true
In the original formulation of EHT, the off-diagonal elements of the 
Hamiltonian is defined as
$$
H_{ij} := \frac{1}{2} K (H_{ii} + H_{jj}) S_{ij} \quad i \neq j
$$

where $K$ is an empirical global constant chosen to be 1.75 by Hoffmann. 
This parametrization was first discussed by Mulliken[^mulliken_hij] and used 
in a molecular calculation by Wolfsberg and Helmholz[^wolfsberg_hij]. 
```


**(b) Calculate the EHT Hamiltonian in the unit of 
[Hartree](https://en.wikipedia.org/wiki/Hartree) for the water molecule 
constructed in (a) using the parameters given above.** 

Expected result:

|        |         |         |         |          |          |
|-------:|--------:|--------:|--------:|---------:|---------:|
| -1.1870|   0.0000|   0.0000|   0.0000|  -0.2054 |  -0.2054 |
|  0.0000|  -0.5439|   0.0000|   0.0000|  -0.2143 |   0.0000 |
|  0.0000|   0.0000|  -0.5439|   0.0000|   0.0000 |  -0.2143 |
|  0.0000|   0.0000|   0.0000|  -0.5439|   0.0000 |   0.0000 |
| -0.2054|  -0.2143|   0.0000|   0.0000|  -0.4998 |  -0.0676 |
| -0.2054|   0.0000|  -0.2143|   0.0000|  -0.0676 |  -0.4998 |

---
&nbsp;

The energies of molecular orbitals (MOs) are obtained as solutions of the 
secular equation
$$
  \bm{H} \vec{c}_i = \epsilon_i \vec{c}_i
$$
with the Hamiltonian $\bm{H}$ defined in {{eqref: eq:eht_hamiltonian}} and
under the approximation of unit overlap, i.e. $\mathbf{S} = \identity$.
The orbital energies $\epsilon_i$ can thus be calculated as
eigenvalues of $\mathbf{H}$, while the eigenvectors $\vec{c}_i$ are the
expansion coefficients of the MOs in the basis of AOs (MO coefficients).

**(c) Calculate the MO energies in the unit of Hartree using the 
Hamiltonian obtained in (b) while neglecting the differential overlap.**

_Hint: The NumPy function 
[`np.linalg.eigh`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html)
could be helpful._

Expected result:

|              |        |        |        |        |        |        |
|--------------|:------:|:------:|:------:|:------:|:------:|:------:|
| $i$          | 1      | 2      | 3      | 4      | 5      | 6      |
| $\epsilon_i$ | -1.3105| -0.7095| -0.6964| -0.5439| -0.2913| -0.2665|

(The indices are 1-based.)

---
&nbsp;

The total electronic energy of the molecule is simply the sum of energies of 
all occupied (spatial) MOs multiplied by 2, assuming the 
$\epsilon$'s are in ascending order, i.e.
$$
E^{\mathrm{elec}} = 2 \sum_{i=1}^{N_\mathrm{occ}} \epsilon_i
$$
where $N_{\mathrm{occ}}$ stands for the number of occupied (spatial) MOs.

**(d) Calculate the total energy of the water molecule constructed in (a) 
using the orbital energies obtained in (c).**

Expected result:

$E^{\mathrm{elec}} = -6.5207\ \mathrm{a.u.}$


[^hoffmann_eht]: R. Hoffmann, _J. Chem. Phys._, **1963**, 39, 1397&ndash;1412.

[^dixon_params]: S. L. Dixon, P. C. Jurs, _J. Comput. Chem._, **1993**, 15, 733&ndash;746.

[^stewart_expansion]: R. F. Stewart, _J. Chem. Phys._, **1970**, 52, 431&ndash;438.

[^mulliken_hij]: R. S. Mulliken, _J. Chim. Phys._, **1949**, 46, 497&ndash;542.

[^wolfsberg_hij]: M. A. X. Wolfsberg, L. Helmholz, _J. Chem. Phys._, **1952**, 20, 837&ndash;843.

[^anderson_alpha]: A. B. Anderson, R. Hoffmann, _J. Chem. Phys._, *1974*, 60, 4271&ndash;4273.

---
&nbsp;

### Problem 2

```admonish tip
You can download the current version of the `Atom`, `Molecule`, `Gaussian`,
and `BasisSet` classes from chapter [3.0](../03-molecular_integrals/00-current_classes.md).
```


A kinetic energy integral between two centres $A$ and $B$ is 
defined as
$$
T_{ijk,lmn}^{A,B} = 
\int g_{ijk} (\vec{r}; \alpha, \vec{A}) 
\left(-\frac{1}{2} \nabla^2 \right)
g_{lmn} (\vec{r}; \beta, \vec{B})\ \mathrm{d}^3 \vec{r}\,.
$$

By expanding the Laplacian, we obtain
$$
T_{ijk,lmn}^{A,B} =
 T_{il}^{AB} S_{jm}^{AB} S_{kn}^{AB} +
 S_{il}^{AB} T_{jm}^{AB} S_{kn}^{AB} +
 S_{il}^{AB} S_{jm}^{AB} T_{kn}^{AB}\,,
$$
where 
$$
    T_{ij}^{AB} = -\frac{1}{2} \int g_{i} (r_p; \alpha, A_p)
    \ \frac{\partial^2}{\partial r_p^2}\ 
    g_{j} (r_p; \beta, B_p)\ \mathrm{d} r_p
$$
with $p \in \{x, y, z\}$ and $S_{ij}^{AB}$ is the overlap 
integral between the two basis functions $g_i$ and $g_j$ 
centered at $A$ and $B$, respectively, with $i$ and $j$ 
denoting their angular momenta.

**(a) Show that the 1-dimensional kinetic energy integral 
$T_{ij}^{AB}$ can be written as a linear combination of up to 
3 overlap integrals like**
$$
T_{ij}^{AB} = 
  -2 \beta^2 S_{i,j+2}^{A,B} + 
  \beta (2 j + 1) S_{i,j}^{A,B} - 
  \frac{1}{2} j (j - 1) S_{i,j-2}^{A,B}
$$

**(b) Generate symbolic expressions for the 1-dimensional kinetic energy 
integrals $T_{ij}^{AB}$ for $s$ and $p$ orbitals using SymPy. 
Wrap the expressions into a function called `t_ij` and write it **into a **Python** file called** `T.py`, just like we did for the overlap integrals in the 
lecture.**

*Hint: $S_{ij}^{AB} = 0$ for $i < 0$ or $j < 0$.*

**(c) Extend the `Gaussian` class with the method `T` to calculate the 
kinetic energy integrals between two Gaussian basis functions. Also, 
extend the `Molecule` class with the method `get_T` to calculate the 
kinetic energy matrix.**

We now take a look again at the water molecule from the last problem set:
```python
{{#include ../codes/psets/02/sol_1cd.py:atoms_in_water}}
```
**(d) Calculate the kinetic energy matrix for this water molecule using 
the standard STO-3G basis set.**

Expected result:

|          |          |          |          |          |          |          |
|---------:|---------:|---------:|---------:|---------:|---------:|---------:|
|  29.0032 |  -0.1680 |   0.0000 |   0.0000 |   0.0000 | -0.0051  | -0.0051  |
|  -0.1680 |   0.8081 |   0.0000 |   0.0000 |   0.0000 |  0.1090  |  0.1090  |
|   0.0000 |   0.0000 |   2.5287 |   0.0000 |   0.0000 |  0.2524  |   0.0000 |
|   0.0000 |   0.0000 |   0.0000 |   2.5287 |   0.0000 |   0.0000 |  0.2524  |
|   0.0000 |   0.0000 |   0.0000 |   0.0000 |   2.5287 |   0.0000 |   0.0000 |
| -0.0051  |   0.1090 |   0.2524 |   0.0000 |   0.0000 |  0.7600  |  0.0181  |
| -0.0051  |   0.1090 |   0.0000 |   0.2524 |   0.0000 |  0.0181  |  0.7600  |

