for x in range(1, 10000):
    binx = bin(x)[2:]
    y = binx.count('1')
    if y % 2 == 0: binx = '10' + binx[2:] + '0'
    else: binx = '11' + binx[2:] + '1'

    if int(binx, 2) >= 16:
        print(x)
        break