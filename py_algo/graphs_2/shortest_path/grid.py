from collections import deque


def bfs(graph, s0, s1, distances):
    visited = set()
    queue = deque()
    queue.append((s0-1, s1-1))
    visited.add((s0-1, s1-1))
    while queue:
        current = queue.popleft()
        if current[0]+1 < n and graph[current[0]+1][current[1]] != "*" and (current[0]+1, current[1]) not in visited:
            visited.add((current[0]+1, current[1]))
            queue.append((current[0]+1, current[1]))
            distances[current[0]+1][current[1]] = distances[current[0]][current[1]] + 1

        if current[0]-1 >= 0 and graph[current[0]-1][current[1]] != "*" and (current[0]-1, current[1]) not in visited:
            visited.add((current[0]-1, current[1]))
            queue.append((current[0]-1, current[1]))
            distances[current[0]-1][current[1]] += distances[current[0]][current[1]] + 1

        if current[1]+1 < m and graph[current[0]][current[1]+1] != "*" and (current[0], current[1]+1) not in visited:
            visited.add((current[0], current[1]+1))
            queue.append((current[0], current[1]+1))
            distances[current[0]][current[1]+1] += distances[current[0]][current[1]] + 1

        if current[1]-1 >= 0 and graph[current[0]][current[1]-1] != "*" and (current[0], current[1]-1) not in visited:
            visited.add((current[0], current[1]-1))
            queue.append((current[0], current[1]-1))
            distances[current[0]][current[1]-1] += distances[current[0]][current[1]] + 1

    return distances


n, m, q = map(int, input().split())
graph = []
distances = []
for _ in range(n):
    temp = []
    for _ in range(m):
        temp.append(0)
    distances.append(temp)

for _ in range(n):
    graph.append(input())

s0, s1 = map(int, input().split())
distances = bfs(graph, s0, s1, distances)
for _ in range(q):
    d0, d1 = map(int, input().split())
    if s0 == d0 and s1 == d1:
        print(0)
    elif distances[d0-1][d1-1] == 0:
        print(-1)
    else:
        print(distances[d0 - 1][d1 - 1])
