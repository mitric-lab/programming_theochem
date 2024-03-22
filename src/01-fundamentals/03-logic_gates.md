## Logic Gates

Truth tables show the result of combining inputs using a given operator.

### NOT Gate
The NOT gate, a logical inverter, has only one input. 
It reverses the logic state. If the input is 0, then the output is 1.
If the input is 1, then the output is 0.

| INPUT | OUTPUT |
|:-----:|:------:|
|   0   |    1   |
|   1   |    0   |


### AND Gate

The AND gate acts in the same way as the logical "and" operator. 
The following truth table shows logic combinations for an AND gate. 
The output is 1 only when both inputs are 1, otherwise, the output is 0.

| A | B | Output |
|:-:|:-:|:------:|
| 0 | 0 |    0   |
| 0 | 1 |    0   |
| 1 | 0 |    0   |
| 1 | 1 |    1   |


### OR Gate

The OR gate behaves after the fashion of the logical inclusive "or".
The output is 1 if either or both of the inputs are 1. 
Only if both inputs are 0, then the output is 0.

| A | B | Output |
|:-:|:-:|:------:|
| 0 | 0 |    0   |
| 0 | 1 |    1   |
| 1 | 0 |    1   |
| 1 | 1 |    1   |


### NAND Gate

The NAND gate operates as an AND gate followed by a NOT gate. 
It acts in the manner of the logical operation "and" followed by negation.
The output is 0 if both inputs are 1. Otherwise, the output is 1.

| A | B | Output |
|:-:|:-:|:------:|
| 0 | 0 |    1   |
| 0 | 1 |    1   |
| 1 | 0 |    1   |
| 1 | 1 |    0   |

### NOR Gate

The NOR gate is a combination of OR gate followed by a NOT gate. 
Its output is 1 if both inputs are 0. Otherwise, the output is 0.

| A | B | Output |
|:-:|:-:|:------:|
| 0 | 0 |    1   |
| 0 | 1 |    0   |
| 1 | 0 |    0   |
| 1 | 1 |    0   |


### XOR Gate

The XOR (exclusive-OR) gate acts in the same way as the logical 
"either/or." The output is 1 if either, __but not both__, of the
inputs are 1. The output is 0 if both inputs are 0
or if both inputs are 1. Another way of looking at this circuit
is to observe that the output is 1 if the inputs are different,
but 0 if the inputs are the same. 

| A | B | Output |
|:-:|:-:|:------:|
| 0 | 0 |    0   |
| 0 | 1 |    1   |
| 1 | 0 |    1   |
| 1 | 1 |    0   |


### XNOR Gate

The XNOR (exclusive-NOR) gate is a combination of XOR gate followed 
by a NOT gate. Its output is 1 if the inputs are the same, 
and 0 if the inputs are different.

| A | B | Output |
|:-:|:-:|:------:|
| 0 | 0 |    1   |
| 0 | 1 |    0   |
| 1 | 0 |    0   |
| 1 | 1 |    1   |


```admonish tip
To see these gates in action, you can try the game 
[Digital Logic Sim](https://sebastian.itch.io/digital-logic-sim), which 
is explained in [https://youtu.be/QZwneRb-zqA](https://youtu.be/QZwneRb-zqA).
```

