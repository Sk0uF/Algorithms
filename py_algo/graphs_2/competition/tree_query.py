"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/tree-query-1645dc27/

You are given a directed acyclic graph G with N nodes and M directed edges. For a directed edge , it is said that this
edge emerges out of node u. We define a sink node as a node in which no edge emerges out of it. Monk has given you the
power to reverse all the edges of the graph together. You want the maximum number of nodes that can be called as sink
node, in the given graph. For this you can either go with the given graph or use Monk's power to reverse all edges of
the graph. Output the maximum sink nodes you can have in the graph.
NOTE:
1) An isolated node is a sink node.
2) Assume no self loops and at most one directed edge from a vertex to another.

Input - Output:
First line contains two integers N and M, denoting the number of nodes and edges in the graph.
Next M lines contain two integers X and Y, denoting that theres a directed edge from node X to Y.
Output a single integer that is the answer to the problem.

Sample input:
4 2
2 3
4 3

Sample Output:
3
"""

"""
The problem is trivial.

Final complexity: O(E)
"""

n, m = map(int, input().split())
a = set()
b = set()
for _ in range(m):
    x, y = map(int, input().split())
    a.add(x)
    b.add(y)

print(max(n-len(a), n-len(b)))
