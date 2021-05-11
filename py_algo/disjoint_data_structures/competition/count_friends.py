"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/count-friends-190fcb36/

There are N students and M relationships of the form u v, which means that student u and student v are friends. If two
students are not friends directly but they have a mutual friend, then they too become friends. Your task is to count the
number of friends of the ith student where 1 <= i <= N.

Input - Output:
The first line consists of two integers N and M denoting the number
of students and the number of relationships respectively.
The next M lines consists of two integers u and v denoting that student u and
student v are friends. u and v can never be equal and relationships are not repeated.
Print N space separated integers which tells us the number of friends of the ith student.

Sample input:
4 3
4 3
2 4
2 3

Sample Output:
0 2 2 2
"""

"""
That's an easy disjoint set problem. We find all the groups and then we iterate from 1 to N, find the root of the group
each index belongs to and then print its size which basically is the number of friends.

Final complexity: O(M*INVERSE_ACKERMAN) 
"""


def find_root(array, value):
    if array[value] != value:
        array[value] = find_root(array, array[value])
    return array[value]


n, m = map(int, input().split())
disjoint = [i for i in range(n)]
sizes = [1] * n

for _ in range(m):
    u, v = map(int, input().split())
    root_u = find_root(disjoint, u-1)
    root_v = find_root(disjoint, v-1)

    if root_u != root_v:
        if sizes[root_u] < sizes[root_v]:
            sizes[root_v] += sizes[root_u]
            disjoint[root_u] = root_v
        else:
            sizes[root_u] += sizes[root_v]
            disjoint[root_v] = root_u

ans = []
for i in range(n):
    temp_ans = find_root(disjoint, i)
    ans.append(sizes[temp_ans]-1)

print(*ans)
