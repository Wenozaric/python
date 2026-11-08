from functools import lru_cache

@lru_cache
def f(n):
    return 3 * g(n - 3) + 7

@lru_cache
def g(n):
    if n <= 20:
        return n + 2
    if n > 20:
        return g(n - 3) + 1

for x in range(1, 37812):
    f(x)

print(f(37811))