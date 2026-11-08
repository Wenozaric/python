from functools import lru_cache

@lru_cache
def f(n):
    if n > 40:
        return f(n - 4) + 3020
    if n <= 40:
        return 3 * (g(n - 2) - 15)

@lru_cache
def g(n):
    if n >= 301208:
        return 10 * n + 50
    if n < 301208:
        return g(n + 7) - 21

for x in range(301209, 1, -1):
    g(x)

for x in range(1, 2026):
    f(x)

print(f(2026)) 