## Problem Set 2

### Problem 1

```admonish tip
You will need an implementation of the Extended Hückel Theory from 
problem set 1. If you did not manage to solve that problem, or if you are 
unsure about your solution, you can download an object-oriented implementation
from
<a href="../codes/psets/02/eht_calculator_pset_01.py" download>here</a>.
Its constructor takes an instance of the `Molecule` class and you can
use the method `get_electronic_energy()` to obtain the electronic energy.
```

As you may have already realised, the secular equation of Extended Hückel
Theory (EHT) as stated in problem set 1 was not solved iteratively, 
like in the case of HF. This is because EHT does not explicitly 
include any two-electron terms, which causes the Fock operator to depend on 
its eigenvectors. By only using a parametrised one-electron operator, EHT 
can be formulated as a (generalized) eigenvalue problem, rather than 
the pseudo eigenvalue problem in the case of HF.

This simplification, however, does not capture the repulsion between 
electrons associated with different atomic centres. One way to include this 
interaction (empirically) would be to assume that the electron-electron 
repulsion energy can be partitioned into pair-wise contributions of atoms, 
i.e.
$$
  E^{\mathrm{elec}}_{\mathrm{rep}} = \sum_{A < B} E^{\mathrm{elec}}_{AB}
$$

The empirical two-body expression found by Klopman[^klopman_repulsion] can 
be modified for our purpose as:[^dixon_params]

$$
  E^{\mathrm{elec}}_{AB} = V_0\ 
    \frac{z_A z_B}{\frac{r_{AB}}{1\ \mathrm{\AA}} + c_A + c_B}
    \exp\left[ -(a_A + a_B) \left( \frac{r_{AB}}{1\ \mathrm{\AA}} \right)^{b_A + b_B} \right]
$$

By construction of this formula, it should be obvious that the internuclear 
distance $ r_{AB} = \| \vec{R}_A - \vec{R}_B \| $ should be inserted 
in the unit of &#8491;. The scaling factor $V_0 = 0.52917721\ \mathrm{a.u.}$ 
compensates for this deviation from the use of atomic units. 
While $z_A$ and $z_B$ are the numbers of 
**valence** electrons on atoms $A$ and $B$, respectively, 
$a_{A/B}$, $b_{A/B}$ and $c_{A/B}$ are atom-specific parameters. 

For the given orbital parameters used in problem set 1, Dixon and Jurs 
optimized these electron-repulsion parameters (as well as the 
nuclear repulsion parameters $\delta$ and $\epsilon$ required in (b)), 
which are listed here:[^dixon_params]

|            | H        | C        | N        | O        |
|------------|----------|----------|----------|----------|
| $a$        | 0.70485  | 0.64786  | 0.60722  | 0.64781  |
| $b$        | 0.83541  | 0.94928  | 1.0975   | 1.0510   |
| $c$        | 0.29684  | 0.71224  | 2.0093   | 3.0455   |
| $\delta$   | 3.8163   | 1.1130   | 2.1880   | 2.2954   |
| $\epsilon$ | 1.2612   | 3.7686   | 2.5854   | 1.2897   |

We shall use the water molecule from problem set 1 again as an example:
```python
{{#include ../codes/psets/01/sol_2cd.py:atoms_in_water}}
```
for which the
<a href="https://codinginchemistry.com/files_SS23/pset_01/vsto-3g.json" download>VSTO-3G</a> 
basis set from the same problem set should be applied.

**(a) Calculate the electron-electron repulsion energy for this water molecule
using the empirical formula given above.**

Expected result:

$E^{\mathrm{elec}}_{\mathrm{rep}} = 0.3994\ \mathrm{a.u.}$

&nbsp;

We are now only missing one last ingredient for the total molecular energy: 
the nuclear repulsion energy. Because we only included valence electrons 
and parametrized the two-electron interaction, the usual formula for nuclear 
repulsion will not be accurate. Therefore, a parametrized version is needed:
$$
  E^{\mathrm{nuc}}_{AB} = V_0\ 
    \frac{z_A z_B}{\frac{r_{AB}}{1\ \mathrm{\AA}}}\ 
    \exp\left[ -(\delta_A + \delta_B) \left( \frac{r_{AB}}{1\ \mathrm{\AA}} \right)^{\epsilon_A + \epsilon_B} \right]
$$

This formula has a very similar structure to the electron-electron repulsion 
energy, with the scaling factor $V_0$, the number of valence electrons 
$z_A$ and $z_B$, and the internuclear distance $r_{AB}$ which 
should be inserted in the unit of &#8491;. The differences are the exact 
$1/r$ part without extra summands in the denominator, as well as the 
parameters $\delta_{A/B}$ and $\epsilon_{A/B}$, which have the same 
functionality as $a_{A/B}$ and $b_{A/B}$, respectively, but are 
different in values. These parameters for H, C, N, and O are listed in the 
table above.

