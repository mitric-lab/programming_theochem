# (Quasi-)Newton Methods

The steepest descent method has a garanteed linear convergence for strongly 
convex functions. In order to achieve quadratic convergence, we must get more 
information from the function. The most straight-forward approach would be to 
take the second derivative, or the Hessian $\bm{H}$ of the function. This 
is called 
[Newton's method](https://en.wikipedia.org/wiki/Newton%27s_method_in_optimization) 
in optimisation. 

### Theoretical Background

#### Newton's Method
Just like the method carrying the same name for root 
finding, which constructs a local linear approximation of the function, 
Newton's method in optimisation constructs a local quadratic approximation 
and updates the current point to the minimum of the parabola. The 
corresponding algorithm would be:
1. Choose a starting point $x_0$.
2. Obtain a quadratic approximation at the current point: 
   $f(x) \approx f_k(x) = f(x_k) + 
     \langle \nabla f(x_k), (x - x_k) \rangle + 
     \frac{1}{2} \langle (x - x_k), \bm{H}(x_k)\, (x - x_k) \rangle $.
3. Update the current point using 
   $x_{k+1} = x_{k} - \bm{H}(x_k)^{-1}\, \nabla f(x_k) $.
4. Repeat until some convergence criteria is met.

For a problem with a handful of independent variables, the Hessian can be 
calculated and inverted without any problem. If we want to optimize 
a molecule with $N$ atoms, we have about $3N$ degrees of freedom 
and the Hessian will have $3N \times 3N$ elements, which quickly
becomes expensive to calculate and invert as $N$ grows. In this case, we can 
start with a guess for the initial Hessian, and use informations along the 
iterations to update this Hessian. This leads to 
[Quasi-Newton methods](https://en.wikipedia.org/wiki/Quasi-Newton_method). 
One very widespread algorithm of this class is the 
[Broyden-Fletcher-Goldfarb-Shanno algorithm](https://en.wikipedia.org/wiki/Broyden–Fletcher–Goldfarb–Shanno_algorithm), 
or the BFGS algorithm.

#### BFGS Algorithm
At first, we expand the function at iteration $k + 1$:
$$
f(x) \approx f_{k + 1}(x) = 
  f(x_{k + 1}) + 
    \nabla \langle f(x_{k + 1}), (x - x_{k + 1}) \rangle + 
    \frac{1}{2} \langle (x - x_{k + 1}), \bm{A}_{k + 1}\, (x - x_{k + 1}) \rangle
$$
where $\bm{A}_{k}$ is the approximate Hessian at $k$-th iteration.

Taking the gradient of the approximant, we get
$$
\nabla f(x) \approx \nabla f_{k + 1}(x) = 
  \nabla f(x_{k + 1}) + \bm{A}_{k + 1}\, (x - x_{k + 1})
$$

Inserting $x = x_k$, the condition
$$
\nabla f(x_k) = \nabla f(x_{k + 1}) + \bm{A}_{k + 1}\, (x_k - x_{k + 1})
$$
approximately holds. After some rearrangement, the quasi-Newton condition 
imposed on the update of $\bm{A}_{k + 1}$ is
$$
  \bm{A}_{k + 1} s_k = y_k
$$
with $y_k = \nabla f(x_{k + 1}) - \nabla f(x_k)$ and 
$s_k = x_{k + 1} - x_k$.

To make the update of Hessian as simple as possible, we choose to add two 
rank-1 matrices at each step, i.e.
$$
\bm{A}_{k + 1} = \bm{A}_k + \bm{U}_k + \bm{V}_k
$$

To ensure the Hessian is symmetric, $\bm{U}_k$ and 
$\bm{V}_k$ are chosen to be symmetric. The equation can thus be 
written as
$$
  \bm{A}_{k + 1} = \bm{A}_k + 
    \alpha\ u_k \otimes u_k + 
    \beta\ v_k \otimes v_k
$$
where $\otimes$ denotes the dyadic product. 
By choosing $u_k = y_k$ and $v_k = \bm{A}_k s_k$, and imposing 
the update condition secant for $\bm{A}_{k + 1}$, we get 
$\alpha = \frac{1}{ \langle y_k, s_k \rangle }$ and
$\beta = -\frac{1}{ \langle s_k, \bm{A}_k s_k \rangle }$.

Finally, we arrive at a viable algorihm, which can be formulate as:
1. Choose a starting point $x_0$ and a starting Hessian $\bm{A}_0$.
2. Obtain a direction by solving$\bm{A}_k d_k = -\nabla f(x_k)$.
3. Perform a line search along $d_k$ to find an appropriate step size $\alpha_k$.
4. Set $s_k = \alpha_k d_k$ and update $x_{k + 1} = x_k + s_k$.
5. Calculate $y_k = \nabla f(x_{k + 1}) - \nabla f(x_{k})$.
6. Update the Hessian using $\bm{A}_{k + 1} = 
   \bm{A}_k + \frac{y_k \otimes y_k}{\langle y_k, s_k \rangle} - 
   \frac{(\bm{A}_k s_k) \otimes (s_k \bm{A}_k)}{\langle s_k, \bm{A}_k s_k \rangle} $.
7. Repeat until the convergence criterion is met.

Although this method works, the determination of $d_k$ requires 
the inversion of $\bm{A}_k$, which could be quite expensive for 
larger Hessians. Fortunately, since the update rules for the Hessian is 
simple enough, we can invert the whole equation analytically with the help 
of the 
[Sherman-Morrison-Woodbury formula](https://en.wikipedia.org/wiki/Sherman–Morrison_formula#Generalization_(Woodbury_matrix_identity)), 
which results in
$$
  \bm{B}_{k + 1} 
  = \bm{B}_k + 
  \frac{( \langle s_k, y_k\rangle + \langle y_k, \bm{B}_k y_k\rangle)(s_k \otimes s_k)}{\langle s_k,  y_k \rangle^2} - 
  \frac{(\bm{B}_k y_k) \otimes s_k + s_k \otimes (y_k \bm{B}_k)}{ \langle s_k, y_k \rangle}
$$
with the approximately **inverted** Hessian $\bm{B}_k$. 

The corresponding algorithm can be formulate as follows:
1. Choose a starting point $x_0$ and a starting inverted Hessian 
   $\bm{B}_0$.
2. Obtain a direction by calculating $d_k = -\bm{B}_k \nabla f(x_k)$.
3. Perform a line search along $d_k$ to find an appropriate step size $\alpha_k$.
4. Set $s_k = \alpha_k d_k$ and update $x_{k + 1} = x_k + s_k$.
5. Calculate $y_k = \nabla f(x_{k + 1}) - \nabla f(x_{k})$.
6. Update the inverted Hessian using $
  \bm{B}_{k + 1} 
  = \bm{B}_k + 
  \frac{( \langle s_k, y_k\rangle + \langle y_k, \bm{B}_k y_k\rangle)(s_k \otimes s_k)}{\langle s_k,  y_k \rangle^2} - 
  \frac{(\bm{B}_k y_k) \otimes s_k + s_k \otimes (y_k \bm{B}_k)}{ \langle s_k, y_k \rangle}
  $
7. Repeat until the convergence criterion is met.

An easy and practical choice of the initial Hessian is the identity matrix, 
whose inversion is also an identity matrix.

### Implementation
Even though the formulas for the BFGS algorithm look indimidating, the 
implementation is actually quite simple. We just have to pay attention not 
to mistype the very long formula for the update of the inverted Hessian and 
make sure to use the correct multiplication.
```python
{{#include ../codes/04-numerical_optimisation/optimiser.py:bfgs}}
```

We can apply our implementation of the BFGS algorithm to both of 
our test functions like this:
```python
{{#include ../codes/04-numerical_optimisation/plot_optimisations.py:imports}}
```
```python
{{#include ../codes/04-numerical_optimisation/plot_optimisations.py:define_objective_functions}}
```
```python
{{#include ../codes/04-numerical_optimisation/plot_optimisations.py:plot_bfgs}}
```

You may understand now why the BFGS algorithm is so popular. 
Both functions could be optimized in a handful of iterations. 
Starting from $x_0 = (0, 0)$, the optimization 
trajectories for both functions are shown in the following figure.
![](../assets/figures/04-numerical_optimisation/plot_optimisation_bfgs.svg)

