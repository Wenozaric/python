def f(a, b, valid):
    if a < b: return 0
    if a == b and valid: return 1
    if a == 30 or a == 42: valid = True
    return f(a - 3, b, valid) + f(a - 4, b, valid) + f(a // 2, b, valid)

print(f(78, 2, False))  