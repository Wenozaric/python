d = []

for x in range(17, 2000):
    binx = bin(x)[2:]
    if x % 2 == 0: binx = '10' + binx
    else: binx = '1' + binx + '01'

    d.append(int(binx, 2))

print(min(d))