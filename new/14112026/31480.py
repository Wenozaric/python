def f1(x, y, s):
    if abs(x - y) >= 40 and s == 3: return True
    if abs(x - y) >= 40: return False
    if s > 3: return False

    if s % 2 == 1:
        return f1(x + 5, y, s + 1) and f1(x, y + 5, s + 1) and f1(x * 2, y, s + 1) and f1(x, y * 2, s + 1)
    else:
        return f1(x + 5, y, s + 1) or f1(x, y + 5, s + 1) or f1(x * 2, y, s + 1) or f1(x, y * 2, s + 1)


for u in range(1, 70):
    if f1(30, u, 1):
        print(f'19) {u}')

def f4(x, y, s):
    if abs(x - y) >= 40: return s == 2
    if s > 2: return 0

    if s % 2 == 1:
        return f4(x + 5, y, s + 1) or f4(x, y + 5, s + 1) or f4(x * 2, y, s + 1) or f4(x, y * 2, s + 1)
    else:
        return f4(x + 5, y, s + 1) and f4(x, y + 5, s + 1) and f4(x * 2, y, s + 1) and f4(x, y * 2, s + 1)

def f2(x, y, s):
    if abs(x - y) >= 40 and s == 4: return True
    if abs(x - y) >= 40: return False
    if s > 4: return False

    if s % 2 == 1:
        return f2(x + 5, y, s + 1) or f2(x, y + 5, s + 1) or f2(x * 2, y, s + 1) or f2(x, y * 2, s + 1)
    else:
        return f2(x + 5, y, s + 1) and f2(x, y + 5, s + 1) and f2(x * 2, y, s + 1) and f2(x, y * 2, s + 1)


for u in range(1, 70):
    if not f4(30, u, 1) and f2(30, u, 1):
        print(f'20) {u}')


def f3(x, y, s):
    if abs(x - y) >= 40 and (s == 3 or s == 5): return s == 5 or s == 3
    if abs(x - y) >= 40: return 0
    if s > 5: return 0

    if s % 2 == 1:
        return f3(x + 5, y, s + 1) and f3(x, y + 5, s + 1) and f3(x * 2, y, s + 1) and f3(x, y * 2, s + 1)
    else:
        return f3(x + 5, y, s + 1) or f3(x, y + 5, s + 1) or f3(x * 2, y, s + 1) or f3(x, y * 2, s + 1)


for u in range(1, 70):
    if f3(30, u, 1) and not f1(30, u, 1):
        print(f'21) {u}')


