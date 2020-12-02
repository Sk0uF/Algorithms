"""
Codemonk link: https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/practice-problems/algorithm/biggest-forest-700592dd/

Imagine the field is a 2D plane. Each cell is either water 'W' or a tree 'T'. A forest is a collection of connected
trees. Two trees are connected if they share a side i.e. if they are adjacent to each other. Your task is, given the
information about the field, to print the size of the largest forest.

Input - Output:
First line contains the size of the matrix N.
The next N lines contain N characters each, either 'W' or 'T'.
Print the size of the biggest forest.

Sample input:
5
TTTWW
TWWTT
TWWTT
TWTTT
WWTTT

Sample Output:
10
"""

"""
For each index of the array we will find the forest. To do that, each time, we try to move in all directions (not 
diagonally), meaning, in 4 different directions. If we visit a tree, from one specific index, we change it to not a
tree, because we can be sure that the same forest will occur when we start for it in another iteration. For each
iteration, we stop when we reach out of the bounds of the array. The biggest forest is the maximum of all the forests.

Final complexity: Undetermined
"""


def find_forest(forest, i, j, inp_len):
    if (i < 0) or (j < 0) or (i >= inp_len) or (j >= inp_len):
        return 0

    count = 0
    if forest[i][j] == "T":
        count += 1
        forest[i][j] = "W"

        # Move in four different directions and count the trees
        count += find_forest(forest, i - 1, j, inp_len)
        count += find_forest(forest, i + 1, j, inp_len)
        count += find_forest(forest, i, j - 1, inp_len)
        count += find_forest(forest, i, j + 1, inp_len)

    return count


inp_len = int(input())
forest = []
for _ in range(inp_len):
    arr = list(i for i in input())
    forest.append(arr)

count = 0

# Find the forest for every index of the array
for i in range(inp_len):
    for j in range(inp_len):
        count = max(count, find_forest(forest, i, j, inp_len))

print(count)
