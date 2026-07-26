a = open('9009.txt')

data = [int(x) for x in a]
data.sort(reverse=True)

count = 0
last = data[0]

for i in range(1, len(data)):
    if last - data[i] >= 8:
        count += 1
        last = data[i]

print(count, last)