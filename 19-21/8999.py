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

from functools import lru_cache

@lru_cache(None)
def game(a, b):
    if a + b >= 211: 
        return 'END'
    moves = [
        game(a + 1, b),  # +1 в первую кучу
        game(a * 2, b),  # *2 в первую кучу
        game(a, b + 1),  # +1 во вторую кучу
        game(a, b * 2)   # *2 во вторую кучу
    ]
    if 'END' in moves: 
        return 'В1'
    if all(m == 'В1' for m in moves): 
        return 'П1'
    if 'П1' in moves: 
        return 'В2'
    if all(m in ('В1', 'В2') for m in moves): 
        return 'П2'
    

for s in range(2, 194):
    res = game(17, s)
    if res in ('П1', 'В2', 'П2'):
        print(f"S = {s}: {res}")
