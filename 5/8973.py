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

def a8885():

    def changeSS(target, ss):
        newX = ''
        while target > 0:
            newX = newX + str(target % 3) 
            target = target // 3
        return newX[::-1]
        
    def findPAndS(target):
        p = 1
        minNum = 10
        maxNum = 0
        for index in target:
            if( int(index, 10) != 0):
                p = p * int(index, 10)
            if int(index, 10) < minNum: minNum = int(index, 10)
            if int(index, 10) > maxNum: maxNum = int(index, 10)
        s = maxNum - minNum

        return p, s
    


    for x in range(100000):
        trX = changeSS(x, 3)
        p, s = findPAndS(trX)
        trP = changeSS(p, 3)
        trS = changeSS(s, 3)

        solve = 0
        if p > s: solve = trS + trP
        else: solve = trP + trS

        if int(solve, 3) == 113:
            return x
            break
        
def a8884():

    def changeSS(target, ss):
        newTarget = ''
        while target > 0:
            newTarget += str(target % ss)
            target = target // ss
        return newTarget[::-1]

    def findSAndP(target):
        p = 1

        minNum = 10
        maxNum = 0

        for num in target:
            if( int(num, 10) != 0): p *= int(num, 10)
            if( int(num, 10) < minNum): minNum = int(num, 10)
            if( int(num, 10) > maxNum): maxNum = int(num, 10)

        return p, maxNum + minNum

    for x in range(10000):
        svX = changeSS(x, 7)
        p, s = findSAndP(svX)

        svP = changeSS(p, 7)
        svS = changeSS(s, 7)

        solve = 0

        if p > s: solve = svS + svP
        else: solve = svP + svS

        if int(solve, 7) == 2725: return x 

runTest(a8973(), 84, 8973)
runTest(a8972(), 31, 8972)
runTest(a8885(), 485, 8885)
runTest(a8884(), 3625, 8884)