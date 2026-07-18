from functools import lru_cache

def multi(num):
    if num % 10 == 0 or num % 10 == 1: return None
    return num * (num % 10)

@lru_cache(None)
def f(current, target):
    if( current == target): return 1
    if( current > target): return 0

    count = f(current + 1, target)

    if multi(current) != None : count += f(multi(current), target)
    return count

print(f(24, 150))