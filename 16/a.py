from sys import *
setrecursionlimit(100000)
def f(N):
    if N >= 19:
        return f(N-4) + 3580
    if N < 19:
        return 6 * (g(N-7) - 36)
def g(N):
    if N >= 248045:
        return N/20 + 28
    if N < 248045:
        return g(N+9) - 4
print(f(673))