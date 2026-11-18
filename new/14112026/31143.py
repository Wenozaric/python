for x in range(1, 1000):
    binx = bin(x)[2:]
    if x % 2 == 0: binx = '10' + binx
    else: binx = '1' + binx + '01'
    
    if int(binx, 2) >= 190:
        print(x)
        break