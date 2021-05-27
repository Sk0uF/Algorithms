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
