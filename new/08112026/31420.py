def f(a, b, prev):
    if a > b: return 0
    if a == b: return 1
    r = 0
    if '1' in str(a) and prev != 'C': r += f(int(str(a).replace('1', '3')), b, 'C')
    if prev != 'B': r += f(a + 3, b, 'B')
    if prev != 'A': r += f(a + 1, b, 'A')
    return r

print(f(11, 94, ''))