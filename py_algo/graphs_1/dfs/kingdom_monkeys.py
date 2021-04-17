"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/kingdom-of-monkeys/

This is the story in Zimbo, the kingdom officially made for monkeys. Our Code Monk visited Zimbo and declared open a
challenge in the kingdom, thus spoke to all the monkeys: You all have to make teams and go on a hunt for Bananas. The
team that returns with the highest number of Bananas will be rewarded with as many gold coins as the number of Bananas
with them. May the force be with you! Given there are N monkeys in the kingdom. Each monkey who wants to team up with
another monkey has to perform a ritual. Given total M rituals are performed. Each ritual teams up two monkeys. If
Monkeys A and B teamed up and Monkeys B and C teamed up, then Monkeys A and C are also in the same team. You are given
an array A where Ai is the number of bananas i'th monkey gathers. Find out the number of gold coins that our Monk should
set aside for the prize.

Input - Output:
First line contains an integer T. T test cases follow.
First line of each test case contains two space-separated N and
M. M lines follow. Each of the M lines contains two integers Xi and Yi,
the indexes of monkeys that perform the i' th ritual.
Last line of the testcase contains N space-separated integer constituting the array A.
Print the answer to each test case in a new line.

Sample input:
1
4 3
1 2
2 3
3 1
1 2 3 5

Sample Output:
6
"""

"""
We find all the connected vertices with DFS and while doing so we also calculate the sum of all the collected bananas
of all monkeys in all the groups. We need the group that has gathered the maximum amount of bananas. The answer is the
amount of bananas.

Final complexity: O(NODES+EDGES)
"""

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
