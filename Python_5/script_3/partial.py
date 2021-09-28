"""Part 1: In file script_3/partial.py, 
Edit the function provided by calling partial() and replacing the first three variables in func(). 
Then print with the new partial function using only one input variable so that the output equals 3150."""

from functools import partial
  
def f(a, b, c, x):
    return 1000*a + 100*b + 10*c + x
  
g = partial(f, 3, 1, 5)
  
print(g(0))