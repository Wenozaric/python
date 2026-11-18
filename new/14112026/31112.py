d = []

for x in range(1, 10000):
    binx = bin(x)[2:]
    if x % 2 == 0: binx = '11' + binx + '11'
    else: binx = '1' + binx + '00'

    if int(binx, 2) <= 113:
        d.append(int(binx, 2))

print(max(d))