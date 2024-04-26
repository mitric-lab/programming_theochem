## Overlap Integrals

We can now proceed to calculate molecular integrals, starting with 
overlap integrals. An overlap integral between two centres $A$ and 
$B$ are defined as
$$
S_{ijk,lmn}^{A,B} = 
  \int g_{ijk}(\vec{r};\alpha, \vec{A})
  \ g_{lmn}(\vec{r};\beta, \vec{B}) 
  \ \du^3 r
$$
Because Cartesian Gaussians are factorizable, we can calculate the overlap 
for each Cartesian direction, i.e.,
$$
S_{ijk,lmn}^{A,B} =
  S_{il}^{A_x, B_x}\ 
  S_{jm}^{A_y, B_y}\ 
  S_{kn}^{A_z, B_z} 
$$
Therefore, we only have to deal with overlaps between 1D Gaussians.

### Hermite Gaussian Overlaps
We now examine the overlap between two (unnormalized) 1D Hermite Gaussian:
$$
\begin{align}
E_{k l}^{A_x, B_x} 
  &= \int h_{k}(x;\alpha, A_x) \ h_{l}(x;\beta, B_x) \ \du x \\
  &= \int \left( \frac{\partial}{\partial A_x} \right)^k
     \eu^{-\alpha(x-A_x)^2} 
     \left( \frac{\partial}{\partial B_x} \right)^l
     \eu^{-\beta(x-B_x)^2} \du x \\
  &= \left( \frac{\partial}{\partial A_x} \right)^k 
     \left( \frac{\partial}{\partial B_x} \right)^l
  \int 
     \eu^{-\alpha(x-A_x)^2} \eu^{-\beta(x-B_x)^2} \du x \\
  &= \left( \frac{\partial}{\partial A_x} \right)^k 
     \left( \frac{\partial}{\partial B_x} \right)^l
     E_{00}^{A_x,B_x}
\end{align}
$$
By using the Gaussian product theorem the integral $E_{00}^{A_x,B_x}$ is 
reduced to
$$
\begin{align}
  E_{00}^{A_x,B_x} &= \eu^{-\mu X_{AB}^2} \int \eu^{-p (x - P_x)^2} \\
  &= \eu^{-\mu X_{AB}^2} \sqrt{\frac{\pi}{p}}
\end{align}
$$
with
$$
\begin{align}
  p &= \alpha + \beta \\
  \mu &= \frac{\alpha \beta}{\alpha + \beta} \\
  X_{AB} &= A_x - B_x \\
  P &= \frac{\alpha A_x + \beta B_x}{\alpha + \beta}
\end{align}
$$
Substituting the variables back, we get
$$
E_{00}^{A_x,B_x} = \sqrt{\frac{\pi}{\alpha + \beta}}\ 
  \exp \left( -\frac{\alpha \beta}{\alpha + \beta} (A_x - B_x)^2 \right)
$$
Differentiate this expression with respect to $A_x$ and $B_x$ will 
deliver us with all possible overlap integrals between Hermite Gaussians.

### Cartesian Gaussian Overlaps
By expanding Cartesian Gaussians into Hermite Gaussians, we can easily obtain 
their overlaps, i.e.,
$$
\begin{align}
  S_{i j}^{A_x, B_x} &= \int g_i(x; \alpha, A_x)\ g_j(x; \beta, B_x)\ \du x \\
  &= \int \sum_{k} c_{ki} h_k(x; \alpha, A_x) 
          \sum_{l} c_{lj} h_l(x; \beta, B_x)\ \du x \\
  &= \sum_{k} \sum_{l} c_{ki} c_{lj} 
    \int h_k(x; \alpha, A_x)\ h_l(x; \beta, B_x)\ \du x \\
  &= \sum_{k} \sum_{l} c_{ki} c_{lj} E_{kl}^{A_x,B_x}
\end{align}
$$
So, we can obtain the Cartesian Gaussian overlaps by linearly combining 
Hermite Gaussian Overlaps with the corresponding Hermite expansion 
coefficients.

We shall now use SymPy to generate formulas for cartesian overlaps.

### Code Generation
We start by importing necessary modules, including our function 
for calculating Hermite expansion coefficients. It is assumed here that 
this function is called `get_ckn` and located in the file `hermite_expansion.py`.
```python
{{#include ../codes/03-molecular_integrals/overlap_generator.py:imports}}
```

Afterwards, we define some symbols for SymPy
```python
{{#include ../codes/03-molecular_integrals/overlap_generator.py:define_symbols}}
```
as well as the overlap $E_{00}^{A_x, B_x}$
```python
{{#include ../codes/03-molecular_integrals/overlap_generator.py:define_s00}}
```

Since we need Hermite Gaussian overlaps up to a certain maximum 
value of angular momentum, we shall write a function to generate them:
```python
{{#include ../codes/03-molecular_integrals/overlap_generator.py:hermite_overlap_function}}
```

One specific overlap integral between two Cartesian Gaussians with 
angular momenta `i` and `j` can then be calculated using the following function:
```python
{{#include ../codes/03-molecular_integrals/overlap_generator.py:single_overlap_function}}
```

We can then write a function to generate all Cartesian Gaussian overlaps up to a certain maximum angular momentum:
```python
{{#include ../codes/03-molecular_integrals/overlap_generator.py:generate_overlaps_function}}
```

We can then set
```python
{{#include ../codes/03-molecular_integrals/overlap_generator.py:define_lmax}}
```
and generate formulas for all possible overlaps up to `LMAX`.

By inspecting the generated expressions, one might realize that some 
expressions occur very frequently, e.g. `AX - BX`, or `alpha + beta`. 
We can calculate these expressions once and store the value to avoid 
repeated calculations. To achieve this, we can substitute these expressions 
with some new symbols:
```python
{{#include ../codes/03-molecular_integrals/overlap_generator.py:substitute_repeated_expressions}}
```

We are almost done! The last step is to wrap these expressions into a 
Python function stored in a `.py` file. For this, we can write the following 
function:
```python
{{#include ../codes/03-molecular_integrals/overlap_generator.py:write_overlaps_function}}
```

In this function, we have imported NumPy with the alias `np`. To convert 
the symbolic expressions into Python code with functions beginning with this 
alias, we set up a `NumPyPrinter`:
```python
{{#include ../codes/03-molecular_integrals/overlap_generator.py:setup_printer}}
```

And finally, we can generate the Python file with all the integral expressions:
 ```python
{{#include ../codes/03-molecular_integrals/overlap_generator.py:write_overlaps}}
```
The path `'.'` stands for the location where you execute your Python script. 
You can replace this with any valid path in your computer to generate 
`S.py` there.

