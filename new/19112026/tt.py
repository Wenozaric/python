#19 s == 3 #20 s == 4 #21 s == 3 or s == 5 + f4()
def f1(x, s):
    if x >= 40 and s == 3: return 1
    if x >= 40 or s > 3: return 0
    if s % 2 == 0:
        return f1(x + 1, s + 1) or f1(x + 4, s + 1) or f1(x * 2 , s + 1)
    else:
        return f1(x + 1, s + 1) and f1(x + 4, s + 1) and f1(x * 2 , s + 1)

for i in range(1, 40):
    if f1(i, 1):
        print(f'19) {i}')


def f2(x, s):
    if x >= 40 and s == 4: return 1
    if x >= 40 or s > 4: return 0
    if s % 2 == 1:
        return f2(x + 1, s + 1) or f2(x + 4, s + 1) or f2(x * 2 , s + 1)
    else:
        return f2(x + 1, s + 1) and f2(x + 4, s + 1) and f2(x * 2 , s + 1)

for i in range(1, 40):
    if f2(i, 1):
        print(f'20) {i}')

#21
def f3(x, s):
    if x >= 40 and (s == 3 or s == 5): return s == 3 or s == 5 # 3 гарант 5 гарант 3 или 5
    if x >= 40 or s > 5: return 0
    if s % 2 == 0:
        return f3(x + 1, s + 1) or f3(x + 4, s + 1) or f3(x * 2 , s + 1)
    else:
        return f3(x + 1, s + 1) and f3(x + 4, s + 1) and f3(x * 2 , s + 1)
    
for i in range(1, 40):
    if f3(i, 1) and not f1(i, 1):
        print(f'21) {i}')


#19
#15 18
#14