def f(x, y, s):
    if x + y >= 155: return s == 3
    if s > 3: return 0

    if s % 2 == 1:
        return f(x + 1, y, s + 1) or f(x, y + 1, s + 1) or f(x * 3, y, s + 1) or f(x, y * 3, s + 1)
    else:
        return f(x + 1, y, s + 1) or f(x, y + 1, s + 1) or f(x * 3, y, s + 1) or f(x, y * 3, s + 1)

for u in range(1, 156):
    if f(15, u, 1):
        print(f'19) {u}') #16


def f2(x, y, s):
    if x + y >= 155: return s == 4
    if s > 4: return 0

    if s % 2 == 1:
        return f2(x + 1, y, s + 1) or f2(x, y + 1, s + 1) or f2(x * 3, y, s + 1) or f2(x, y * 3, s + 1)
    else:
        return f2(x + 1, y, s + 1) and f2(x, y + 1, s + 1) and f2(x * 3, y, s + 1) and f2(x, y * 3, s + 1)


for u in range(1, 156):
    if f2(15, u, 1):
        print(f'20) {u}')  #19 46


def f4(x, y, s):
    if x + y >= 155: return s == 3
    if s > 3: return 0

    if s % 2 == 0:
        return f4(x + 1, y, s + 1) or f4(x, y + 1, s + 1) or f4(x * 3, y, s + 1) or f4(x, y * 3, s + 1)
    else:
        return f4(x + 1, y, s + 1) and f4(x, y + 1, s + 1) and f4(x * 3, y, s + 1) and f4(x, y * 3, s + 1)



def f3(x, y, s):
    if x + y >= 155: return s == 5 or s == 3
    if s > 5: return 0

    if s % 2 == 0:
        return f3(x + 1, y, s + 1) or f3(x, y + 1, s + 1) or f3(x * 3, y, s + 1) or f3(x, y * 3, s + 1)
    else:
        return f3(x + 1, y, s + 1) and f3(x, y + 1, s + 1) and f3(x * 3, y, s + 1) and f3(x, y * 3, s + 1)


for u in range(1, 156):
    if f3(15, u, 1) and not f4(15, u, 1):
        print(f'21) {u}') #45