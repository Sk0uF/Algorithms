"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/monk-and-inversions-arrays-strings-e5aaa427/

Monk's best friend Micro, who happen to be an awesome programmer, got him an integer matrix M of size N X N for his
birthday. Monk is taking coding classes from Micro. They have just completed array inversions and Monk was successful in
writing a program to count the number of inversions in an array. Now, Micro has asked Monk to find out the number of
inversion in the matrix M. Number of inversions, in a matrix is defined as the number of unordered pairs of cells
{(i, j), (p, q)} such that M[i][j] > M[p][q] & i <= p & j <= q. Monk is facing a little trouble with this task and since
you did not got him any birthday gift, you need to help him with this task.

Input - Output:
The first line denotes the number of test cases.
First line of each test case consists of one integer denoting N.
Following N lines consists of N space separated integers denoting the matrix M.
Print the answer to each test case in a new line.

Sample input:
2
3
1 2 3
4 5 6
7 8 9
2
4 3
1 4

Sample Output:
0
2
"""

"""
Begin from every cell of the array and find how many unordered cells will arise. 

For every cell we scan the whole array. O(N^2) for the nested "for" statements.
The above statements are nested inside the while statement, which will go through
the whole array, meaning that we have to multiply with O(N).

Final complexity: O(N*N^2) = O(N^3)
"""

inp_len = int(input())

for _ in range(inp_len):
    n = int(input())
    m = list()

    for _ in range(n):
        m.append([i for i in map(int, input().rstrip().split())])
        # m.append(list(map(int, input().rstrip().split())))

    count_i = 0
    count_j = 0
    unpaired = 0
    while True:
        if count_i == n:
            break
        for i in range(count_i, n):
            for j in range(count_j, n):
                if m[i][j] < m[count_i][count_j]:
                    unpaired += 1

        if count_j == (n-1):
            count_j = 0
            count_i += 1
        else:
            count_j += 1

    print(unpaired)
