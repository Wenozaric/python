def changeSS(a):
    stri = ''
    while a > 0:
        stri = str(a % 5) + stri
        a = a // 5

    return stri


for x in range(1, 2031):
    a = 25 ** 75 - x
    aS = changeSS(a)

    if aS.count('1') <= 1:
        print(x)
        break

