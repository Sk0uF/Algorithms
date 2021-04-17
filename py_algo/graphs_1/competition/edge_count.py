"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/little-monk-and-edge-count-61365ba4/

You are given an undirected graph of N nodes and N-1 edges. There is a unique path from any node to any other node. For
a given edge e, you need to find the number of pairs (a, b), considering a and b as nodes of graph, such that e lies in
the path between node a and node b.

Input - Output:
The first line contains N, Q denoting the number of nodes and number of queries.
Next N-1 lines contain a, b, denoting there is an edge between a and b.
Next Q lines contain one integer, x, denoting xth edge.
For each query, print the number of pairs of nodes such that xth edge lies in the path between a and b.

Sample input:
5 4
1 2
1 3
2 4
2 5
1
2
3
4

Sample Output:
6
4
4
4
"""

"""
A tree with N nodes has N*(N-1)/2 paths. That means we can subtract all the paths that don't contain the specified edge
and find the answer. Removing an edge from the graph will create 2 trees, one with K and the other with size N-K. We 
perform an one time DFS to find all the nodes beginning from every subtree. We also save all the node pairs from the 
input. After doing that, we find which pair the xth edge disconnects. The one that has the bigger amount of reachable
nodes is the ancestor. Thus, the tree is separated in 2 subtrees, one with the amount of reachable nodes of the node
that has the lower value, lets say k, and the other with n-k, lets call these K, L. The final answer is N*(N-1)/2 -
K*(K-1)/2 - L*(L-1)/2 

Final complexity: O(NODES+EDGES+Q)
"""

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
    print(count_paths)
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
