## Bitwise Operators

Bitwise operators are used to manipulate the states of bits directly. 
In Python (>3.5), 6 bitwise operators are defined:

| Operator | Name           | Example  | Output (x=7, y=2)|
|----------|----------------|----------|------------------|
| `<<`     | left bitshift  | `x << y` |                28|
| `>>`     | right bitshift | `x >> y` |                 1|
| `&`      | bitwise and    | `x & y`  |                 2|
| <code>&#124;<code> | bitwise or | <code>x &#124; y<code> |7|
| `~`      | bitwise not    | `~x`     |                -8|
| `^`      | bitwise xor    | `x ^ y`  |                 5|

### Left Bitshift

Returns x with the bits shifted to the left by y places 
(and new bits on the right-hand-side are zeros). 
This is the same as multiplying \\(x\\) by \\(2^y\\).

The easiest way to visualize this operation is to consider a number 
that consists of only a single 1 in binary representation. 
If we now simply shift a 1 to the left three times in succession, 
we get the following: 
```python
assert (1 << 1) == 2  # ..0001 => ..0010
assert (2 << 1) == 4  # ..0010 => ..0100
assert (4 << 1) == 8  # ..0100 => ..1000
```
But we can also do this operation with just one call: 
```python
assert (1 << 3) == 8  # ..0001 => ..1000
```

Of course, we can also apply this operation to any other number: 
```python
assert (3 << 2) == 12 # ..0011 => ..1100
```

### Right Bitshift

Returns x with the bits shifted to the right by y places. 
This is the same as dividing \\(x\\) by \\(2^y\\).

```python
assert (8 >> 1) == 4 # ..1000 => ..0100
assert (4 >> 1) == 2 # ..0100 => ..0010
assert (2 >> 1) == 1 # ..0010 => ..0001
```
As we did with the bit shift to the left side, we can also shift a bit 
multiple times to the right:
```python
assert (8 >> 3) == 1 # ..1000 => ..0001
```
Or apply the operator to any other number that is not a multiple of 2. 
```python
assert (11 >> 2) == 2 # ..1011 => ..0010
```

### Bitwise AND

Does a "bitwise and". Each bit of the output is 1 if the corresponding 
bit of \\(x\\) AND \\(y\\) is 1, otherwise it is 0.

```python
assert (1 & 2) == 0  # ..0001 & ..0010 => ..0000 
assert (7 & 5) == 5  # ..0111 & ..0101 => ..0101
assert (12 & 3) == 0 # ..1100 & ..0011 => ..0000
```

### Bitwise OR 
Does a "bitwise or". Each bit of the output is 0 if the corresponding 
bit of \\(x\\) OR \\(y\\) is 0, otherwise it's 1.
```python
assert (1 | 2) == 3   # ..0001 & ..0010 => ..0011 
assert (7 | 5) == 7   # ..0111 & ..0101 => ..0111
assert (12 | 3) == 15 # ..1100 & ..0011 => ..1111
```
### Bitwise NOT

Returns the complement of \\(x\\) - the number you get by switching each 
1 for a 0 and each 0 for a 1. This is the same as \\(-x - 1\\).
```python
assert ~0 == -1      
assert ~1 == -2
assert ~2 == -3
assert ~3 == -4 
```

### Bitwise XOR

Does a "bitwise exclusive or". Each bit of the output is the same as 
the corresponding bit in \\(x\\) if that bit in \\(y\\) is 0, and it is the 
complement of the bit in x if that bit in y is 1.

```python
assert (1 ^ 2) == 3   # ..0001 & ..0010 => ..0011 
assert (7 ^ 5) == 2   # ..0111 & ..0101 => ..0010
assert (12 ^ 3) == 15 # ..1100 & ..0011 => ..1111
```
