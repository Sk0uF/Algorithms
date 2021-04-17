"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/monk-and-xor-tree-a190a1ed/

Given a Tree T consisting of N nodes rooted at node 1, each node has a value, where the value of the ith node is A[i].
In addition to the tree, you have also been given an integer K. Now, you need to find in this tree, the number of
distinct pairs (i, j) where node i is an ancestor of node j, and the XOR of the values of all nodes lying on the path
from i to j is equal to K. In short, you need to find the number of pairs (i, j), where node i is an ancestor of j, and
for every x lying on the path from i to j inclusive, xorA[x] = K. A node x is considered an ancestor of another node y
if x is parent of y or x is an ancestor of parent of y. For the purposes of this problem, we consider every node to be
an ancestor of itself.

Input - Output:
The first line contains 2 space separated integers N and K.
The next line contains N space separated integers where the ith integer denotes A[i].
The next line contain N-1 space separated integers, where the ith integer denotes the
parent of node i+1.

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
We have to remember that XOR is cumulative. That basically translates to the following: To find the xor between nodes 2
and 5 for example we have to XOR from root to 5, from root to 2 and then XOR the results. The problem in fact disallows
strange paths because it basically wants to account for the pairs (i, j) in which i is the ancestor of j. We solve the
problem by creating an auxiliary array big enough that will hold the amount of times we have reached a specific XOR 
value. Remember, if we have 3xor4 = 7 then 7xor3 = 4 and 7xor4 = 3. We use DFS to go through the tree and calculate the
xor for the path. Each time, we increase the aux[path] by 1. We then add to our answer aux[path^k]. If path^k index is
in the array has a value other than 0 it basically means that the k value already existed as the xor of a path in the
whole path. After a specific subtree has no more nodes we decrease aux[path] by 1 because that node is not the ancestor
of any other node. At the beginning we also have aux[0] = 1. This accounts in case a path begins from the root.

Final complexity: O(NODES+EDGES)
"""

import sys
from threading import Thread, stack_size

sys.setrecursionlimit(10 ** 6)
stack_size(70000000)


def dfs(graph, begin, values, k, ans, xor, auxiliary):
    xor ^= values[begin - 1]
    ans += auxiliary[xor ^ k]
    auxiliary[xor] += 1
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
    print(ans)


thread = Thread(target=main)
thread.start()
