def f(a, b, valid):
    if a > b or a == 20 or a == 33: return 0
    if a == 15 or a == 26: valid = True
    if a == b and valid: return 1
    return f(a + 3, b, valid) + f(a + 4, b, valid) + f(a * 2, b, valid)

print(f(3, 63, False))

#2 часа ровно отсидел