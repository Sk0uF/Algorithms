"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/practice-problems/algorithm/mr-president/

You have recently started playing a brand new computer game called "Mr. President". The game is about ruling a country,
building infrastructures and developing it. Your country consists of N cities and M bidirectional roads connecting them.
Each road has assigned a cost of its maintenance. The greatest achievement in the game is called "Great administrator"
and it is given to a player who manage to have all cities in the country connected by roads in such a way that it is
possible to travel between any two cities and that the sum of maintenance costs of these roads is not greater than K.
This is very hard to accomplish, but you are very close to do it. More precisely, you have just discovered a new method
of transforming standard roads into super roads, with cost of maintenance just 1, due to their extreme durability. The
bad news is that it is very expensive to transform a standard road into a super road, but you are so excited that you
are going to do it anyway. In addition, because you have a lot of other expenses, you also want to first demolish as
many roads as possible in order to safe some money on their maintenance first and then start working on getting the
achievement. You can demolish any road in the country and that operation does not cost you anything. Because you want to
spend the absolutely minimum money in order to get the achievement, you are interested in the smallest number of
transformations of standard roads into super roads in such a way that you can do that.

Input - Output:
In the first line there are 3 integers N, M and K denoting the number of cities in the country,
the number of roads in it and the desired sum of costs of maintenance.
M lines describing these roads follow. In each of them there are 3 integers A, B and C, where A and B denote
the endpoints of the road while C denotes the cost of its maintenance.
Output the minimum number of roads which need to be transformed in order to get the achievement.
If you cannot do it no matter what, output -1.

Sample input:
3 3 25
1 2 10
2 3 20
3 1 30

Sample Output:
1
"""

"""
The problem is simple. We have to find the MST for the given graph (cities and roads connecting them can be represented
by a graph) and then, iterate from the biggest to smallest weight and find how many roads we need to change to achieve
our goal, of keeping the cost lower than K. That's possible if there is no MST for the graph or if even if we replace
the roads the cost will still be greater than K. Think of it!

Final complexity: O(E*INVERSE_ACKERMAN + ElogE)
"""


def balance(disjoint_set, i):
    if disjoint_set[i] != i:
        disjoint_set[i] = balance(disjoint_set, disjoint_set[i])
    return disjoint_set[i]


def kruskal(graph):
    disjoint_set = [i for i in range(n)]
    sizes = [1] * n
    priority_array = []
    total = 0
    count = 0
    for i in range(m):
        root_a = balance(disjoint_set, graph[i][1]-1)
        root_b = balance(disjoint_set, graph[i][2]-1)

        if root_a != root_b:
            if sizes[root_a] <= sizes[root_b]:
                sizes[root_b] += sizes[root_a]
                disjoint_set[root_a] = root_b
            else:
                sizes[root_a] += sizes[root_a]
                disjoint_set[root_b] = root_a

            total += graph[i][0]
            priority_array.append(graph[i][0])

    for i in range(len(priority_array)-1, -1, -1):
        if total > k:
            count += 1
            total = total - priority_array[i] + 1

    if total > k:
        return -1

    current = balance(disjoint_set, 0)
    for i in range(1, len(disjoint_set)):
        temp = balance(disjoint_set, i)
        if temp != current:
            return -1
        current = temp

    return count


n, m, k = map(int, input().split())
sorted_graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    sorted_graph.append((c, a, b))

sorted_graph = sorted(sorted_graph, key=lambda x: x[0])
print(kruskal(sorted_graph))
