## Problem Set 0

### Problem 1
We learned about two algorithms for floor division in the lecture. 
A regular division, however, does not only give us the quotient but also 
the remainder. 

**Modify the algorithms `naive_div` and `div` in chapter 
[1.5.2](../01-fundamentals/05-arithmetic_operators/02-impl_division.html)
to also return the remainder.**

### Problem 2
In the lecture, we have coloured the real spherical harmonics to make them 
look better. The colour can also be used to carry information. Every complex 
number can be written in polar form
$$z = r \mathrm{e}^{\mathrm{i}\phi}$$
with the magnitude $r$ and phase $\phi$. By only plotting the 
magnitude, the phase information is lost. In the lecture, we tried to mitigate 
this problem by using real spherical harmonics. These are, however, not 
eigenfunctions of the Schrödinger equation. The complex functions can be 
plotted without loss of information. A common practice is to plot the 
magnitude as usual and use colours to indicate the phase.

**Write a program to plot complex spherical harmonics with phases indicated by 
colours. Choose an appropriate 
[colormap](https://matplotlib.org/stable/tutorials/colors/colormaps.html).**

*Hint: the functions `abs` and `angle` from NumPy could be helpful.*

### Problem 3
The notation $\langle \hat{A} \rangle_{\psi}$ stands for the 
expectation value of the operator $\hat{A}$ when applied to 
the quantum state $| \psi \rangle$, i.e.
$$
  \langle \hat{A} \rangle_{\psi} = \langle \psi | \hat{A} | \psi \rangle
$$
The variance of an observable $A$ is defined as:
$$
\mathrm{Var}(A) = \langle \hat{A}^2 \rangle - \langle \hat{A} \rangle^2
$$
where the index $\psi$ is omitted for notational simplicity.
The standard deviation of the observable is then defined as
$$
\sigma_A = \sqrt{\mathrm{Var}(A)}
$$

In the lecture, we generated the eigenstates of the quantum harmonic 
oscillator in the position basis, known as wavefunctions. In the position 
basis, the position and momentum operator is given as
$$
\hat{x} = x,\quad \hat{p}=-\mathrm{i}\frac{\mathrm{d}}{\mathrm{d}x}
$$
**Calculate $\sigma_{x}$ and $\sigma_{p}$ for the first 5 eigenstates 
of the harmonic oscillator and verify Heisenberg's uncertainty principle.**

*Hint: the imaginary unit in SymPy can be accessed using `sp.I`.*

### Problem 4
Recursion is a key concept in computer science where a problem is solved 
by breaking it down into smaller instances of the same problem. This is 
done by using functions that call themselves within their code. It is 
widely applicable to different types of problems.

The factorial function, for example, can be defined recursively in the 
following manner:
```python
{{#include ../codes/psets/00/recursion.py:factorial_recursive}}
```
For every recursive function, a termination condition is needed. Otherwise, 
the function will go on until it is stopped by some safety mechanism or the 
program crashes. In this case, the recursion stops at `n = 0` if only nonnegative 
integers are used as the argument. If `n` is not zero, this function calls 
itself with `n` decreased by 1, until the termination condition is met.

The same thing can also be accomplished with an iterative approach:
```python
{{#include ../codes/psets/00/recursion.py:factorial_iterative}}
```

In this case, both implementations have similar code lengths. But often, a 
recursive approach can be easier to implement, e.g. the generation of 
Lucas numbers, which are closely related to the Fibonacci numbers.

The $n$-th Lucas numbers $L_n$ is defined as
$$
L_n := \begin{cases}
  2 & n = 0 \\
  1 & n = 1 \\
  L_{n-1} + L_{n-2} & n > 1
\end{cases}
$$

**(a) Implement the function `lucas_number(n)` which takes one argument `n` 
and generates the $n$-th Lucas number recursively.**

Although easy to implement, recursive algorithms often perform worse than 
their iterative counterparts. This problem can sometimes be mitigated using 
the `lru_cache` function decorator from the module `functools`. You can apply 
this decorator like
```python
{{#include ../codes/psets/00/recursion.py:cache_usage}}
```

**(b) Calculate $L_{35}$ using the undecorated as well as the decorated 
function, and pay attention to the execution time. Inform yourself about this 
decorator and explain how it was able to speed up your recursive function.**

In the lecture, we generated the Hermite polynomials directly from their 
definition. Since they satisfy the recurrence relation
$$
H_{n+1}(z) = 2z\ H_n(z) - 2n\ H_{n-1}(z)
$$
with the initial conditions
$$
H_0(z) = 1,\quad H_1(z) = 2z,
$$
they can be generated recursively.

**(c) Implement the function `hermite_recursive(n)` which takes one argument `n` 
and symbolically generates the $n$-th Hermite polynomial with the help 
of SymPy in a recursive manner by using the recurrence relation above.**

