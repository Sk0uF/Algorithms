"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/monk-and-rotation-3-bcf1aefe/

Monk loves to preform different operations on arrays, and so being the principal of Hackerearth School, he assigned a
task to his new student Mishki. Mishki will be provided with an integer array A of size N and an integer K , where she
needs to rotate the array in the right direction by K steps and then print the resultant array. As she is new to the
school, please help her to complete the task.

Input - Output:
The first line denotes the number of test cases.
For each test case:
1) The first line consists of two integers N and K, N being the number of
elements in the array and K denotes the number of steps of rotation.
2) The next line consists of N space separated integers , denoting the elements of the array A.
Print the required array.

Sample input:
1
5 2
1 2 3 4 5

Sample Output:
4 5 1 2 3
"""

"""
The problem is straight forward. Python is very easy when we need to manage arrays. 

The complexity comes from printing the array, meaning it depends on the input.

Final complexity: O(N)
"""

inp_len = int(input())

for _ in range(inp_len):
    n, k = map(int, input().rstrip().split())
    a = list(map(int, input().rstrip().split()))

    rotate = k % n
    print(*a[n-rotate:], *a[:n-rotate])
