"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/monk-and-conversion-game-code-monk-168d2bad/

Monk was having a great time in the Digital World, and was surprised to see a new game called, "Conversion Game". In
this game, two arrays of N integers are playing against each other and Array A wants to convert itself in Array B.
Array A can do two types of operations on itself:
1 Take two adjacent elements Ai and Ai+1 , increase Ai by 1 and decrease Ai+1 by 1.
2 Take two adjacent elements Ai and Ai+1 , decrease Ai by 1 and increase Ai+1 by 1.
Monk being an awesome coder, wants to know whether Array A can convert itself into Array B, by using any number of such
operations. You have to print "YES" (without quotes), if Array A can convert itself into array B, else print "NO"
(without quotes).

Input - Output:
First line of input will consists of integer T denoting total number of test cases.
Each test case will begin with integer N.
Next line will consists of N integers, representing Array B.
Next line will consists of N integers, representing Array B.
Print "YES" (without quotes), if Array A can convert itself into array B by using any number of operations,
else print "NO" (without quotes).

Sample input:
2
5
1 2 1 3 2
1 1 1 2 4
5
1 1 10 1 1
1 2 2 2 4

Sample Output:
YES
NO
"""

"""
For array A to convert to array B, the difference between each corresponding index of both arrays has to be 0. Lets take
for example the array A=1 2 1 3 2 and B=1 1 1 2 4. A[0]-B[0]=0, A[1]-B[1] = 1, so that means we have to add 1 to A[1]
to become 2 but that would mean we would have to subtract 1 from the A[2], and this is exactly what we are going to do,
iterating from 0 to N-1, we are going to find what we have to add to each next value, which could be either 0 positive 
or negative. If we end up with 0 we have a "YES", think about it!!

Final complexity: O(N)
"""

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    add = 0
    for i in range(n):
        temp = a[i] + add
        add = temp - b[i]

    if add == 0:
        print("YES")
    else:
        print("NO")