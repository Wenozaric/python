def runTest(myValue, mustValue, issue):
    if myValue == mustValue: print(f"-- {issue} -- Ответ одинаковый, равен {myValue} ✅")
    else: print(f"-- {issue} -- Ответ неверный, равен {myValue}, должен {mustValue} ❌")

import sys
sys.setrecursionlimit(10000)

def a9154():
    s = {}

    for x in range(1, 37812):
        if x <= 20: s[x] = x + 2
        if x > 20: s[x] = s[x - 3] + 1

    return 3 * s[x - 3] + 7

def a9152():
    f = {}
    
    def g(a):
        if a >= 22560: return a // 23 + 33
        else: return g(a + 11) - 4

    for x in range(1, 549):
        if x < 21: f[x] = 10 * (g(x - 7) - 36)
        if x >= 21: f[x] = f[x - 8] + 1095

    return f[548]

runTest(a9154(), 37861, 9154)
runTest(a9152(), 50, 9152)