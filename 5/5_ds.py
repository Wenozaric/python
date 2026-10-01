for x in range (10000000):
    binx = bin(x)[2:]
    suma = binx.count('1')
    
    #2
    if suma % 2 == 0:
        binx = '10' + binx[2:] + '0'
    else:
        binx = '11' + binx[2:] + '1'

    if int(binx, 2) > 480:
        print(x)
        break