result = set()

def f(current, step):
    if( step == 7 ): 
        result.add(current)
        return None
    
    if( step == 6 ):
        f(current - 3, step + 1)
    
    if( step < 6):
        f(current + 5, step + 1)
        f(current - 3, step + 1)
        f(current + 1, step + 1)
    
    return len(result)
print(f(2, 0))