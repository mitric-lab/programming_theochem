### Implementation: Division

Just like for multiplication, the integer (floor) division may be treated as 
repeated subtractions. The quotient \\( \lfloor A/B  \rfloor \\) tells us how
often \\(B\\) can be subtracted from \\(A\\) before it becomes negative.

The na&iuml;ve floor division can thus be implemented as:
```python
{{#include ../../codes/01-fundamentals/division.py:naive_division}}
```

Just like na&iuml;ve multiplication, this division algorithm scales linearly with 
the size of the dividend, if the effect of the divisor is ignored.

#### Can we do better?

In the school, we have learned to do long divisions. This can also be done 
using binary numbers. We at first left-align the divisor `b` with the 
dividend `a` and compare the sizes of the overlapping part. If the divisor is 
smaller, it goes once into the dividend. Therefore, the quotient at that bit 
becomes 1 and the dividend is subtracted from the part of the divisor. Otherwise, this
quotient bit will be 0 and no subtraction takes place. Afterwards, 
the dividend is right-shifted and the whole process is repeated. 
This algorithm is illustrated in the following table for example `11 /`/ 2`: <br>

|Iteration       | `a`    | `b`     | `r`    | Action                         |
|----------------|:------:|:-------:|:------:|--------------------------------|
| preparation    | `1011` | `0010`  | `0000` | `b <<= 2`                      |
| 0              | `1011` | `1000`  | `0000` | `a -= b`, `r.2 = 1`, `b >>= 1` |
| 1              | `0011` | `0100`  | `0100` | `b >>= 1`                      |
| 2              | `0011` | `0010`  | `0100` | `a -= b`, `r.0 = 1`, `b >>= 1` |
| 3              | `0001` | `0001`  | `0101` |  Value of `b` smaller than initial. Stop.   |

An example implementation is given in the following listing:
```python
{{#include ../../codes/01-fundamentals/division.py:division}}
```

In this implementation, rather than setting the result bitwise like described 
in the table above, it is initialized to `0` and appended with `0` or `1`.
Also, the divisor is shifted by the bit-length of `a` instead of the difference 
between `a` and `b`. This may increase the number of loops but prevents 
negative shifts when the bit-length of `a` is smaller than that of `b`.

This algorithm is linear in the bit-length of the dividend and thus a
\\(\mathcal{O}(\log n)\\) algorithm. Again, we want to quantify the performance 
of both algorithms by timing them. 

Since the size of the divisor does not have a simple relation with the 
execution time, we shall fix its size. Here we choose `nb = 10`. An example 
function for timing is shown in the following listing:
```python
{{#include ../../codes/01-fundamentals/division.py:timing}}
```

Because we cannot divide by zero, the second argument, the divisor in this case, 
is chosen between 1 and n instead of 0 and n. 

The execution time per execution for different sizes is listed below:

| `na`      | `naive_div` / &#956;s | `div` / &#956;s |
|----------:|-----------------:|-----------:|
|      `10` | 0.38             | 1.06       |
|     `100` | 1.54             | 1.67       |
|   `1 000` | 13.79            | 1.83       |
|  `10 000` | 117.20           | 1.89       |
| `100 000` | 1085.89          | 2.24       |

Again, although the na&iuml;ve method is faster for smaller numbers, its scaling 
prevents it from being used for larger numbers.
