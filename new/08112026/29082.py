from functools import lru_cache

@lru_cache
def f(n):
    if n < 19:
        return 5
    if n >= 19:
        return (n + 4) * f(n - 7)

for x in range(1, 157164):
    f(x)

print((f(157163) // 234 + f(157149) // 533) / f(157142))