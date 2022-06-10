#!/usr/bin/env python
from functools import lru_cache
# write up more on lru_cache
# https://realpython.com/lru-cache-python/#using-lru_cache-to-implement-an-lru-cache-in-python


@lru_cache(maxsize=256)
def f(x):
  return x*x


for each in range(20):
  print(f(each))
for each in range(20):
  print(f(each))
