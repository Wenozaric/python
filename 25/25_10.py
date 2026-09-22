from fnmatch import fnmatch

d = []

for x in range (100000, 1000000, 2):
    if len(d) == 5: 
        print(d)
        break
    if str(x).count('0') == 0:
        B = 1
        while 3 ** B < x:
            A = 113
            currentB = 3 ** B
            while (currentB + A) <= x:
                if currentB + A == x:
                    d.append([x, B])
                    A += 100000000
                else:
                    A += 226
            B += 1
