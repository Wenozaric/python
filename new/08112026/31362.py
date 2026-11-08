from functools import lru_cache

@lru_cache()
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return (n + 1) * f(n - 1)

for x in range(1, 42038):
    f(x)

print((f(42038) + 3 * f(42037)) / f(42036))