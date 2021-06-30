"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/monk-and-hops-357a2ca6/

Monk has a connected graph with N nodes and M weighted undirected edges.He gave a task to you on the same. You need to
travel from node 1 to node N using a path with the minimum cost. If many such paths with minimum cost exists you need
the one with the minimum hops. Path is a sequence of vertices u1, u2, ..., uk  such that:
1) All ui are distinct.
2) ui and ui+1 are connected by an edge.
The cost of a path is the sum of weight of the edges. The hops in a path are the number of pairs of adjacent edges in
the path such that the weight of one edge is even and the other is odd.
NOTE: The graph may contain multiple edges between same pair of nodes. It does not contain self loops.

Input - Output:
First line contains the two integers N and M, denoting the number of nodes and the number of edges in the graph.
M lines follow each containing three integers U, V and W, denoting that there exists an edge between nodes U and V with
weight W.
Output, on a single line, two space separated integers, the cost and the number of hops of the path.

Sample input:
5 5
1 2 4
2 4 6
1 3 5
3 4 5
4 5 5

Sample Output:
15 0
"""

"""
We solve the problem by using dijkstra's algorithm with a simple alternation. What we have to do is keep track of the
previous weight of the edge we used to reach a node and more importantly keep track if that weight was even or odd. That
way, we can find the new path weight to that vertex as well as the number of hops. We must not use a visited array 
because there is the case in which 2 paths to a vertex have the same weight and hops but the edge we used to visit
them differs which is key to finding the next hops. That makes the complexity worse though. 

Final complexity: O(E*logE) => O(E*logV) because E <= (V*V-1)/2 
                  and thus O(E*logE) becomes O(E*logV^2) which is O(2*E*logV) 
"""


import heapq
from sys import stdin


def decide(a, b):
    if a[0] and b[0]:
        return 0
    if a[1] and b[1]:
        return 0
    return 1


def dijkstra(graph):
    distances = [float("inf")] * len(graph)
    hops = [float("inf")] * len(graph)
    distances[0] = 0
    hops[0] = 0
    priority = []

    for vertex, weight in graph[0]:
        parent = [0, 0]
        parent[weight % 2] = 1
        distances[vertex] = weight
        hops[vertex] = 0
        heapq.heappush(priority, (weight, vertex, parent))

    while priority:
        path_weight, vertex, parent = heapq.heappop(priority)
        for new_vertex, weight in graph[vertex]:
            new_parent = [0, 0]
            new_parent[weight % 2] = 1
            if path_weight + weight < distances[new_vertex]:
                distances[new_vertex] = path_weight + weight
                hops[new_vertex] = hops[vertex] + decide(parent, new_parent)
                heapq.heappush(priority, (distances[new_vertex], new_vertex, new_parent))
            elif path_weight + weight == distances[new_vertex]:
                hop_value = hops[vertex] + decide(parent, new_parent)
                if hop_value <= hops[new_vertex]:
                    hops[new_vertex] = hop_value
                    heapq.heappush(priority, (distances[new_vertex], new_vertex, new_parent))
    return distances, hops


n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, stdin.readline().split())
    graph[u-1].append((v-1, w))
    graph[v-1].append((u-1, w))

ans1, ans2 = dijkstra(graph)
print(ans1[-1], ans2[-1])
