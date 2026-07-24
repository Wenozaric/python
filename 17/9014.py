from math import isqrt

a = open('17-465.txt')
b = [int(x) for x in a]

d = []

def checkNum(num):
    if num < 2: return 0
    for x in range(2, isqrt(num) + 1):
        if num % x == 0: return 0
    return 1

for index in range(len(b) - 3):
    a1 = b[index]
    a2 = b[index + 1]
    a3 = b[index + 2]
    a4 = b[index + 3]

    if 255 >= a1 >= 0 and 255 >= a2 >= 0 and 255 >= a3 >= 0 and 255 >= a4 >= 0:
        countNum = bin(a1)[2:].count('1') + bin(a2)[2:].count('1') + bin(a3)[2:].count('1') + bin(a4)[2:].count('1')
        total = a1 + a2 + a3 + a4
        if checkNum(countNum) == 1:
           d.append(total)

print(len(d))
print(max(d))