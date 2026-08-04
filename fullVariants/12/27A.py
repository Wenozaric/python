from math import dist

data = []

for x in open('27A.txt'):
    x = x.replace(',', '.').split()
    b = [float(y) for y in x]
    data.append(b)

print(data)


cls = []

while len(data) > 0:
    cls.append([data.pop(0)])
    for x in cls[-1]:
        sosedi = [y for y in data if dist(x, y) < 1]
        cls[-1] += sosedi
        for sosed in sosedi: data.remove(sosed)

print(len(cls))

def findPoint(claster):
    newA = []
    prevCount = 0

    for a in claster:
        count = 0
        for x in claster:
            if dist(a, x) <= 1:
                count += 1
        if count == prevCount:
            if a[0] > newA[0]:
                newA = a
                prevCount = count
        elif count > prevCount:
            newA = a
            prevCount = count

    return newA


a1 = findPoint(cls[0])
a2 = findPoint(cls[1])
a3 = findPoint(cls[2])
a4 = findPoint(cls[3])

print(int(((a1[0] + a2[0] + a3[0] + a4[0]) / 4) * 100000), int(((a1[1] + a2[1] + a3[1] + a4[1]) / 4) * 100000))