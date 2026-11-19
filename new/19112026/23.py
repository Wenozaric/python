def f(x, target):
    if x < target or x == 13: return 0
    if x == target: return 1

    return f(x - 1, target) + f(x - 2, target) + f(x // 3, target)

print(f(19, 6) * f(6, 4))