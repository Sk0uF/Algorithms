"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/monk-and-the-islands/

Monk visits the land of Islands. There are a total of N islands numbered from 1 to N. Some pairs of islands are
connected to each other by Bidirectional bridges running over water. Monk hates to cross these bridges as they require a
lot of efforts. He is standing at Island #1 and wants to reach the Island #N. Find the minimum the number of bridges
that he shall have to cross, if he takes the optimal route.

Input - Output:
First line contains T. T testcases follow.
First line of each test case contains two space-separated integers N, M.
Each of the next M lines contains two space-separated integers X and Y,
denoting that there is a bridge between Island X and Island Y.

Sample input:
2
3 2
1 2
2 3
4 4
1 2
2 3
3 4
4 2

Sample Output:
2
2
"""

"""
The answer to the problem is given by a simple BFS. We basically need to find the minimum amount of bridges we have to 
cross to reach node N.

O(NODES+EDGES) for the BFS. 

Final complexity: O(NODES+EDGES)
"""


# Hardcore BFS, we create the queue ourselves.
def bfs(array, goal):
    start = 0
    end = 1
    queue = [-1] * 1000000
    visited = [0] * (len(array)+1)
    queue[0] = 1

    while start != end:
        current = queue[start]
        queue[start] = -1
        start += 1
        for i in range(len(array[current-1])):
            if visited[array[current-1][i]] > visited[current] + 1 or visited[array[current-1][i]] == 0:
                visited[array[current - 1][i]] = visited[current] + 1
                queue[end] = array[current-1][i]
                end += 1

    return visited[goal]


# Easy BFS, we use a ready to go queue.
# from collections import deque
# def bfs(array, goal):
#     queue = deque()
#     visited = [False] * (len(array)+1)
#     depth = [0] * (len(array)+1)
#     queue.append(1)
#
#     while queue:
#         current = queue.popleft()
#         for i in range(len(array[current-1])):
#             if not visited[array[current - 1][i]]:
#                 visited[array[current - 1][i]] = True
#                 depth[array[current - 1][i]] = 1 + depth[current]
#                 queue.append(array[current-1][i])
#                 if goal == array[current-1][i]:
#                     return depth[array[current - 1][i]]
#     return -1


inp_len = int(input())
for _ in range(inp_len):
    n, m = map(int, input().split())
    graph = [[-1]] * n
    for _ in range(m):
        p1, p2 = map(int, input().split())
        if graph[p1 - 1][0] == -1:
            graph[p1 - 1] = [p2]
        else:
            graph[p1 - 1].append(p2)

        if graph[p2 - 1][0] == -1:
            graph[p2 - 1] = [p1]
        else:
            graph[p2 - 1].append(p1)

    print(bfs(graph, n))
