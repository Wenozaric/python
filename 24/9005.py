a = open('24-385.txt').readline()
maxLen = 0
currentLen = 0
for symb in a:
    if symb in '123456789AB': currentLen += 1
    else: currentLen = 0
    maxLen = max(maxLen, currentLen)

print(maxLen)