"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/big-p-and-punishment-5/

Big P has become a Physical Education teacher at Hack International School. Today, the students of class XII have been
very undisciplined and he decides to punish them all. He makes all of the N student (numbered 1 to N ) to stand in a
line and asks them to sit down on their knees. Students know that Big P is a very cruel and sadistic person and students
start to sit down themselves when they see a friend sit down. However, there are always some students who do not follow
the trend. Now when Big P sees that happen , he slaps that student and makes him sit down. The same process as above is
followed and is stopped when any - one student in the line refuses to sit down by himself. Given the students that Big
P slaps to make them sit down , you need to tell the total no. of students who sat down in that line. Note: It is not
necessary that if A is friend of B then B is also friend of A.

Input - Output:
First Line Contains an integer T denoting no of test cases.
Each test case begins with a line containing three integers N, F, S where N is the number of students in the line.
Next F lines have two integers A and B denoting the friendship between the students A and B.
Next S lines have one integer X denoting the student that was slapped by Big P .
For each test case, output a line containing one integer, the total number of students that sit down in that line

Sample input:
1
3 2 1
1 2
2 3
2

Sample Output:
2
"""

"""
Our graph consists of all the friendships. Note that here the graph is directional. For each slapped student we perform
DFS and find all the other students that will sit down. It basically is like performing DFS to find all the connected 
nodes. 

Final complexity: O(NODES+EDGES)
"""


def dfs(graph, begin, down):
    down.add(begin)
    for node in graph[begin-1]:
        if node == -1:
            continue
        if node not in down:
            dfs(graph, node, down)


# def dfs_alt(graph, begin, down):
#     n = 1
#     down.add(begin)
#     for node in graph[begin-1]:
#         if node == -1:
#             continue
#         if node not in down:
#             n += dfs(graph, node, down)
#     return n


inp_len = int(input())
for _ in range(inp_len):
    N, F, S = map(int, input().split())
    graph = [[-1] for _ in range(N)]
    for _ in range(F):
        a, b = map(int, input().split())
        if graph[a-1][0] == -1:
            graph[a-1][0] = b
        else:
            graph[a-1].append(b)

    down = set()
    for _ in range(S):
        x = int(input())
        if x not in down:
            # n += dfs_alt(graph, x, down)
            dfs(graph, x, down)

    print(len(down))
    # print(n)
