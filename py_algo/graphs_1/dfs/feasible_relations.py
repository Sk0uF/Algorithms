"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/feasible-relations/

As a programmer, you sometimes have to deal with some math and this is the time to do it. You are given a list of binary
relations, equalities and inequalities, like a = b, a != d, b = c etc. Your task is to output YES if you can assign
integers to input variables in such a way, that you can satisfy all equalities and inequalities. Otherwise you should
output NO.

Input - Output:
In the first line there is one integer T denoting the number of test cases.
Description of T test cases follow. Each one have two integers N and K given in
the first line denoting the number of variables and the number of relations between
them for this test case. All variables are represented by integers in range [1, N].
K lines follow. Each of them is of the form "x1 R x2" where x1 and x2 are
representing variables and R is either "=" or "!=" and denotes the kind of relation between these variables.
Output exactly T lines. In i-th of them, output the answer to the i-th test case.

Sample input:
2
2 2
1 = 2
1 != 2
3 2
1 = 2
2 != 3

Sample Output:
NO
YES
"""

"""
We perform DFS to find all the groups of connected nodes. We consider the nodes to be the integers and the edge between
them exists if and only if we have the "=" sign between them. We assign a number to every different group. Then, we 
iterate through all the inequalities and if 2 not equal integers exists in the same group then the answer is NO,
otherwise it's YES. Note that the integers represent unknown variables.

Final complexity: O(NODES+EDGES) + O(AMOUNT of INEQUALITIES)
"""

import sys
from sys import stdin, stdout
sys.setrecursionlimit(10**9)


# Pycharm has some problems with recursion even with the limit
# set to the maximum. The problem is with the stack size. To
# solve that we either have to use a simple thread with the
# threading library that allows us to change the stack size
# or use t he iterative version of DFS.
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
