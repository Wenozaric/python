t = '*' + '1' * 1000 + '0' + '*'


#превращаем строку массив, чтобы заменять символы на позициях
t = list(t)

#последний символ
pos = 0
stop = False
current = 'q0'

print(t)
while not stop:
    #q0
    if current == 'q0':
        if t[pos] == '*':
            current = 'q0'
            pos += 1

        elif t[pos] == '0':
            current = 'q0'
            t[pos] = '1'
            stop = True

        else:
            current = 'q1'
            t[pos] = '0'
            pos += 1

    else:
        if t[pos] == '0':
            t[pos] = '1'
            current = 'q0'
            pos += 1

        elif t[pos] == '1':
            t[pos] = '0'
            current = 'q1'

        else:
            stop = True
            current = 'q1'

print((''.join(t)[1:][:-1]).count('1'))