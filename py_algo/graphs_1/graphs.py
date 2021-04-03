"""
Graphs part 1

- A connected graph has EDGES >= NODES - 1 and a graph without cycles has EDGES <= NODES - 1. That's also called a tree.
- Based on handshaking lemma, the sum of the degrees of all the VERTICES (or else NODES) is equal to 2*EDGES.
- We represent a graph with an ADJACENCY LIST or an ADJACENCY MATRIX. The former is much better than the latter.
- There was no need to represent a binary tree with an ADJACENCY LIST because we could simply do it with a simple class
  containing only the pointers to the children.
"""

# 7
# 9
# 1 2
# 1 3
# 2 5
# 3 4
# 4 6
# 4 7
# 6 7
# 5 3
# 7 4

# Adjacency List
# If we have a third variable for the weight then we simply
# add a tuple or a  list of (m, weight) instead of just the edge.
nodes = int(input())
edges = int(input())
adjacency_list = [[-1]] * nodes
for i in range(edges):
    n, m = map(int, input().split())
    if adjacency_list[n-1][0] == -1:
        adjacency_list[n-1] = [m]
    else:
        adjacency_list[n-1].append(m)

print(adjacency_list)

# Adjacency Martix
nodes = int(input())
edges = int(input())
adjacency_matrix = [[0] * edges for _ in range(nodes)]
for i in range(edges):
    n, m = map(int, input().split())
    adjacency_matrix[n-1][m-1] = 1

print(adjacency_matrix)


def bfs(graph, begin):
    """
    Breadth First Search
    Complexity: O(V+Q) => O(V+2*E) => O(V+E)

    Where V are the vertices and Q the sum of the degrees of all nodes.
    For undirected graphs. It can obviously work with minor adjustments
    for directed graphs as well. We don't use BFS for weighted graphs
    and if we do we ignore the weights. For unweighted graphs bfs will
    produce the shortest distance (minimum amount of edges we have to
    cross to get to the desired node) between the starting and the desired
    node.
    """
    start = 0
    end = 1
    queue = [-1] * len(graph)
    queue[0] = begin
    visited = [False] * (len(graph)+1)  # We can also use a set.
    visited[begin] = True
    while start != end:
        current = queue[start]
        queue[start] = -1
        start += 1
        print("Node: " + str(current))
        for i in range(len(graph[current-1])):
            if not visited[graph[current-1][i]]:
                queue[end] = graph[current-1][i]
                visited[graph[current-1][i]] = True
                end += 1


bfs(adjacency_list, 1)


def bfs_deque(graph, begin):
    from collections import deque
    """
    Breadth First Search (with the usage of the deque)
    Complexity: O(V+Q) => O(V+2*E) => O(V+E)

    Where V are the vertices and Q the sum of the degrees of all nodes.
    For undirected graphs. It can obviously work with minor adjustments
    for directed graphs as well. We don't use BFS for weighted graphs
    and if we do we ignore the weights. For unweighted graphs bfs will
    produce the shortest distance (minimum amount of edges we have to 
    cross to get to the desired node) between the starting and the desired
    node. 
    """
    queue = deque()
    queue.append(begin)
    visited = [False] * (len(graph)+1)  # We can also use a set.
    visited[begin] = True
    while queue:
        current = queue.popleft()
        print("Node: " + str(current))
        for i in range(len(graph[current-1])):
            if not visited[graph[current-1][i]]:
                queue.append(graph[current-1][i])
                visited[graph[current-1][i]] = True


print()
bfs_deque(adjacency_list, 1)


def dfs_iter(graph, begin):
    """
    Depth First Search - Iterative
    Complexity: O(V+Q) => O(V+2*E) => O(V+E)

    Where V are the vertices and Q the sum of the degrees of all nodes.
    For undirected graphs. It can obviously work with minor adjustments
    for directed graphs as well.
    """
    stack = [begin]
    visited = [False] * (len(graph)+1)  # We can also use a set.
    visited[begin] = True
    while stack:
        current = stack.pop()
        print("Node: " + str(current))
        for i in range(len(graph[current-1])):
            if not visited[graph[current-1][i]]:
                stack.append(graph[current-1][i])
                visited[graph[current-1][i]] = True


print()
dfs_iter(adjacency_list, 1)


def dfs_rec(graph, begin, visited):
    """
    Depth First Search - Recursive
    Complexity: O(V+Q) => O(V+2*E) => O(V+E)

    Where V are the vertices and Q the sum of the degrees of all nodes.
    For undirected graphs. It can obviously work with minor adjustments
    for directed graphs as well.
    """
    print("Node: " + str(begin))
    visited[begin] = True  # We can also use a set.
    for i in range(len(graph[begin-1])):
        if not visited[graph[begin-1][i]]:
            dfs_rec(graph, graph[begin-1][i], visited)


print()
dfs_rec(adjacency_list, 1, [False] * (len(adjacency_list)+1))
