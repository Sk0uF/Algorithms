# https://www.hackerearth.com/problem/algorithm/teachers-dilemma-3-00955296/

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
