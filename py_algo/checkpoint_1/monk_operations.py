"""
Monk created a NxM array and defined 4 types of operations. 1) Add v1 to all elements of a row. 2) Update all elements
of a row to v2. 3) Add v3 to all elements of a columns. 4) Update all elements of a column to v4. At any cell of the
array, only 1 operation can be performed. Any operation can be performed any number of times. Monk wants us to find the
summation of the elements of all cells of the array. We must always get the absolute value of the element of the cell.
But we have to be careful because this summation must be the biggest possible.


Input - Output:
First line contains N and M.
The next N lines contain M integers where the jth integer
in the ith line denotes A[i][j].
The last line contains v1, v2, v3 and v4.

Constraints:
1 <= N <= 1000, 1 <= M <= 1000
-10^9 <= A[i][j] <= 10^9
-10^9 <= v1, v2, v3, v4 <= 10^9

Sample input:
2 2
-5 8
6 -9
-2 5 -1 6

Sample Output:
29
"""

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

v1, v2, v3, v4 = map(int, input().split())
