"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/trees/binary-and-nary-trees/practice-problems/algorithm/mancunian-and-colored-tree/

After a hectic week at work, Mancunian and Liverbird decide to go on a fun weekend camping trip. As they were passing
through a forest, they stumbled upon a unique tree of N nodes. Vertices are numbered from 1 to N. Each node of the tree
is assigned a color (out of C possible colors). Being bored, they decide to work together (for a change) and test their
reasoning skills. The tree is rooted at vertex 1. For each node, they want to find its closest ancestor having the same
color.

Input - Output:
The first line contains two integers N and C denoting the number of vertices
in the tree and the number of possible colors.
The second line contains N-1 integers. The ith integer denotes the parent of the (i+1)th vertex.
The third line contains N integers, denoting the colors of the vertices.
Each color lies between 1 and C inclusive.
Print N space-separated integers. The ith integer is the vertex number of lowest
ancestor of the ith node which has the same color. If there is no such ancestor, print -1 for that node.

Sample input:
5 4
1 1 3 3
1 4 2 1 2

Sample Output:
-1 -1 -1 1 3
"""

"""
Even though we have to deal with a tree, the input of the problem makes it easy to solve it with a simple array. For
every node of N nodes, its ancestor can be found in the array nodes[i-1] and its color is at the index nodes[i-1] - 1 of
the colors array. By following that logic we can keep going to every parent from each node until we reach the root. If
we find an ancestor with same color we print the ancestor, otherwise we print -1.

The complexity is O(N^2) because in case of having a tree with just right of left children
and without any of them having the same color we would have to do 1+2+3+4+...+N operations
from every node to the root. That is N*(N+1)/2 operations.

Final complexity: O(N^2)
"""

n, c = map(int, input().split())
nodes = list(map(int, input().split()))
colors = list(map(int, input().split()))

ans = ["-1"]
for i in range(1, n):
    j = nodes[i-1] - 1
    color = colors[i]
    while j > 0 and colors[j] != color:
        j = nodes[j-1] - 1
    if j > - 1 and colors[j] == color:
        ans.append(str(j+1))
    else:
        ans.append("-1")
    print(i, ans)

print(' '.join(ans))
