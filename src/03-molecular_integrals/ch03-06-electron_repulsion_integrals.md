# Electron Repulsion Integrals

The last type of integrals we need for Hartree-Fock calculations is 
the electron repulsion integral (ERI). The ERI between four basis
functions \\(g_{ijk}(\vec{r}; \alpha, \vec{A})\\),
\\(g_{lmn}(\vec{r}; \beta, \vec{B})\\),
\\(g_{opq}(\vec{r}; \gamma, \vec{C})\\) and
\\(g_{rst}(\vec{r}; \delta, \vec{D})\\) is defined as
$$
G_{ijk,lmn,opq,rst}^{A,B,C,D} = 
  \iint g_{ijk}(\vec{r}\_1; \alpha, \vec{A}) 
  \ g_{lmn}(\vec{r}\_1; \beta, \vec{B}) 
  \ \frac{1}{r_{12}}
  \ g_{opq}(\vec{r}\_2; \gamma, \vec{C})
  \ g_{rst}(\vec{r}\_2; \delta, \vec{D})
  \ \mathrm{d}^3 \vec{r}\_1 \ \mathrm{d}^3 \vec{r}\_2
$$
with \\(r_{12} = \\|\vec{r}\_1 - \vec{r}\_2\\|\\), which is often 
abbreviated as \\( (g_{ijk} g_{lmn} | g_{opq} g_{rst}) \\). The ERI is 
also known as the two-electron integral.

### Evaluation of \\(G_{000,000,000,000}^{A,B,C,D}\\)
You should now know the game: we will first calculate the ERI between 
4 s-orbitals, 
i.e. \\((i, j, k) = (l, m, n) = (o, p, q) = (r, s, t) = (0, 0, 0)\\), 
and then apply recursive relations of Hermite Gaussians to obtain 
integrals involving higher angular momenta. 

The ERI between 4 s-orbitals can be derived in a similar way as the 
nuclear attraction integral. We just use the potential of one electron 
instead of the potential of a nucleus. After some algebra, we get 
$$
G_{000, 000, 000, 000}^{A, B, C, D} = 
  \frac{2 \pi^{5/2} \exp{(-\mu R_{AB}^2)} \exp{(-\nu R_{CD}^2})}{pq \sqrt{p + q}}
  F_0(\rho R_{PQ}^2)
$$
where
$$
\begin{align}
  p &= \alpha + \beta \\\\
  q &= \gamma + \delta \\\\
  P &= \frac{\alpha \vec{A} + \beta \vec{B}}{\alpha + \beta} \\\\
  Q &= \frac{\gamma \vec{C} + \delta \vec{D}}{\gamma + \delta} \\\\
  \mu &= \frac{\alpha \beta}{\alpha + \beta} \\\\
  \nu &= \frac{\gamma \delta}{\gamma + \delta} \\\\
  R_{AB} &= \\|\vec{A} - \vec{B}\\| \\\\
  R_{CD} &= \\|\vec{C} - \vec{D}\\| \\\\
  R_{PQ} &= \\|\vec{P} - \vec{Q}\\|
\end{align}
$$

This expression will only become more complicated when we go to higher 
angular momenta. So let us use SymPy to generate the formulae symbolically.

### Code Generation
Again, we start by importing necessary modules, including our function 
for calculating Hermite expansion coefficients. It is assumed here that 
this function is called `get_ckn` and located in the file `hermite_expansion.py`.
```python
{{#include ../code/ch03/electron_repulsion_generator.py:imports}}
```
Afterwards, we define some symbols for SymPy. We now have four 3D-Gaussians, 
so a bit more symbols are needed.
```python
{{#include ../code/ch03/electron_repulsion_generator.py:define_symbols}}
```

Again, we define the Boys function
```python
{{#include ../code/ch03/electron_repulsion_generator.py:define_boys}}
```
as well as the function `generate_tree` which 
generates all possible derivatives of Hermite Gaussians up to a certain 
angular momentum:
```python
{{#include ../code/ch03/nuclear_attraction_generator.py:define_generate_triple}}
```
```python
{{#include ../code/ch03/nuclear_attraction_generator.py:define_generate_derivative}}
```
```python
{{#include ../code/ch03/nuclear_attraction_generator.py:define_generate_tree}}
```

Afterwards, we define the ERI between four s-orbitals:
```python
{{#include ../code/ch03/electron_repulsion_generator.py:define_g000000000000}}
```

Now we can proceed to the generation of ERIS between higher angular momenta. 
Like we have always done, start with ERIs between Hermite Gaussians:
```python
{{#include ../code/ch03/electron_repulsion_generator.py:hermite_electron_repulsion}}
```

and define a function to generate ERI between Cartesian Gaussians with 
arbitrary angular momenta:
```python
{{#include ../code/ch03/electron_repulsion_generator.py:generate_single_electron_repulsion_function}}
```

After defining some repeated expressions for substitution, we can finally 
generate the ERIs:
```python
{{#include ../code/ch03/electron_repulsion_generator.py:generate_electron_repulsion}}
```

Again, we want to write a function to export the generated expressions to 
a python file
```python
{{#include ../code/ch03/electron_repulsion_generator.py:write_electron_repulsions_py}}
```
and setup a `NumPyPrinter` to convert the symbolic expressions into 
Python code with functions with proper aliasing:
```python
{{#include ../code/ch03/electron_repulsion_generator.py:setup_printer}}
```

Finally, we can generate the python file with all the integral expressions:
```python
{{#include ../code/ch03/electron_repulsion_generator.py:write_electron_repulsions}}
```
This will generate a file called `ERI.py` with the integrals we want.

### Testing on Molecules
In order to test our generated expressions for electron repulsion integrals, 
we have to extend our `Gaussian` class and `Molecule` class to accomodate 
this. For the `Gaussian` class, we extend it with the `twoel` method:
```python
{{#include ../code/ch03/basis_set.py:imports_electron_repulsion}}
```
```python
{{#include ../code/ch03/basis_set.py:gaussian_electron_repulsion}}
```

We can then use this method to extend our `Molecule` class with the method 
`get_twoel` to calculate electron repulsion integrals:
```python
{{#include ../code/ch03/molecule.py:molecule_electron_repulsion}}
```

With the extended classes in hand, we will again use ethene as a guinea 
pig to test our generated expressions. You can download the xyz-file for
ethene from 
<a href="https://codinginchemistry.com/files_SS23/molecular_integrals/ethene.xyz" download>here</a>.

After importing the necceary modules, we 
load the molecule from a xyz-file and calculate the electron repulsion 
integrals using the method `get_twoel()`:
```python
{{#include ../code/ch03/electron_repulsion_ethene.py:imports}}
```
```python
{{#include ../code/ch03/electron_repulsion_ethene.py:calculate_electron_repulsions}}
```
Unfortunately, since the ERI tensor is 4-dimensional, it can not be nicely 
visualized as a heatmap. If you have PySCF installed, you can use the 
following code to calculate the electron repulsion integrals with it:
```python
{{#include ../code/ch03/electron_repulsion_ethene.py:pyscf_imports}}
```
```python
{{#include ../code/ch03/electron_repulsion_ethene.py:calculate_electron_repulsions_pyscf}}
```
and compare these two tensors:
```python
{{#include ../code/ch03/electron_repulsion_ethene.py:compare_eris}}
```

