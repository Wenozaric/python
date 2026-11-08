def f(a, b):
    if a > b: return 0
    if a == b: return 1
    y = 0
    for x in str(a):
        y += int(x)
    if y < 10: return f(a + 1, b) + f(int(str(a) + str(y)), b)
    else: return f(a + 1, b)
print(f(3, 200))