**(b) Calculate the nuclei-nuclei repulsion energy for the water molecule 
constructed in (a) using the empirical formula given above.**

Expected result:

$E^{\mathrm{nuc}}_{\mathrm{rep}} = 0.0141\ \mathrm{a.u.}$

&nbsp;

The total energy of the molecule is then given by
$$
  E^{\mathrm{tot}} 
  = E^{\mathrm{elec}} + E^{\mathrm{elec}}_{\mathrm{rep}} 
    + E^{\mathrm{nuc}}_{\mathrm{rep}} 
  = E^{\mathrm{elec}} 
    + \sum_{A < B} \left( E^{\mathrm{elec}}_{AB} + E^{\mathrm{nuc}}_{AB} \right)
$$

**(c) Calculate the total energy for the water molecule constructed 
in (a).**

[^klopman_repulsion]: G. Klopman, _J. Am. Chem. Soc._, *1964*, 86, 4550&ndash;4557.

[^dixon_params]: S. L. Dixon, P. C. Jurs, _J. Comput. Chem._, **1993**, 15, 733&ndash;746.

---
&nbsp;

### Problem 2
The steepest descent method is simple, but plagued by several problems, one 
of which is its oscillatory behavior. If the objective function has a minimum 
located in an elongated valley, even if we choose a sufficiently small step 
size (which means painfully slow convergence), steepest descent will still 
zig-zag toward the solution. If the step size is too large, the method will 
either oscillate around the minimum or towards infinity.

An oscillation in numerical algorithms can often be fixed by introducing 
damping. In the case of steepest descent, we can combine the gradient 
descent direction with the previous descent direction to obtain an 
averaged direction, which should dampen the oscillations. This method is 
called conjugate gradient.

<span class="comment">
The conjugate gradient method is often combined with a line search 
to determine the optimal step size. We will use a fixed step size here 
for simplicity. 
</span>

The conjugate gradient algorithm can be described as follows:
1. Choose a starting point $x_0$ and a step size $\alpha$.
2. In the first iteration, perform a steepest descent step and save the 
   gradient $\nabla f(x_0)$. Set $s_0 = -\nabla f(x_0)$.
3. In the following iterations, calculate $\beta_k$.
4. If $\beta_k < 0$, set it to 0.
5. Calculate $s_{k} = \frac{-\nabla f(x_k) + \beta_k s_{k - 1}}{1 + \beta_k}$
6. Update the current point using $x_{k+1} = x_k + \alpha \cdot s_k$.
7. Repeat until the convergence criterion is met.

There are several ways to calculate $\beta_k$. We will use the 
Fletcher-Reeves formula:
$$
\beta_k = 
  \frac{\langle \nabla f(x_k), \nabla f(x_k) \rangle}
       {\langle \nabla f(x_{k-1}), \nabla f(x_{k-1}) \rangle}
$$

**(a) Implement the class `SimpleConjugateGradient` as a child class of 
`OptimiserBase`, which implements the conjugate gradient method described 
above. Use the method `_check_convergence_grad()` to check convergence.**

*Hint: Since several variables need to be updated in each 
iteration, it is recommended to define them in the constructor, for example 
like this:*
```python
{{#include ../codes/psets/02/sol_2.py:simple_conjugate_gradient_init}}
```

&nbsp;

**(b) Use `SimpleSteepestDescent` and `SimpleConjugateGradient` to optimize 
the Rosenbrock function with $a = 1$ and $b = 100$. Start from 
$x_0 = (0, 0)$, choose a step size of $\alpha=0.005$, and set the 
maximum iteration to 10000. Plot the optimization trajectory.**

*Hint: `SimpleSteepestDescent` is expected to diverge, while 
`SimpleConjugateGradient` should converge.*

Expected result:
![](../assets/figures/psets/02/conjugate_gradient.svg)

---
&nbsp;

### Problem 3

We have implemented the two-electron integrals in the lecture and you may 
have noticed that the evaluation is quite time-consuming. This is because 
of the $\mathcal{O}(N^4)$ scaling for calculating these integrals. 
Thankfully, there are some tricks we can use to speed up the calculation and 
we will implement two (easy) ones in this problem.

To test your implementation, you can use the water molecule, this time 
with a saner geometry:
```python
{{#include ../codes/psets/02/sol_3.py:water_molecule}}
```
The first trick is to exploit the 8-fold symmetry of two-electron integrals 
when real-valued basis functions are used, namely
$$
  (ij|kl) = (kl|ij) = (ji|lk) = (lk|ji) = (ji|kl) = (lk|ij) = (ij|lk) = (kl|ji)
