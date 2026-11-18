# def climbStairs(n):
#         dp = [0] * (n + 1)
#         dp[0] = 1
#         for i in range(1, n + 1):
#             if i - 1 >= 0:
#                   dp[i] += dp[i - 1]
#             if i - 2 >= 0:
#                   dp[i] += dp[i - 2]
  
#         return dp[n]

# print(climbStairs(3))    

# def maxProfit(prices):
#     max_profit = 0
#     min_price = prices[0]

#     for i in prices:
#         if i < min_price:
#                 min_price = i
#         elif i - min_price > max_profit:
#             max_profit = i - min_price
    
#     return max_profit

# print(maxProfit([7,6,4,3,1]))

# def countBits(n):
#     d = [0] * (n + 1)
    
#     for i in range(1, n + 1):
#         d[i] = d[i // 2] + (i % 2)
        
#     return d

# print(countBits(2))
# print(countBits(5))

# def f(x):
#     dp = [0] * (x + 1)

#     for x in range(2, x + 1):
#         dp[x] = dp[x - 1] + 1
        
#         if x % 2 == 0:
#             dp[x] = min(dp[x], (dp[x // 2] + 1))

#         if x % 3 == 0:
#             dp[x] = min(dp[x], (dp[x // 3] + 1))

#     return dp[-1]

# print(f(32718))
# def r(n):
#     d = [0] * (n + 1)
#     for x in range(1, n + 1):
#         if x == 1: d[x] = 1
#         else:
#             d[x] = d[x - 1] + d[x - 2]

#     return d[n]


# print(r(2))
# print(r(3))
# print(r(4))

# def u(n):
#     d = [-1] * (len(n))
#     d[0] = n[0]
#     d[1] = n[1]
#     for x in range(2, len(n)):
#         print(d)
#         d[x] = min(d[x - 1], d[x - 2]) + n[x]

#     return min(d[-1], d[-2])

# print(u([10, 15, 20]))

# def o(n):
#     d = [False] * (n + 1)
#     for i in range(2, n + 1):
#         print(d)
#         for x in range(1, i):
#             if i % x == 0 and not d[i - x]:
#                 d[i] = True
#                 break


#     return d[n]

# print(o(5))

# def tribonacci(n):
#     if n >= 4:
#         d = [-1] * (n + 1)
#     else:
#         d = [0] * 4

#     d[1] = 1
#     d[2] = 1
#     d[3] = 2

#     for i in range(4, n + 1):
#         d[i] = d[i - 1] + d[i - 2] + d[i - 3]
#     return d[n]

# print(tribonacci(25))

# def maxRepeating(sequence, word):
#     d = [0] * (len(sequence) + 1)

#     for i in range(len(word), len(sequence) + 1):
#         for i in range(len(word), len(sequence) + 1):
#             if sequence[i - len(word) : i] == word:
#                 d[i] = d[i - len(word)] + 1

#     return max(d)



# print(maxRepeating('ababc', 'ab'))

def getLongestSubsequence(words, groups):
    if len(groups) < 1: return 1
    d = [[] for _ in range(len(groups))]
    for i in range(len(groups)):
        best_prev = []
        for k in range(0, i):
            if groups[i] != groups[k]:
                if len(best_prev) < len(d[k]): best_prev = d[k]
        d[i] = best_prev + [words[i]]

    return max(d, key = len)

print(getLongestSubsequence(["a","b","c","d"], [1,0,1,1]))
print(getLongestSubsequence(["d"], [1]))
