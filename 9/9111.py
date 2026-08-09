count = 0
for line in open('9-291.txt'):
    dline = [int(x) for x in line.split()]

    have3 = 0
    for x in dline:
        if dline.count(x) == 3: have3 = x

    b = set()
    if have3 != 0:
        b = {int(x) for x in dline if x != have3}

        if len(b) == 3:
            
            t = 1
            for x in b:
                t = t * x

            if have3 ** 3 < t:
                count += 1

print(count)



