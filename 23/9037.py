newSet = set()

def f(current, step, valid):
    if( current == 17): valid = True
    if( valid and step == 8 ): 
        newSet.add(current)
        return None
    if( step < 8 ):
        f(current + 8, step + 1, valid)
        f(current - 6, step + 1, valid)

    return len(newSet)
print(f(7, 0, False))


    