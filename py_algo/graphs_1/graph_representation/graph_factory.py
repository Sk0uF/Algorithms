"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/monk-at-the-graph-factory/

Identify whether the incoming graph is a tree or not.

Input - Output:
First line contains an integer N, the number of vertices.
Second line contains N space-separated integers, the degrees of the N vertices.
Print "Yes" (without the quotes) if the graph is a tree or "No" (without the quotes) otherwise.

Sample input:
3
1 2 1

Sample Output:
Yes
"""

"""
A tree has NODES-1 edges. The handshaking lemma states that the sum of the degrees of all the nodes in a graph equals
2*EDGES. Thus, if 2*EDGES = sum(degrees) => 2*(NODES-1) = sum(degrees) then the graph is a tree.

Final complexity: O(1)
"""

n = int(input())
degrees = list(map(int, input().split()))
total = sum(degrees)
if total == 2*(n - 1):
    print("Yes")
else:
    print("No")
