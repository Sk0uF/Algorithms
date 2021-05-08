# https://www.hackerearth.com/problem/algorithm/marriage-problem-4bd56e24/

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
