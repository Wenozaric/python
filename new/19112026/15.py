def f(x, y, a):
    return (x >= 9) or ((2 * x) < y) or ((x * y) < a)

for a in range(1, 150):
    valid = True
    for x in range(1, 500):
        for y in range(1, 500):
            if f(x, y, a) == False:
                valid = False
    if valid:
        print(a)