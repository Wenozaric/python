def f(a, b, valid1, valid2):
    if a < b: return 0
    if a == b and valid1 != valid2: return 1
    if a == 25: valid1 = True
    if a == 47: valid2 = True
    return f(a - 2, b, valid1, valid2) + f(a - 3, b, valid1, valid2) + f(a // 5, b, valid1, valid2)

print(f(63, 3, False, False))