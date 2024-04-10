## Hermite Gaussian Orbitals

Though very intuitive, the Cartesian Gaussians are not easy to integrate 
except for s-type Gaussians, since the polynomial product makes the evaluation 
quite tedious. It would be nice if we could somehow generate integrals involving 
higher orbital angular momenta from integrals involving only s-type Gaussians.

### Hermite Gaussian Functions

We now introduce another form of GTOs, the Hermite Gaussians. Ignoring 
the normalisation constant, they are defined as

$$
h_{ijk}(\vec{r}; \alpha, \vec{A}) = 
  \left( \frac{\partial}{\partial A_x} \right)^{i}
  \left( \frac{\partial}{\partial A_y} \right)^{j}
  \left( \frac{\partial}{\partial A_z} \right)^{k}
  \eu^{-\alpha \| \vec{r} - \vec{A} \|^2}
$$

Although it might look very complicated in the first glance, it is 
essentially a Cartesian Gaussian with the Cartesian polynomial part 
replaced by a polynomial obtained through differentiation of an s-type 
Gaussian, or the Hermite polynomial. 

Just like their Cartisian counterparts, the Hermite Gaussians can also be 
factored into Cartesian directions. A 1D Hermite Gaussian of degree $k$ 
can thus be expressed as
$$
h_{k}(x; \alpha, A_x) =
  \left( \frac{\partial}{\partial A_x} \right)^k
  \eu^{-\alpha ( x - A_x )^2}
$$

### Recurrence Relations
While it is straight-forward to generate a Cartesian Gaussian of degree 
$n + 1$ from a degree $n$ one by just multiplying $x - A_x$ 
to it, i.e.
$$
g_{n + 1}(x) = (x - A_x)\ g_{n}(x)
$$
the relation for Hermite Gaussians is a bit complicated. 

We shall start with the definition of Hermite Gaussians, which states
$$
h_{k+1}(x) = 
  \left( \frac{\partial}{\partial A_x} \right)^k 
  \frac{\partial}{\partial A_x} \exp\left( -\alpha (x - A_x)^2 \right) = 
  2 \alpha \left( \frac{\partial}{\partial A_x} \right)^k (x - A_x) 
  \ \eu^{-\alpha (x - A_x)^2}
