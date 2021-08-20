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
If we think a bit  we can find a linear solution. Consider the array 1 2 3 4 5 6 7 8 9 10 with a jumping step of 4. We 
can reach 2 with only one way, 3 with two ways, 4 with four ways and 5 with eight ways. Why? At each step, it is obvious
that we can reach from the index behind. The answer is prev_index + X. We can find X by thinking that we can jump from 
each previous index from the beginning. But that would just give as the same answer as prev_index so the answer is 
2 * prev_index. But happens at 6? It is obvious that the same logic holds but we have to look at max i-k-1 steps behind.
That means the answer now is dp[i] = 2*dp[i-1] - dp[i-k-1] whereas for the first k indices it was dp[i] = 2*dp[i-1] with
base cases d[1] = dp[2] = 1, considering we start counting the indices from 1 and not from 0.

Final complexity: O(N)
"""

modulo = 1000000007
n, k = map(int, input().split())
dp = [0] * (n+1)
dp[1] = 1
dp[2] = 1
for i in range(3, k+1):
    dp[i] = 2 * dp[i-1]

for i in range(k+1, n+1):
    dp[i] = 2*dp[i-1] - dp[i-k-1]

print(dp[-1] % modulo)

"""
First, lets see a quadratic solution. We can simply iterate through the whole array and at each index look from the 
0th up until the i-k index and add all the possible steps. 

Final complexity: O(N^2)
"""

modulo = 1000000007
n, k = map(int, input().split())
dp = [0] * n
dp[0] = 1
for i in range(1, n):
    for j in range(max(0, i-k), i):
        dp[i] = (dp[i] + dp[j]) % modulo

print(dp[-1])