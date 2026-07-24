from math import isqrt

a = open('17-465.txt')
b = [int(x) for x in a]

d = []

def isPrime(num):
    if num < 2: return 0
    for x in range(2, isqrt(num) + 1):
        if num % x == 0: return 0
    return 1

for index in range(len(b) - 3):
    a1, a2, a3, a4 = b[index: index + 4]

    if 255 >= a1 >= 0 and 255 >= a2 >= 0 and 255 >= a3 >= 0 and 255 >= a4 >= 0:
        countPrime = isPrime(a1) + isPrime(a2) + isPrime(a3) + isPrime(a4)
        if countPrime == 2: d.append(a1 + a2 + a3 + a4)

print(len(d))
print(max(d))