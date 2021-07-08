from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
for i, elem in enumerate(a):
    if elem % 2 == 0:
        a[i] = 1
    else:
        a[i] = -1

auxiliary = defaultdict(int)
auxiliary[0] = 1
count = 0
ans = 0
for elem in a:
    count += elem
    ans += auxiliary[count]
    auxiliary[count] += 1

print(ans)
