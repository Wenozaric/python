a = open('26.txt')
b = [x.split() for x in a]
totalSum = 0
for x in range(len(b)):
    if x != 0:
        totalSum += int(b[x][1])
srPrice = totalSum / int(b[0][0])
print(srPrice)

cleB = b[1:]
expensiveT = [x for x in cleB if int(x[1]) > srPrice]

uniqueId = set()

[uniqueId.add(int(x[0])) for x in expensiveT]
print(uniqueId)

table = []

for art in uniqueId:
    price = next((int(x[1]) for x in b if int(x[0]) == art), 0)
    sold = sum(1 for x in b if int(x[0]) == art and x[2] == '0')
    left = sum(1 for x in b if int(x[0]) == art and x[2] == '1')

    table.append([int(art), price, sold, left])

#print('1')
#print(table)
#print('2')
table.sort(key=lambda x: x[2])
print(table)

print(f'{802*46} 45510')