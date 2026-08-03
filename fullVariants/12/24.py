a = open('24.txt').readline()

maxNum = ''
lastIndex = 0

left = 0

#12 0123456789ab

for right in range(len(a)):
    #print('текущий отрезок ' + a[left: right + 1])
    if a[right] not in '0123456789AB':
        #print('сработало условие не подходящего символа')
        #print(f'последний символ той строки {lastIndex}')
        if a[left: right] != '':
            #print(f'предыдущая подстрока {a[left: right]}')
            if int(a[left: right], 12) % 6 == 0:
                if maxNum != '':
                    if int(a[left: right], 12) > int(maxNum, 12):
                        lastIndex = right - 1
                        maxNum = a[left: right]
                else:
                    lastIndex = right - 1
                    maxNum = a[left: right]
            left = right
    while left < len(a) and a[left] not in '0123456789AB':
        left += 1

print(lastIndex)