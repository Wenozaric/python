def a23(num, total, valid):
    if num == 66: valid = True
    if num == 4 and valid: return 1
    if num < 4: return 0

    total = a23(num - 2, total, valid)
    total += a23(num // 2, total, valid)
    total += a23(num // 3, total, valid)

    return total

print(a23(150, 0, False))