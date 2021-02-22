"""
Monk created an NxM array and defined 4 types of operations. 1) Add v1 to all elements of a row. 2) Update all elements
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

"""
To solve the problem, we first have to notice that we can either make operations on the rows or on the columns. That
comes from the fact that we can perform only one operation to each cell. If we decide to perform an operation to a row
then directly those cells which are a part of m columns would reach the limit of operations, making them invalid for
column operations. The same holds if we decide to first perform a column operation. Now the problem becomes simpler. We
have 6 cases, 3 if we decide to perform row operations and 3 if we decide to perform column operations. 

1) The sum of the row (taking the absolute value of each cell) is the biggest.
2) m * v2 is bigger than the result of (1).
3) The sum of the row after we add v1 to each cell and then taking the absolute value of the result and finding the sum
   is bigger than the biggest of (1) and (2).

Based on the above cases, we find the biggest value for the row, we do that for every row and we find the overall sum. 
We follow the exact same logic but this time for the column operations, finding the overall sum by columns and we the
final answer is the biggest overall sum from the two.

Final complexity: O(N^2)
"""

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

v1, v2, v3, v4 = map(int, input().split())

rows = [0] * n
columns = [0] * m
rows_amount = [0] * n
columns_amount = [0] * m
for i in range(n):
    for j in range(m):
        rows[i] += abs(a[i][j])
        columns[j] += abs(a[i][j])
        rows_amount[i] += abs(a[i][j] + v1)
        columns_amount[j] += abs(a[i][j] + v3)


overall_sum_1 = 0
temp_sum_v1 = v1
temp_sum_v2 = abs(m*v2)
for i in range(n):
    add = max(temp_sum_v2, rows[i])
    add = max(rows_amount[i], add)
    overall_sum_1 += add

overall_sum_2 = 0
temp_sum_v3 = v3
temp_sum_v4 = abs(n*v4)
for j in range(m):
    add = max(temp_sum_v4, columns[j])
    add = max(columns_amount[j], add)
    overall_sum_2 += add

print(max(overall_sum_1, overall_sum_2))
