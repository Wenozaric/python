from functools import lru_cache

@lru_cache
def f(n):
    if n < 10:
        return 3
    if n >= 10:
        return (n + 4) * f(n - 5)

for x in range(1, 257488):
    f(x)

print((f(257487) // 683 + 67 * f(257477)) / f(257472))