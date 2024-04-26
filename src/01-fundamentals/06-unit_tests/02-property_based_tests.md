### Property-Based Tests

Instead of comparing produced with expected outputs, we could use properties 
that the function must satisfy as testing criteria. 
Let us consider a function `cat` which takes two `str` as input and outputs 
the concatenation of them. Using example-based tests, we would feed the 
function with different strings and compare the outputs, i.e.
```python
{{#include ../../codes/01-fundamentals/test_cat.py:example_test}}
```
With property-based tests, however, we can use the property that the 
concatenated string must contain and only contain both inputs in the given 
order and nothing else. This yields the following listing:
```python
{{#include ../../codes/01-fundamentals/test_cat.py:property_test}}
```

Although we used an example here, no expected output is needed. So in 
principle, we could use randomly generated strings. Because property-based 
tests are designed to test a large number of inputs, smart ways of choosing 
inputs and finding errors have been developed. All of these are implemented 
in the module [`Hypothesis`](https://hypothesis.readthedocs.io/en/latest/).
This can be installed by running
```bash
mamba install -c conda-forge hypothesis
```

The package `Hypothesis` contains two key components. The first one is called 
`strategies`. This module contains a range of functions that return a search 
strategy, an object with methods that describe how to generate and simplify 
certain kinds of values. The second one is the `@given` decorator, which takes 
a test function and turns it into a parametrized one, which, when called, will 
run the test function over a wide range of matching data from the selected 
strategy.

#### Test the `mul` function
For multiplication, we could use the property that the product must divide both inputs, i.e. 
```python
assert r % a == 0
assert r % b == 0
```
But since we have a reference method, we can combine the best of two worlds: 
intuitive output comparison from example-based testing **and**** smart 
algorithms as well as lots of inputs from property-based testing. The test 
function can thus be written like
```python
{{#include ../../codes/01-fundamentals/test_mul_div_prop.py:test_mul}}
```

Since this test is very similar to the test with randomly generated 
examples, we expect it to pass too. Calling `pytest`, the test failed, 
however. `Hypothesis` gives us the following output:
```
Falsifying example: test_mul_property(
    a=-1, b=1,
)
```

Of course! We did not have negative numbers in mind while implementing this
algorithm! But why did we not discover this problem with our last test? 
In order to generate random inputs, we have used the function `randrange`, 
which does not include negative numbers as possible outputs. This fact is 
easily overlooked. By using predefined, well-thought strategies, 
we can minimize human errors while designing tests. 

After writing this problem down to fix it later, we can continue testing 
by excluding negative numbers. This can be achieved by using `min_value` 
argument of `integer()`:
```python
{{#include ../../codes/01-fundamentals/test_mul_div_prop.py:test_mul_non_neg}}
```

Using only non-negative integers, the test passes. 

#### Test the `div` function
We can now test the `div` function by writing
```python
{{#include ../../codes/01-fundamentals/test_mul_div_prop.py:test_div}}
```
This time, `Hypothesis` tells us
<pre><code><span style="color:#de3f3b"><b><!--
-->E   hypothesis.errors.MultipleFailures: Hypothesis found 2 distinct failures.<!--
--></b></span></code></pre>
with 
```
Falsifying example: test_div_property(
    a=0, b=-1,
)

Falsifying example: test_div_property(
    a=0, b=0,
)
```

From this, we can exclude negative dividends and non-positive divisors by 
writing
```python
{{#include ../../codes/01-fundamentals/test_mul_div_prop.py:test_div_non_neg}}
```
After this modification, the test passes. `Hypothesis` provides a large amount 
of [strategies](https://hypothesis.readthedocs.io/en/latest/data.html#core-strategies) 
and [adaptations](https://hypothesis.readthedocs.io/en/latest/data.html#adapting-strategies), 
with which very flexible tests can be created. 

One might notice that the counterexamples raised by `Hypothesis` are all very 
"simple". This is no coincidence but deliberately made. This process is called 
[shrinking](https://hypothesis.readthedocs.io/en/latest/data.html#shrinking) 
and is designed to produce the most human-readable counterexample.

To see this point, we shall implement a bad multiplication routine, which 
breaks for `a > 10` and `b > 20`:
```python
{{#include ../../codes/01-fundamentals/test_bad_mul.py:bad_mul}}
```

We then test this bad multiplication with
```python
{{#include ../../codes/01-fundamentals/test_bad_mul.py:test_bad_mul}}
```

`Hypotheses` reports

```
Falsifying example: test_bad_mul(
    a=11, b=21,
)
```
which are the smallest example that breaks equality.
