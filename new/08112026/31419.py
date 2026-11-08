def f(a, b, count):
    if a > b: return 0
    if a == b and count == 3: return 1
    if str(a).count('1') > 0:
        return f(a + 1, b, count) + f(int(str(a).replace('1', '3')), b, count + 1)
    else:
        return f(a + 1, b, count)

print(f(11, 94, 0))