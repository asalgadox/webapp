#!/usr/bin/env python
from functools import wraps

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@memo
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)
