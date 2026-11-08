from functools import lru_cache

@lru_cache
def f(n):
    if n < 10:
        return 1
    if n >= 10:
        return (n + 3) * f(n - 3)

for x in range(1, 247564):
    f(x)

print((f(247563) // 519 - 477 * f(247560)) / f(247557))
