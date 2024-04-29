# Solution to Problem Set 0

### Problem 1

**Modify the algorithms `naive_div` and `div` in chapter 
[1.5.2](../01-fundamentals/05-arithmetic_operators/02-impl_division.html)
to also return the remainder.**

For `naive_div`, the remainder is given by `a + b` after the execution of 
the division:
```python
{{#include ../codes/psets/00/sol_1.py:naive_div}}
```

For `div`, the remainder is just `a`:
```python
{{#include ../codes/psets/00/sol_1.py:div}}
```

### Problem 2

**Write a programme to plot complex spherical harmonics with phases indicated by 
colours. Choose an appropriate 
[colormap](https://matplotlib.org/stable/tutorials/colors/colormaps.html).**

Just like in the lecture, we import the necessary libraries

```python
{{#include ../codes/psets/00/sol_2.py:import}}
```

and define the symbols, as well as the spherical harmonic as a Python function:
```python
{{#include ../codes/psets/00/sol_2.py:func}}
```

Afterwards, we create the angular grid
```python
{{#include ../codes/psets/00/sol_2.py:grid}}
```
and convert it into Cartesian coordinates:
```python
{{#include ../codes/psets/00/sol_2.py:grid_cart}}
```
Note that the complex spherical harmonics are asked here, we should not add 
the complex conjugate but instead only use `Ylm` itself. The distance `r` is 
obtained directly by taking the absolute value of the complex function values 
of `Ylm`.

The phases can be calculated using the NumPy function `angle`. 
Since colourmaps from Matplotlib take a number between 0 and 1 to output 
a colour, we should normalise the phases. Because `np.angle` produces values 
from $-\pi$ to $\pi$, we divide the phases by $2\pi$ to bring 
the range to -0.5 &#8211; 0.5 and add 0.5 to get the desired interval. 
These numbers can then be fed to the colourmap function. The produced colours 
are parsed to the optional argument `facecolors` of the function 
`plot_surface`. 

```python
{{#include ../codes/psets/00/sol_2.py:plot}}
```
Because the phase is cyclic, i.e. a phase of $\pi$ equals a phase 
of $-\pi$, a cyclic colourmap should be chosen to reflect this. In 
Matplotlib 3.8, three cyclic colourmaps are available, `twilight, 
`twilight_shifted`, and `hsv`. We have used `hsv` in this example.

The following figure is obtained for `l = 3` and `m = 1`:
<p align="center">
  <img src="../assets/figures/psets/00/Y31_complex.svg">
</p>

### Problem 3

**Calculate $\sigma_{x}$ and $\sigma_{p}$ for the first 5 eigenstates 
of the harmonic oscillator and verify Heisenberg's uncertainty principle.**

Just like in the lecture, we first define the wavefunction after importing 
the necessary libraries:

```python
{{#include ../codes/psets/00/sol_3.py:import}}
```
```python
{{#include ../codes/psets/00/sol_3.py:wf}}
```
Since we are going to do lots of integrations, it is worth defining 
a function to do it:
```python
{{#include ../codes/psets/00/sol_3.py:integrate}}
```

By using the definition for $\sigma_x$ and $\sigma_p$, we can 
construct a function for each operator to calculate its standard deviation 
given a wavefunction:
```python
{{#include ../codes/psets/00/sol_3.py:get_sigma_x}}
```
```python
{{#include ../codes/psets/00/sol_3.py:get_sigma_p}}
```

These two functions can then be used to calculate $\sigma_x$ and 
$\sigma_p$ for the first 5 eigenfunctions. By calculating their product, 
we can verify that they fulfill Heisenberg's uncertainty principle.
```python
{{#include ../codes/psets/00/sol_3.py:print}}
```

### Problem 4

**(a) Implement the function `lucas_number(n)` which takes one argument `n` 
and generates the $n$-th Lucas number recursively.**

The function follows directly from the definition of the Lucas numbers:
```python
{{#include ../codes/psets/00/sol_4.py:lucas_number}}
```

**(b) Calculate $L_{35}$ using the undecorated as well as the decorated 
function, and pay attention to the execution time. Inform yourself about this 
decorator and explain how it was able to speed up your recursive function.**

For the speed comparison, we define the cached version of `lucas_number`:
```python
{{#include ../codes/psets/00/sol_4.py:lucas_number_cache}}
```

Here, just an estimation suffices to compare the performance of both 
functions. While `lucas_number` takes several seconds to complete, 
`lucas_number_cache` finishes in the blink of an eye. Of course, you can 
obtain a more precise result by utilizing the `time.time()` or 
`time.perf_counter()` function from the `time` module. If you work with 
IPython (e.g. Jupyter Notebook), you can also use the 
[magic commands](https://ipython.readthedocs.io/en/stable/interactive/magics.html)
`%time`, `%`%time`, or `%timeit``. 

The `lru_cache` (least recently used cache) decorator is a built-in 
function in Python's `functools` module that provides a memoization 
mechanism for functions. Memoization is a technique used to cache the 
results of function calls and avoid redundant computations by storing 
the results for specific inputs.

When applied to the `lucas_number` function, the `lru_cache` decorator 
stores the results of function calls in a cache, allowing subsequent calls 
with the same arguments to retrieve the result from the cache instead of 
recomputing it. This significantly improves the performance of the function, 
especially for larger values of `n`, where there would be many repeated 
computations without memoization.

Here's how the `lru_cache` decorator enhances the `lucas_number` function:

1. The first time `lucas_number` is called with a specific argument `n`, 
the decorator executes the function body and stores the result in a cache.

2. If `lucas_number` is called again with the same argument `n`, 
instead of executing the function body, the decorator checks the cache. 
If the result for `n` is present in the cache, it returns the cached 
result directly without further computation.

By avoiding redundant recursive function calls and reusing previously 
computed results, the `lru_cache` decorator significantly reduces the number 
of function evaluations needed to compute the Lucas number for a given `n`. 
This caching mechanism provides a considerable speed boost, especially when 
dealing with larger values of `n` or when there are overlapping subproblems 
in the recursive calls.

Note that when using `lru_cache`, note that the cache size is limited. If the 
cache becomes full, the least recently used results will be discarded to 
make room for new entries, therefore the name "least recently used" cache. 
You can make the cache size unlimited by supplying `maxsize=None`, or, 
with `Python >= 3.9`, using `@cache` instead of `@lru_cache` to cache 
everything without a size limit.

**(c) Implement the function `hermite_recursive(n)` which takes one argument `n` 
and symbolically generates the $n$-th Hermite polynomial with the help 
of SymPy in a recursive manner by using the recurrence relation above.**

By following the recursion relation, it is straightforward to define the 
function we seek for:
```python
{{#include ../codes/psets/00/sol_4.py:hermite_recursive}}
```
Just remember to shift **all** indices by 1, since the recursion relation 
given is defined for $n+1$, $n$, and $n-1$, while in programming, 
`n`, `n `- 1`, and `n -` 2` are needed.

