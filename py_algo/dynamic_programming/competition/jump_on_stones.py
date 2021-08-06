# https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/jump-k-forward-250d464b/

# O(N)
modulo = 1000000007
n, k = map(int, input().split())
dp = [0] * (n+1)
dp[1] = s = 1
for i in range(2, k+1):
    dp[i] = s
    s += dp[i]

for i in range(k+1, n+1):
    dp[i] = s - dp[i-k-1]
    s += dp[i] - dp[i-k-1]

print(dp[-1] % modulo)

# O(N^2)
modulo = 1000000007
n, k = map(int, input().split())
dp = [0] * n
dp[0] = 1
for i in range(1, n):
    for j in range(max(0, i-k), i):
        dp[i] = (dp[i] + dp[j]) % modulo

print(dp[-1])