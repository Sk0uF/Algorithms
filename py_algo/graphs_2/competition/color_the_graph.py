"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/color-the-graph-e140de5a/

You are given a graph with N nodes and M undirected edges. This graph does not contain self loops and multiple edges
between same pair of nodes. You plan to give this to Monk for his birthday so you wish to colour it. You want to colour
all the nodes of the graph in either red or blue colour such that each edge has endpoints of different colours. As Monk
loves red colour, you also want the number of nodes with red colour to be maximum. Output the maximum number of red
coloured nodes you can get in the graph after colouring every vertex under the given constraint. If no such colouring is
possible output "NO" (without quotes).

Input - Output:
First line contains T, denoting the number of test cases.
First line contains two integers N and M, the number of nodes in the graph and the number of edges in the graph.
Next M lines follow each containing two integers U and V, denoting an undirected edge between them.
Output T lines each containing the answer for the ith test case.

Sample input:
1
3 2
1 2
2 3

Sample Output:
2
"""

"""
The problem can be solved by using BFS (or DFS) but with a simple twist. Instead of checking if a node is already 
visited, we are going to check if a node has a color and if so what that color is. If it doesn't have a color then it 
means that that node has not been visited, otherwise, if it has a color different than the one we want to paint it that
would mean there is some kind of problem. That problem occurs when we visit a node that we have already visited (in 
our case painted) and the whole path that created a "circle" consists of an odd number of nodes. The graph might not
be connected and thus we do the same for all the nodes, so that we can find all the components. Each time, we want to
add to our answer the maximum amount of blue and red nodes from each component to our red and blue counter respectively.
We choose the maximum from these counters because we have to notice that color doesn't play any significat role. For 
example, if the blue nodes are more, then we consider that we just re-paint them red and the previous red nodes become
blue.

Final complexity: O(V+E)
"""

from collections import deque


def bfs(graph, i):
    count_red = 0
    count_blue = 0
    queue = deque()
    queue.append(i)
    colors[i] = "red"
    count_red += 1
    while queue:
        current = queue.popleft()
        for i in range(len(graph[current])):
            if graph[current][i] == -1:
                continue
            if colors[graph[current][i]] == "":
                queue.append(graph[current][i])
                if colors[current] == "red":
                    colors[graph[current][i]] = "blue"
                    count_blue += 1
                else:
                    colors[graph[current][i]] = "red"
                    count_red += 1
            elif colors[graph[current][i]] == colors[current]:
                return False, 0, 0

    return True, count_red, count_blue


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = [[-1] for _ in range(n)]
    colors = [""] * n
    for _ in range(m):
        u, v = map(int, input().split())
        if graph[u-1][0] == -1:
            graph[u-1][0] = v-1
        else:
            graph[u-1].append(v-1)

        if graph[v-1][0] == -1:
            graph[v-1][0] = u-1
        else:
            graph[v-1].append(u-1)

    cnt_red = 0
    cnt_blue = 0
    for i in range(n):
        if colors[i] == "":
            ans, count_red, count_blue = bfs(graph, i)
            cnt_red += max(count_red, count_blue)
            cnt_blue += max(count_blue, count_red)
            if not ans:
                print("NO")
                break

    if ans:
        print(max(cnt_blue, cnt_red))
