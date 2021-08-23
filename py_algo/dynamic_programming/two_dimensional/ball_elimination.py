"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/ball-elimination/

You have a sequence of balls. Every ball has a color. You can eliminate any single ball and pay one pound. Also you can
eliminate any two neighboring balls which have the same colors for no cost. Find minimal amount you need to spend to
eliminate all balls.

Input - Output:
First line contains single integer n -- number of balls.
Second line contains n space-separated integers a1, a2, ..., an -- colors of balls.

Sample input:
3
2 1 2

Sample Output:
1

"""

"""
The problem can be solved by iterating the whole array in pairs. First, from the start up to the end with pairs of 2
then pairs of 3 etc. We can do two things, either remove the ball from the start of the pair, or try and find a matching
ball inside the same pair, remove everything else in the pair and then remove those 2 balls. The complexity of this 
approach is cubic.

Final complexity: O(N^3)
"""

n = int(input())
balls = list(map(int, input().split()))
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for length in range(1, n+1):
    for start in range(n - length + 1):
        stop = start + length
        dp[start][stop] = dp[start+1][stop] + 1
        for point in range(start+1, stop):
            if balls[start] == balls[point]:
                dp[start][stop] = min(dp[start][stop], dp[start+1][point] + dp[point+1][stop])

print(dp[0][n])
