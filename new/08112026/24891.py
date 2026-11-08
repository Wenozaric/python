from functools import lru_cache

@lru_cache
def f(n):
    if n <= 10:
        return n
    if n > 10:
        return n - 7 + f(n - 21)

for x in range(1, 185735):
    f(x)

print((f(185734) - f(185650)) / f(40))