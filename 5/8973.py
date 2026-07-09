def runTest(myValue, mustValue, issue):
    if myValue == mustValue: print(f"-- {issue} -- Ответ одинаковый, равен {myValue} ✅")
    else: print(f"-- {issue} -- Ответ неверный, равен {myValue}, должен {mustValue} ❌")


def a8973():   
    d = []
    for x in range(1000):
        binX = bin(x)[2:]
        if x % 2 == 0: binX = '10' + binX
        else: binX = '1' + binX + '01'
        if x > 18:
            d.append(int(binX, 2))
    return min(d)

def a8972():
    d = []
    for x in range(1000):
        binX = bin(x)[2:]
        if x % 3 == 0: binX += binX[-3:]
        else: binX += bin((x % 3) * 3)[2:]
        d.append(int(binX, 2))

    prevDef = 100000
    indexSolve = -1
    for index in range(len(d)):
        prevDefNew = abs(130 - d[index])
        if prevDefNew <= prevDef:
            prevDef = prevDefNew
            indexSolve = index

    return indexSolve



runTest(a8973(), 84, 8973)
runTest(a8972(), 31, 8972)