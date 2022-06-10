#!/usr/bin/env python
from cachetools import cached


# speed up calculating Fibonacci numbers with dynamic programming
# https://cachetools.readthedocs.io/en/stable/
@cached(cache={})
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


# Can only run a maximum of 499 due to a recursion limit to avoid a stackoverflow
print(fib(499))

# However, if we increase the limit, we can go much further
import sys
sys.setrecursionlimit(1500)
print(fib(1225))
