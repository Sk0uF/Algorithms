"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/jump-k-forward-250d464b/

There are n stones in a row from left to right. You are standing on the first stone. From every step from stone number i
you can jump at most k stones further. You cannot jump over stone number n. How many ways are there to travel to stone
number n?

Input - Output:
First line contains n and k.
Output the answer modulo 10^9 + 7.

Sample input:
5 2

Sample Output:
5
"""

"""
We can simply find the partial sums array, iterate throught the array end at each step check for the minimum X number 
that is required.

Final complexity: O(N)
"""

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