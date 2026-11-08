from functools import lru_cache

@lru_cache
def f(n):
    if n >= 128:
        return f(n - 5) + 1092
    if n < 128:
        return 5 * g(n - 7) + 29

@lru_cache
def g(n):
    if n > 303728:
        return n - 15
    if n <= 303728:
        return g(n + 8) / 2 - 109

for x in range(303729, 1, -1):
    g(x)

for x in range(1, 2050):
    f(x)

print(f(2049))
    