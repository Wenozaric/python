def f(a, b):
    if a > b: return 0
    elif a == b: return 1
    else:
        if str(a)[1] < str(a)[2]:
            return f(a + 1, b) + f(int(str(a)[0] + str(a)[2] + str(a)[1]), b)
        else:
            return f(a + 1, b)

print(f(100, 141))
