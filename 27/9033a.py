from math import dist

data = []

for i in open('9033a.txt'):
    i = i.replace(',', '.').split()
    x, y = [float(j) for j in i[:2]]
    z = i[2]

    data.append([x, y, z])

clasters = []

while len(data) > 0:
    clasters.append([data.pop(0)])
    for t in clasters[-1]:
        sosedi = [a for a in data if dist(t[:2], a[:2]) < 1]
        clasters[-1] += sosedi
        for sosed in sosedi: data.remove(sosed)

def findCenter(claster):
    mn = []

    for t in claster:
        s = sum(dist(t[:2], a[:2]) for a in claster)
        mn.append([s, t])

    return min(mn)[1]

def kvazar(claster, point):
    minDist = []

    for t in claster:
        if t[2].count('VII') == 1:
            minDist.append(dist(point[:2], t[:2]))

    return [min(minDist), max(minDist)]

a = findCenter(clasters[0])
b = findCenter(clasters[1])

a1, a2 = kvazar(clasters[0], a)
b1, b2 = kvazar(clasters[1], b)

print(abs(int(a1 * 10000)))
print(abs(int(a2 * 10000)))
print(abs(int(b1 * 10000)))
print(abs(int(b2 * 10000)))

