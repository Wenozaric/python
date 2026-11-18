def f1(x, y, s):
    if (x + y) <= 53: return s == 3
    if s > 3: return 0

    if s % 2 == 1:
        return f1(x - 3, y, s + 1) or f1(x, y - 3, s + 1) or f1(x // 3, y, s + 1) or f1(x, y // 3, s + 1)
    else:
        return f1(x - 3, y, s + 1) or f1(x, y - 3, s + 1) or f1(x // 3, y, s + 1) or f1(x, y // 3, s + 1)


for u in range(35, 1000):
    if f1(19, u, 1):
        print(f'19) {u}')

#19) 38

def f3(x, y, s):
    if (x + y) <= 53: return s == 2
    if s > 2: return 0
    return f3(x - 3, y, s + 1) or f3(x, y - 3, s + 1) or f3(x // 3, y, s + 1) or f3(x // 3, y, s + 1)


def f2(x, y, s):
    if (x + y) <= 53: return s == 4
    if s > 4: return 0

    if s % 2 == 1:
        return f2(x - 3, y, s + 1) or f2(x, y - 3, s + 1) or f2(x // 3, y, s + 1) or f2(x , y // 3, s + 1)
    else:
        return f2(x - 3, y, s + 1) and f2(x, y - 3, s + 1) and f2(x // 3, y, s + 1) and f2(x, y // 3, s + 1)

for u in range(35, 1000):
    if f3(19, u, 1):
        print(f'20 *) {u}')

for u in range(35, 1000):
    if f2(19, u, 1) and not f3(19, u, 1):
        print(f'20) {u}')

#48?
def f6(x, y, s):
    if (x + y) <= 53: return s == 3
    if s > 3: return 0

    if s % 2 == 1:
        return f6(x - 3, y, s + 1) and f6(x, y - 3, s + 1) and f6(x // 3, y, s + 1) and f6(x, y // 3, s + 1)
    else:
        return f6(x - 3, y, s + 1) or f6(x, y - 3, s + 1) or f6(x // 3, y, s + 1) or f6(x, y // 3, s + 1)

def f4(x, y, s):
    if (x + y) <= 53: return s == 5 or s == 3
    if s > 5: return 0

    if s % 2 == 0:
        return f4(x - 3, y, s + 1) or f4(x, y - 3, s + 1) or f4(x // 3, y, s + 1) or f4(x, y // 3, s + 1)
    else:
        return f4(x - 3, y, s + 1) and f4(x, y - 3, s + 1) and f4(x // 3, y, s + 1) and f4(x, y // 3, s + 1)


for u in range(35, 1000):
    if f4(19, u, 1) and not f6(19, u, 1):
        print(f'21) {u}')

#38
#48 53
#52