"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/practice-problems/algorithm/city-and-campers/

"Money money MONEY, I want money" thought Alex. "Now how do I get money? Well... I'll open up a camp!"
Well, unfortunately things didn't go so well for Alex's campers, and now there are N campers wandering around the city
aimlessly. You have to handle Q queries; which consist of two groups finding each other and becoming one larger group.
After each query, output the difference between the group of largest size and group of smallest size. If there is only
one group, output 0. At first, everyone is in their own group. Also note, if the two campers in the query are already in
the same group, print the current answer and skip merging the groups together.

Input - Output:
The first line consists of two space separated integers, N and Q
The next Q line consists of two integers, A and B, meaning that the groups
involving camper A and camper B find each other.
Output Q lines, the answer after each query.

Sample input:
2 1
1 2

Sample Output:
0
"""

"""
Classic implementation of a disjoint set. The cool thing is how we maintain the max and min values. For the max, it's 
quite straightforward. We begin from 1 and each time we perform a union we find the new max size. For the min we have
to do the exact same thing but we begin from a huge value. The key here is to understand that if we have performed less
than n steps in the algorithm, meaning there are single groups that haven't been merged, then the min is 1, otherwise
we take the min value we calculated with the above technique.

Final complexity: O(Q*INVERSE_ACKERMAN)
"""


def find_root_and_balance(array, root):
    if root != array[root]:
        array[root] = find_root_and_balance(array, array[root])
    return array[root]


n, q = map(int, input().split())
disjoint = [i for i in range(n)]
sizes = [1] * n
max_group = 1
min_group = float('inf')
steps = 0
for _ in range(q):
    a, b = map(int, input().split())
    root_a = find_root_and_balance(disjoint, a-1)
    root_b = find_root_and_balance(disjoint, b-1)

    if root_a != root_b:
        if sizes[root_a] < sizes[root_b]:
            sizes[root_b] += sizes[root_a]
            max_group = max(max_group, sizes[root_b])
            min_group = max(min_group, sizes[root_b])
            disjoint[root_a] = disjoint[root_b]
        else:
            sizes[root_a] += sizes[root_b]
            disjoint[root_b] = disjoint[root_a]
            max_group = max(max_group, sizes[root_a])
            min_group = max(min_group, sizes[root_a])
        steps += 1
    if max_group == n:
        print(0)
    else:
        if steps < n:
            print(max_group-1)
        else:
            print(max_group-min_group)
