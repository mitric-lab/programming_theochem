### Example Based Tests

```admonish note
Since we want to discover errors using unit tests, let us assume 
that we did not discuss anything about the edge cases for multiplication 
and division routines we have written.
```

Although Python has the built-in module `unittest`, another framework for 
unit tests, [`pytest`](https://docs.pytest.org/en/7.1.x/), exists,
which is easier to use and offers more functionalities. Therefore, we will 
stick to `pytest` in this class. The thoughts presented however, 
can be used with any testing framework.

We start by installing `pytest` with
```bash
mamba install pytest
```

~~~admonish info title="Info for Jupyter Notebook Users"
When using jupyter-notebook, the module [`ipytest`](https://github.com/chmp/ipytest)
could be very handy. This can be installed with
```bash
mamba install ipytest
```
~~~

Suppose we have written the `mul` function in the file `multiplication.py` 
and `div` function in the file `division.py`, we can create the file 
`test_mul_div_expl.py` in the same directory and import both functions as:
```python
{{#include ../../codes/01-fundamentals/test_mul_div_expl.py:import}}
```

#### Unit test with examples
We choose one example for each function and write
```python
{{#include ../../codes/01-fundamentals/test_mul_div_expl.py:example_test}}
```
where we call each function on the selected example and compare the output 
with the expected outcome.

After saving and exiting the document, we can execute
```bash
pytest
```
in the console. `pytest` will then find every `.py` files in the directory 
which begins with `test` execute every function inside, which begins with 
`test`. If we only want to execute test functions from one specific file, 
say, `test_mul_div_expl.py`. we should call
```bash
pytest test_mul_div_expl.py
```

If any `assert` statement throws an exception, `pytest` will informs 
us about it. In this case, we should see
<pre><code><!--
--><span style="color:#1ba536">================================ <!--
-->2 passed in 0.10s ================================</span><!--
--></code></pre>
although the time may differ. It is good to see that the tests passed. But 
just because something works on one example does not mean it will always work. 
One way to be more confident is to go through more examples. Instead of 
writing the same function for all examples, we can use the function decorator
`@parametrize` provided by `pytest`.

#### Unit test with parametrized examples
We can use the function decorator by importing `pytest` and write
```python
{{#include ../../codes/01-fundamentals/test_mul_div_expl.py:parametrized_example_test}}
```

The decorator `@parametrize` feeds the test function with values and makes 
testing with multiple examples easy. It will becomes tedious however, if 
we want to try even more examples. 

#### Unit test with random examples
By going through a large amount of randomly generated examples, we may 
uncover rarely occuring errors. This method is not always available, since 
you must get your hands on expected outputs for every possible inputs. 
In this case however, we can just use python's built-in `*`
and `//` operator to verify our own function.  

The following listing shows tests for 50 examples:
```python
{{#include ../../codes/01-fundamentals/test_mul_div_expl.py:random_example_test}}
```

Running `pytest` should probably give us 2 passes. To be more confident, we 
can increase the number of loops to, say, 700. Now, calling `pytest` several 
times, we might get something like
<pre><code><!--
-->=========================================<!--
--> short test summary info <!--
-->==========================================
FAILED test_mul_div.py::test_div_random_example - <!--
--> ZeroDivisionError: integer division or modulo by zero
<span><!--
--><span style="color:#de3f3b">=======================================</span><!--
--> <!--
--><span style="color:#de3f3b; font-weight:bold">1 failed</span><!--
-->, <!--
--><span style="color:#1ba536">1 passed</span><!--
--> <!--
--><span style="color:#de3f3b">in 0.20s =======================================</span><!--
--></span>
</code></pre>

This tells us that the `ZeroDivisonError` exception occured while running 
`test_div_random_example` function. Some more information can be seen above 
the summary, and it should look like
<pre><code><!--
--><span class="hljs-keyword">def</span><!--
--> <!--
--><span class="hljs-title">test_div_random_example</span><!--
-->():<!--
--></span>
        <!--
--><span class="hljs-keyword">for</span><!--
--> _ <!--
--><span class="hljs-keyword">in</span><!--
--> range(<!--
--><span class="hljs-number">0</span><!--
-->, N):
            a = randrange(<!--
--><span class="hljs-number">1</span><!--
-->_000)
            b = randrange(<!--
--><span class="hljs-number">1</span><!--
-->_000)
&gt;           <!--
--><span class="hljs-keyword">assert</span><!--
--> div(a, b) == a // b
<span style="color:#de3f3b"><b><!--
-->E          ZeroDivisionError: integer division or modulo by zero</b><!--
--></span>
</code></pre>

The arrow in the second last line shows the code where the exception occured. 
In this case, we have provided the floor division operator `//` with a zero 
on the right side. We thus know that we should properly handle this case, both 
for our implementation and testing.

We have found the error without knowing the detailed implementation of the 
functions. This is desired since human tends to overlook things when analyzing 
code and some special cases might not be covered by testing with just a few 
examples. Although with 700 loops, the test passes about 50 % of the time. 
If we increase the number of loops to several thousands or even higher, 
the test is almost guaranteed to fail and can inform us about deficies in 
our implementations.

The existence of a reference method is not only possible in our toy example, 
but also occurs in realistic cases. A common case is an intuitive, easy and 
less error-prone to implement method, which has a long runtime. A more 
complicated implementation which runs faster can then be tested against this 
reference method. In our case, we could use `naive_mul` and `naive_div` as 
reference methods for `mul` and `div`, respectively.

But what if we really do not have a reference method to produced a large 
amount of expected outputs? The so called *property based testing* could 
help us in this case.
