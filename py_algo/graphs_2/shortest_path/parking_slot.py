"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/the-parking-slot-9fac40d6/

There is a parking facility which is in the form of a graph having N nodes and M edges. The graph does not have self
loops or multiple edges. Each node represents a parking slot and has a capacity of vehicles it can hold. Each edge has a
weight w representing we can reach from node u to node v incurring a cost of w units. All parking slots have a parking
fee F per vehicle which is same for all slots. There are K identical vehicles entering the parking facility, each
vehicle enumerated with a distinct number from 1 to K. The vehicles enter in their natural order, that is, vehicle
number 1 enters, then vehicle number 2, then 3 and so on till vehicle number K. For each vehicle, you have to print the
minimum total cost that is incurred on the vehicle owner. Here, total cost includes cost of the path taken to reach the
parking slot and parking fee of the slot. It is guaranteed that you can reach any slot from any other slot. All vehicles
entering the parking facility enter from the parking slot 1.

Input - Output:
The first line consists of three integers N, M and F, denoting number of nodes,
number of edges and parking fee respectively.
The second line consists of N space separated integers denoting the parking capacity of each parking slot.
This array is represented by C[].
Following M lines contain three space separated integers each: u, v and w, denoting
we can reach from node u to node v incurring a cost of w units.
The last line of input contains an integer K.
Print K space separated integers denoting answer for each vehicle.
ith integer in the space separated integers denotes answer for ith vehicle number.
If it is not possible to park a vehicle , print -1 for that vehicle.

Sample input:
5 4 20
1 2 1 1 2
1 2 2
4 5 1
3 4 1
1 3 1
5

Sample Output:
20 21 22 22 22
"""

"""
The first think we have to do is find the Shortest Path in the graph. After we do that, we have to short the Shortest
Paths from the first node to all the other nodes. We have to make sure that we keep track of the final vertex when
shorting. For example, if the shortest paths are [0, 12, 5, 4, 3] then we the result should be 
[(0, 0), (3, 4), (4, 3), (5, 2), (12, 1)]. Now, the only thing we have to do is start placing cars based on their 
capacity and according to the shortest paths array.

Final complexity: O(E*INVERSE_ACKERMAN + ElogE)
"""


import heapq


def dijkstra(graph):
    distances = [float("inf")] * len(graph)
    visited = [False] * len(graph)
    distances[0] = 0
    pq = []
    heapq.heappush(pq, (0, 0))

    while pq:
        current = heapq.heappop(pq)
        current = current[1]
        if visited[current]:
            continue
        visited[current] = True

        for i in range(len(graph[current])):
            if graph[current][i] == -1:
                break
            next = graph[current][i][0]
            weight = graph[current][i][1]
            if distances[next] > distances[current] + weight:
                distances[next] = distances[current] + weight
                heapq.heappush(pq, (distances[next], next))

    return distances


n, m, f = map(int, input().split())
slots = list(map(int, input().split()))
graph = [[-1] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    if graph[u-1][0] == -1:
        graph[u-1][0] = (v-1, w)
    else:
        graph[u-1].append((v-1, w))

    if graph[v-1][0] == -1:
        graph[v-1][0] = (u-1, w)
    else:
        graph[v-1].append((u-1, w))


k = int(input())
distances = dijkstra(graph)

distances = [(distances[i], i) for i in range(len(distances))]
distances = sorted(distances, key=lambda x: x[0])

counter = 0
ans = []
while k > 0:
    if counter >= len(distances):
        ans.append(-1)
        k -= 1
        counter += 1
        continue
    total = distances[counter][0] + f
    ans.append(total)
    slots[distances[counter][1]] -= 1
    if slots[distances[counter][1]] == 0:
        counter += 1
    k -= 1

print(*ans)
