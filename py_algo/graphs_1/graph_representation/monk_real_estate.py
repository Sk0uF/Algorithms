"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/monk-in-the-real-estate/

The Monk wants to buy some cities. To buy two cities, he needs to buy the road connecting those two cities. Now, you
are given a list of roads, bought by the Monk. You need to tell how many cities did the Monk buy.

Input - Output:
First line contains an integer T, denoting the number of test cases.
The first line of each test case contains an integer E, denoting the number of roads.
The next E lines contain two space separated integers X and Y,
denoting that there is an road between city X and city Y.
For each test case, you need to print the number of cities the Monk bought.

Sample input:
1
3
1 2
2 3
1 3

Sample Output:
3
"""

"""
We simply need to count he total amount of unique cities. We can do that by using a set.

Final complexity: O(T*EDGES)
"""

inp_len = int(input())
for _ in range(inp_len):
    edges = int(input())
    count = set()
    for _ in range(edges):
        city1, city2 = map(int, input().split())
        count.add(city1)
        count.add(city2)

    print(len(count))
