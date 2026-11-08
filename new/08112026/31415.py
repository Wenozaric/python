def f(a, b):
    if a > b: return 0
    if a == b: return 1
    if str(a)[0] < str(a)[-1]:
        return f(a + 1, b) + f(int(str(a)[-1] + str(a)[1:][:-1] + str(a)[0]), b)
    else:
        return f(a + 1, b)

print(f(102, 300))