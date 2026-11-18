d = []

for x in range(1, 10000):
    binX = bin(x)[2:]
    if x % 2 == 0:
        binX = '11' + binX + '11'
    else:
        binX = '1' + binX + '00'

    if int(binX, 2) > 95:
        d.append(int(binX, 2))

print(min(d))