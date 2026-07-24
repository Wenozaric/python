from fnmatch import fnmatch

a = open('17-465.txt')
b = [int(x) for x in a]

d = []

for index in range(len(b) - 3):
    a1, a2, a3, a4 = b[index: index + 4]
    if 255 >= a1 >= 0 and 255 >= a2 >= 0 and 255 >= a3 >= 0 and 255 >= a4 >= 0:
        if fnmatch(str(a1), '?') and fnmatch(str(a2), '*1*') and fnmatch(str(a3), '2*') and fnmatch(str(a4), '?'):
            d.append(a1 + a2 + a3 + a4)

print(len(d))
print(max(d))
