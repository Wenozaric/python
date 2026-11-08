def f(a, b):
    if a > b: return 0
    if a == b: return 1
    if str(a).count('1') >= 1:
        return f(a + 1, b) + f(int(str(a).replace('1', '2')), b)
    else: return f(a + 1, b)

print(f(11, 92))