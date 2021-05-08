# https://www.hackerearth.com/problem/algorithm/monk-and-palindromes-52299611/
def find_root(array, value):
    if array[value] != value:
        array[value] = find_root(array, array[value])
    return array[value]


n = int(input())
q = int(input())
disjoint = [i for i in range(n)]
sizes = [1] * n
for _ in range(q):
    a, b = map(int, input().split())
    ind = b
    for i in range(a-1, (b+a)//2):
        val_a = i
        ind -= 1
        val_b = ind

        root_a = find_root(disjoint, val_a)
        root_b = find_root(disjoint, val_b)

        if root_a != root_b:
            if sizes[root_a] < sizes[root_b]:
                disjoint[root_a] = root_b
                sizes[root_b] += sizes[root_a]
            else:
                disjoint[root_b] = root_a
                sizes[root_a] += sizes[root_b]

groups = {}
for i in range(n):
    temp = find_root(disjoint, i)
    if temp in groups:
        continue
    else:
        groups[temp] = 1

ans = 1
temp_mod = 1000000007
for i in range(1, len(groups)+1):
    ans = ((ans % temp_mod) * (10 % temp_mod)) % temp_mod

print(ans)
