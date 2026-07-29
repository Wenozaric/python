def changeSS(x, ss):
    stri = ''
    while x > 0:
        stri = str(x % ss) + stri
        x = x // ss

    return stri

for x in range(1, 500):
    tripX = changeSS(x, 3)
    if x % 3 == 0: tripX += tripX[-2:]
    else: tripX = tripX + changeSS((x % 3) * 3, 3)

    if int(tripX, 3) <= 150:
        print(x)
