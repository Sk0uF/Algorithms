def dfs(graph, begin, down):
    down.add(begin)
    for node in graph[begin-1]:
        if node == -1:
            continue
        if node not in down:
            dfs(graph, node, down)


# def dfs_alt(graph, begin, down):
#     n = 1
#     down.add(begin)
#     for node in graph[begin-1]:
#         if node == -1:
#             continue
#         if node not in down:
#             n += dfs(graph, node, down)
#     return n


inp_len = int(input())
for _ in range(inp_len):
    N, F, S = map(int, input().split())
    graph = [[-1] for _ in range(N)]
    for _ in range(F):
        a, b = map(int, input().split())
        if graph[a-1][0] == -1:
            graph[a-1][0] = b
        else:
            graph[a-1].append(b)

    down = set()
    for _ in range(S):
        x = int(input())
        if x not in down:
            # n += dfs_alt(graph, x, down)
            dfs(graph, x, down)

    print(len(down))
    # print(n)
