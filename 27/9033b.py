from math import dist

data = []

for i in open('9033b.txt'):
    i = i.replace(',', '.').split()
    x, y = [float(j) for j in i[:2]]
    z = i[2]

    data.append([x, y, z])

clasters = []

while len(data) > 0:
    clasters.append([data.pop(0)])
    for t in clasters[-1]:
        sosedi = [i for i in data if dist(t[:2], i[:2]) < 2]
        clasters[-1] += sosedi
        for sosed in sosedi: data.remove(sosed)

cl1 = clasters[0]
cl2 = clasters[1]
cl3 = clasters[2]

def get8(cl):
    newCl = [i for i in cl if int(i[2][1]) >= 8]
    return newCl

b8 = []

b1_8 = get8(cl1)
b2_8 = get8(cl2)
b3_8 = get8(cl3)

def getMinRanges(cl1_8, cl2_8, cl3_8):
    ranges = []

    for t1 in cl1_8:
        for t2 in cl2_8:
            ranges.append(dist(t1[:2], t2[:2]))
        for t3 in cl3_8:
            ranges.append(dist(t1[:2], t3[:2]))

    for t2 in cl2_8:
        for t3 in cl3_8:
            ranges.append(dist(t2[:2], t3[:2]))

    return min(ranges)

b1_otv = getMinRanges(b1_8, b2_8, b3_8)

def getOneClasterRanges(cl_8):
    ranges = []
    for i in cl_8:
        for j in cl_8:
            range = dist(i[:2], j[:2])
            if range != 0: ranges.append(range)

    return ranges
 
cl1_b2 = getOneClasterRanges(b1_8)
cl2_b2 = getOneClasterRanges(b2_8)
cl3_b2 = getOneClasterRanges(b3_8)

sumAll = sum(cl1_b2) + sum(cl2_b2) + sum(cl3_b2)
allLen = len(cl1_b2) + len(cl2_b2) + len(cl3_b2)
print(int(b1_otv * 10000), int((sumAll / allLen) * 10000))

