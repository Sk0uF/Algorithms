import sys
from sys import stdin, stdout
import threading

threading.stack_size(200000000)
sys.setrecursionlimit(10**6)


def dfs(graph, begin, visited, bananas):
    amount = bananas[begin-1]
    visited.add(begin)
    for node in graph[begin-1]:
        if node == -1:
            continue
        if node not in visited:
            amount += dfs(graph, node, visited, bananas)
    return amount


def main():
    inp_len = int(stdin.readline())
    for _ in range(inp_len):
        n, m = map(int, stdin.readline().split())
        graph = [[-1] for _ in range(n)]
        for _ in range(m):
            x, y = map(int, stdin.readline().split())
            if graph[x-1][0] == -1:
                graph[x-1][0] = y
            else:
                graph[x-1].append(y)

            if graph[y-1][0] == -1:
                graph[y-1][0] = x
            else:
                graph[y-1].append(x)

        bananas = list(map(int, stdin.readline().split()))
        visited = set()

        max_bananas = -1
        for i in range(len(graph)):
            if i+1 not in visited:
                max_bananas = max(dfs(graph, i+1, visited, bananas), max_bananas)

        stdout.write(str(max_bananas) + "\n")


thread = threading.Thread(target=main)
thread.start()
