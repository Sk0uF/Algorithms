def balance(disjoint_set, i):
    if disjoint_set[i] != i:
        disjoint_set[i] = balance(disjoint_set, disjoint_set[i])
    return disjoint_set[i]


def kruskal(graph, type="first"):
    disjoint_set = [i for i in range(n)]
    sizes = [1] * n
    count = 0
    for i in range(len(graph)):
        root_a = balance(disjoint_set, graph[i][1]-1)
        root_b = balance(disjoint_set, graph[i][2]-1)
        if root_a != root_b:
            if sizes[root_a] <= sizes[root_b]:
                sizes[root_b] += sizes[root_a]
                disjoint_set[root_a] = root_b
            else:
                sizes[root_a] += sizes[root_a]
                disjoint_set[root_b] = root_a

            count += 1

    if type == "first":
        current = balance(disjoint_set, 0)
        for i in range(1, len(disjoint_set)):
            temp = balance(disjoint_set, i)
            if temp != current:
                return -1
            current = temp

    return count


n, m = map(int, input().split())
graph = []
graph1 = []
graph2 = []
for _ in range(m):
    a, b, c = map(int, input().split())
    if c == 3:
        graph.append((c, a, b))
        graph1.append((c, a, b))
        graph2.append((c, a, b))
    elif c == 2:
        graph1.append((c, a, b))
    else:
        graph2.append((c, a, b))

graph1 = sorted(graph1, key=lambda x: x[0], reverse=True)
graph2 = sorted(graph2, key=lambda x: x[0], reverse=True)
men = kruskal(graph1)
women = kruskal(graph2)
general = kruskal(graph, "second")

if men == -1 or women == -1:
    print(-1)
else:
    print(m - ((n-1-general) * 2 + general))
