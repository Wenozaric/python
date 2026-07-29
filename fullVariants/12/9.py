k = 0
for x in open('9.txt'):
    b = [int(i) for i in x.split()]

    a = [x for x in b if b.count(x) >= 3]
    c = [x for x in b if b.count(x) >= 2]
    z = [x for x in b if b.count(x) == 1]
    if len(a) > 0 and len(z) > 0:
        if sum(c) / len(c) < sum(z) / len(z):
            k += 1
print(k)
