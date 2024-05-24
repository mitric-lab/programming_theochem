# Numerical Optimisation

Optimisation is the process of finding the optimal solution to a problem. 
Mathematically, we can define the problem as follows: Given a function 
$$
\begin{align}
f: D &\rightarrow \mathbb{R} \\
f(x) &\mapsto y
\end{align}
$$
with the domain $D$. To be as general as possible, we allow $D$ to 
be any set. But for the sake of notational simplicity, we will only use $x$
to denote the elements in $D$. Just keep in mind that $x$ do not have 
to be a real number, but can e.g. also be a vector.

The goal of optimisation is to find 
$x^{\*}$ that minimises of maximises $f$, i.e., 
$$
  x^{*} = \argmin{x \in D} f(x) 
  \quad \text{or} \quad
  x^{*} = \argmax{x \in D} f(x)
$$
with
$$
  f(x^{*}) = \min_{x \in D} f(x) 
  \quad \text{or} \quad
  f(x^{*}) = \max_{x \in D} f(x)
$$

respectively. The function $f$ is called the objective function. 
Since finding the maximum of $f$ is equivalent to finding the minimum 
of $-f$, we will focus on finding the minimum of $f$ in the 
following discussion. 

In general, such problems are impossible to solve analytically. Therefore, 
we need to use numerical methods to find the optimal solution iteratively.
This section will at first introduce the notion of convergence, and then 
define some desirable properties of the objective function. After that, 
we will introduce some basic optimisation methods and implement them.

