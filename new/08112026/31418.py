def f(a, b):
    if a > b: return 0
    if a == b: return 1
    z = bin(a)[2:].count('1')
    return f(a + 1, b) + f(a + z, b)

print(f(5, 40))