n, m, g = map(int, input().rstrip().split())
t = list(map(int, input().rstrip().split()))
a = list(map(int, input().rstrip().split()))
gaps = []

for i in range(n - 1):
    gaps.append(t[i+1] - t[i])

max_gap = max(gaps)
count = 0
for i in range(m):
    if a[i] <= max_gap:
        count += 1

print(count)
