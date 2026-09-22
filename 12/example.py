t = '*' + bin(375)[2:] + '*'


#превращаем строку массив, чтобы заменять символы на позициях
t = list(t)

#последний символ
pos = len(t) - 1
stop = False
current = 'q0'

print(t)
while not stop:
    #q0
    if current == 'q0':
        if t[pos] == '*':
            current = 'q1'
            pos -= 1

    #current ?? q0 / q1  
    #q1
    else:
        if t[pos] == '1':
            t[pos] = '0'
            pos -= 1

        elif t[pos] == '0':
            t[pos] = '1'
            pos -= 1

        else:
            stop = True

print(int(''.join(t)[1:][:-1], 2))

