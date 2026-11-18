def f1(x, y, s):
    if (x + y) <= 47: return s == 3
    if s > 3: return 0
    if s % 2 == 1:
        return f1(x - 2, y, s + 1) or f1(x, y - 2, s + 1) or f1(x // 3, y, s + 1) or f1(x, y // 3, s + 1)
    else:
        return f1(x - 2, y, s + 1) or f1(x, y - 2, s + 1) or f1(x // 3, y, s + 1) or f1(x, y // 3, s + 1)


for e in range(32, 1000):
    if f1(16, e, 1):
        print(f'19) {e}')


def f4(x, y, s):
    if (x + y) <= 47: return s == 2
    if s > 2: return 0
    if s % 2 == 1:
        return f4(x - 2, y, s + 1) and f4(x, y - 2, s + 1) and f4(x // 3, y, s + 1) and f4(x, y // 3, s + 1)
    else:
        return f4(x - 2, y, s + 1) or f4(x, y - 2, s + 1) or f4(x // 3, y, s + 1) or f4(x, y // 3, s + 1)


def f2(x, y, s):
    if (x + y) <= 47: return s == 4
    if s > 4: return 0
    if s % 2 == 0:
        return f2(x - 2, y, s + 1) and f2(x, y - 2, s + 1) and f2(x // 3, y, s + 1) and f2(x, y // 3, s + 1)
    else:
        return f2(x - 2, y, s + 1) or f2(x, y - 2, s + 1) or f2(x // 3, y, s + 1) or f2(x, y // 3, s + 1)


for e in range(32, 1000):
    if f2(16, e, 1) and not f4(16, e, 1):
        print(f'20) {e}')


def f3(x, y, s):
    if (x + y) <= 47: return s == 5 or s == 3
    if s > 5: return 0
    if s % 2 == 1:
        return f3(x - 2, y, s + 1) and f3(x, y - 2, s + 1) and f3(x // 3, y, s + 1) and f3(x, y // 3, s + 1)
    else:
        return f3(x - 2, y, s + 1) or f3(x, y - 2, s + 1) or f3(x // 3, y, s + 1) or f3(x, y // 3, s + 1)


for e in range(32, 1000):
    if f3(16, e, 1) and not f1(16, e, 1):
        print(f'21) {e}')


#34
#98 293
#100