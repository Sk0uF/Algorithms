# https://www.hackerearth.com/problem/algorithm/monk-and-xor-tree-a190a1ed/
import sys
from threading import Thread, stack_size

sys.setrecursionlimit(10 ** 6)
stack_size(70000000)


# We have to remember that XOR is cumulative. That basically translates to the following: To find the xor between
# nodes 2 and 5 f or example we have to XOR from root to 5, from root to 2 and then XOR the results. The problem in fact
# disallows strange paths because it basically wants to account for the pairs (i, j) in which i is the ancestor of j.
# We solve the problem by creating an auxiliary array big enough that will hold the amount of times we have reached a
# specific XOR value. Remember, if we have 3xor4 = 7 then 7xor3 = 4 and 7xor4 = 3. We use DFS to go through the tree
# and calculate the xor for the path. Each time, we increase the aux[path] by 1. We then add to our answer aux[path^k].
# If path^k index in the array has a value other than 0 it basically means that the k value already existed as the xor
# of a path in the whole path. After a specific subtree has no more nodes we decrease aux[path] by 1 because that node
# is no the ancestor if any other node. At the beginning we also have aux[0] = 1. This accounts in case a path begins
# from the root.
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


