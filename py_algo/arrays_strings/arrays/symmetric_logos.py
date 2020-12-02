"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/roy-and-symmetric-logos-1/

Roy likes Symmetric Logos. How to check whether a logo is symmetric? Align the center of logo with the origin of
Cartesian plane. Now if the colored pixels of the logo are symmetric about both X-axis and Y-axis, then the logo is
symmetric. You are given a binary matrix of size N x N which represents the pixels of a logo. 1 indicates that the pixel
is colored and 0 indicates no color.

Input - Output:
The first line contains the number of test cases.
First line of each test case contains the N - size of matrix.
Next N lines contains binary strings of length N.
Print YES or NO in a new line for each test case

Sample input:
5
2
11
11
4
0101
0110
0110
0101
4
1001
0000
0000
1001
5
01110
01010
10001
01010
01110
5
00100
01010
10001
01010
01110

Sample Output:
YES
NO
YES
YES
NO
"""

"""
This can be solved with a naive approach. Just scan the array and find if the symmetric position in the array is equal
to the current position. If we are at position (i, j) the symmetric y position is the (n-i-1, j) and the symmetric x
position is the (i, n-j-1).

O(N^2) for the nested "for" statements. The input lines constraint is insignificant.

Final complexity: O(N)
"""

inp_len = int(input())

for _ in range(inp_len):
    n = int(input())
    logo = []
    for _ in range(n):
        logo.append(input())

    is_symmetric = True
    for i in range(0, n):
        for j in range(0, n):
            if logo[i][j] != logo[n-i-1][j] or logo[i][j] != logo[i][n-j-1]:
                is_symmetric = False

    if is_symmetric:
        print("YES")
    else:
        print("NO")
