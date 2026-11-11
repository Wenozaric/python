def f(x, y, s):
    if x * y >= 600 and s == 3: return True
    if x * y < 600 and s == 3: return False
    if x * y >= 600: return False
    else:
        if s % 2 == 1:
            return f(x + 2, y, s + 1) and f(x - 3, y + 3, s + 1)
        else:
            return f(x + 2, y, s + 1) or f(x - 3, y + 3, s + 1)

for s in range(1, 15):
    if f(40, s, 1):
        print(s)


def f2(x, y, s):
    if x * y >= 600 and s == 4: return True
    if x * y < 600 and s == 4: return False
    if x * y >= 600: return False
    else:
        if s % 2 == 0:
            return f2(x + 2, y, s + 1) and f2(x - 3, y + 3, s + 1)
        else:
            return f2(x + 2, y, s + 1) or f2(x - 3, y + 3, s + 1)

for s in range(1, 15):
    if f2(40, s, 1):
        print(s)

def f3(x, y, s):
    if x * y >= 600 and (s == 3 or s == 5): return True
    if x * y < 600 and s == 5: return False
    if x * y >= 600: return False
    else:
        if s % 2 == 1:
            return f3(x + 2, y, s + 1) and f3(x - 3, y + 3, s + 1)
        else:
            return f3(x + 2, y, s + 1) or f3(x - 3, y + 3, s + 1)

for s in range(1, 15):
    if f3(40, s, 1):
        print(f'21) {s}')