def f(a, b):
    if a > b: return 0
    if a == b: return 1
    if str(a)[-2] < str(a)[-1]:
        return f(a + 1, b) + f(int(str(a)[:-2] + str(a)[-1] + str(a)[-2]), b)
    else: return f(a + 1, b)

print(f(100, 150))
