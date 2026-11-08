from functools import lru_cache

@lru_cache
def f(n):
    if n > 30:
        return f(n - 6) + 2048
    if n <= 30:
        return 3 * (g(n - 5) + 13)

@lru_cache
def g(n):
    if n >= 221337:
        return 2 * n + 50
    if n < 221337:
        return g(n + 11) - 48

for x in range(221338, 1, -1):
    g(x)

for x in range(1, 5079):
    f(x)

print(f(5078))