def f(x, y, s):
    if x + y >= 171: return s == 3
    if s > 3: return 0

    if s % 2 == 1:
        return f(x + 1, y, s + 1) or f(x, y + 1, s + 1) or f(x * 2, y, s + 1) or f(x, y * 2, s + 1)
    else:
        return f(x + 1, y, s + 1) or f(x, y + 1, s + 1) or f(x * 2, y, s + 1) or f(x, y * 2, s + 1)


for b in range(1, 146):
    if f(25, b, 1):
        print(f'19) {b}') #37


def f2(x, y, s):
    if x + y >= 171: return s == 4
    if s > 4: return 0

    if s % 2 == 1:
        return f2(x + 1, y, s + 1) or f2(x, y + 1, s + 1) or f2(x * 2, y, s + 1) or f2(x, y * 2, s + 1)
    else:
        return f2(x + 1, y, s + 1) and f2(x, y + 1, s + 1) and f2(x * 2, y, s + 1) and f2(x, y * 2, s + 1)


for b in range(1, 146):
    if f2(25, b, 1):
        print(f'20) {b}') #60 72
def f4(x, y, s):
    if x + y >= 171: return s == 3
    if s > 3: return 0

    if s % 2 == 0:
        return f4(x + 1, y, s + 1) or f4(x, y + 1, s + 1) or f4(x * 2, y, s + 1) or f4(x, y * 2, s + 1)
    else:
        return f4(x + 1, y, s + 1) and f4(x, y + 1, s + 1) and f4(x * 2, y, s + 1) and f4(x, y * 2, s + 1)

def f3(x, y, s):
    if x + y >= 171: return s == 5 or s == 3
    if s > 5: return 0

    if s % 2 == 0:
        return f3(x + 1, y, s + 1) or f3(x, y + 1, s + 1) or f3(x * 2, y, s + 1) or f3(x, y * 2, s + 1)
    else:
        return f3(x + 1, y, s + 1) and f3(x, y + 1, s + 1) and f3(x * 2, y, s + 1) and f3(x, y * 2, s + 1)


for b in range(1, 146):
    if f3(25, b, 1) and not f4(25, b, 1):
        print(f'21) {b}') #59

#37
#60 72
#59