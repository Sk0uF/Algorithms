"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/circular-distance-3-c8592f16/

Its time for yet another challenge, and this time it has been prepared by none other than Monk himself for Super
Hardworking programmers like you. So, this is how it goes: Given N points located on the co-ordinate plane, where the
ith point is located at co-ordinate (xi, yi), you need to answer q queries. In the ith  query, you shall be given an
integer ri, and considering you draw a circle centered at the origin (0, 0) with radius ri, you need to report the
number of points lying inside or on the circumference of this circle. For each query, you need to print the answer on a
new line.

Input - Output:
The first line contains a single integer N denoting the
number of points lying on the co-ordinate plane.
Each of the next N lines contains 2 space separated integers
xi and y1, denoting the x and y coordinates of the  point.
The next line contains a single integer q, denoting the number of queries.
Each of the next q lines contains a single integer, where the integer on
the ith line denotes the parameters of the ith query ri.

Sample input:
5
1 1
2 2
3 3
-1 -1
4 4
2
3
32

Sample Output:
3
5
"""

"""
Find all the distances and sort them. Use binary search to find the maximum possible index that can exists inside the
circle. The index is actually the amount of points inside the circle.

Final complexity: O(N + QlogN) => O(QlogN)
"""

n = int(input())
distance = []
for _ in range(n):
    x, y = map(int, input().rstrip().split())
    distance.append((x**2 + y**2)**(1/2))

distance = sorted(distance)
q = int(input())
for _ in range(q):
    r = int(input())

    lower = 0
    upper = n - 1
    while lower <= upper:
        mid = (lower+upper) // 2

        if distance[mid] <= r:
            lower = mid + 1
        else:
            upper = mid - 1

    print(lower)
