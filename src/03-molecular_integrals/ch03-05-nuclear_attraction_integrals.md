# Nuclear Attraction Integrals

The next type of integrals we shall examine are the nuclear attraction 
integrals. A nuclear attraction integral between two basis functions 
\\(g_{ijk}\\) and \\(g_{lmn}\\) centered at \\(A\\) and \\(B\\), 
respectively, and with respect to a nucleus \\(C\\) is defined as
$$
V_{ijk,lmn}^{A,B}(C) = 
  \int g_{ijk}(\vec{r}; \alpha, \vec{A}) 
  \ \frac{Z_C}{r_C} \ 
  g_{lmn}(\vec{r}; \beta, \vec{B}) 
  \ \mathrm{d}^3 r
$$
where \\(Z_C\\) is the nuclear charge of \\(C\\). Just like overlap 
integrals, we shall at first calculate the nuclear attraction integrals 
between 2 s-orbitals, i.e. \\((i, j, k) = (l, m, n) = (0, 0, 0)\\), 
For notational simplicity, we will define \\(V_p(C) := V_{000,000}^{A,B}(C)\\).
Integrals involving higher angular momenta can then be obtained by applying 
recursive relations of Hermite Gaussians.

However, unlike the overlap integrals, nuclear attraction integrals are 
not factorizable because of the factor \\(1/r_C\\). Therefore, we have 
to use some tricks.

### Evaluation of \\(V_{000,000}^{A,B}(C)\\)
Remember the 1D gaussian integral
$$
\int \mathrm{e}^{-\alpha x^2} \ \mathrm{d} x = \sqrt{\frac{\pi}{\alpha}}
$$
If we choose \\(\alpha = r_C^2\\) (and change the integration variable to 
\\(t\\)), we obtain
$$
\int \mathrm{e}^{-r_C^2 t^2} \ \mathrm{d} t 
= \sqrt{\frac{\pi}{r_C^2}} = \frac{\sqrt{\pi}}{r_C}
$$
This means we can rewrite the \\(1/r_C\\) factor as
$$
\frac{1}{r_C} = \frac{1}{\sqrt{\pi}} \int \mathrm{e}^{-r_C^2 t^2} \ \mathrm{d} t
$$
Substituting this back into the nuclear attraction integral, we get
$$
V_p(C) = 
  \frac{Z_C}{\sqrt{\pi}} \int g_{000}(\vec{r}; \alpha, \vec{A}) 
  g_{000}(\vec{r}; \beta, \vec{B}) 
  \int \mathrm{e}^{-r_C^2 t^2} \ \mathrm{d} t
  \ \mathrm{d}^3 r
$$
We have thus transformed the original 3-dimensional integral into a 
4-dimensional integral. Wait what? Shouldn't we simplify the expressions 
instead of complicating them? Well, the new integral does not have the 
annoying \\(1/r_C\\) factor and is now separable. 

We at first apply Gaussian product theorem to 
\\(g_{000}(\vec{r}; \alpha, \vec{A}) g_{000}(\vec{r}; \beta, \vec{B})\\),
which gives us \\(g_{000}(\vec{r}; p, \vec{P}) \exp(-\mu R_{AB}^2)\\) with 
\\(p = \alpha + \beta\\), 
\\(\vec{P} = (\alpha \vec{A} + \beta \vec{B}) / p\\), 
\\(\mu = \alpha \beta / (\alpha + \beta)\\) and 
\\(R_{AB} = \vec{A} - \vec{B}\\). The 4-dimensional integral is then
$$
V_p(C) = 
  \frac{Z_C}{\sqrt{\pi}} \exp(-\mu R_{AB}^2)
  \int \int \mathrm{e}^{-p \\|\vec{r} - \vec{P}\\|^2} 
  \mathrm{e}^{-r_C^2 t^2} \ \mathrm{d} t
  \ \mathrm{d}^3 r
$$
The product Gaussian does not explicitly depend on vector \\(\vec{r}\\), 
but only the length \\(\\|\vec{r} - \vec{P}\\|\\). Therefore, it is a 1D 
Gaussian and we can apply Gaussian product theorem to it and the Gaussian in 
\\(r_C^2\\) to obtain
$$
\begin{align}
V_p(C) &= 
  \frac{Z_C}{\sqrt{\pi}} \exp(-\mu R_{AB}^2)
  \int \int \exp \left(- \frac{p t^2}{p + t^2} R_{PC}^2 \right) 
  \exp \left(- (p + t^2) \\|\vec{r} - \vec{S}\\|^2 \right)
  \ \mathrm{d} t \ \mathrm{d}^3 r \\\\
  &= \frac{Z_C}{\sqrt{\pi}} \exp(-\mu R_{AB}^2)
  \int \int \exp \left(- (p + t^2) \\|\vec{r} - \vec{S}\\|^2 \right)\ \mathrm{d}^3 r 
  \left(- \frac{p t^2}{p + t^2} R_{PC}^2 \right)\ \mathrm{d} t \\
