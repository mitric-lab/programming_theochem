## Basic Operations

```admonish tip
We strongly advise you to try out the following small code examples yourself,
preferably in a Jupyter notebook. There you can easily see the value of the 
variables and the equations can be rendered as latex. 
Just write the SymPy variable at the end of Jupyter cell without calling
the `print` function explicitly. 
```

### Defining Variables
Before solving any problem, we start defining our symbolic variables. 
SymPy provides the constructor `sp.Symbol()` for this:
```python
x = sp.Symbol('x')
```
This defines the Python variable `x` as a SymPy `Symbol` with the representation
'x'. If you print the variable in a Jupyter cell, you should see a rendered 
symbol like: \\( x \\).
Since it might be annoying to define a lot variables, SymPy provides a another
function, which can initialize a arbitrary number of symbols. 
```python
x, y, t, omega = sp.symbols('x y t omega')
```
which is just a shorthand for
```python
x, y, t, omega = [sp.Symbol(n) for n in ('x', 'y', 't', 'omega')]
```
Note that it is important to separate each symbol in the `sp.symbols()` call
with a space. 
SymPy also provides often used symbols (Latin and Greek letters) as predefined 
variables. They are located in the submodule called `abc` 
and can be imported by calling
```python
from sympy.abc import x, y, nu
```
### Expressions

Now we can use these variables to define an expression. We first want to 
define the following expression:
$$
x + 2 y
$$
SymPy allows us to write this expression in Python as we would do on paper:
```python
{{#include ../codes/02-symbolic_computation/basic_operations.py:expression}}
```
If you now print `f` in Jupyter cell you should see the same rendered equation
as above. 
Lets assume we want to multiply our expression not by \\( x \\). We can 
just do the following: 
```python
{{#include ../codes/02-symbolic_computation/basic_operations.py:f_times_x}}
```
Now, we can print `g` and should get: 
$$
x (x + 2y)
$$
One may expect this expression to transform into 
\\(x^2 + 2xy\\), but we get the factorized form instead. SymPy 
only performs obvious simplifications automatically, since one might 
prefer the expanded or the factorized form depending on the circumstances. 
But we can easily switch between both representations using the
transformation functions `expand` and `factor`: 
```python
{{#include ../codes/02-symbolic_computation/basic_operations.py:expand}}
```
If you print `g_expanded`, you should see the expanded form of the equation:
$$
x^2 + 2xy
$$
Factorization of `g_expanded` brings us back to where we started. 
```python
{{#include ../codes/02-symbolic_computation/basic_operations.py:factor}}
```
with the following representation:
$$
x (x + 2y)
$$

If you prefer a more automated approach, you can use the function `simplify`. 
SymPy will then try to figure out which form would be the most suitable. 


We can also write more complicated functions using elementary functions:
```python
{{#include ../codes/02-symbolic_computation/basic_operations.py:complicated_expression}}
```
Note that since the division operator `/` on a number produces 
floating-point numbers, we should modify numbers with the function `sympify`. 
When dealing with rationals like `2/5`, we can use `sp.Rational(2, 5)` instead. 
If you print f the rendered equation should look like:
$$
\frac{\sqrt{2} e^{-t} \cos \left( \omega t \right)}{2}
$$
On some platforms, you may get a nicely rendered expression. While other 
platforms does not support LaTeX-rendering, you could try to turn on
unicode support by executing
```python
sp.init_printing(use_unicode=True)
```
at the beginning of your code.

We can also turn our expression into a function with either one 
```python
{{#include ../codes/02-symbolic_computation/basic_operations.py:function_one_arg}}
```
or multiple arguments
```python
{{#include ../codes/02-symbolic_computation/basic_operations.py:function_two_args}}
```
by using the `Lambda` function. In the first case printing of `f_func1`
should look like
$$
\left(t \mapsto \frac{\sqrt{2} e^{-t} \cos (\omega t)}{2}\right)
$$
while `f_func2` should give you: 
$$
\left((t, \omega) \mapsto \frac{\sqrt{2} e^{-t} \cos (\omega t)}{2}\right)
$$
As you can see, these are still symbolic expressions. But the Python object is
now a callable function with either one or two positional arguments.
This allows us to substitute e.g. the variable \\( t \\) with 
 a number: 
```python
{{#include ../codes/02-symbolic_computation/basic_operations.py:function_call_one}}
```
This gives us: 
$$
\frac{\sqrt{2} \cos (\omega)}{2 e}
$$ 
We can also call our second function, which takes 2 arguments (\\(t\\), and \\(\omega\\)).
```python
{{#include ../codes/02-symbolic_computation/basic_operations.py:function_call_two}}
```
Which will result in:
$$
\frac{\sqrt{2} \cos \left(\frac{1}{2}\right)}{2 e^{\frac{1}{2}}}
$$
Note: We have now eliminated all variables and are left with an exact number, but this still
a SymPy object. You might wonder how we can transform this to a numerical value which 
can be use by other Python modules. SymPy provides this transformation with the function
`lambdify`, this looks similar to the `Lambda` function and also returns a Python function, that
we can call. However, the returned value of this function is now numerical value. 

```python
{{#include ../codes/02-symbolic_computation/basic_operations.py:numeric_function}}
```

Alternatively, we can convert the expression directly into a float 
(or complex) by using the built-in functions `float()` or `complex`:
```python
{{#include ../codes/02-symbolic_computation/basic_operations.py:expression_to_python_float}}
```

SymPy also offers us a way to convert an expression to a float (or complex):
```python
{{#include ../codes/02-symbolic_computation/basic_operations.py:expression_to_sympy_float}}
```
Although `f_01_expr_num` gives us the same result as the python float in the 
first glance, its type is not ´float´, but rather `sympy.core.numbers.Float`. 
Note the capital F. This is a floating point data type from sympy, which has 
arbitrary precision. The last line, for example, evaluates the expression 
with 50 valid decimal places instead of the standard 15 or 16 of Python's 
built-in `float`.

