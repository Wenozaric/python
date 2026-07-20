from functools import lru_cache


@lru_cache(None)
def f(current, total, valid):    
    if( current == 16): valid = True
    if( current == 5 and valid): return 1
    if current < 5: return 0

    total = f(current - 1, total, valid)
    total += f(current // 2, total, valid)

    return total

print(f(50, 0, False))