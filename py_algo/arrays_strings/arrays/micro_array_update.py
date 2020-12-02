"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/micro-and-array-update/

Micro purchased an array A having N integer values. After playing it for a while, he got bored of it and decided to
update value of its element. In one second he can increase value of each array element by 1. He wants each array
element's value to become greater than or equal to K. Please help Micro to find out the minimum amount of time it will
take, for him to do so.

Input - Output:
First line contains the number of test cases.
First line of each test case consists of two space separated integers denoting N and K.
Second line of each test case consists of N space separated integers denoting the array A.
For each test case, print the minimum time in which all the array elements will become greater
than or equal to K. Print a new line after each test case.

Sample input:
2
3 4
1 2 5
3 2
2 5 5

Sample Output:
3
0
"""

"""
The problem is straight forward. All we need to do is find how many steps the minimum value of the array needs in order
to reach the desired value. The rest values of the array will always be grater or equal to the desired value in this 
number of steps.

O(N) to find the minimum value of the array. The input lines constraint is insignificant.

Final complexity: O(N)
"""

inp_len = int(input())

for _ in range(inp_len):
    n, k = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split()))
    temp_min = min(arr)
    if k > temp_min:
        print(k - temp_min)
    else:
        print(0)
