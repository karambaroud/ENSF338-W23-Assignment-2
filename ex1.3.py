import timeit

cache = {}

def func(n):
    if n == 0 or n == 1:
        return n;
    elif n in cache.keys():
        return cache[n]
    else:
        cache[n] = func(n-1) + func(n-2)
        return cache[n]
