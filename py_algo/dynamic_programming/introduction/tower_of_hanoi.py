"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/tower-of-hanoi-17/

Bob and Alice like to play the game tower of Hanoi. One day Alice challenges Bob to build the tallest tower from a set
of disks of different height and radius. The tower of Hanoi can be built by stacking disks on top of each other. In
order to put disk A on top of disk B, the radius and height of A must be strictly smaller than those of B. Help Bob to
win the challenge.

Input - Output:
First line of input contains number of test cases T.
First line of each test case contains value of N, the number of disks.
The next N lines contains two positive integer number Ri and Hi corresponding
to the radius and height of ith Disk respectively.
For each test case print the maximum height of the tower possible.

Sample input:
2
3
4 3
1 4
3 2
5
5 6
4 3
1 2
7 5
3 4

Sample Output:
5
12
"""

"""
We will follow a simple quadratic solution. We are going to sort the disks either by radius or by height and after that
we will iterate through the sorted array and find the maximum height we can achieve by iterating from the beginning up
to our current index and try stacking the disks. That can be expressed as dp[i] = max(dp[i], dp[j] + cur_disk_height)
if of course the disk is stackable, meaning is has sorted radius and height.

Final complexity: O(N^2)
"""

t = int(input())
for _ in range(t):
    n = int(input())
    disks = []
    for _ in range(n):
        r, h = map(int, input().split())
        disks.append((r, h))

    disks = sorted(disks)
    dp = [0] * n
    dp[0] = disks[0][1]
    for i in range(1, n):
        dp[i] = disks[i][1]
        for j in range(i):
            if disks[j][0] < disks[i][0] and disks[j][1] < disks[i][1]:
                dp[i] = max(dp[i], dp[j] + disks[i][1])

    print(max(dp))
