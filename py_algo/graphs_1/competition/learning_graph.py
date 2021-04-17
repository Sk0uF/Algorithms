"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/monk-learning-graph-3-29310db5/

Monk once went to the graph city to learn graphs, and meets an undirected graph having N nodes, where each node has
value val[i] where 1 <= i <= N. Each node of the graph is very curious and wants to know something about the nodes which
are directly connected to the current node. For each node, if we sort the nodes (according to their values), which are
directly connected to it, in descending order (in case of equal values, sort it according to their indices in ascending
order), then what will be the number of the node at kt position, if positions are given starting from 1.

Input - Output:
The first line will consist of 3 space separated integers N, M, k
denoting the number of nodes, number of edges and value of k respectively.
In next line, there will be N space separated integers denoting the value of ith node.
In next M lines, each line contains 2 integers X and Y, representing an edge between X and Y.
Print N lines, where ith line contains the required node for the ith node. If there is no such node, print -1.

Sample input:
3 3 2
2 4 3
1 3
1 2
2 3

Sample Output:
3
1
1
"""

"""
We create the graph by using an adjacency list and after that we first sort the nodes in descending order and then based
on their values. By doing that we can directly know the kth node.

Final complexity: O(NODES*(EDGESlogEDGES+EDGESlogEDGES)) => O(N*ElogE)
"""

n, m, k = map(int, input().split())
values = list(map(int, input().split()))
graph = [[-1] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    if graph[x-1][0] == -1:
        graph[x-1][0] = y
    else:
        graph[x-1].append(y)

    if graph[y-1][0] == -1:
        graph[y-1][0] = x
    else:
        graph[y-1].append(x)

for i in range(n):
    current = graph[i]
    if current[0] == -1:
        print(-1)
    else:
        current = sorted(current, reverse=True)
        connected_sorted = sorted(current, key=lambda node: values[node-1], reverse=True)
        print(connected_sorted[k-1])
