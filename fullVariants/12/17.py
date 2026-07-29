a = open('17.txt')
b = [int(x) for x in a]

minB4 = [y for y in b if 1000 <= y <= 9999]
minB2 = [y for y in b if 10 <= y <= 99]

b2 = min(minB2)
b4 = min(minB4)

d = []


for index in range(len(b) - 2):
    a1, a2, a3 = b[index: index + 3]
    cur1 = 0
    cur2 = 0

    if a1 % 7 == b4 % 11:
        cur1 += 1
    if a2 % 7 == b4 % 11:
        cur1 += 1
    if a3 % 7 == b4 % 11:
        cur1 += 1

    if a1 % 5 == b2 % 3:
        cur2 += 1
    if a2 % 5 == b2 % 3:
        cur2 += 1
    if a3 % 5 == b2 % 3:
        cur2 += 1

    if cur1 == 1 and cur2 == 1:
        d.append(a1 + a2 + a3)

print(len(d))
print(min(d))
