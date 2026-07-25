from math import dist

data = []

for i in open('???'):
    x, y = [float(j) for j in i.replace(',',  '.'.split())]
    data.append([x, y])

clasters = []

while len(data) != 0:
    clasters.append([data.pop(0)])
    for p in clasters[-1]:
        sosed = [p1 for p1 in data if dist(p, p1) < 1]
        clasters[-1] += sosed
        for p1 in sosed: data.remove(p1)

def center(claster):
    mn = []

    for p1 in claster:
        s = sum(dist(p1, p2) for p2 in claster)
        mn.append([s, p1])
    return min(mn)[1]