from functools import lru_cache

@lru_cache
def f(n):
    if n < 17:
        return 6
    if n >= 17:
        return (n + 5) * f(n - 9)

for x in range(1, 234562):
    f(x)

print((f(234561) // 436 + f(234552) // 218) / f(234534))