$$
The $k$-th derivative of the product 
$ (x - A_x) \cdot \eu^{-\alpha (x - A_x)^2} $
can be calculated using the [general Leibniz rule](https://en.wikipedia.org/wiki/General_Leibniz_rule):
$$
\left(\frac{\partial}{\partial A_x}\right)^k 
  \left[(x - A_x) \eu^{-\alpha (x - A_x)^2}\right] 
  = \sum_{j=0}^k \binom{k}{j} 
    \left(\frac{\partial}{\partial A_x}\right)^j (x - A_x) 
    \left(\frac{\partial}{\partial A_x}\right)^{k-j} \eu^{-\alpha (x - A_x)^2}
$$

Since the first factor $(x - A_x)$ is a first-order polynomial in 
$A_x$, derivatives with order 2 or higher become zero. The whole 
expression thus simplifies to
$$
\begin{align}
\left(\frac{\partial}{\partial A_x}\right)^k 
  \left[(x - A_x) \eu^{-\alpha (x - A_x)^2}\right] 
  &= \binom{k}{0} \left(\frac{\partial}{\partial A_x}\right)^0 (x - A_x) 
    \left(\frac{\partial}{\partial A_x}\right)^{k} \eu^{-\alpha (x - A_x)^2} \\
  &\hphantom{=} + \binom{k}{1}
    \left(\frac{\partial}{\partial A_x}\right)^1 (x - A_x) 
    \left(\frac{\partial}{\partial A_x}\right)^{k-1} \eu^{-\alpha (x - A_x)^2} \\
  &= (x - A_x) \left(\frac{\partial}{\partial A_x}\right)^{k} \eu^{-\alpha (x - A_x)^2} - 
  k \left(\frac{\partial}{\partial A_x}\right)^{k-1} \eu^{-\alpha (x - A_x)^2} \\
  &= (x - A_x)\ h_k(x) - k\ h_{k-1}(x)
\end{align}
$$
Combined with the equation for $h_{k+1}(x)$ above, we get
$$
h_{k+1}(x) =  2\alpha \left[ (x - A_x)\ h_k(x) - k\ h_{k-1}(x) \right]
$$
We can thus get the Hermite Gaussian of order $k+1$ with Hermite Gaussians 
of order $k$ and $k-1$. This kind of relations, where an object with 
one or several indices is related to objects with smaller indices, are called 
recurrence relations.

The recurrence relation for Hermite Gaussians is often expressed as
$$(x - A_x) h_{k}(x) = \frac{1}{2 \alpha} h_{k+1}(x) + k h_{k-1}(x)$$
which is obtained by simple algebraic manupulation from the recurrence 
relation above.

Why are Hermite Gaussians useful? suppose we want to evaluate an integral 
involving a $k$-th order Hermite Gaussian, we can reduce it to an integral 
involving an zeroth order Hermite Gaussian as follows
$$
\begin{align}
\int h_k(x) f(x)\ \mathrm{d}x
  &= \int h_k(x)\ f(x)\ \mathrm{d}x \\
  &= \int \left( \frac{\partial}{\partial A_x} \right)^k \eu^{-\alpha (x - A_x)^2} f(x)\ \mathrm{d}x \\
  &= \left( \frac{\partial}{\partial A_x} \right)^k \int \eu^{-\alpha (x - A_x)^2} f(x)\ \mathrm{d}x \\
  &= \left( \frac{\partial}{\partial A_x} \right)^k \int h_0(x)\ f(x)\ \mathrm{d}x
\end{align}
$$
where $f(x)$ denotes an arbitrary function. Therefore, if we can solve 
an integral for $h_0(x)$, we can solve the integrals for all 
$h_k (x)$. 

### Hermite Gaussian Expansion
However, since our basis functions are Cartesian Gaussians, we have to expand 
them into Hermite Gaussians:
$$
g_n(x) = \sum_k c_{kn} h_k(x)
$$

To find the expansion coefficients, we shall examine $g_{n+1}$:
$$
\begin{align}
g_{n+1} &= (x-A_x)\cdot g_n \\
  &= (x-A_x) \cdot \sum_k c_{kn} h_k \\
  &= \sum_k c_{kn} (x-A_x)\ h_k \\
  &= \sum_k c_{kn} \left( \frac{1}{2\alpha} h_{k+1} + h_{k-1} \right) \\
  &= \sum_k \frac{1}{2\alpha} c_{kn} h_{k+1} + \sum_k k c_{kn} h_{k-1}
\end{align}
$$
Note that we have used the recurrence relation for Hermite Gaussians in the 
second last step. Since the summation indices can be named as we like, we 
shall replace $k$ with $k+1$ in the first sum and with 
$k-1$ in the second sum to obtain
$$
g_{n+1} = \sum_k \frac{1}{2\alpha} c_{k-1,n} h_{k} + \sum_k (k+1) c_{k+1,n} h_{k} = \sum_k \left( \frac{1}{2\alpha} c_{k-1,n} + (k+1) c_{k+1,n} \right) h_k
$$
By evaluating $g_{n+1}$ directly, we obtain
$$
g_{n+1} = \sum_k c_{k,n+1} h_k
$$
Comparing the coefficients for each $h_k$, we can get the recurrence 
relation for the expansion coefficients:
$$
c_{k,n+1} = \frac{1}{2\alpha}\ c_{k-1,n} + (k+1)\ c_{k+1,n}
$$

Such recurrence relations can be intuitively implemented in a recursive manner:
```python
{{#include ../codes/03-molecular_integrals/hermite_expansion.py:hermite_expansion}}
```

The function decorater `cache` is used to speed up the execution.

