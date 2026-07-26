start = list('*' + f"{127:0b}" + '*')

current = 'q0'
pos = start.index('1') + len(f"{127:0b}") 

stop = False

while not stop:
    if current == 'q0':
        if start[pos] == '*':
            pos -= 1
            current = 'q1'

    elif current == 'q1':
        if start[pos] == '*':
            start[pos] = '1'
            pos += 1 
            current = 'q2'
        elif start[pos] == '0':
            start[pos] = '1'
            pos += 1
            current = 'q2'
        elif start[pos] == '1':
            start[pos] = '0'
            pos -= 1
            current = 'q1'

    elif current == 'q2':
        if start[pos] == '*':
            start[pos] = '1'
            stop = True
        elif start[pos] == '0':
            pos += 1
        elif start[pos] == '1':
            pos += 1    

result = "".join(start).strip('*')
print(int(result, 2))