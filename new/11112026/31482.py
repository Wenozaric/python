def f(defX, x, s):
    if 4 * defX <= x and s == 3: return True
    if 4 * defX > x and s == 3: return False 
    if 4 * defX <= x: return False
    else:
        if s % 2 == 1:
            return f(defX, x + 5, s + 1) and f(defX, x * 3, s + 1)
        else:
            return f(defX, x + 5, s + 1) or f(defX, x * 3, s + 1)
        
n = 0
for s in range(1, 151):
    if f(s, s, 1):
        print(f'19) {s}')
        n += 1

print(n)

def f2(defX, x, s):
    if 4 * defX <= x and s == 4: return True
    if 4 * defX > x and s == 4: return False 
    if 4 * defX <= x: return False
    else:
        if s % 2 == 1:
            return f2(defX, x + 5, s + 1) or f2(defX, x * 3, s + 1)
        else:
            return f2(defX, x + 5, s + 1) and f2(defX, x * 3, s + 1)
        
for s in range(1, 151):
    if f2(s, s, 1):
        print(f'20) {s}')

def f3(defX, x, s):
    if 4 * defX <= x and (s == 3 or s == 5): return True
    if 4 * defX > x and s == 5: return False 
    if 4 * defX <= x: return False
    else:
        if s % 2 == 1:
            return f3(defX, x + 5, s + 1) and f3(defX, x * 3, s + 1)
        else:
            return f3(defX, x + 5, s + 1) or f3(defX, x * 3, s + 1)
        
for s in range(1, 151):
    if f3(s, s, 1):
        print(f'21) {s}')