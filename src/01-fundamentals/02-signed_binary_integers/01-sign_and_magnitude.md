### Sign and Magnitude

The most significant bit (MSB) determines if the number is positive 
(MSB is 0) or negative (MSB is 1). All the other bits are the so-called
magnitude bits. This means that an 8-bit signed integer can represent all
numbers from -127 to 127 ($-2^6$ to $2^6$). Except for the MSB,
all positive and negative numbers share the same representation.

<p align="center"> <img src="../../assets/figures/01-fundamentals/sam_1.svg" alt="Sign and Magnitude 1"/> </p>

<!---
```bob
  MSB                                       LSB
   |                                         |
   v                                         v
.-----+-----+-----+-----+-----+-----+-----+-----+----------------.
|Bit 7|Bit 6|Bit 5|Bit 4|Bit 3|Bit 2|Bit 1|Bit 0| Decimal Number | 
+-----+-----+-----+-----+-----+-----+-----+-----+----------------+
|  0  |  0  |  0  |  0  |  1  |  1  |  0  |  1  |                |
|-----+-----+-----+-----+-----+-----+-----+-----+       13       |
| -1  | 64  | 32  | 16  |  8  |  4  |  2  |  1  |                |
'-----+-----+-----+-----+-----+-----+-----+-----+----------------'
   ^     |                                   |
   |     |___________________________________|
  sign              magnitude bits
```
-->

*Visualization of the Sign and Magnitude representation of the 
decimal number +13.*

In the case of a negative number, the only difference is that the first
bit (the MSB) is inverted, as shown in the following Scheme. 

<p align="center"> <img src="../../assets/figures/01-fundamentals/sam_2.svg" alt="Sign and Magnitude 2"/> </p>

<!---
```bob
.-----+-----+-----+-----+-----+-----+-----+-----+----------------.
|Bit 7|Bit 6|Bit 5|Bit 4|Bit 3|Bit 2|Bit 1|Bit 0| Decimal Number | 
+-----+-----+-----+-----+-----+-----+-----+-----+----------------+
|  1  |  0  |  0  |  1  |  1  |  1  |  1  |  1  |                |
|-----+-----+-----+-----+-----+-----+-----+-----+       -31      |
| -1  | 64  | 32  | 16  |  8  |  4  |  2  |  1  |                |
'-----+-----+-----+-----+-----+-----+-----+-----+----------------'
```
-->

*Visualization of the Sign and Magnitude representation of the decimal 
number -31*

Although this representation seems very intimate and simple, several 
problems associated with the sign bit arise:
- There are two ways to represent zero, `0000 0000` and `1000 0000`.
- Addition and subtraction require different behaviours depending
  on the sign bit.
- Comparisons (e.g. greater, less, ...) also require inspection of 
  the sign bit.

This approach is directly comparable to the common way of showing a
sign (placing a "+" or "−" next to the number's magnitude).
This kind of representation was only used in early binary computers
and was replaced by representations that we will discuss in the 
following. 


