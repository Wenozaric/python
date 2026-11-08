from functools import lru_cache


@lru_cache
def f(n):
    if n == 1:
        return n
    if n > 1:
        return n * f(n - 1)

for x in range(1, 3239):
    f(x)

print(((f(3238) // 2) + f(3237)) / f(3236))

