a = open('24-384.txt').readline()

left = 0
minLen = len(a)
zCount = 0

for right in range(len(a)):
    if a[right] == 'Z': zCount += 1
    while zCount >= 270:
        current = right - left + 1
        minLen = min(minLen, current)

        if a[left] == 'Z':
            zCount -= 1
        left += 1

print(minLen)