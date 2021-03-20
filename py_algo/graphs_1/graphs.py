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
