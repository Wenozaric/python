from functools import lru_cache

@lru_cache
def f(n):
    if n == 1:
        return n
    if n > 1:
        return ( n - 1) * f(n - 1)

for x in range(1, 32029):
    f(x)

print((3 * f(32028) - f(32027)) / f(32026))
