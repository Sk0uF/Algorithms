"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/teachers-dilemma-3-00955296/

Monk is having a hard time teaching the 2nd standard students. He wants to divide the students into small groups so that
he can conduct some fun-filled activities for them. But students also want their friends in the same group. So, if
student A is a friend of student B, and student B is a friend of student C, then the students A,B and C must be in the
same group, otherwise they will start crying. After dividing the students, he will choose a leader from each group who
will lead their respective groups. Now he wants to know the number of ways he can choose the group leaders from all the
groups. Print this answer modulo 10^9 + 7. Note: Two ways A and B will be considered different if at least 1 person is a
leader in group A, and is not a leader in group B, or vice-versa.

Input - Output:
The first line consists of two integers N and M denoting the number of students
and the number of relationships respectively.
The next M lines consists of two integers u and v denoting that student u and student v
are friends. u and v can never be equal and relationships are not repeated.
Print the answer modulo 10^9 + 7 in a single line.

Sample input:
5 4
1 2
2 3
1 3
4 5

Sample Output:
6
"""

"""
That's an easy disjoint set problem. We just need to multiply the sizes of all groups. Be careful to reset the size 
of each smaller group when merging it with the bigger one. 

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
            sizes[root_u] = 1
            disjoint[root_u] = root_v
        else:
            sizes[root_u] += sizes[root_v]
            sizes[root_v] = 1
            disjoint[root_v] = root_u

ans = 1
for size in sizes:
    ans = (ans*size) % 1000000007

print(ans)
