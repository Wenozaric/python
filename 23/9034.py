newSet = set()

def f(current, step):
    if current != 5:
        if( step == 10):
            newSet.add(current)
            return None
        if( step < 10):
            f(current + 3, step + 1)
            f(current - 2, step + 1)
    
    return len(newSet)

print(f(0, 0))

