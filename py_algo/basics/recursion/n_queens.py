"""
Codemonk link: https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/practice-problems/algorithm/n-queensrecursion-tutorial/description/

Given a chess board having NxN cells, you need to place N queens on the board in such a way that no queen attacks any
other queen.

Input - Output:
The only line of input consists of a single integer denoting N.
If it is possible to place all the N queens in such a way that no queen
attacks another queen, then print N lines having N integers. The integer
inline and  column will denote the cell  of the board and should be 1 if
a queen is placed at  otherwise 0. If there are more than way of placing
queens print any of them. If it is not possible to place all N queens in
the desired way, then print "Not possible" (without quotes).

Sample input:
4

Sample Output:
0 1 0 0
0 0 0 1
1 0 0 0
0 0 1 0
"""

"""
Solution with recursion and backtracking. We start placing queens in each row. We check whether or not there is another
queen places in the same row, column or diagonal. If in some step, a queen cannot be placed, we go one step before, in
the placement of the previous queen and we try to find a different solution. This process continues until we find a way
or not to place all the queens.

Final complexity: Undetermined
"""


def find_cell(placed, queens, z):
    if queens == 0:
        return True
    for i in range(z, z+1):                # We want to place each queen on a different row.
        for j in range(chessboard_len):
            if is_attacked(i, j, placed):  # If the queen cannot be placed, try a different column.
                continue
            # Occupy the specific cell.
            # Call the function for the next queen on the next row.
            placed[i][j] = 1
            if find_cell(placed, queens-1, i+1):
                return True
            # If there wasn't a much, backtrack to another solution for the
            # previous queen.
            placed[i][j] = 0
    return False


def is_attacked(x, y, placed):
    for i in range(chessboard_len):
        if placed[x][i] == 1:
            return True
        if placed[i][y] == 1:
            return True
        for j in range(chessboard_len):
            # We can find queens on the same diagonal
            # if the absolute difference between the (x, y) of a checked cell
            # and the (i, j) of the queen we want to place are equal.
            row = abs(i-x)
            col = abs(j-y)
            if row == col and placed[i][j] == 1:
                return True
    return False


chessboard_len = int(input())
placed = [[0] * chessboard_len for _ in range(chessboard_len)]
solved = find_cell(placed, chessboard_len, 0)

if solved:
    for i in placed:
        print(*i)
else:
    print("Not possible")
