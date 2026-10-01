#11Hx05 + 3Fx54x8 + Gxxx9
def писать(a):
    print(a)

for x in '0123456789abcdefgh':
    a1 = int(f'11H{x}05', 18)
    a2 = int(f'3F{x}54{x}8', 18)
    a3 = int(f'G{x}{x}{x}9', 18)
    a = a1 + a2 + a3
    if a % 14 == 0:
        писать(a // 14)
        break