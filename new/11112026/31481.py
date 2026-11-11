def f(x, y, s):
    if (x + y >= 120 or x * y >= 1000) and s == 3: return True
    if (x + y < 120 and x * y < 1000) and s == 3: return False
    if (x + y >= 120 or x * y >= 1000) and s < 3: return False 
    if s > 3: return False
    else:
        if s % 2 == 1:
            return f(x + 2, y, s + 1) and f(x, y + 2, s + 1) and f(x * 2, y, s + 1) and f(x, y * 2, s + 1)
        else:
            return f(x + 2, y, s + 1) or f(x, y + 2, s + 1) or f(x * 2, y, s + 1) or f(x, y * 2, s + 1)

for s in range(1, 46):
    if f(22, s, 1):
        print(f'19) {s}')
        break

def f2(x, y, s):
    if (x + y >= 120 or x * y >= 1000) and s == 4: return True
    if (x + y < 120 and x * y < 1000) and s == 4: return False
    if (x + y >= 120 or x * y >= 1000) and s < 4: return False 
    if s > 4: return False
    else:
        if s % 2 == 1:
            return f2(x + 2, y, s + 1) or f2(x, y + 2, s + 1) or f2(x * 2, y, s + 1) or f2(x, y * 2, s + 1)
        else:
            return f2(x + 2, y, s + 1) and f2(x, y + 2, s + 1) and f2(x * 2, y, s + 1) and f2(x, y * 2, s + 1)

for s in range(1, 46):
    if f2(22, s, 1):
        print(f'20) {s}')

def f3(x, y, s):
    if (x + y >= 120 or x * y >= 1000) and (s == 3 or s == 5): return True
    if (x + y < 120 and x * y < 1000) and s == 5: return False
    if (x + y >= 120 or x * y >= 1000) and s < 5: return False 
    if s > 5: return False
    else:
        if s % 2 == 1:
            return f3(x + 2, y, s + 1) and f3(x, y + 2, s + 1) and f3(x * 2, y, s + 1) and f3(x, y * 2, s + 1)
        else:
            return f3(x + 2, y, s + 1) or f3(x, y + 2, s + 1) or f3(x * 2, y, s + 1) or f3(x, y * 2, s + 1)

for s in range(1, 46):
    if f3(22, s, 1):
        print(f'21) {s}')

#21 11 19 18