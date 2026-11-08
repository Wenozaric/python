from functools import lru_cache

@lru_cache
def f(n):
    if n == 1:
        return n
    if n > 1:
        return (n - 1) * f(n - 1)

for x in range(1, 17259):
    f(x)

print((f(17258) + 3 * f(17257)) / f(17256))

