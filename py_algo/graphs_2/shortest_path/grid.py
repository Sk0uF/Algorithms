"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/robot-in-grid-b7d391f7/

You are given a grid A of size NxM, two integers (Si, Sj) and Q tasks. Each task contains two integers, (Di, Dj). Each
cell in the grid is either empty cells denoted by O (Capital English character 'o') or occupied cells denoted by *.
Initially, you are at (Si, Sj). Find the minimum number of steps in which you have to take to reach (Di, Dj) from
(Si, Sj) without traversing the occupied cells. In a single step, you can move from any cell (i, j) to the 4 neighboring
provided these cells are inside the grid A.

Input - Output:
The first line of input contains 3 space separated integers N, M and Q where N and M denotes
the dimensions of the grid A and Q denotes the number of tasks.
Each of the next N lines contain a string of length M, jth character in the ith line of which
is either O or * denoting that the cell (i, j) is empty or occupied.
The next line contains 2 space separated integers Si and Sj denoting the source cell of the grid.
This is followed by Q lines each containing 2 space separated integers Di and Dj .
Print the answer to each query on a new line. If there is no path between (Si, Sj) and (Di, Dj), print -1.

Sample input:
3 3 2
O*O
OOO
*OO
2 2
1 1
1 2

Sample Output:
2
-1
"""

"""
This is a basic implementation of a flood-fill algorithm with the use of BFS to also find the minimum distances (we can
do that because the paths are weightless).

Final complexity: O(V+E)
"""


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
