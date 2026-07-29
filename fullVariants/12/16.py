b = set()

def f(n):
    if n % 2 == 0:
        return f(n // 2) + 5
    elif n % 2 != 0 and n % 5 == 0:
        return f(n // 5) + 2
    elif n % 2 == 1 and n % 5 != 0:
        return 0

for x in range(1, 1000001):
    b.add(f(x))

print(len(b))