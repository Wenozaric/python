from math import dist

data = []
with open('27B.txt') as f:
    for line in f:
        line = line.replace(',', '.').split()
        if line:
            data.append((float(line[0]), float(line[1])))

cls = [[] for _ in range(7)]

for x, y in data:
    if -10 <= x <= -5:
        cls[0].append((x, y))
    elif -4 <= x <= 0:
        if y < -3:
            cls[1].append((x, y))
        else:
            cls[2].append((x, y))
    elif 1 <= x <= 5:
        if y < 1:
            cls[3].append((x, y))
        else:
            cls[4].append((x, y))
    elif 6 <= x <= 11:
        if y < 0:
            cls[5].append((x, y))
        else:
            cls[6].append((x, y))


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
a5 = findPoint(cls[4])
a6 = findPoint(cls[5])
a7 = findPoint(cls[6])

print(int(((a1[0] + a2[0] + a3[0] + a4[0] + a5[0] + a6[0] + a7[0]) / 7) * 100000), abs(int(((a1[1] + a2[1] + a3[1] + a4[1] + a5[1] + a6[1] + a7[1]) / 7) * 100000)))