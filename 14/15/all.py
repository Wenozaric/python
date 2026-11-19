def runTest(myValue, mustValue, issue):
    if myValue == mustValue: print(f"-- {issue} -- Ответ одинаковый, равен {myValue} ✅")
    else: print(f"-- {issue} -- Ответ неверный, равен {myValue}, должен {mustValue} ❌")


def a9151():
    last = 0
    def dela(n, m): return n % m == 0

    for a in range(1, 10000):
        if all( dela(x, 33) <= ((not dela(x, a)) <= (not dela(x, 242))) for x in range(1, 10000)):
            last = a

    return last

runTest(a9151(), 726, 9151)