\end{align}
$$
with \\(R_{PC} = \vec{P} - \vec{C}\\). Note that we have assumed that 
[Fubini's theorem](https://en.wikipedia.org/wiki/Fubini%27s_theorem) holds.
The vector \\(\vec{S}\\) is just like \\(\vec{P}\\) for our first product 
gaussian, but its exact form is not important, because it just represents 
a constant translation in \\(\vec{r}\\) and we are going to integrate over 
the whole space anyway.

The integral over \\(\vec{r}\\) is now just a 3D Gaussian integral and 
we already know the result. By inserting it, a one-dimensional remains:
$$
\begin{align}
V_p(C) &=
  \frac{Z_C}{\sqrt{\pi}} \exp(-\mu R_{AB}^2)
  \int_{-\infty}^{\infty} \left(\frac{\pi}{p + t^2}\right)^{3/2} 
  \exp \left(- \frac{p t^2}{p + t^2} R_{PC}^2 \right)\ \mathrm{d} t \\\\
  &= \frac{2 Z_C}{\sqrt{\pi}} \exp(-\mu R_{AB}^2)
  \int_{0}^{\infty} \left(\frac{\pi}{p + t^2}\right)^{3/2} 
  \exp \left(- \frac{p t^2}{p + t^2} R_{PC}^2 \right)\ \mathrm{d} t \\\\
\end{align}
$$
We have used the symmetry of the remaining Gaussian to change the integration 
limits to \\(0\\) and \\(\infty\\). To "solve" this integral, we introduce 
a new variable \\(u^2 = \frac{t^2}{p + t^2}\\), whose differential is
$$
\begin{equation}
2 u \ \mathrm{d} u = \frac{2 t (p + t^2) - t^2 (2t)}{(p + t^2)^2}\ \mathrm{d} t
= \frac{2 t p}{(p + t^2)^2}\ \mathrm{d} t \\\\
\Leftrightarrow \\\\
\mathrm{d} t = \frac{(p + t^2)^2}{2tp} 2u\ \mathrm{d} u
= \frac{(p + t^2)^2}{t} \frac{u}{p}\ \mathrm{d} u
= \frac{(p + t^2)^2}{t^4} \frac{ut^3}{p}\ \mathrm{d} u
= \frac{1}{u^4} \frac{ut^3}{p}\ \mathrm{d} u 
= \frac{1}{p}\frac{t^3}{u^3}\ \mathrm{d} u
\end{equation}
$$

By performing this substitution, the integral becomes
$$
\begin{align}
V_p(C)
  &= \frac{2 Z_C}{\sqrt{\pi}} \exp(-\mu R_{AB}^2)
  \int_{0}^{1} \left(\frac{\pi}{p + t^2}\right)^{3/2} 
  \exp \left(- p u^2 R_{PC}^2 \right)\ 
  \frac{1}{p}\frac{t^3}{u^3}\ \mathrm{d} u \\\\
  &= \frac{2 \pi Z_C}{p} \exp(-\mu R_{AB}^2)
  \int_{0}^{1} \left(\frac{1}{p + t^2} \frac{t^2}{u^2} \right)^{3/2} 
  \exp \left(- p u^2 R_{PC}^2 \right)\ \mathrm{d} u \\\\
  &= \frac{2 \pi Z_C}{p} \exp(-\mu R_{AB}^2)
  \int_{0}^{1} \exp \left(- p u^2 R_{PC}^2 \right) \mathrm{d} u
\end{align}
$$
Note that the integral limits are changed to \\(0\\) and \\(1\\) upon 
substitution. The remaining integral, unfortunately, cannot be solved 
analytically. We thus introduce the Boys function:
$$
  F_n(x) := \int_0^1 \exp(-xt^2) t^{2n} \mathrm{d} t
$$
with which the original integral can be written as 
$$
V_p(C) = \frac{2 \pi Z_C}{p} \exp(-\mu R_{AB}^2) F_{0}(p R_{PC}^2)
$$

Although the last expression we derived does not have any integral signs, 
the Boys function is still an integral. So what did we achieve? We started 
from a 3-dimensional integral over the whole space and could reduce it to a 
1-dimensional integral over the interval \\([0, 1]\\). This is a huge 
simplification, since such 1D integrals can be efficiently approximated using 
techniques like series expansion.

Substituting all variables back, we obtain the final expression for \\(V_p(C)\\):
$$
V_p(C) = \frac{2 \pi Z_C}{\alpha + \beta}
  \exp\left(-\frac{\alpha \beta}{\alpha + \beta} \\|\vec{A} - \vec{B}\\|^2\right) 
  F_{0}\left(\frac{1}{\alpha + \beta} \\| \alpha \vec{A} + \beta{\vec{B}} - (\alpha + \beta)\vec{C} \\|^2\right)
$$

### Evaluation of arbitrary nuclear attraction integrals
We can now obtain the nuclear attraction integral between Hermite Gaussians 
of arbitrary angular momenta \\(W_{ijk,lmn}^{A,B}(C)\\) by utilizing its 
definition through derivatives:
$$
\begin{align}
W_{ijk, lmn}^{A,B}(C)
  &= \int h_{ijk}(\vec{r}; \alpha, \vec{A}) \frac{Z_C}{r_C} \ h_{lmn}(x;\beta, B_x) \ \mathrm{d}^3 x \\\\
  &= \left( \frac{\partial}{\partial A_x} \right)^i
     \left( \frac{\partial}{\partial A_y} \right)^j
     \left( \frac{\partial}{\partial A_z} \right)^k
     \left( \frac{\partial}{\partial B_x} \right)^l
     \left( \frac{\partial}{\partial B_y} \right)^m
     \left( \frac{\partial}{\partial B_z} \right)^n
     V_p(C)
\end{align}
$$
The dependency on nuclear coordinates \\(A\\) and \\(B\\) comes from the 
exponential part as well as the Boys function. While we already know how to 
differentiate the exponential part, we still need to find derivatives 
of the Boys function. We start by taking the derivative of the Boys function 
directly using its definition:
$$
\begin{align}
\frac{\mathrm{d}}{\mathrm{d}x} F_n(x) 
  &= \frac{\mathrm{d}}{\mathrm{d}x} \int_0^1 \exp(-xt^2) t^{2n} \mathrm{d} t \\\\
  &= \int_0^1 \frac{\mathrm{d}}{\mathrm{d}x} \exp(-xt^2) t^{2n} \mathrm{d} t \\\\
  &= \int_0^1 -t^2 \exp(-xt^2) t^{2n} \mathrm{d} t \\\\
  &= -\int_0^1 \exp(-xt^2) t^{2(n+1)} \mathrm{d} t \\\\
  &= -F_{n+1}(x)
\end{align}
$$

Although we were not able to get something simpler through differentiation, 
at least the expression does not get more complicated and we still only have 
to evaluate Boys function numerically.

Now we can differentiate \\(V_p(C)\\) with respect to \\(A_x\\) and \\(B_x\\) 
according to the desired angular momenta to obtain arbitrary nuclear attraction 
integrals between Hermite Gaussians . To obtain nuclear attraction integrals 
between Cartesian Gaussians, \\(V_{ijk,lmn}^{A,B}(C)\\), we simply use 
Hermite Gaussian expansion:
$$
\begin{align}
V_{ijk,lmn}^{AB}(C)
= \sum_{abc} \sum_{def} 
  c_{ai} c_{bj} c_{ck} c_{dl} c_{em} c_{fn}
  W_{abc, def}^{A,B}(C)
\end{align}
$$

Although we have now derived a general expression for nuclear attraction 
integrals, the expressions are everything but simple. It would be a nightmare 
if you had to evaluate them by hand. So let us use SymPy to generate the 
formulae symbolically and let the computer do the work for us.

### Code Generation
Again, we start by importing necessary modules, including our function 
for calculating Hermite expansion coefficients. It is assumed here that 
this function is called `get_ckn` and located in the file `hermite_expansion.py`.
```python
{{#include ../code/ch03/nuclear_attraction_generator.py:imports}}
```
Afterwards, we define some symbols for SymPy. Since we are now dealing with 
3-dimentional Gaussians, we need a bit more symbols than before.
```python
{{#include ../code/ch03/nuclear_attraction_generator.py:define_symbols}}
```

Because Boys function is not (yet) implemented in SymPy, we have to do it 
ourselfves:
```python
{{#include ../code/ch03/nuclear_attraction_generator.py:define_boys}}
```
We have left out the `eval` method, because we will never use SymPy to 
evaluate Boys functions, for which this method is needed. The `fdiff` method, 
however, is important, because it tells SymPy how to evaluate derivatives of 
Boys functions.

Now we can define \\(V_p(C)\\):
```python
{{#include ../code/ch03/nuclear_attraction_generator.py:define_v000000}}
```

Because we have to work with all three components of angular momentum, 
it would we very wasteful to iterate over all indices independently. 
Suppose we want to calculate the nuclear attraction integrals for just 
s- and p-orbitals, which means that the maximum angular momentum is 1. 
If we iterate over \\(i\\), \\(j\\) and \\(k\\) independently from 0 to 1, 
we will end up with orbitals with \\((i,j,k)=(1,1,1)\\), which is definitely 
not s- or p-orbital. Because the symbolic gereration of nuclear attraction 
integrals can be rather time-consuming, we want to avoid such unnecessary 
calculations. Furthermore, because we want to calculate the integrals for 
Cartesian Gaussians using a linear combination of integrals for Hermite 
Gaussians, with the latter required multiple times during the calculation, 
it can be helpful to store them at first in a dictionary. To achieve both 
goals, we define the following functions:
```python
{{#include ../code/ch03/nuclear_attraction_generator.py:define_generate_triple}}
```
```python
{{#include ../code/ch03/nuclear_attraction_generator.py:define_generate_derivative}}
```
```python
{{#include ../code/ch03/nuclear_attraction_generator.py:define_generate_tree}}
```

Now we can proceed to the generation of nuclear attraction integrals, 
starting with Hermite Gaussians:
```python
{{#include ../code/ch03/nuclear_attraction_generator.py:hermite_nuclear_attraction}}
```

Now we can easily generate nuclear attraction integrals between two 
Cartesian Gaussians with arbitrary angular momenta:
```python
{{#include ../code/ch03/nuclear_attraction_generator.py:generate_single_nuclear_attraction_function}}
```

After defining some repeated expressions for substitution, we can finally 
generate all nuclear attraction integrals between two Cartesian Gaussians 
up to a maximum angular momentum:
```python
{{#include ../code/ch03/nuclear_attraction_generator.py:generate_nuclear_attraction}}
```

Again, we want to write a function to export the generated expressions to 
a python file:
```python
{{#include ../code/ch03/nuclear_attraction_generator.py:write_nuclear_attractions_function}}
```

Because we import NumPy the alias `np`, we setup a `NumPyPrinter` to convert 
the symbolic expressions into Python code with functions beginning with this 
alias:
```python
{{#include ../code/ch03/nuclear_attraction_generator.py:setup_printer}}
```
Because we need the function `boys` which is known to NumPy, we have to 
set the option `allow_unknown_functions` to `True`. It is now our 
responsibility to ensure that all the other functions are supported by 
NumPy or native Python.

Finally, we can generate the python file with all the integral expressions:
```python
{{#include ../code/ch03/nuclear_attraction_generator.py:write_nuclear_attractions}}
```
This will generate a file called `V.py` with the integrals we want.

### Testing on Molecules
In order to test our generated expressions for nuclear attraction integrals, 
we have to extend our `Gaussian` class and `Molecule` class to accomodate 
this. For the `Gaussian` class, we extend it with the `VC` method:
```python
{{#include ../code/ch03/basis_set.py:imports_nuclear_attraction}}
```
```python
{{#include ../code/ch03/basis_set.py:gaussian_nuclear_attraction}}
```

We can then use this method to extend our `Molecule` class with two methods 
to calculate nuclear attraction integrals:

```python
{{#include ../code/ch03/molecule.py:molecule_nuclear_attraction}}
```

With the extended classes in hand, we can test our generated expressions on 
an example molecule, say, ethene. You can download the xyz-file for ethene 
from 
<a href="https://codinginchemistry.com/files_SS23/molecular_integrals/ethene.xyz" download>here</a>.

After importing the necceary modules, we 
load the molecule from a xyz-file and calculate the nuclear attraction 
integrals using the method `get_V()`:
```python
{{#include ../code/ch03/nuclear_attraction_ethene.py:imports}}
```
```python
{{#include ../code/ch03/nuclear_attraction_ethene.py:calculate_nuclear_attractions}}
```

Instead of printing the individual integrals, we can visulize the whole 
matrix using a heatmap:
```python
{{#include ../code/ch03/nuclear_attraction_ethene.py:plot_nuclear_attractions}}
```
This should give you the following plot:
<p align="center">
  <img src="figures/03_molecular_integrals/ethene_kinetic.svg"/>
</p>

If you have PySCF installed, you can use the following code to calculate 
the nuclear attraction integrals using PySCF and compare them with our 
results:
```python
{{#include ../code/ch03/nuclear_attraction_ethene.py:pyscf_nuclear_attractions}}
```


