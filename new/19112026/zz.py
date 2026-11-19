def f1(x, y, s):
    if (x + y) >= 259 and s == 3: return 1
    if s > 3 or (x + y) >= 259: return 0

    if s % 2 == 1:
        return f1(x + 1, y, s + 1) or f1(x, y + 1, s + 1) or f1(x * 2, y, s + 1) or f1(x, y * 2, s + 1)
    else:
        return f1(x + 1, y, s + 1) or f1(x, y + 1, s + 1) or f1(x * 2, y, s + 1) or f1(x, y * 2, s + 1)

for i in range(1, 242):
    if f1(17, i, 1):
        print(f'19) {i}') #61
        break

def f2(x, y, s):
    if (x + y) >= 259 and s == 4: return 1
    if s > 4 or (x + y) >= 259: return 0
    if s % 2 == 1:
        return f2(x + 1, y, s + 1) or f2(x, y + 1, s + 1) or f2(x * 2, y, s + 1) or f2(x, y * 2, s + 1)
    else:
        return f2(x + 1, y, s + 1) and f2(x, y + 1, s + 1) and f2(x * 2, y, s + 1) and f2(x, y * 2, s + 1)

for i in range(1, 242):
    if f2(17, i, 1):
        print(f'20) {i}') #112 120

def f4(x, y, s):
    if (x + y) >= 259 and s == 3: return 1
    if s > 3 or (x + y) >= 259: return 0
    if s % 2 == 0:
        return f4(x + 1, y, s + 1) or f4(x, y + 1, s + 1) or f4(x * 2, y, s + 1) or f4(x, y * 2, s + 1)
    else:
        return f4(x + 1, y, s + 1) and f4(x, y + 1, s + 1) and f4(x * 2, y, s + 1) and f4(x, y * 2, s + 1)


def f3(x, y, s):
    if (x + y) >= 259 and (s == 3 or s == 5): return s == 3 or s == 5
    if s > 5 or (x + y) >= 259: return 0
    if s % 2 == 0:
        return f3(x + 1, y, s + 1) or f3(x, y + 1, s + 1) or f3(x * 2, y, s + 1) or f3(x, y * 2, s + 1)
    else:
        return f3(x + 1, y, s + 1) and f3(x, y + 1, s + 1) and f3(x * 2, y, s + 1) and f3(x, y * 2, s + 1)

for i in range(1, 242):
    if f3(17, i, 1) and not f4(17, i, 1):
        print(f'21) {i}')
        break

#61
#112 120
#111