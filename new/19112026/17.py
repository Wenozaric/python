a = open('17.txt')
b = [int(x) for x in a]
u = [int(x) for x in b if x < 0]
ttl = sum(u)
print(ttl)

d = []

for x in range(0, len(b) - 2):
    i1 = b[x]
    i2 = b[x + 1]
    i3 = b[x + 2]

    maxI = max(i1, i2, i3)
    minI = min(i1, i2, i3)

    if (maxI * minI) > ttl:
        d.append(i1 + i2 + i3)
print(len(d))
print(abs(max(d)))