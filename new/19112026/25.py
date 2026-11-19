# def factor(n):
#     res = []
#     d = 2
#     while d ** 2 <= n:
#         if n % d == 0:
#             res.append(d)
#             n //= d
#         else:
#             d += 1
#     if n > 1:
#         res.append(n)

#     return res

# u = []
# for y in range(2700034, 1000000000, 100):
#     s = factor(y)
#     p = False
#     s = sorted(s)
#     last = 0
#     n = 0
#     deli = 0
#     for x in s:
#         if last == x:
#             if n == 0:
#                 n = 2
#             else:
#                 n += 1
#         else:
#             n = 0
#         last = x
#         if n >= 5:
#             deli = x
#             p = True
#     if p:
#         u.append([y, deli])

#     if len(u) == 5:
#         print(u)
#         break
    


# def factor(n):
#     d = 2
#     res = []
#     while d ** 2 <= n:
#         if n % d == 0:
#             res.append(d)
#             n //= d
#         else:
#             d += 1
#     if n > 1:
#         res.append(n)

#     return res
# print(factor(24))