"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/practice-problems/algorithm/city-and-flood-1/

Fatland is a town that started with N distinct empires, namely empires 1, 2, ..., N. But over time, the armies of some
of these empires have taken over other ones. Each takeover occurred when the army of empire i invaded empire j. After
each invasion, all of empire j became part of empire i, and empire j was renamed as empire i. Empire Huang, leader of
Badland, wants to invade Fatland. To do this, he needs to calculate how many distinct empires still remain in Fatland
after all the takeovers.

Input - Output:
The first line contains an integer N, the number of empires that were originally in Fatland.
The second line contains an integer K, denoting the number of takeovers that took place.
Each of the next K lines contains 2 space-separated integers i, j, representing that the army
of empire i took over that of empire j. As a result, empire j does not exist anymore and is now
renamed as empire i. It is guaranteed that empire i still exists.
Output one integer, the number of empires that exist in Fatland.

Sample input:
4
2
1 2
4 1

Sample Output:
2
"""

"""
By using a set, we find the amount of cities that don't exist any more. The answer is the total starting cities minus
the cities that don't exist anymore. 

Final complexity: O(K)
"""

n = int(input())
k = int(input())
aux = set()
for _ in range(k):
    i, j = map(int, input().split())
    aux.add(j)

print(n-len(aux))
