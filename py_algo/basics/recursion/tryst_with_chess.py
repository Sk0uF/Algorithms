"""
Codemonk link: https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/practice-problems/algorithm/a-tryst-with-chess/

You are given a 10X10 chessboard with a knight on coordinate (I,J). You have to find the number of blocks on the
chessboard that the knight can be at in exactly N moves. For the chessboard (1, 1) is the top left cornet and (1, 10) is
the top right corner. (10, 10) is the bottom right corner.

Input - Output:
Input will consist of three space separated integers I, J, N.
Print a single integer denoting the number of blocks on the chessboard
that the knight can be at in exactly N moves.

Sample input:
3 3 1

Sample Output:
8
"""

"""
The problem itself is not difficult. It is just that recursion as an idea is "not that easy to digest". If a knight is 
out of bounds, don't count that as a move, otherwise, if we have already made N moves and we haven't visited the same
square a again, count that square. The knight can move with a very specific manner at 8 different squares each time.

Final complexity: Undetermined
"""


def knight_movement(i, j, n):
    # If knight is out of bounds don't count it.
    if i < 0 or i >= 10 or j < 0 or j >= 10 or n < 0:
        return 0
    # If the knight is in the bounds and haven't visited the square
    # then count it.
    if n == 0 and visited[i][j] == 0:
        visited[i][j] = 1
        return 1
    count = 0
    # Those are the possible 8 different squares the knight can move.
    count += knight_movement(i+2, j+1, n-1)
    count += knight_movement(i-2, j+1, n-1)
    count += knight_movement(i+2, j-1, n-1)
    count += knight_movement(i-2, j-1, n-1)
    count += knight_movement(i+1, j+2, n-1)
    count += knight_movement(i-1, j+2, n-1)
    count += knight_movement(i+1, j-2, n-1)
    count += knight_movement(i-1, j-2, n-1)
    return count


i, j, n = map(int, input().rstrip().split())
visited = [[0] * 10 for _ in range(10)]
print(knight_movement(i-1, j-1, n))
