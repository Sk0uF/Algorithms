"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/choosing-the-judges-7/

Harry was contesting to be the most stylist person in his college. He had to collect maximum points from the judges to
be able to win. However there was a problem. The judges were sitting in a line and each pair of adjacent judges had ego
issues with each other. So if one judge gave X points to Harry then the next judge won’t give him any points. Harry had
a friend in the organizing team and through him he had found out the exact points he would get from each judge if he
chose their score to be considered. Help him find out the maximum points he can score.

Input - Output:
The first line of input contains the number of test cases, T.
0 < T < = 10
Each test case starts with a number N, the number of judges.
0 <= N < = 10^4.
The next line will have N numbers, number of points each judge gave Harry
0 < = X(i) < = 10^9.
The order of the judges does not change.
For each test case print “Case T: A” without quotes in a single line.
T is the case number, starting with 1.
A is the maximum number of points Harry can collect.

Sample input:
2
5
1 2 3 4 5
1
10

Sample Output:
Case 1: 9
Case 2: 10
"""

"""
We can either choose the judge at our current index i plus what was best for the judge 2 steps behind (i-2) or we are
going to choose the best at index i-1. That can be expressed as points[i] = max(points[i-2] + judge[i], points[i-1]).

Final complexity: O(N)
"""

# Bottom - Up
t = int(input())
for k in range(t):
    n = int(input())
    judges = list(map(int, input().split()))
    points = [0] * n
    if n == 1:
        print(f"Case {k+1}: {judges[0]}")
    elif n == 2:
        print(f"Case {k+1}: {max(judges[0], judges[1])}")
    else:
        points[0] = judges[0]
        points[1] = max(judges[0], judges[1])
        for i in range(2, n):
            points[i] = max(points[i-2] + judges[i], points[i-1])

        print(f"Case {k+1}: {points[-1]}")

# Top - Down
import sys
sys.setrecursionlimit(10 ** 6)


def solve(index):
    if index == 0:
        return judges[0]

    if index == 1:
        return max(judges[0], judges[1])

    if points[index] != -1:
        return points[index]

    points[index] = max(solve(index-2) + judges[index], solve(index-1))
    return points[index]


t = int(input())
for k in range(t):
    n = int(input())
    judges = list(map(int, input().split()))
    points = [-1] * n
    print(f"Case {k+1}: {solve(n-1)}")
