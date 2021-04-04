import sys
from sys import stdin, stdout
sys.setrecursionlimit(10**9)


# Pycharm has some problems with recursion even with the limit
# set to the maximum.
def dfs_rec(graph, begin, visited, group, connected):
    visited.add(begin)
    group[begin-1] = connected
    for i in range(len(graph[begin-1])):
        if graph[begin-1][i] == -1:
            continue
        if graph[begin-1][i] not in visited:
            dfs_rec(graph, graph[begin-1][i], visited, group, connected)


def dfs_iter(graph, begin, visited, group, connected):
    stack = [begin]
    visited.add(begin)
    while stack:
        current = stack.pop()
        group[current-1] = connected
        for i in range(len(graph[current-1])):
            if graph[current-1][i] not in visited:
                stack.append(graph[current-1][i])
                visited.add(graph[current-1][i])


inp_len = int(stdin.readline())
for _ in range(inp_len):
    n, k = map(int, stdin.readline().split())
    adj_list = [[-1] for _ in range(n)]
    ineq_array = []
    for _ in range(k):
        x, eq, y = stdin.readline().split()
        x = int(x)
        y = int(y)
        if eq == "=":
            if adj_list[x-1][0] == -1:
                adj_list[x-1][0] = y
            else:
                adj_list[x-1].append(y)
            if adj_list[y-1][0] == -1:
                adj_list[y-1][0] = x
            else:
                adj_list[y-1].append(x)
        else:
            ineq_array.append((x, y))

    group = [-1] * n
    connected = 0
    visited = set()
    for i in range(n):
        if i not in visited:
            # dfs_rec(adj_list, i+1, visited, group, connected)
            dfs_iter(adj_list, i+1, visited, group, connected)
            connected += 1

    ans = "YES\n"
    for pair in ineq_array:
        if group[pair[0]-1] == group[pair[1]-1]:
            ans = "NO\n"
            break

    stdout.write(ans)
