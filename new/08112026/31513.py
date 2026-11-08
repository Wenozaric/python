from functools import lru_cache

@lru_cache()
def f(n):
    if n == 1:
        return n
    return n * f(n - 1)

for x in range(1, 3038):
    f(x)

print((f(3038) + 5 * f(3037))/ f(3036))