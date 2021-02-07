"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/monk-and-square-root-0c152c9a/

Given two integers N and M, help Monk find an integer X, such that X^2 mod M = N  and X >= 0. If there are multiple
values of X print smallest one. If there is no possible value of X print -1. Also, N < M.

Input - Output:
First line consists of a single integer T denoting the number of test cases.
Each test case consists of a single line containing two space separated integers denoting N and M.
For each test case print the required answer.

Sample input:
2
4 5
0 4

Sample Output:
2
0
"""

"""
Since N < M, we don't need to check for values bigger than M. For example, if we had the numbers 0, 1, 2, 3, 4, 5, 6
and M was 5 then we would only need to check from 0 to 4, because the mod(k) operation is always going to yield a number
between 0 and k-1. The only difference with the above example is that we have the square of the numbers and to the
actual numbers but the fact that the mod(k) will yield a number between 0 and k-1 is not going to change. For the
squared numbers, we also take advantage of the fact that the result after M//2 will repeat (and it may not include all
the results from 0 to M//2).

Final complexity: O(100*M//2) => O(M)
"""

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    ans = -1
    for i in range(int(n**0.5), m//2+1):
        if (i*i) % m == n:
            ans = i
            break

    print(ans)

# Cool way to find an array of squares
# squares = [0, 1]
# count = 1
# for i in range(2, 100):
#     count += 2
#     squares.append(count+squares[i-1])
