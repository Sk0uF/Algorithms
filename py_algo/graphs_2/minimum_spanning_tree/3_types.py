"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/practice-problems/algorithm/3-types/

Let's consider some weird country with N cities and M bidirectional roads of 3 types. It's weird because of some unusual
rules about using these roads: men can use roads of types 1 and 3 only and women can use roads of types 2 and 3 only.
Please answer the following very interesting question: what is maximum number of roads it's possible to destroy that the
country will be still connected for both men and women? Connected country is country where it's possible to travel from
any city to any other using existing roads.

Input - Output:
The first line contains 2 space-separated integer: N and M.
Each of the following M lines contain description of one
edge: three different space-separated integers: a, b and c.
a and b are different and from 1 to N each and denote numbers of vertices that are connected by this edge.
c denotes type of this edge.
For each test case output one integer - maximum number of roads it's possible to destroy or -1 if the country is not
connected initially for both men and women.

Sample input:
5 7
1 2 3
2 3 3
3 4 3
5 3 2
5 4 1
5 2 2
1 5 1


Sample Output:
2
"""

"""
The first thing we need to do is find if there is minimum spanning tree for both men and women. To do that, we create
2 different graphs, one tha only has edges of types 1 and 3 and the other of types 2 and 3. Now, if there is a MST then
we would need to do N-1 "merges" using Kruskal's algorithm for each graph. That would take a total of 2N-2 merges. We
be a little smart and create a graph tha only consists of edges of the 3rd type. If we perform Kruskal's algorithm for 
that graph (which contains the common paths for both men and women) and find the MST for it, then that would mean that
if we made K merges for each of the men's and women's graphs. That gives us a total of 2*K merges and we still need 
2N-2-2K merges if those graphs have a MST. Thus, the answer is TOTAL_EDGES - 2N-2-2K + 2K. That's the total amount of
roads we can destroy and still have an MST for both women and men.

Final complexity: O(E*INVERSE_ACKERMAN + ElogE)
"""


def balance(disjoint_set, i):
    if disjoint_set[i] != i:
        disjoint_set[i] = balance(disjoint_set, disjoint_set[i])
    return disjoint_set[i]


def kruskal(graph, type="first"):
    disjoint_set = [i for i in range(n)]
    sizes = [1] * n
    count = 0
    for i in range(len(graph)):
        root_a = balance(disjoint_set, graph[i][1]-1)
        root_b = balance(disjoint_set, graph[i][2]-1)
        if root_a != root_b:
            if sizes[root_a] <= sizes[root_b]:
                sizes[root_b] += sizes[root_a]
                disjoint_set[root_a] = root_b
            else:
                sizes[root_a] += sizes[root_a]
                disjoint_set[root_b] = root_a

            count += 1

    if type == "first":
        current = balance(disjoint_set, 0)
        for i in range(1, len(disjoint_set)):
            temp = balance(disjoint_set, i)
            if temp != current:
                return -1
            current = temp

    return count


n, m = map(int, input().split())
graph = []
graph1 = []
graph2 = []
for _ in range(m):
    a, b, c = map(int, input().split())
    if c == 3:
        graph.append((c, a, b))
        graph1.append((c, a, b))
        graph2.append((c, a, b))
    elif c == 2:
        graph1.append((c, a, b))
    else:
        graph2.append((c, a, b))

graph1 = sorted(graph1, key=lambda x: x[0], reverse=True)
graph2 = sorted(graph2, key=lambda x: x[0], reverse=True)
men = kruskal(graph1)
women = kruskal(graph2)
general = kruskal(graph, "second")

if men == -1 or women == -1:
    print(-1)
else:
    print(m - ((n-1-general) * 2 + general))
