"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/monk-and-lucky-minimum-3-8e22f1cb/

Monk just purchased an array A having N integers. Monk is very superstitious. He calls the array A Lucky if the
frequency of the minimum element is odd, otherwise he considers it Unlucky. Help Monk in finding out if the array is
Lucky or not.

Input - Output:
First line consists of a single integer T denoting the number of test cases.
First line of each test case consists of a single integer N denoting the size of array A.
Second line of each test case consists of N space separated integers denoting the array A.
For each test case, print "Lucky" (without quotes) if frequency of minimum element is odd,
otherwise print "Unlucky"(without quotes). Print a new line after each test case

Sample input:
2
5
8 8 9 5 9
5
3 3 3 5 3

Sample Output:
Lucky
Unlucky
"""

"""
Straight forward problem.

Final complexity: O(N)
"""

t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))

    count = 0
    num_min = min(array)
    for i in range(n):
        if num_min == array[i]:
            count += 1

    if count % 2 == 0:
        print("Unlucky")
    else:
        print("Lucky")
