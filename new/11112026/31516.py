def f1(x, y, p):
    if x + y >= 133 and p == 3: return True
    if x + y < 133 and p == 3: return False
    if x + y >= 133: return False
    else:
        return f1(x + 4, y, p + 1) or f1(x, y + 4, p + 1) or f1(x * 2, y, p + 1) or f1(x, y * 2, p + 1)

for s in range(1, 116):
    if f1(17, s, 1):
        print(f'19) {s}')
        break

def f2(x, y, p):
    if x + y >= 133 and p == 4: return True
    if x + y < 133 and p == 4: return False
    if x + y >= 133: return False
    else:
        if p % 2 == 0:
            return f2(x + 4, y, p + 1) and f2(x, y + 4, p + 1) and f2(x * 2, y, p + 1) and f2(x, y * 2, p + 1)
        if p % 2 == 1:
            return f2(x + 4, y, p + 1) or f2(x, y + 4, p + 1) or f2(x * 2, y, p + 1) or f2(x, y * 2, p + 1)

z = 0
for s in range(1, 116):
    if f2(17, s, 1):
        print(f'20) {s}')
        z += 1
        if z == 2: break



def f3(x, y, p):
    if x + y >= 133 and (p == 3 or p == 5): return True
    if x + y < 133 and p == 5: return False
    if x + y >= 133: return False
    else:
        if p % 2 == 1:
            return f3(x + 4, y, p + 1) and f3(x, y + 4, p + 1) and f3(x * 2, y, p + 1) and f3(x, y * 2, p + 1)
        if p % 2 == 0:
            return f3(x + 4, y, p + 1) or f3(x, y + 4, p + 1) or f3(x * 2, y, p + 1) or f3(x, y * 2, p + 1)

for s in range(1, 116):
    if f3(17, s, 1):
        print(f'21) {s}')