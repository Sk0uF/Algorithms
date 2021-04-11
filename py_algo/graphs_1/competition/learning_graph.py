# https://www.hackerearth.com/problem/algorithm/monk-learning-graph-3-29310db5/

n, m, k = map(int, input().split())
values = list(map(int, input().split()))
graph = [[-1] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    if graph[x-1][0] == -1:
        graph[x-1][0] = y
    else:
        graph[x-1].append(y)

    if graph[y-1][0] == -1:
        graph[y-1][0] = x
    else:
        graph[y-1].append(x)


for i in range(n):
    current = graph[i]
    if current[0] == -1:
        print(-1)
    else:
        current = sorted(current, reverse=True)
        connected_sorted = sorted(current, key=lambda node: values[node-1], reverse=True)
        print(connected_sorted[k-1])
