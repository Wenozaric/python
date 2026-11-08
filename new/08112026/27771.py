from functools import lru_cache

@lru_cache
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n - 1)

for x in range(1, 2025):
    f(x)

print((f(2024) - 2 * f(2023)) / f(2022))