## Binary System of Signed Integers

Since digital electronics only have access to two levels standing for 
0 and 1, we will not be able to use a minus sign (\\(-\\)) for 
representing negative numbers. There are a few common ways to 
represent negative binary numbers by only using ones and zeros, which 
we will discuss in the following subsections.

```admonish note
Note: Unlike other programming languages, where different
types of integers exist (signed, unsigned, different number of bits),
Python only has one integer type (`int`). This is a __signed__
integer type with __arbitrary__ precision. This means, the integer
does not have a fixed number of bits to represent the number, but will
dynamically use as many bits as needed to represent the
number. Therefore, [integer overflows](https://en.wikipedia.org/wiki/Integer_overflow) 
cannot occur in Python.
This doesn't hold for `floats`, which have a fixed size of 64 bits and 
__can overflow__. 
```

