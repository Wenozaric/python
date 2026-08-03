d = []

def getOtherDel(num):
    val = False

    for x in range(17, num, 10):
        if num % x == 0:
            val = True
            d.append([num, x])
        if val: return None
    return None

a = 1125000
while len(d) < 5:
    valid = getOtherDel(a)
    a += 1

print(d)