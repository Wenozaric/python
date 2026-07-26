from fnmatch import fnmatch

d = []

for x in range(0, 100000001, 271):
    if fnmatch(str(x), '12??15*6'): d.append([x, x // 271])

print(d)