def ls(s):
    b = 'abcdefghijklmnopqrstuvwxyz'
    n = 0
    for char in s:
        n = n * 26 + (b.index(char) + 1)
    return n
slovo = 'screen'
pos = ls(slovo)

print(pos)
print(slovo)
