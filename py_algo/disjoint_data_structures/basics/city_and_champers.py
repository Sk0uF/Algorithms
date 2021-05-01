def find_root_and_balance(array, root):
    if root != array[root]:
        array[root] = find_root_and_balance(array, array[root])
    return array[root]


n, q = map(int, input().split())
disjoint = [i for i in range(n)]
sizes = [1] * n
max_group = 1
min_group = float('inf')
for _ in range(q):
    a, b = map(int, input().split())
    root_a = find_root_and_balance(disjoint, a-1)
    root_b = find_root_and_balance(disjoint, b-1)

    if root_a != root_b:
        if sizes[root_a] < sizes[root_b]:
            sizes[root_b] += sizes[root_a]
            max_group = max(max_group, sizes[root_b])
            min_group = min(min_group, sizes[root_a])
            disjoint[root_a] = disjoint[root_b]
        else:
            sizes[root_a] += sizes[root_b]
            disjoint[root_b] = disjoint[root_a]
            max_group = max(max_group, sizes[root_a])
            min_group = min(min_group, sizes[root_b])
    if max_group == n:
        print(0)
    else:
        print(max_group-min_group)
