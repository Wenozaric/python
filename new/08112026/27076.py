from functools import lru_cache

@lru_cache
def f(n):
    if n < 43:
        return g(n + 4)
    if n >= 43:
        return 2 * f(n - 2) - f(n - 4) + 2

@lru_cache
def g(n):
    if n < 11240:
        return g(n + 3) + 2
    if n >= 11240:
        return q(n)

@lru_cache
def q(n):
    if n < 21:
        return n + 4
    if n >= 21:
        return q(n - 4) + 2

for x in range(1, 11245):
    q(x)

for x in range(11245, 1, -1):
    g(x)

print(f(2026))