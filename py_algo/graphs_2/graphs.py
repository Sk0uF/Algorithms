"""
MST Algorithms
"""

# 4 5
# 1 2 7
# 1 4 6
# 4 2 9
# 4 3 8
# 2 3 6


def find_root(array, value):
    """
    Find the root and balance
    Complexity: O(logN)
    """
    if array[value] != value:
        array[value] = find_root(array, array[value])
    return array[value]


def kruskal(array, v, e):
    """
    Kruskal's Algorithm for MST
    Complexity: O(E*INVERSE_ACKERMAN + ElogE)

    We first sort the edges and then we use a disjoint set technique
    to find the MST.
    """
    array = sorted(array, key=lambda val: val[0])
    disjoint_set = [i for i in range(v)]
    sizes = [1] * v
    min_cost = 0
    for i in range(e):
        a = array[i][1]
        b = array[i][2]
        cost = array[i][0]
        root_a = find_root(disjoint_set, a-1)
        root_b = find_root(disjoint_set, b-1)

        if root_a != root_b:
            min_cost += cost
            if sizes[root_a] < sizes[root_b]:
                disjoint_set[root_a] = disjoint_set[root_b]
                sizes[root_b] += sizes[root_a]
            else:
                disjoint_set[root_b] = disjoint_set[root_a]
                sizes[root_a] += sizes[root_b]

    return min_cost


v, e = map(int, input().split())
graph = []
for _ in range(e):
    x, y, w = map(int, input().split())
    graph.append((w, x, y))

print(kruskal(graph, v, e))


def prim():
    """
    Prim's Algorithm for MST

    Works better than Kruskal's only in Dense graphs.
    """
    pass


"""
Shortest Path Algorithms
"""
# 5 5
# 1 2 5
# 1 3 2
# 3 4 1
# 1 4 6
# 3 5 5
import heapq


def dijkstra(graph):
    """
    Dijkstra's Algorithm for Shortest Path
    Complexity: O(V + E*logV)

    We use a min heap as the priority queue.
    """
    visited = [False] * len(graph)
    distances = [float("inf")] * len(graph)
    distances[0] = 0
    priority_queue = []
    heapq.heappush(priority_queue, (0, 0))
    while priority_queue:
        min_vert = heapq.heappop(priority_queue)
        vert = min_vert[1]
        if visited[vert]:
            continue

        visited[vert] = True
        for i in range(len(graph[vert])):
            next_vert = graph[vert][i][0]-1
            next_weight = graph[vert][i][1]
            if distances[vert] + next_weight < distances[next_vert]:
                distances[next_vert] = distances[vert] + next_weight
                heapq.heappush(priority_queue, (distances[next_vert], next_vert))

    return distances


n, m = map(int, input().split())
graph = [[-1] for _ in range(n)]
for _ in range(m):
    a, b, w = map(int, input().split())
    if graph[a-1][0] == -1:
        graph[a-1][0] = (b, w)
    else:
        graph[a-1].append((b, w))

    if graph[b-1][0] == -1:
        graph[b-1][0] = (a, w)
    else:
        graph[b-1].append((a, w))

print(*dijkstra(graph)[1:])


def bellman(graph):
    distances = [float("inf")] * len(graph)
    distances[0] = 0
    for _ in range(len(graph)):
        for i in range(len(graph)):
            if distances[graph[i][0]-1] + graph[i][2] < distances[graph[i][1]-1]:
                distances[graph[i][1]-1] = distances[graph[i][0]-1] + graph[i][2]

    return distances


n, m = map(int, input().split())
graph = []
for _ in range(m):
    a, b, w = map(int, input().split())
    graph.append((a, b, w))

print(*bellman(graph)[1:])


def warshall(graph):
    """
    Warshall's Algorithm for Shortest Path
    Complexity: O(V^3)

    It produces the shortest paths between all the vertices.
    """
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return graph


n, m = map(int, input().split())
graph = []
for i in range(n):
    temp = []
    for j in range(n):
        if j == i:
            temp.append(0)
        else:
            temp.append(float("inf"))
    graph.append(temp)

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a-1][b-1] = w

print(warshall(graph))
