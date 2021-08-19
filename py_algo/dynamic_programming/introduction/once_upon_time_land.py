"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/once-upon-a-time-in-time-land/

In a mystical TimeLand, a person's health and wealth is measured in terms of time(seconds) left. Suppose a person there
has 24x60x60 = 86400 seconds left, then he would live for another 1 day. A person dies when his time left becomes 0.
Some time-amount can be borrowed from other person, or time-banks. Some time-amount can also be lend to another person,
or can be used to buy stuffs. Our hero Mr X, is in critical condition, has very less time left. Today's the inaugural
day of a new time-bank. So they are giving away free time-amount worth 1000 years. Bank released N slips, A[1],
A[2], .... A[N]. Each slip has a time-amount(can be +ve as well as -ve). A person can pick any number of slips (even
none, or all of them, or some of them) out of the N slips. But bank introduced a restriction, they announced one more
number K. Restriction is that, if a person picks a slip A[i], then the next slip that he can choose to pick will be
A[i+K+1]. It means there should be a difference of at least K between the indices of slips picked. Now slip(s) should be
picked in such a way that their sum results in maximum positive time-amount sum possible with the given restriction. If
you predict the maximum positive sum possible, then you win. Mr X has asked for your help. Help him win the lottery, and
make it quick!

Input - Output:
First line of the test file contains single number T, the number of test cases to follow.
Each test case consists of two lines.
First line contains two numbers N and K, separated by a space. Second line contains the N
numbers A[1], A[2] ..... A[N] separated by space.
For every test case, output in a single line the maximum positive sum possible, that is output for the case.

Sample input:
2
10 1
1 2 -3 -5 4 6 -3 2 -1 2
10 2
1 2 -3 -5 4 6 -3 2 -1 2

Sample Output:
12
10
"""

"""
We are either going to pick the previous or the current money plus the k+1 previous. The answer is given by the 
expression dp[i] = max(dp[i-1], dp[i-k-1] + bank[i]). That's a linear solution.

Final complexity: O(N)
"""

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    bank = list(map(int, input().split()))
    dp = [0] * n

    if n == 0:
        print(0)
    elif n == 1:
        print((max(bank[0], bank[1])), 0)
    elif k > n:
        print(max(bank))
    else:
        for j in range(n):
            if j <= k:
                if bank[j] < 0:
                    if j == 0:
                        dp[j] = 0
                    else:
                        dp[j] = dp[j-1]
                else:
                    if j == 0:
                        dp[j] = bank[j]
                    else:
                        dp[j] = max(bank[j], dp[j-1])
            else:
                dp[j] = max(bank[j] + dp[j-k-1], dp[j-1])

        if dp[n-1] > 0:
            print(dp[n-1])
        else:
            print(0)
