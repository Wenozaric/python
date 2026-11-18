a = input().split(' ')
b = [int(x) for x in a if x != '']

E = b[0]
n = b[1]
idx = 2

d = [-1] * (E + 1)
d[0] = 0

for _ in range(n):
    k = b[idx]
    idx += 1

    mod = []

    for _ in range(k):
        mod.append((b[idx], b[idx+1]))
        idx += 2
    new_d = [-1] * (E + 1)

    for ne in range(E + 1):
        if d[ne] != -1:
            for e, p in mod:
                if ne + e <= E:
                    if d[ne] + p > new_d[ne + e]:
                        new_d[ne + e] = d[ne] + p
    d = new_d

best_p = 0
best_e = 0
for e in range(E + 1):
    if d[e] > best_p:
        best_p = d[e]
        best_e = e

print(f"{best_p};{best_e}")