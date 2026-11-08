from functools import lru_cache

@lru_cache
def f(n):
    if n >= 19:
        return f(n - 4) + 3580
    if n < 19:
        return 6 * (g(n - 7) - 36)

@lru_cache
def g(n):
    if n >= 248045:
        return n / 20 + 28
    if n < 248045:
        return g(n + 9) - 4

for x in range(248046, 1, -1):
    g(x)

for x in range(1, 674):
    f(x)

print(f(673))