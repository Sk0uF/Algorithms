
# First solution, what's the max value we can get with i elements for weight j
n, c = map(int, input().split())
u = list(map(int, input().split()))
w = list(map(int, input().split()))

# Capacity is to big!!!
dp = [[0 for _ in range(c+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, c+1):
        if w[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-w[i-1]] + u[i-1], dp[i-1][j])

print(dp[-1][-1])

# Second solution, what's the min weight we can get with i elements for value j
# n, c = map(int, input().split())
# u = list(map(int, input().split()))
# w = list(map(int, input().split()))
#
# max_val = sum(u)
# dp = [[float('inf') for _ in range(max_val+1)] for _ in range(n+1)]
# ans = 0
# dp[0][0] = 0
# for i in range(n+1):
#     dp[i][0] = 0
#
# for i in range(1, n+1):
#     for j in range(1, max_val+1):
#         if u[i-1] > j:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = min(dp[i-1][j-u[i-1]] + w[i-1], dp[i-1][j])
#
# for i in range(max_val+1):
#     if dp[n][i] <= c:
#         ans = i
#
# print(ans)


# Third solution, can be the first one or the second one but if we don't
# need the whole list then we can only keep track of the previous and current
# rows. That will lose us the information of how we got there though!
# n, c = map(int, input().split())
# u = list(map(int, input().split()))
# w = list(map(int, input().split()))
#
# max_val = sum(u)
# dp = [[float('inf') for _ in range(max_val+1)] for _ in range(2)]
# ans = 0
# dp[0][0] = 0
# dp[1][0] = 0
# curr = dp[1]
# prev = dp[0]
# for i in range(1, n+1):
#     curr = dp[i & 1]
#     prev = dp[not (i & 1)]
#     for j in range(1, max_val+1):
#         if u[i-1] > j:
#             curr[j] = prev[j]
#         else:
#             curr[j] = min(prev[j-u[i-1]] + w[i-1], prev[j])
#
# for i in range(max_val+1):
#     if curr[i] <= c:
#         ans = i
#
# print(ans)

# Fourth solution, can be the first one or the second one but if we don't
# need the whole list then we can do the dirty work by only using a 1D array
# but traversing j backwards. Think of it.
# n, c = map(int, input().split())
# u = list(map(int, input().split()))
# w = list(map(int, input().split()))
#
# max_val = sum(u)
# dp = [float('inf') for _ in range(max_val+1)]
# dp[0] = 0
# ans = 0
# for i in range(1, n+1):
#     for j in range(max_val, u[i-1]-1, -1):
#         if u[i-1] > j:
#             dp[j] = dp[j]
#         else:
#             dp[j] = min(dp[j-u[i-1]] + w[i-1], dp[j])
#
# for i in range(max_val+1):
#     if dp[i] <= c:
#         ans = i
#
# print(ans)
#
