"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/knapsack-with-large-weights-33a2433a/

The famous knapsack problem but with a twist!

Input - Output:
The first line contains n and c, denoting the number if objects and the capacity
where 1 <= n <= 10^3 and 0 <= c <= 2*10^6.
The second line contains n integers, denoting the values, where 0 <= ui <= 50.
The third line contains n integers, denoting the weights, where 0 <= wi <= 2*10^6.

Sample input:
4 20
10 2 1 3
10 5 10 10

Sample Output:
13
"""

"""
Classic knapsack solution given by dp[i][j] = max(dp[i-1][j-w[i]] + u[i], dp[i-1][j]) or dp[i][j] = dp[i-1][j] if 
w[i] > j where i basically means the subset of the first i items, j is the weight and dp[i][j] has the value. So the
question is, for i items, and for j weight what is the maximum value we can get? 

Final complexity: O(C*N)
"""

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

"""
When the capacity is too big and max value is small we can easily switch our logic and ask another question. What's the
minimum weight to have a value j for the subset of the first i elements? That can be expressed as 
dp[i][j] = min(dp[i-1][j-u[i]] + w[i], dp[i-1][j]) or dp[i][j] = dp[i-1][j] if u[i] > j.

Final complexity: O(MAX_VAL*N)
"""

n, c = map(int, input().split())
u = list(map(int, input().split()))
w = list(map(int, input().split()))

max_val = sum(u)
dp = [[float('inf') for _ in range(max_val+1)] for _ in range(n+1)]
ans = 0
dp[0][0] = 0
for i in range(n+1):
    dp[i][0] = 0

for i in range(1, n+1):
    for j in range(1, max_val+1):
        if u[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i-1][j-u[i-1]] + w[i-1], dp[i-1][j])

for i in range(max_val+1):
    if dp[n][i] <= c:
        ans = i

print(ans)

"""
When we don't need to keep track of the way we followed to reach the final answer then we can simply just keep track
of the previous and current rows! That way we are going to use less memory.

Final complexity: O(C*N) or O(MAX_VAL*N)
"""

n, c = map(int, input().split())
u = list(map(int, input().split()))
w = list(map(int, input().split()))

max_val = sum(u)
dp = [[float('inf') for _ in range(max_val+1)] for _ in range(2)]
ans = 0
dp[0][0] = 0
dp[1][0] = 0
curr = dp[1]
prev = dp[0]
for i in range(1, n+1):
    curr = dp[i & 1]
    prev = dp[not (i & 1)]
    for j in range(1, max_val+1):
        if u[i-1] > j:
            curr[j] = prev[j]
        else:
            curr[j] = min(prev[j-u[i-1]] + w[i-1], prev[j])

for i in range(max_val+1):
    if curr[i] <= c:
        ans = i

print(ans)

"""
For the final solution we can be a little bit more observant and solve the problem by only using one 1D array and 
traversing it backwards. We can do that because each time we are looking at the previous row we are only looking at
its left. That also saves some more space than the previous solution but asymptomatically it's the same.

Final complexity: O(C*N) or O(MAX_VAL*N)
"""

n, c = map(int, input().split())
u = list(map(int, input().split()))
w = list(map(int, input().split()))

max_val = sum(u)
dp = [float('inf') for _ in range(max_val+1)]
dp[0] = 0
ans = 0
for i in range(1, n+1):
    for j in range(max_val, u[i-1]-1, -1):
        if u[i-1] > j:
            dp[j] = dp[j]
        else:
            dp[j] = min(dp[j-u[i-1]] + w[i-1], dp[j])

for i in range(max_val+1):
    if dp[i] <= c:
        ans = i

print(ans)
