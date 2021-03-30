# 4
# 5
# 1 2
# 2 4
# 3 1
# 3 4
# 4 2

# Connected E >= N-1, without cycles E <= N-1, that's a tree E = N-1.

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
    and if we do we ignore the weights.
    """
    start = 0
    end = 1
    queue = [-1] * len(graph)
    queue[0] = begin
    visited = [False] * (len(graph)+1)
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
