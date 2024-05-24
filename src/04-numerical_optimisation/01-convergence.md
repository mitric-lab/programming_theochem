## Convergence

There are several ways to define convergence in numerical optimisation.
Here, we will use the distance between the iterate $x_k$ and the optimal solution 
$x^{*}$ as the measure of convergence.

For a given convergence tolerance $\epsilon > 0$, we say that the 
optimization method converges to the optimal solution $x^{*}$ when 
$$
\|x_k - x^{*}\| \leq \epsilon
$$
for some $k$. Here, $x_k$ denotes the $k$-th iterate of 
the optimization method. For two successive iterates $x_k$ and 
$x_{k+1}$, we say that a method has the *order of convergence* 
$q\geq 1$ and the *rate of convergence* $r$ if
$$
  \|x_{k+1} - x^{*}\| \leq r \|x_k - x^{*}\|^q
$$
In English, this means that in the long run, each iteration reduces the 
error at least by a factor of $r$ and it gets a bonus reduction 
if $q > 1$.

```admonish note
The order of convergence is not necessarily an integer.
```

We now examine some special cases of $q$ and $r$.

### Linear Convergence
If $q = 1$ and $r \in (0, 1)$, we say that the method has *linear 
convergence*. In this case, the inequality simplifies to
$$
  \|x_{k+1} - x^{*}\| \leq r \|x_k - x^{*}\|
$$
which can be recursively applied to yield
$$
  \|x_{k+1} - x^{*}\| \leq r^{k+1} \|x_0 - x^{*}\| = r^{k+1} R_0
$$
with $x_0$ being the initial guess. So, the error at the $k$-th 
iteration is at most $r^{k} R_0$. By requiring $r^k R_0 \leq \epsilon$, 
we see that $r_k \leq \frac{\epsilon}{R_0}$, or equivalently 
$$
\begin{align}
  k \ln r &\leq \ln \frac{\epsilon}{R_0} = \ln \epsilon - \ln R_0 \\
  k &\geq \frac{\ln \epsilon}{\ln r} - \frac{\ln R_0}{\ln r} \\
  k &\geq \frac{1}{|\ln r|} \ln \frac{1}{\epsilon} + \frac{\ln R_0}{|\ln r|} \\
\end{align}
$$

Therefore, **in the worst case**, the number of iterations $k$ required 
to achieve the tolerance $\epsilon$ is proportional to 
$\frac{1}{\epsilon}$, which means $k$ is of order 
$\mathcal{O}\left(\log \frac{1}{\epsilon}\right)$.

### Sublinear Convergence
If $q = 1$ and $r = 1$, we say that the method has *sublinear 
convergence*. In this case, the inequality above reads
$$
  \|x_{k+1} - x^{*}\| \leq \|x_k - x^{*}\|
$$
which means that the error is not reduced at all in the worst case. 
In not-so-worst cases, the error can be written as
$$
  \|x_{k} - x^{*}\| \leq \frac{1}{k^{1/\alpha}} \|x_0 - x^{*}\| 
  = \frac{1}{k^{1/\alpha}} R_0
$$
where $\alpha$ is a constant. Again, by requiring 
$\frac{1}{k^{1/\alpha}} R_0 \leq \epsilon$, we obtain
$$
  k \geq \frac{R_0}{\epsilon^{\alpha}}
$$
after some algebra. So $k$ is of order 
$\mathcal{O}\left(\frac{1}{\epsilon^{\alpha}}\right)$.

### Quadratic Convergence
If $q = 2$ and $r \in (0, \infty)$, we say that the method has 
*quadratic convergence*. The inequality becomes
$$
  \|x_{k+1} - x^{*}\| \leq r \|x_k - x^{*}\|^2
$$
or, after recursive application,
$$
  \|x_{k+1} - x^{*}\| 
  \leq r^{2^{k+1} - 1} \|x_0 - x^{*}\|^{2^{k+1}} = r^{2^{k+1} - 1} R_0^{2^{k+1}}
$$
You know the drill by now. By requiring the upper bound of the 
error at the $k$-th iteration to be less than $\epsilon$, i.e. 
$r^{2^k - 1} R_0^{2^k} \leq \epsilon$, we obtain
$$
  (r R_0)^{2^k} \leq \frac{\epsilon}{r}
  \Leftrightarrow 
  2^k \ln (r R_0) \leq \ln (\epsilon r) = \ln \epsilon + \ln r
$$
Assume that $r R_0 \leq 1$, so $\ln (r R_0) \leq 0$. 
So we divide both sides by $\ln (r R_0)$ and flip the inequality 
sign to obtain
$$
  2^k \geq \frac{\ln \epsilon}{\ln (r R_0)} + \frac{\ln r}{\ln (r R_0)}
  = \frac{1}{|\ln (r R_0)|} \ln \frac{1}{\epsilon} - \frac{\ln r}{|\ln (r R_0)|}
$$
Taking the logarithm again, we get
$$
  k \leq c_1 \ln \ln \frac{1}{\epsilon} + c_2
$$
with all constants being absorbed into $c_1$ and $c_2$. Therefore, 
$k$ is of order $\mathcal{O}\left(\log \log \frac{1}{\epsilon}\right)$.

```admonish note
We have assumed that $r R_0 \leq 1$, which translates to 
$\|x_0 - x^{*}\| \leq \frac{1}{r}$, i.e. the initial guess must 
be sufficiently close to $x^{*}$. This is a typical requirement for 
second-order methods. If this is not the case, then quadratic convergence 
is not guaranteed.
```

### Other Convergence Measures
Except for the difference between the $k$-th iterate and the optimal 
solution $\|x_{k}-x^{*}\|$, another intuitive measure of convergence 
would be the difference between the function value of the $k$-th 
iteration and the optimal value $f(x^{*})$, i.e. 
$|f(x_{k+1})-f(x^{*})|$.

These two measures, however, are only useful for theoretical analysis and 
cannot be used in practice. The reason is that we do not know the optimal 
solution $x^{*}$ in advance. Some of the alternative, heuristic but 
more practical convergence measures are listed below.

- Absolute difference between two successive iterates: $\|x_{k+1}-x_k\|$
- Relative difference between two successive iterates: $\frac{\|x_{k+1}-x_k\|}{\|x_k\|}$
- Absolute difference between two successive function values: $|f(x_{k+1})-f(x_k)|$
- Relative difference between two successive function values: $\frac{|f(x_{k+1})-f(x_k)|}{|f(x_k)|}$
- Gradient norm: $\|\nabla f(x_k)\|$

