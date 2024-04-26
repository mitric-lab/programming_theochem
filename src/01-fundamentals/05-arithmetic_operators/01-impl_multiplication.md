## Implementation: Arithmetic Operators

All arithmetic operators can be implemented using bitwise operators. 
While addition and subtraction are implemented through hardware, 
the other operators are often realized via software. In this section, we shall 
implement multiplication and division for positive integers using addition, 
subtraction, and bitwise operators.

### Implementation: Multiplication

The multiplication of integers may be thought of as repeated addition; 
that is, the multiplication of two numbers is equivalent to the following
sum:
$$
A \cdot B = \sum_{i=1}^{A} B
$$
Following this idea, we can implement a na&iuml;ve multiplication: 
```python
{{#include ../../codes/01-fundamentals/multiplication.py:naive_multiplication}}
```

Although we could be smart and reduce the number of loops by choosing the 
smaller one to be the multiplier, the number of additions always 
grows linearly with the size of the multiplier. Ignoring the effect of the
multiplicand, this behavior is called linear scaling, which is often denoted 
as \\(\mathcal{O}(n)\\). 

#### Can we do better?

We have learned that multiplication by powers of 2 can be easily realized by
the left shift operator `<<`. Since every integer can be written as a sum of 
powers of 2, we may try to compute the necessary products of the multiplicand 
with powers of 2 and sum them up. We shall do an example: `11 * 3`.
```python
assert (2**3 + 2**1 + 2**0) * 3 == 11 * 3
assert (2**3 * 3 + 2**1 * 3 + 2**0 *3) == 11 * 3
assert (3 << 3) + (3 << 1) + 3 == 11 * 3
```
To implement this idea, we can start from the multiplicand (`b`) and check the 
least-significant-bit (LSB) of the multiplier (`a`). If the LSB is 1, this 
power of 2 is present in `a`, and `b` will be added to the result. If 
the LSB is 0, this power is 
not present in `a` and nothing will be done. In order to check the second LSB of `a` 
and perhaps add `2 * b`, we can just right-shift `a`. In this way, the second LSB
will become the new LSB and `b` needs to be multiplied by 2 (left shift).
This algorithm is illustrated in the example above: <br>

|Iteration | `a`    | `b`       | `r`      | Action                          |
|----------|:------:|:---------:|:--------:|---------------------------------|
| 0        | `1011` | `000011`  | `000000` | `r += b`,  `b <<= 1`, `a >>= 1` |
| 1        | `0101` | `000110`  | `000011` | `r += b`,  `b <<= 1`, `a >>= 1` |
| 2        | `0010` | `001100`  | `001001` | `b <<= 1`, `a >>= 1`            |
| 3        | `0001` | `011000`  | `001001` | `r += b`,  `b <<= 1`, `a >>= 1` |
| 4        | `0000` | `110000`  | `100001` | Only zeros in `a`. Stop.        |

An example implementation is given in the following listing:
```python
{{#include ../../codes/01-fundamentals/multiplication.py:multiplication}}
```

This new algorithm should scale with the length of the binary representation of 
the multiplier, which grows logarithmically with its size. This is denoted as
\\(\mathcal{O}(\log n)\\). 

To show the difference between these two algorithms, we can write a function 
to time their executions. The following example uses the function 
`perf_counter` from the `time` module:
```python
{{#include ../../codes/01-fundamentals/multiplication.py:timing}}
```

The execution time per execution for different sizes is listed below:

| `n`       | `naive_mul` / &#956;s | `mul` / &#956;s |
|----------:|-----------------:|-----------:|
|      `10` | 0.48             | 0.80       |
|     `100` | 2.83             | 1.56       |
|   `1 000` | 28.83            | 1.88       |
|  `10 000` | 224.33           | 2.02       |
| `100 000` | 2299.51          | 2.51       |

Although the na&iuml;ve algorithm is faster for \\(a,b \leq 10\\), its time 
consumption grows rapidly when `a` and `b` become larger. For even larger 
numbers, it will quickly become unusable. The second algorithm, however, 
scales resonably well to be applied for larger numbers.
