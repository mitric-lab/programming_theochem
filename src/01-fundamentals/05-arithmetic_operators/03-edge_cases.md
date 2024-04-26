### Edge Cases

#### Division by zero
Since division by zero is not defined, we should handle the case when the 
user calls the division function with `0` as a divisor. While our na&iuml;ve 
division algorithm would be stuck in the `while` loop if `0` is 
passed as the second argument and thus blocks further commands from being 
executed, the other algorithm would deliver us with a number 
(which is obviously wrong) without further notice. Neither 
of these behaviours is wanted.

In general, there are two ways to deal with "forbidden" values. The first 
one is to raise an error, just like the built-in division operators, which 
raises a `ZeroDivisionError` and halts the program. This is realized by adding 
an if-condition at the beginning of the algorithm:
```python
{{#include ../../codes/01-fundamentals/edge_cases.py:zero_division_err}}
```

Sometimes, however, we want the program to continue even after encountering 
forbidden values. In this case, we can make the algorithm return something, 
which is recognizable as invalid. This way, the user can be informed about 
forbidden values through the outputs. One possible choice of such an invalid 
object is the `None` object which can be used like
```python
{{#include ../../codes/01-fundamentals/edge_cases.py:zero_division_none}}
```

#### Negative input
While implementing multiplication and division algorithms, we only used 
non-negative integers as examples to analyze the problems. Inputs of 
negative integers may therefore lead to undefined behaviors. 
Again, we can raise an exception when 
this happens or utilise an invalid object. The following listings show both 
cases on the multiplication algorithm:
```python
{{#include ../../codes/01-fundamentals/edge_cases.py:negative_input_err}}
```
```python
{{#include ../../codes/01-fundamentals/edge_cases.py:negative_input_none}}
```
These lines can be directly added to division algorithms to deal with negative 
inputs. 

#### Floating-point input
Just like in the case of negative input values, floating-point numbers as 
inputs may also lead to undefined behaviours. Although the same input guards 
can be applied to deal with floating-point numbers, a more sensible way would 
be to convert the input values to integers using `int` function before 
executing the algorithms.
