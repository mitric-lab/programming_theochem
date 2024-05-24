# Problem Set 2

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
electrons associated with different atomic centers. One way to include this 
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
{{#include ../codes/psets/02/sol_3bc.py:atoms_in_water}}
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
should be inserted in the unit of &#8491;. The differences are the exakt 
$1/r$ part without extra summands in the denominator, as well as the 
parameters $\delta_{A/B}$ and $\epsilon_{A/B}$, which have the same 
functionaliy as $a_{A/B}$ and $b_{A/B}$, respectively, but are 
different in values. These parameters for H, C, N and O are listed in the 
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
located in a elongated valley, even if we choose a sufficiently small step 
size (which means painfully slow convergence), steepest descent will still 
zig-zag towards the solution. If the step size is too large, the method will 
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

*Hint: Since there are several variables that need to be updated in each 
iteration, it is recommended to define them in the constructor, for example 
like this:*
```python
{{#include ../codes/psets/02/sol_2.py:simple_conjugate_gradient_init}}
```

&nbsp;

**(b) Use `SimpleSteepestDescent` and `SimpleConjugateGradient` to optimize 
the Rosenbrock function with $a = 1$ and $b = 100$. Start from 
$x_0 = (0, 0)$, choose a step size of $\alpha=0.005$ and set the 
maximum iteration to 10000. Plot the optimization trajectory.**

*Hint: `SimpleSteepestDescent` is expected to diverge, while 
`SimpleConjugateGradient` should converge.*

Expected result:
![](../assets/figures/psets/02/conjugate_gradient.svg)

---
&nbsp;

### Problem 3

In problem 1, you have calculated the total molecular energy 
using the extended Hückel method. Now we can use optimisation 
algorithms to minimize the molecular energy with respect to the nuclear 
coordinates to obtain (in the best case) a relaxed geometry. 

For this purpose, we shall at first optimise a model function:
$$
V(q) = \frac{\Delta}{2 q_0} (q - q_0) + 
  \frac{E^{\mathrm{TS}} - \Delta / 2}{q_0^4} (q - q_0)^2 (q + q_0)^2
$$

As an example, we shall use the following parameters
$$
\begin{align}
  q_0 &= 2 \\
  \Delta &= 1 \\
  E^{\mathrm{TS}} &= 2
\end{align}
$$

We shall at first define a Python function to obtain the objective function. 
For $V(q)$, it could look like this:
```python
{{#include ../codes/psets/02/sol_3a.py:def_double_well}}
```

Note that we have set the indepentent variable `q` as the first argument 
of this function. This is necessary because we want to use 
the SciPy function 
[`optimize.minimize`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html), 
which requires the objective function to have the independent variable as 
its first argument. We now call of `minimize` on our example function in 
combination with the 
[BFGS](https://en.wikipedia.org/wiki/Broyden–Fletcher–Goldfarb–Shanno_algorithm)
optimization algorithm:
```python
{{#include ../codes/psets/02/sol_3a.py:optimise_double_well}}
```
The function `minimize` calculates numerical gradient of the objective 
function automatically, so you do not need to provide it. 
The optimised value $q^{*}$ is stored in the attribute `x` 
of the object `res`.

**(a) Run the code for optimising `double_well` above yourself to find 
one local minimum. Adjust the initial guess `q_init` to find another 
local minimum.**

Expected results:

$q^{*}_1 = 1.9108;\quad q^{*}_2 = -2.0706$

&nbsp;

After playing around with the model function, we shall take a look at 
the water molecule from problem 1:
```python
{{#include ../codes/psets/02/sol_3bc.py:atoms_in_water}}
```
You may have notices that the bond angle $\angle_{\mathrm{HOH}}$ is 
$90^{\circ}$ in this geometry, which is certainly not optimal.

**(b) Optimise the geometry of the water molecule listed above
using the total energy as the objective function.**

_Hint: Start by defining a function which takes the 
[flattened](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html) 
coordinate array (which should have 9 elements) as its first argument and 
everything else you need to construct a molecule as remaining arguments. 
This function should construct a molecule using the coordinates you provide 
and calculate the total energy as its return value. Afterwards, call 
`minimize` on this function using the coordinates given in problem 1 as an initial guess._

&nbsp;

**(c) Calculate the bond length $r_{\mathrm{OH}}$ and the bond angle 
$\angle_{\mathrm{HOH}}$ of the optimised geometry.**

Expected results:

$r_{\mathrm{OH}} = 0.9819\ \mathrm{\AA};\quad \angle_{\mathrm{HOH}} = 102.4^\circ$

