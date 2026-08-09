count = 0

for line in open('9-290.txt'):
    dline = [int(x) for x in line.split()]

    count1 = {x for x in dline if dline.count(x) == 2}
    count2 = [x for x in dline if dline.count(x) == 1]

    if len(count1) == 2 and len(count2) == 2 and sum(count1) * 2 > sum(count2):
        count += 1

print(count)