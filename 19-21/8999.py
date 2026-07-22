from functools import lru_cache
import math


issueOne = set()

@lru_cache
def findS(currentOne, currentTwo, step, baseS):
    if step == 1:
        if (currentOne + currentTwo) >= 207: return None
        a1 = currentOne + 1 + currentTwo
        a2 = currentOne * 2 + currentTwo
        a3 = currentOne + currentTwo * 2
        if a1 >= 207 or a2 >= 207 or a3 >= 207:
            issueOne.add(baseS)
    if step < 2:
        findS(currentOne + 1, currentTwo, step + 1, baseS)
        findS(currentOne * 2, currentTwo, step + 1, baseS)
        findS(currentOne, currentTwo + 1, step + 1, baseS)
        findS(currentOne, currentTwo * 2, step + 1, baseS)
        
for x in range(0, 190):
    findS(17, x, 0, x)
print(min(issueOne))

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


def moves(boulders):
    p1, p2 = boulders
    return [(p1 + 1, p2), (p1 * 2, p2), (p1, p2 + 1), (p1, p2 * 2)]

@lru_cache(None)
def game(boulders):
    p1, p2 = boulders
    if p1 + p2 >= 207:
        return 'win'
        
    next = [game(m) for m in moves(boulders)]
    
    if 'win' in next:
        return 'petya1'
    
    if all(m == 'petya1' for m in next):
        return 'vanya1'

    if 'vanya1' in next:
        return 'petya2'

    if all(m == 'petya1' or m == 'petya2' for m in next):
        return 'vanya2'

d = []
for s in range(1, 190):
    if game((17, s)) == 'vanya2':
        d.append(s)

print(d)
