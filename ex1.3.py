cache = {}

def func2(n):
    if n == 0 or n == 1:
        return n;
    elif n in cache.keys():
        return cache[n]
    else:
        cache[n] = func2(n-1) + func2(n-2)
        return cache[n]
