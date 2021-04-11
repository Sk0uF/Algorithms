# https://www.hackerearth.com/problem/algorithm/little-monk-and-edge-count-61365ba4/
import sys
from threading import Thread, stack_size

sys.setrecursionlimit(10 ** 6)
stack_size(70000000)


def main():
    def dfs(graph, begin, visited):
        visited.add(begin)
        current = graph[begin - 1]
        count = 1
        for node in current:
            if node == -1:
                continue
            if node not in visited:
                count += dfs(graph, node, visited)
        count_paths[begin - 1] = count
        return count

    n, q = map(int, input().split())
    graph = [[-1] for _ in range(n)]
    pairs = []
    for _ in range(n-1):
        x, y = map(int, input().split())
        if graph[x-1][0] == -1:
            graph[x-1][0] = y
        else:
            graph[x-1].append(y)
        if graph[y-1][0] == -1:
            graph[y-1][0] = x
        else:
            graph[y-1].append(x)

        pairs.append((x, y))

    count_paths = [0] * n
    total_paths = (n * (n-1))//2
    visited = set()
    count = dfs(graph, 1, visited)

    for _ in range(q):
        edge = int(input())
        a = pairs[edge-1][0]
        b = pairs[edge-1][1]
        ans = 0
        if count_paths[a-1] > count_paths[b-1]:
            a = n - count_paths[b-1]
            b = count_paths[b-1]
            ans = total_paths - a*(a-1)//2 - b*(b-1)//2
        else:
            b = n - count_paths[a-1]
            a = count_paths[a-1]
            ans = total_paths - a*(a-1)//2 - b*(b-1)//2

        print(ans)


thread = Thread(target=main)
thread.start()
