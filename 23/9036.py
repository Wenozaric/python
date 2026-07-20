newSet = set()

def f(current, step):
    if(step == 12 and str(current).count('7') == 0): 
        newSet.add(current)
        return ''
    if(step < 12 and str(current).count('7') == 0):
        f(current + 6, step + 1)
        f(current - 5, step + 1)
    return len(newSet)

print(f(10, 0))