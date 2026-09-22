from fnmatch import fnmatch

d = []


def checkMash(x):
    if len(str(x)) != len('ЧНЧЧНЧН'): return False
    stringi = 'ЧНЧЧНЧН'
    condition = True
    for pos in range(len(str(x))):
        if stringi[pos] == 'Ч':
            if int(str(x)[pos]) % 2 != 0:
                condition = False
        else:
            if int(str(x)[pos]) % 2 == 0:
                condition = False
    return condition

for x in range(100004443, 1000000000, 7777):
    if checkMash(str(x)[:-2]) and x % 7777 == 0 and x % 100 == 77:
        print(x, x // 7777)
        d.append([x, x // 7777])

