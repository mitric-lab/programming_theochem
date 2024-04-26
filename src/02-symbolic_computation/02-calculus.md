## Calculus

Calculus is hard. So why not let the computer do it for us? 

### Limits
Let us start by 
evaluating the limit
$$\lim_{x\to 0} \frac{\sin(x)}{x}$$
We first define our variable \\( x \\) and the expression inside on the 
right-hand side. Then we can use the method `limit` to evaluate the
limit for \\( x \to 0 \\). 
```python
{{#include ../codes/02-symbolic_computation/calculus.py:limit}}
```
Even one-sided limits like 
$$
\lim_{x\to 0^+} \frac{1}{x} \mathrm{\ \ vs.\ } \lim_{x\to 0^-} \frac{1}{x}
$$
can be evaluated.
```python
{{#include ../codes/02-symbolic_computation/calculus.py:one_side_limit}}
```
### Derivatives
Suppose we want to find the first derivative of the following function
$$f(x, y) = x^3 + y^3 + \cos(x \cdot y) + \exp(x^2 + y^2)$$
We first start by defining the expression on the right side. In the next 
step, we can call the `diff` function, which expects an expression as the
first argument. The second to last argument (you can use one or more) is 
the symbolic variables by which the expression will be differentiated. 
```python
{{#include ../codes/02-symbolic_computation/calculus.py:first_derivative}}
```
This way, we create the first derivative of $f(x, y)$ with respect to
$x$. You should get:
$$
x^{3}+y^{3}+e^{x^{2}+y^{2}}+\cos (x y)
$$

We can also build the second and third derivatives with respect to `x`:
```python
{{#include ../codes/02-symbolic_computation/calculus.py:2_3_derivative}}
```
Note that two different methods for computing higher derivatives are presented here. Of course, it is also possible to create the first derivative with respect to 
\\( x\\) and \\(y\\):
```python
{{#include ../codes/02-symbolic_computation/calculus.py:x_y_derivative}}
```
#### Evaluating Derivatives (or any other expression)
Sometimes, we want to evaluate derivatives, or just any expression at 
specified points. For this purpose, we could again use `Lambda` to convert 
the expression into a function and insert values by function calls; 
However, SymPy expressions have the `subs` method to avoid the detour:
```python
{{#include ../codes/02-symbolic_computation/calculus.py:substitution}}
```
This method takes a pair of arguments. The first one is the variable to be 
substituted and the second one is the value. Note that the value can also be a 
variable or an expression. A list of such pairs can also be supplied to 
substitute multiple variables.

### Integrals

Even the most challenging part in calculus (integrals) can be evaluated
$$
\int \mathrm{e}^{-x} \mathrm{d}x
$$
```python
{{#include ../codes/02-symbolic_computation/calculus.py:indefinit_integral}}
```
This evaluates to
$$
-e^{-x}
$$
Note that SymPy does not include the constant of integration. 
But this can be added easily by oneself if needed.

A definite integral could be computed by substituting the integration variable 
with upper and lower bounds using `subs`. But it is more straightforward to 
just pass the tuple with both bounds as the second argument to the 
`integrate` function: 
Suppose we want to compute the definite integral
$$\int_{0}^{\infty} \mathrm{e}^{-x}\  \mathrm{d}x$$
one can write
```python
{{#include ../codes/02-symbolic_computation/calculus.py:definit_integral}}
```
which evaluates to 1.

Also multivariable integrals like
$$ \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \mathrm{e}^{-x^2-y^2}\  \mathrm{d}x \mathrm{d}y $$
can be easily solved. In this case the integral
```python
{{#include ../codes/02-symbolic_computation/calculus.py:multivariable_integral}}
```
evaluates to \\( \pi \\).

