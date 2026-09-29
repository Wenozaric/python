table = [[['*', 1, 'q1']], [['*', 1, 'q2'], ['0', 1, 'q1'], ['1', 1, 'q1']], [['1', 1, 'q3']], ['*', 'S', 'q3']]
x = bin(2027)[2:] + '*'
x = list(x)
pos = 0
stop = False

current = 1
while not stop:
    currentString = table[current]
    print(currentString)
    positionIntoString = 0
    for underTable in currentString:
        print(underTable)
        print('position intro string')
        print(positionIntoString)
        print(x[positionIntoString])
        #if x[positionIntoString] == x[pos]:


        #if x[positionIntoString] ==
        #if x[pos] != '*':
        #    print(x[pos])
        #    x[pos] = underTable[x[pos]]
        #    print(underTable[x[pos]])
        #else:
        #    x[pos] = underTable[0]
        #    print(underTable[0])
        #positionIntoString += 1
    break