$$
where the chemists' notation for two-electron integrals
$$
  (ij|kl) = \iint
  g_i (\vec{r}_1) g_j (\vec{r}_1)\ \frac{1}{r_{12}}\  
  g_k (\vec{r}_2) g_l (\vec{r}_2)\ 
  \mathrm{d}^3 \vec{r}_1 \mathrm{d}^3 \vec{r}_2\ 
$$
is used.

This way, we only have to calculate about 1/8 of all possible two-electron 
integrals when the number of basis functions is large.

**(a) Extend the `Molecule` class with the method `get_twoel_symm`, 
which calculates the two-electron integrals exploiting the 8-fold symmetry.**

*Hint: You can apply the `get_twoel` method from the lecture on the water 
molecule (or just the O atom) and check if the result is the same as that 
from your implementation of `get_twoel_symm`.*

&nbsp;

The second trick is called *integral screening*. 
Its idea is based on the 
[Cauchy-Bunyakovsky-Schwarz inequality](https://en.wikipedia.org/wiki/Cauchy–Schwarz_inequality),
which gives an upper bound on the inner product of two vectors.
Suppose we have vectors $u, v \in \mathbb{R}^n$. The inner product 
between then is bounded by
$$
\left| \langle u, v \rangle \right|^2 \leq \langle u, u \rangle \cdot \langle v, v \rangle\,,
$$
as first shown by Cauchy in 1821. 

**(b) Prove the Cauchy-Bunyakovsky-Schwarz inequality 
for arbitrary vectors $u, v \in \mathbb{R}^n$ (by hand).**

*Hint: Consider the following quadratic function in $\lambda$*
$$
  f(\lambda) := \langle \lambda u + v, \lambda u + v \rangle 
    = \langle u, u \rangle \lambda^2 + 2 \langle u, v \rangle \lambda + \langle v, v \rangle
    \geq 0
$$
*and insert* 
$\lambda = -\frac{\langle u, v \rangle}{\langle u, u \rangle}$
*into it.*

&nbsp;

The Cauchy-Bunyakovsky-Schwarz inequality also applies to other vector spaces,
such as the space of square-integrable functions $L^2(\mathbb{R}^n)$. In this
case, the inequality states that
$$
\left| \int_{\mathbb{R}^n} f^*(x) g(x)\ \mathrm{d} x \right|^2
\leq
\int_{\mathbb{R}^n} |f(x)|^2\ \mathrm{d} x \cdot 
\int_{\mathbb{R}^n} |g(x)|^2\ \mathrm{d} x
$$
for $f, g \in L^2(\mathbb{R}^n)$, as first shown by Bunyakovsky in 1859.

By appling the inequality above to the two-electron integrals, we can derive
$$
\left| (ij|kl) \right| \leq Q_{ij} Q_{kl}
$$
with $Q_{ij} = (ij|ij)^{1/2}$ and $Q_{kl} = (kl|kl)^{1/2}$ 
using some simple algebra.[^haeser_scf]

This means that we can approximate the two-electron integral 
$(ij|kl)$ by zero if $Q_{ij} Q_{kl}$ is smaller than some 
threshold $Q_{\mathrm{min}}$. Since the integrals involved in 
$Q_{ij}$ and $Q_{kl}$ are integrals we have to calculate 
anyway, this screening does not cost us any additional evaluation 
of two-electron integrals. On the contrary, by choosing a suitable 
threshold $Q_{\mathrm{min}}$, we can save a lot of time by 
skiping the evaluation of integrals that are close to zero anyway. 

It should be mentioned that the integral screening is an approximation, 
so we will obtain slightly different results. However, by making the 
threshold $Q_{\mathrm{min}}$ smaller, we can make the approximation 
as accurate as we want. In practice, a threshold smaller than the SCF 
convergence threshold is usually sufficient.

The inequality above suggests that we should at first calculate two-electron 
integrals of the type $(ij|ij)$. Afterwards, we evaluating the remaining 
integrals, we can check if the product of the corresponding $Q$ values 
is smaller than $Q_{\mathrm{min}}$. If this is the case, the absolute 
value of the integral must be smaller than $Q_{\mathrm{min}}$ and be 
set to zero. Otherwise, we calculate the integral as usual.

**(c) Extend the `Molecule` class with the method `get_twoel_screening`, 
which calculates the two-electron integrals using integral screening.**

*Hint: This approximation can greatly speed up the calculation of 
two-electron integrals if lots of atom pairs are far away from each other. 
The water molecule is too small for this method to be effective. For testing 
purposes, you can set the threshold to be a relatively large value, e.g. 
$Q_{\mathrm{min}} = 0.05$ and compare the results with that from the 
`get_twoel` method by adjusting the `atol` argument of 
[`np.allclose`](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html).*

&nbsp;

```admonish note
These two tricks mentioned above can be combined to further 
speed up the calculation of two-electron integrals. You do not have to
implement this combined method.
```

[^haeser_scf]: M. Häser, R. Ahlrichs, _J. Comput. Chem._, **1989**, 10, 104&ndash;111.

### Problem 4

The so-called spin-orbit coupling (SOC) plays a crucial role in the transition 
between singlet and triplet states. All spin-related effects are ultimately 
derived from the relativistic Dirac equation. Since the derivation of SOC 
from the Dirac formalism is rather lengthy, we will not go into detail here. 
After applying several transformations, one arrives at the following 
additional term in the Hamiltonian:
$$
\frac{\hbar}{4m^2 c^2} \bm{\sigma} \cdot (\mathbf{\nabla}V) \times \mathbf{p}
$$

Here, $\bm{\sigma}$ denotes the vector of Pauli matrices, $V$ is 
the nuclear potential, $\mathbf{p}$ is the momentum operator, and $m$ and $c$ 
refer to the electron mass and the speed of light, respectively. 
The potential $V$ is given by:
$$
\begin{align*}
  V(\mathbf{r}) &= \sum_n \frac{Z_n}{r_n}\\
  \mathbf{\nabla}V(\mathbf{r}) 
    &= \sum_n \frac{Z_n}{r_n^3}(\mathbf{r}-\mathbf{C}_n)
\end{align*}
$$
with $Z_n$ being the nuclear charge and $\mathbf{C}_n$ the position of the 
$n$th nucleus. Substituting this into the SOC term leads to a 
more compact expression:
$$
\frac{\hbar}{4m^2c^2} \bm{\sigma} \cdot \sum_n \frac{Z_n}{r_n^3}(\mathbf{r}-\mathbf{C}_n) \times \mathbf{p} = \frac{\hbar}{4m^2c^2} \bm{\sigma} \cdot \sum_n \frac{Z_n}{r_n^3}\mathbf{l}_n
$$
where $\mathbf{l}_n = (\mathbf{r}-\mathbf{C}_n) \times \mathbf{p}$ 
is the angular momentum operator with respect to nucleus $n$. 
We can now separate the spin and spatial parts of the SOC operator:
$$
\begin{align*}
  \frac{\hbar}{4m^2c^2} \bm{\sigma} \cdot \sum_n \frac{Z_n}{r_n^3}\mathbf{l}_n = \bm{\sigma} \cdot \left( \frac{\hbar}{4m^2c^2} \sum_n \frac{Z_n}{r_n^3}\mathbf{l}_n\right)
\end{align*}
$$

Although SOC integrals can in principle be evaluated for arbitrary 
Gaussian orbitals, in this task we will restrict ourselves to the SOC 
matrix element between two identical p<sub>z</sub>-type orbitals with the 
same exponent $\alpha$. These orbitals are defined as:
$$
\begin{align*}
    \phi_{i,p_z}(\mathbf{r}) &= N z \exp\left(-\alpha \left( (x - \frac{d}{2})^2 + y^2 + z^2\right)\right) \\
    \phi_{j,p_z}(\mathbf{r}) &= N z \exp\left(-\alpha \left( (x + \frac{d}{2})^2 + y^2 + z^2\right)\right)\;\mathrm{.}
\end{align*}
$$
Here, the $x$-axis is chosen as the bond axis, and $d$ is the distance between 
the centres of the two orbitals. $N$ is the normalization factor, which will be 
ignored in the derivation since it does not affect the structure of the SOC term.

**Compute the spatial part of the SOC matrix element between the two 
p<sub>z</sub>-orbitals:**
$$
\begin{align*}
    \frac{\hbar}{4m^2c^2} \sum_n Z_n \int \du^3 {\mathbf{r}}\ \phi_{i,p_z}^*(\mathbf{r})
     \begin{pmatrix}
        \hat{l}_{n,x} \\
        \hat{l}_{n,y} \\
        \hat{l}_{n,z}
     \end{pmatrix}
     \frac{1}{r_n^3} \phi_{j,p_z}(\mathbf{r})
\end{align*}
$$

*Hint:
Since the angular momentum operator is a vector, the result of this integral 
will also be a vector with three components. Therefore, you will need to 
evaluate three integrals, one for each spatial component of the angular momentum. 
Use the relevant expressions and techniques from the lecture to simplify 
the integrals. You are encouraged to use SymPy to assist with the 
symbolic computation of the integrals where appropriate.*


