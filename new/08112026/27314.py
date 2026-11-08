def f(a, b, valid):
    if a > b or a == 28 or a == 36: return 0
    if a == 18 or a == 30: valid = True
    if a == b and valid: return 1
    return f(a + 1, b, valid) + f(a + 5, b, valid) + f(a * 3, b, valid)

print(f(2, 49, False))