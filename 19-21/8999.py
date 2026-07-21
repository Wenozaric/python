from functools import lru_cache
import math
issueOne = set()


@lru_cache
def findS(currentOne, currentTwo, step):
    if( step == 2):
        target = 211 - currentOne
        currentTwo = currentTwo[::-1]
        for index in range(len(currentTwo)):
            if(currentTwo[index] == '*'): target = math.ceil(target / 2)
            if(currentTwo[index] == '+'): target -= 1
        issueOne.add(target)
    else:
        findS(currentOne + 1, currentTwo, step + 1)
        findS(currentOne * 2, currentTwo, step + 1)
        findS(currentOne, currentTwo + '+', step + 1)
        findS(currentOne, currentTwo + '*', step + 1)
    return issueOne
        
print(findS(17, 'x', 0))

secondSet = set()

def isValid(array):
    a1 = array[0] + array[1] + 1
    a2 = array[0] * 2 + array[1]
    a3 = array[0] + array[1] * 2
    if a1 < 207 and a2 < 207 and a3 < 207: return False
    return True 

def getOtherVariants(currentOne, currentTwo):
    a1 = [currentOne + 1, currentTwo]
    a2 = [currentOne * 2, currentTwo]
    a3 = [currentOne, currentTwo + 1]
    a4 = [currentOne, currentTwo * 2]
    if sum(a1) < 207 and sum(a2) < 207 and sum(a3) < 207 and sum(a4) < 207: return [a1, a2, a3, a4]
    return []

def game(currentOne, currentTwo, step, baseS):
    if step == 1 and (currentOne + currentTwo < 207):
        isPosibileVariant = True
        b = getOtherVariants(currentOne, currentTwo)
        if len(b) > 0:
            for variant in b:
                if isValid(variant) == False: isPosibileVariant = False
            if isPosibileVariant: secondSet.add(baseS)
        return None
    if( step < 1):
        game(currentOne + 1, currentTwo, step + 1, baseS)
        game(currentOne * 2, currentTwo, step + 1, baseS)
        game(currentOne, currentTwo + 1, step + 1, baseS)
        game(currentOne, currentTwo * 2, step + 1, baseS)
    
    return None

for x in range(1, 190):
    game(17, x, 0, x)

print(secondSet)
