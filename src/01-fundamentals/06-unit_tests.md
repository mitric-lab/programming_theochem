## Unit Tests

Everybody makes mistakes. Although the computer which executes programs 
does exactly what it is told to, we can make mistakes which may 
cause unexpected behaviors. Therefore, proper testing is mandatory for 
any serious application. _"But I can just try some semi-randomly 
picked inputs after writing a function and see if I get the expected 
output, so ..."_

### Why bother with writing tests?
First of all, if you share your program with other people, you have to 
persuade them that your program works properly. It is far more 
convincing if you have written tests, which they can run for themselves and 
see that nothing is out of order, than just tell them that you have tested 
some hand-picked examples.

Furthermore, functions are often rewritten multiple times to improve their 
performance. Since you want to ensure that the function still works properly 
after even the slightest modification, you will have to run your manual tests 
over and over again. The problem only gets worse for larger projects. Nested 
conditions, interdependent modules, multiple inheritance, just to name a few, 
will make manual testing a horrible choice; even the tiniest change could 
make you re-test **every** routine you have written.

So, to make your (and other's) life easier, just write tests. 

### What are unit tests?
Unit tests are typically automated tests to ensure that a part of a program 
(known as a "unit") behaves as intended. A unit could be an entire module, 
but it is more commonly an individual function or an interface, such as a 
class.

Since unit tests focus on a specific part of the program, it is very good at 
isolating individual parts and find errors in them. This can accelerate 
the debugging process, because only the code of units corresponding to failed 
tests have to be inspected. Exactly due to this isolating action however, 
unit tests cannot be used to evaluate every execution path in any but the 
most trivial programs and will not catch every error. Nevertheless, unit 
tests are really powerful and can greatly reduce the number of errors.
