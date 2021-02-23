"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/infinity-array-715a233b/

You are given a 1000x1000 array. In this array, some portions represent agricultural fields. A landlord gave these
fields but he made a mistake and there were overlapping fields. Because he sold these fields, he now needs to return the
money for every overlapping field. Find the total amount of money he needs to return.


Input - Output:
The first line of the input contains an integer N,
denoting the total number of land pieces he had distributed.
Next N line contains the 5 space separated integers (X1, Y1),
(X2, Y2) to represent a rectangular piece of land, and cost per unit area C.
(X1, Y1) and (X2, Y2) are the locations of first and last square block on the
diagonal of the rectangular region.
Print the total amount he has to return to farmers to solve the conflict.

Sample input:
3
1 4 4 6 1
4 3 6 6 2
2 2 5 4 3

Sample Output:
35
"""

"""
Since we know the cost of each cell of each fields, we can create a helper array with dimensions 1000x1000 in which we 
will compute the cost cell by cell. For example, if the first field has x = (1, 4) and y = (4, 6), with a cost of 1 per
cell, the array will have all its corresponding cells equal to the cost, which in this case is 1. Then for each next
field, if the value of the array in the specific cell is not 0, this means that there is an overlap, thus, we add the 
extra new cost and multiply by -1, to indicate an overlap. Then, if there is another overlap with some other field, we 
simply add the negative value of the new cost. When we finish this procedure, we simply add all the negative values and
by multiplying with -1 we have the total cost.

Most of the constraints are insignificant, but lets suppose that they aren't.
We have O(N) for the input fields multiplied by O(X*Y) for the nested "for" statements.
Then we have O(X*Y) for the last nested "for" statements. 

Final complexity: O(N*2*X*Y)
"""


def rectangles():
    try:
        n = int(input())
    except:
        return 0

    costs = [[0] * 1001 for _ in range(1001)]
    min_x = min_y = float("inf")
    max_x = max_y = float("-inf")

    for _ in range(n):
        x1, y1, x2, y2, cost = map(int, input().rstrip().split())
        # By finding the min and max X and Y values we can reduce
        # the complexity to O(N*X*Y).
        min_x = min(min_x, x1)
        min_y = min(min_y, y1)
        max_x = max(max_x, x2)
        max_y = max(max_y, y2)

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if costs[i][j] == 0:
                    costs[i][j] += cost
                elif costs[i][j] > 0:
                    costs[i][j] = (-1) * (costs[i][j] + cost)
                else:
                    costs[i][j] = costs[i][j] - cost

    total_cost = 0
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            if costs[i][j] < 0:
                total_cost += costs[i][j]

    return -total_cost


print(rectangles())
