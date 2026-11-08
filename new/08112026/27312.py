def f(a, b, valid1, valid2):
    if a < b: return 0
    if a == b and valid1 != valid2: return 1
    if a == 48: valid1 = True
    if a == 61: valid2 = True
    return f(a - 1, b, valid1, valid2) + f(a // 2, b, valid1, valid2) + f(a // 3, b, valid1, valid2)

print(f(106, 6, False, False))