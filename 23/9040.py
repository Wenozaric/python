from functools import lru_cache
from math import isqrt

def pr(ogr):
    if ogr < 2:
        return False
    for a in range(2, isqrt(ogr) + 1):
        if ogr % a == 0:
            return a
    return None
        
@lru_cache(None)
def f(current, target):
    if current < target: return 0
    if current == target: return 1

    count = f(current - 1, target)

    b = pr(current)

    if b is not None:
        count += f(current // b, target)

    return count


print(f(150, 7))
