a = list('**' + '1' * 30 + '0' * 45 + '**')
print(a)
pos = 1
currentQ = 'q0'
stop = False

while not stop:
    if currentQ == 'q0':
        currentQ = 'q1'
        pos += 1

    if currentQ == 'q1':
        if a[pos] == '*':
            stop = True
        if a[pos] == '0':
            currentQ = 'q2'
            pos += 1
        if a[pos] == '1':
            currentQ = 'q2'
            pos += 1

    if currentQ == 'q2':
        if a[pos] == '*':
            stop = True
        if a[pos] == '0':
            a[pos] = '1'
            currentQ = 'q3'
            pos += 1
        if a[pos] == '1':
            a[pos] = '0'
            currentQ = 'q3'
            pos += 1

    if currentQ == 'q3':
        if a[pos] == '*':
            stop = True
        if a[pos] == '0':
            currentQ = 'q2'
            pos += 1
        if a[pos] == '1':
            currentQ = 'q1'
            pos += 1

b = "".join(a)
print(b.count('1'))


a = 9

print(int('111111111111', 2))
count = 0
for x in range(0, 4096):
    if (a + f"{x:0b}".count('1')) == 17:
        count += 1

print(count)