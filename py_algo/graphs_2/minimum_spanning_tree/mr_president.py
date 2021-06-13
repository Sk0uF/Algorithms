def balance(disjoint_set, i):
    if disjoint_set[i] != i:
        disjoint_set[i] = balance(disjoint_set, disjoint_set[i])
    return disjoint_set[i]


def kruskal(graph):
    disjoint_set = [i for i in range(n)]
    sizes = [1] * n
    priority_array = []
    total = 0
    count = 0
    for i in range(m):
        root_a = balance(disjoint_set, graph[i][1]-1)
        root_b = balance(disjoint_set, graph[i][2]-1)

        if root_a != root_b:
            if sizes[root_a] <= sizes[root_b]:
                sizes[root_b] += sizes[root_a]
                disjoint_set[root_a] = root_b
            else:
                sizes[root_a] += sizes[root_a]
                disjoint_set[root_b] = root_a

            total += graph[i][0]
            priority_array.append(graph[i][0])

    for i in range(len(priority_array)-1, -1, -1):
        if total > k:
            count += 1
            total = total - priority_array[i] + 1

    if total > k:
        return -1

    current = balance(disjoint_set, 0)
    for i in range(1, len(disjoint_set)):
        temp = balance(disjoint_set, i)
        if temp != current:
            return -1
        current = temp

    return count


n, m, k = map(int, input().split())
sorted_graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    sorted_graph.append((c, a, b))

sorted_graph = sorted(sorted_graph, key=lambda x: x[0])
print(kruskal(sorted_graph))
