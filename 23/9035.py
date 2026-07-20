newSet = set()

def f(current, step):
    if( step == 9 and str(current)[-1] != '4'):
        newSet.add(current)
        return ''
    if( step < 9 and str(current)[-1] != '4'):
        f(current + 7, step + 1)
        f(current - 4, step + 1)

    return len(newSet)

print(f(0, 0))