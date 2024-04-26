## Arithmetic Operators

Arithmetic operators are used to perform mathematical operations 
like addition, subtraction, multiplication, and division. 
In Python (>3.5), 7 arithmetic operators are defined:

| Operator | Name           | Example  | Output (x=7, y=2)|
|----------|----------------|----------|------------------|
| `+`      | Addition       | `x + y`  |                 9|
| `-`      | Subtraction    | `x - y`  |                 5|
| `*`      | Multiplication | `x * y`  |                14|
| `/`      | Division       | `x / y`  |               3.5|
| `//`     | Floor division | `x // y` |                 3|
| `%`      | Modulus        | `x % y`  |                 1|
| `**`     | Exponentiation | `x ** y` |                49|

### Addition
The `+` (addition) operator yields the sum of its arguments. 

The arguments must **either both be numbers or both be sequences** of the same type. 
Only in the former case, the numbers are converted to a common type, 
and an arithmetic addition is performed. 
In the latter case, the sequences are concatenated, e.g.
```python
a = [1, 2, 3]
b = [4, 5, 6]
assert (a + b) == [1, 2, 3, 4, 5, 6]
```

### Subtraction

The `-` (subtraction) operator yields the difference of its arguments. 
The numeric arguments are first converted to a common type.
Note: In contrast to the addition, the subtraction operator cannot be applied to sequences. 

### Multiplication

The `*` (multiplication) operator yields the product of its arguments.
The arguments must **both be numbers** or alternatively, **one argument must be an integer while the other must be a sequence**.
In the former case, the numbers are converted to a common type and then multiplied together. 
In the latter case, sequence repetition is performed; e.g. 
```python
a = [1, 2]
assert (3 * a) == [1, 2, 1, 2, 1, 2]
```

Note: a negative repetition factor yields an empty sequence; e.g. 
```python
a = 3 * [1, 2]
assert (-2 * a) == []
```

### Division & Floor division

The `/` (division) and `//` (floor division) operators yield the 
quotient of their arguments. 
The numeric arguments are first converted to a common type. 
Be aware that the **division of integers yields a float**, 
while the **floor division of integers results in an integer**.
The result of the floor division operator is that of mathematical division 
with the `floor` function applied to the result. 
Division by zero raises a `ZeroDivisionError` exception.

### Modulus

The `%` (modulo) operator yields the remainder from the division of the first argument by the second. 
The numeric arguments are first converted to a common type. 
A right-side argument of zero raises the `ZeroDivisionError` exception. 
The arguments may even be floating point numbers, e.g., 
```python
import math 
assert math.isclose(3.14 % 0.7, 0.34)
assert math.isclose(3.14, 4*0.7 + 0.34) 
```
The modulo operator always yields a result with the same sign 
as its second operand (or zero); 
the absolute value of the result is strictly smaller than the 
absolute value of the second operand.

> **Note**: As you may have noticed in the listing above, 
> we did not use the comparison operator `==` to test the 
> equality of two floats. Instead we imported the `math` package
> and used the built-in 
> [isclose](https://docs.python.org/3/library/math.html#math.isclose) function.
> If you want to learn more about float representation errors, you may find 
> some useful information in this
> [blog post](https://davidamos.dev/the-right-way-to-compare-floats-in-python/).

> **Note**: If you need both the quotient and the remainder, instead of 
> performing a floor division followed by a modulus evaluation, you should 
> use the built-in 
> [`divmod`](https://docs.python.org/3/library/functions.html#divmod)
> function.

### Exponentiation 

The `**` (power) operator has the same semantics as the 
built-in `pow()` function, when called with two arguments,
it yields the left argument raised to the power of the right argument. 
Numeric arguments are first converted to a common type, the result 
type is that of the arguments after coercion.
If the result is not expressible in that type, 
(as in raising an integer to a negative power)
the result is expressed as a float (or complex). 
In an unparenthesised sequence of power and unary operators, the operators are evaluated from right to left
 (this does not constrain the evaluation order for the operands), e.g.
```python
assert 2**2**3 == 2**(2**3) == 2**8 == 256
```

