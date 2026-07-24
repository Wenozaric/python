a = open('24-378.txt').readline()

left = 0
minLen = len(a)
letters = 0

for right in range(len(a)):
    if a[right] in 'ABCDEF': letters += 1

    while letters > 3 or (a[left] not in 'ABCDEF' and (a[left] not in '0123456789' or a[left] in a[left + 1 : right + 1])):
        if a[left] in 'ABCDEF': 
            letters -= 1
        left += 1

    if letters == 3:
        if len({c for c in a[left : right + 1] if c.isdigit()}) == 10:
            minLen = min(minLen, right - left + 1)

print(minLen)
