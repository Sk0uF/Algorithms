"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/marriage-problem-4bd56e24/

Monk has recently created a matrimonial site. X men and Y women registered there. As Monk has access to everyone'
Facebook profile, he can see whether a person is a friend of another person or not. He doesn't want any two people who
are in a single group to get married together. So, first we have q1 relationships among men. Then, we have q2
relationships among women. Finally we have q3 relationships among men and women. Read the input format for more clarity.
Now, Monk wants to calculate the total number of unique marriages he can set between men and women provided the
conditions are followed. Note - Two person are said to be in a group if they are friends directly or connected through a
chain of mutual friends.

Input - Output:
The first line consists of X and Y.
Next line consists of variable, q1.
The next q1 lines will have two integers of the form A B where A and B are both men and are friends on facebook.
Next line consists of variable, q2.
The next q2 lines will have two integers of the form A B where A and B are both women and are friends on facebook.
Next line consists of variable, q3.
The next q3 lines will have two integers of the form A B where A is a man and B is a woman and they both are friends on
facebook.

Sample input:
4 5
1
1 3
2
1 4
1 5
2
1 2
4 1

Sample Output:
15
"""

"""
We create 3 disjoint sets, 1 with the men, 1 with the women and 1 with both of them. We have to be smart with the
indices and make our lives easier when we get the final disjoint set. We also make sure to keep track of the the total
size of each group as well as the total amount of men and women in each set. Obviously, total_size = total_men+
total_women. We loop through each group and add to the answer the total amount of men multiplied by the amount of women
in all the other groups which is overall_total_women - women_of_the_current_group.

Final complexity: O(Q*INVERSE_ACKERMAN) 
"""


def find_root(array, value, extra=0):
    if array[value-extra] != value:
        array[value-extra] = find_root(array, array[value-extra], extra)
    return array[value-extra]


x, y = map(int, input().split())
dis_men = [i for i in range(x)]
dis_women = [(i+x) for i in range(y)]
sizes_men = []
sizes_women = []

for _ in range(x):
    sizes_men.append((1, 1, 0))

for _ in range(y):
    sizes_women.append((1, 0, 1))

q1 = int(input())
for _ in range(q1):
    a, b = map(int, input().split())
    root_a = find_root(dis_men, a-1)
    root_b = find_root(dis_men, b-1)

    if root_a != root_b:
        if sizes_men[root_a][0] < sizes_men[root_b][0]:
            sizes_men[root_b] = (sizes_men[root_b][0]+sizes_men[root_a][0], sizes_men[root_b][1]+sizes_men[root_a][1],
                                 sizes_men[root_b][2]+sizes_men[root_a][2])
            dis_men[root_a] = root_b
        else:
            sizes_men[root_a] = (sizes_men[root_b][0]+sizes_men[root_a][0], sizes_men[root_b][1]+sizes_men[root_a][1],
                                 sizes_men[root_b][2]+sizes_men[root_a][2])
            dis_men[root_b] = root_a

q2 = int(input())
for _ in range(q2):
    a, b = map(int, input().split())
    root_a = find_root(dis_women, a - 1 + x, x)
    root_b = find_root(dis_women, b - 1 + x, x)

    if root_a != root_b:
        if sizes_women[root_a-x][0] < sizes_women[root_b-x][0]:
            sizes_women[root_b-x] = (sizes_women[root_b-x][0]+sizes_women[root_a-x][0],
                                     sizes_women[root_b-x][1]+sizes_women[root_a-x][1],
                                     sizes_women[root_b-x][2]+sizes_women[root_a-x][2])
            dis_women[root_a-x] = root_b
        else:
            sizes_women[root_a-x] = (sizes_women[root_b-x][0] + sizes_women[root_a-x][0],
                                     sizes_women[root_b-x][1] + sizes_women[root_a-x][1],
                                     sizes_women[root_b-x][2] + sizes_women[root_a-x][2])
            dis_women[root_b-x] = root_a

q3 = int(input())
sizes = sizes_men + sizes_women
dis = dis_men + dis_women
groups = {}
for _ in range(q3):
    a, b = map(int, input().split())

    root_a = find_root(dis, a - 1)
    root_b = find_root(dis, b - 1 + x)

    if root_a != root_b:
        if sizes[root_a][0] < sizes[root_b][0]:
            sizes[root_b] = (sizes[root_b][0]+sizes_men[root_a][0], sizes[root_b][1]+sizes[root_a][1],
                             sizes[root_b][2]+sizes[root_a][2])
            dis[root_a] = root_b
        else:
            sizes[root_a] = (sizes[root_b][0]+sizes[root_a][0], sizes[root_b][1]+sizes[root_a][1],
                             sizes[root_b][2]+sizes[root_a][2])
            dis[root_b] = root_a

ans = 0
for i in range(len(dis)):
    temp_root = find_root(dis, i)
    if temp_root in groups:
        continue

    groups[temp_root] = "visited"
    total_group_men = sizes[temp_root][1]
    ans = ans + sizes[temp_root][1] * (y-sizes[temp_root][2])

print(ans)
