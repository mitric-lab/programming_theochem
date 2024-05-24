## Steepest Descent

By noticing that the gradient of a function points to the direction of the 
steepest ascent, we can use the negative gradient to guide us toward 
the minimum. This method is called 
[steepest descent](https://en.wikipedia.org/wiki/Gradient_descent)
or 
[gradient descent](https://en.wikipedia.org/wiki/Gradient_descent).

### Theoretical Background

#### Fixed Step Size
We can formalise the idea above into an algorithm:
1. Choose a starting point $x_0$ and a step size $\alpha$.
2. Calculate the gradient at the current point $\nabla f(x_k)$.
3. Update the current point using $x_{k+1} = x_k - \alpha \cdot \nabla f(x_l)$.
4. Repeat until the convergence criterion is met.

The step size $\alpha$, also known as the learning rate, determines how far
we move in the direction of the negative gradient. Because the gradient 
vanishes at a stationary point, when this algorithm converges, it is 
guaranteed to converge to a stationary point. One should check afterwards 
whether the stationary point is a (local) minimum. 

If we assume some desirable
```admonish info title="properties for the objective function" collapsible=true
Here, the objective function $f$ is assumed to be *convex* and has 
*Lipschitz continuous* gradient. 

A function $f$ is called *convex* if and only if
$$
  f(tx + (1-t)y) \leq tf(x) + (1-t)f(y)
$$
for all $0 \leq t \leq 1$ and all $x, y \in D$, 
where $D$ is the domain of $f$.

The right-hand side of the inequality represents the straight line between
$(x, f(x))$ and $(y, f(y))$. In English, this inequality states that this
straight line is always above the graph of $f$.

The Lipschitz continuity of the gradient means that there exists a constant
$L > 0$, called the *Lipschitz constant*, such that
$$
  \| \nabla f(x) - \nabla f(y) \| \leq L \| x - y \|
$$
for all $x, y \in D$. This is a stronger condition than the continuity of
the gradient.
```
beyond the obvious differentiability, we can show that the steepest descent
algorithm always converges if the step size is sufficiently small. In the
worst case, steepest descent converges sublinearly. 
```admonish proof collapsible=true
We start by inserting $y = x - \alpha \nabla f(x)$ into the 
quadradic upper bound of the objective function:
$$
\begin{align*}
  f(y) &\leq f(x) + \langle \nabla f(x), (y - x)\rangle + \frac{L}{2} \|y - x\|^2 \\
  f(x - \alpha \nabla f(x)) 
    &\leq f(x) - \alpha \langle \nabla f(x), \nabla f(x)\rangle + 
      \frac{L}{2} \| \alpha \nabla f(x)\|^2 \\
  &= f(x) - \alpha \left( 1 - \frac{L \alpha}{2}\right) \| \nabla f(x)\|^2
\end{align*}
$$

If we choose $0 < \alpha \leq \frac{1}{L}$, then 
$\alpha \left(1 - \frac{L \alpha}{2}\right) > \frac{\alpha}{2}$
and we have
$$
  f(x_{k+1}) \leq f(x_k) - \frac{\alpha}{2} \| \nabla f(x)\|^2
$$
by putting $x_k = x$ and identifying 
$x_{k+1} = y = x_k - \alpha \nabla f(x_k)$.

Because of the convexity of $f$, we have 

$$
  f(x^{*}) \geq f(x_{k}) + \langle \nabla f(x_{k}), x^{*} - x_{k} \rangle
  \quad \Leftrightarrow \quad 
  f(x^{*}) + \langle \nabla f(x_{k}), x_{k} - x^{*} \rangle \geq f(x_{k})
$$

Therefore, we can further estimate $f(x_{k+1})$ using
$$
\begin{align*}
  f(x_{k+1}) &\leq f(x_k) - \frac{\alpha}{2} \| \nabla f(x)\|^2 \\
  &\leq f(x^{*}) + \langle \nabla f(x_k), x_k - x^* \rangle - \frac{\alpha}{2} \| \nabla f(x)\|^2 \\
  &= f(x^{*}) + 
    \left\langle \frac{1}{2} \nabla f(x_k), 2(x_k - x^{*}) \right\rangle - 
    \left\langle \frac{1}{2} \nabla f(x_k), \alpha \nabla f(x_k) \right\rangle \\
  &= f(x^{*}) +
    \left\langle \frac{1}{2} \nabla f(x_k), (2x - 2 x^{*} - \alpha \nabla f(x_k)) \right\rangle \\
  &= f(x^{*}) + \frac{1}{2\alpha} 
    \langle \alpha \nabla f(x_k), (2x - 2 x^{*} - \alpha \nabla f(x_k)) \rangle \\
  &= f(x^{*}) + \frac{1}{2\alpha} 
    \left( \| x - x^{*} \|^2 - \| x - x^{*} - \alpha \nabla f(x_k) \|^2 \right) \\
  &= f(x^{*}) + \frac{1}{2\alpha}
    \left( \| x - x^{*} \|^2 - \| x_{k+1} - x^{*} \|^2 \right)
\end{align*}
$$

Summing over all $k$'s on both sides, we obtain:
$$
\begin{align*}
  \sum_{i=0}^k (f(x_{i+1}) - f(x^{*})) &\leq 
    \frac{1}{2\alpha} \sum_{i=0}^k 
    \left( \| x_i - x^{*} \|^2 - \| x_{i+1} - x^{*} \|^2 \right) \\
  &= \frac{1}{2\alpha} \left( \| x_0 - x^{*} \|^2 - \| x_{k+1} - x^{*} \|^2 \right) \\
  &\leq \frac{1}{2\alpha} \| x_0 - x^{*} \|^2
\end{align*}
$$

Because $f(x_{k+1}) \leq \frac{\alpha}{2} \|\nabla f(x)\|^2 $, 
$(f(x_{k}))$ is a decreasing sequence. Therefore, the sum on the left hand 
can be estimated by 
$$
  \sum_{i=0}^k (f(x_{i+1}) - f(x^{*})) \geq 
    \sum_{i=0}^k (f(x_{k+1}) - f(x^{*})) 
    = (k+1)(f(x_{k+1}) - f(x^{*}))
$$
which leads to
$$
f(x_{k+1}) - f(x^{*}) \leq 
  \frac{1}{k+1} \sum_{i=0}^k (f(x_{i+1}) - f(x^{*})) \leq
  \frac{1}{2\alpha(k+1)} \| x_0 - x^{*} \|^2
$$

This shows that for any $\epsilon > 0$, we can choose a $k$ large 
enough such that $f(x_{k+1}) - f(x^{*}) \leq \epsilon$. Therefore, 
with the step size $\alpha \leq \frac{1}{L}$, steepest descent is 
guaranteed to converge to the minimum of the objective function. In the 
worst case, steepest descent converges sublinearly with the order 
$\mathcal{O}\left(\frac{1}{k}\right)$ for konvex functions.
```
By assuming
```admonish info title="even stronger properties for the objective function" collapsible=true
Here, the objective function $f$ is assumed to be *strongly convex* and has 
*Lipschitz continuous* gradient.

A function $f$ is called *strongly convex* with parameter $\mu > 0$ 
if and only if
$$
  f(tx + (1-t)y) \leq tf(x) + (1-t)f(y) - \frac{1}{2} \mu t(1-t) \| x - y \|^2
$$
for all $0 \leq t \leq 1$ and all $x, y \in D$. This condition is just the
convexity condition with an additional negative quadratic term on the 
right-hand side. In English, this inequality states that $f$ must be 
more convex than a quadratic function.
```
steepest descent can be shown to converge linearly in the worst case
if a sufficiently small step size $\alpha$ is chosen. 
```admonish proof collapsible=true
By inserting $x_{k+1} = x_k - \alpha \nabla f(x_k)$, we obtain
$$
\begin{align*}
  \|x_{k+1} - x^{*}\|^2 &= \|x_k - \alpha \nabla f(x_k) - x^{*}\|^2 \\
  &= \|x_k - x^{*}\|^2 - 2 \alpha \langle \nabla f(x_k), x_k - x^{*} \| + 
    \alpha^2 \| \nabla f(x_k) \|^2 \\
\end{align*}
$$

From the quadratic lower bound of the strongly convex function, we have 
$$
  f(y) \geq f(x) + \langle \nabla f(x), y - x \rangle + 
    \frac{\mu}{2} \| y - x \|^2
$$
Putting $y = x^{*}$ and $x = x_k$, we obtain 
$$
  f(x^{*}) \geq f(x_k) + \langle \nabla f(x_k), x^{*} - x_k \rangle + 
    \frac{\mu}{2} \| x^{*} - x_k \|^2 \\
  \Leftrightarrow \quad
  \langle \nabla f(x_k), x_k - x^{*} \rangle \geq
    f(x_k) - f(x^{*}) + \frac{\mu}{2} \| x_k - x^{*} \|^2
$$

Insert this inequality into the previous equation, we can write
$$
\begin{align*}
  \|x_{k+1} - x^{*}\|^2 &\leq \|x_k - x^{*}\|^2 - 
    2 \alpha (f(x_k) - f(x^{*}) + \frac{\mu}{2} \| x_k - x^{*} \|^2) + 
    \alpha^2 \| \nabla f(x_k) \|^2 \\
  &= (1 - \alpha \mu) \|x_k - x^{*}\|^2 - 2 \alpha (f(x_k) - f(x^{*})) + 
    \alpha^2 \| \nabla f(x_k) \|^2 \\
\end{align*}
$$

For $\alpha \leq \frac{1}{L}$, we have shown for convex functions 
$$
  f(x_{k+1}) \leq f(x_k) - \frac{\alpha}{2} \| \nabla f(x)\|^2
$$
Because $f(x^{*}) \leq f(x_k)\ \forall k$, we get
$$
  f(x^{*}) - f(x_k) \leq f(x_{k+1}) - f(x_k) \leq 
    - \frac{\alpha}{2} \| \nabla f(x)\|^2 \\
  \Leftrightarrow \quad
  \| \nabla f(x)\|^2 \leq \frac{2}{\alpha} (f({x_k}) - f(x^{*}))
$$
which helps us to write the previous equation as
$$
\begin{align*}
  \|x_{k+1} - x^{*}\|^2 
  &\leq (1 - \alpha \mu) \|x_k - x^{*}\|^2 - 2 \alpha (f(x_k) - f(x^{*})) + 
    \alpha^2 \| \nabla f(x_k) \|^2 \\
  &\leq (1 - \alpha \mu) \|x_k - x^{*}\|^2 - 2 \alpha (f(x_k) - f(x^{*})) + 
    2 \alpha (f({x_k}) - f(x^{*})) \\
  &= (1 - \alpha \mu) \|x_k - x^{*}\|^2
\end{align*}
$$
Taking the square root on both sides, we get 
$$
  \|x_{k+1} - x^{*}\| \leq \sqrt{1 - \alpha \mu} \|x_k - x^{*}\|
$$
which shows that steepest descent converges linearly for strongly convex 
functions.
```

#### Variable Step Size
A very easy modification we can do to improve the performance of 
the steepest descent algorithm with fixed step size is to make $\alpha$ 
variable. We can use the gradient to determine a direction and find a minimum 
in this direction. This is called a line search. Since we just want to obtain 
a reasonable step size, this line search does not have to be precise. 
This can be done by the so-called 
[backtracking line](https://en.wikipedia.org/wiki/Backtracking_line_search) search](https://en.wikipedia.org/wiki/Backtracking_line_search). 

The Armijo variant of this method can be described as follows:
1. Choose a starting point $x$, a maximum step size $\alpha_0$, 
   a descent direction $d$ and control parameters 
   $\tau \in (0, 1)$ and $c \in (0, 1)$.
2. Calculate the directional derivative $m = \langle \nabla f(x), d \rangle$
   and the threshold $t = -c \cdot m$. Note that it is assumed that 
   $d$ leads to a local decrease in $f$ and hence $m < 0$.
3. Check if the condition $ f(x) - f(x + \alpha_j d) \geq \alpha_j t $
   is satisfied. If yes, return $\alpha_j$. If not, set 
   $\alpha_{j+1} = \tau \cdot \alpha_j$.
4. Repeat until the condition above is satisfied.

Let us try to gain some intuition from this cryptic description. 
The right-hand side of the condition, $\alpha_j t = c \alpha_j |m|$, 
is the expected decrease in $f$ using linear approximation scaled by 
$c$. So we start with a large step size $\alpha_0$ and check if 
it leads to a sufficient decrease in $f$. If not, we decrease the step
and decrease it check again. In this way, we will rarely find the 
minimum in the search direction, but it is good enough because we do not 
use line search to find the minimum, but to find a reasonable step size for 
steepest descent.

Steepest descent with the backtracking line search can be summarised as follows:
1. Choose a starting point $x$ and a maximum step size $\alpha_0$.
2. Calculate the gradient at the current point $\nabla f(x_k)$.
3. Use the gradient as the direction for the backtracking line search to find 
   a step size $\alpha_k$.
4. Update the current point using $x_{k+1} = x_k - \alpha_k \nabla f(x_k)$.
5. Repeat until the convergence criterion is met.


### Implementation
Because we aim to implement several optimization algorithms, we will
first implement a base class `OptimiserBase` which contains the common 
methods and attributes of all optimization algorithms. 

```python
{{#include ../codes/04-numerical_optimisation/optimiser.py:imports}}
```
```python
{{#include ../codes/04-numerical_optimisation/optimiser.py:optimiser_base}}
```

This base class implements the `_check_convergence_grad` method, which 
checks whether the gradient norm is smaller than a given tolerance. One could 
implement other convergence criteria, e.g. absolute or relative change of the 
iterate, absolute or relative change of the objective function value, etc.
This base class also implements 
the `run` method which runs the optimization algorithm until convergence 
or until a maximum number of iterations is reached. The `run` method calls 
the `next_step` method to obtain the next iterate and the `check_convergence` 
method to check whether the algorithm has converged. These two methods are 
abstract methods which need to be implemented by subclasses.

With these boilerplate codes in place, we can concentrate on the important 
part: How to obtain the next iterate. For steepest descent with a fixed 
step size, it is very straightforward to implement.

```python
{{#include ../codes/04-numerical_optimisation/optimiser.py:simple_steepest_descent}}
```

For steepest descent with variable step size, we need to incorporate a 
line search, like the Armijo line search mentioned in the theory section. 
```python
{{#include ../codes/04-numerical_optimisation/optimiser.py:armijo_line_search}}
```
Afterwards, we can implement the steepest descent with a variable step size 
by doing only minor modifications to the steepest descent algorithm with a
fixed step size.
```python
{{#include ../codes/04-numerical_optimisation/optimiser.py:steepest_descent}}
```

We can apply our implementation of the steepest descent algorithm to both of 
our test functions like this:
```python
{{#include ../codes/04-numerical_optimisation/plot_optimisations.py:imports}}
```
```python
{{#include ../codes/04-numerical_optimisation/plot_optimisations.py:define_objective_functions}}
```
```python
{{#include ../codes/04-numerical_optimisation/plot_optimisations.py:plot_steepest_descent}}
```

If you play around with the step size, you may realize that the Rosenbrock 
function requires a very small step size to converge, which leads to a very 
slow convergence. Starting from $x_0 = (0, 0)$, the optimization 
trajectories for both functions are shown in the following figure.
![](../assets/figures/04-numerical_optimisation/plot_optimisation_sd.svg)

