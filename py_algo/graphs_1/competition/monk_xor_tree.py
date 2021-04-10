# https://www.hackerearth.com/problem/algorithm/monk-and-xor-tree-a190a1ed/
import sys
from threading import Thread, stack_size

sys.setrecursionlimit(10 ** 6)
stack_size(70000000)


def dfs(graph, begin, values, k, ans, xor, auxiliary):
    xor ^= values[begin - 1]
    ans += auxiliary[xor ^ k]
    auxiliary[xor] += 1
    print(begin, values[begin-1], xor, ans)
    for node in graph[begin - 1]:
        if node == -1:
            break
        ans = dfs(graph, node, values, k, ans, xor, auxiliary)

    auxiliary[xor] -= 1
    return ans


def main():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    graph_relations = list(map(int, input().split()))

    graph = [[-1] for _ in range(n)]
    for i in range(len(graph_relations)):
        if graph[graph_relations[i] - 1][0] == -1:
            graph[graph_relations[i] - 1][0] = i + 2
        else:
            graph[graph_relations[i] - 1].append(i + 2)

    ans = 0
    xor = 0
    auxiliary = [0] * 10000000
    auxiliary[0] = 1
    ans = dfs(graph, 1, values, k, ans, xor, auxiliary)
    # print(ans)


thread = Thread(target=main)
thread.start()
