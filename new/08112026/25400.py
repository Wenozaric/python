from functools import lru_cache

@lru_cache
def f(n):
    if n < 31054:
        return f(n + 4) + 3020
    if n >= 31054:
        return 3 * (g(n - 2) - 15)

@lru_cache
def g(n):
    if n >= 28:
        return g(n - 5) - 15
    if n < 28:
        return 3 * n - 4

for x in range(1, 31055):
    g(x)

for x in range(31055, 15, -1):
    f(x)

print(f(15))