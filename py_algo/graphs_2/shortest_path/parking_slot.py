import heapq


def dijkstra(graph):
    distances = [float("inf")] * len(graph)
    visited = [False] * len(graph)
    distances[0] = 0
    pq = []
    heapq.heappush(pq, (0, 0))

    while pq:
        current = heapq.heappop(pq)
        current = current[1]
        if visited[current]:
            continue
        visited[current] = True

        for i in range(len(graph[current])):
            if graph[current][i] == -1:
                break
            next = graph[current][i][0]
            weight = graph[current][i][1]
            if distances[next] > distances[current] + weight:
                distances[next] = distances[current] + weight
                heapq.heappush(pq, (distances[next], next))

    return distances


n, m, f = map(int, input().split())
slots = list(map(int, input().split()))
graph = [[-1] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    if graph[u-1][0] == -1:
        graph[u-1][0] = (v-1, w)
    else:
        graph[u-1].append((v-1, w))

    if graph[v-1][0] == -1:
        graph[v-1][0] = (u-1, w)
    else:
        graph[v-1].append((u-1, w))




k = int(input())
distances = dijkstra(graph)

distances = [(distances[i], i) for i in range(len(distances))]
distances = sorted(distances, key=lambda x: x[0])

counter = 0
ans = []
while k > 0:
    if counter >= len(distances):
        ans.append(-1)
        k -= 1
        counter += 1
        continue
    total = distances[counter][0] + f
    ans.append(total)
    slots[distances[counter][1]] -= 1
    if slots[distances[counter][1]] == 0:
        counter += 1
    k -= 1

print(*ans)
