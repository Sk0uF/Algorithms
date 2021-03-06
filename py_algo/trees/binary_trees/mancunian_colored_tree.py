n, c = map(int, input().split())
nodes = list(map(int, input().split()))
colors = list(map(int, input().split()))

ans = ["-1"]
for i in range(1, n):
    j = nodes[i-1] - 1
    color = colors[i]
    while j > 0 and colors[j] != color:
        j = nodes[j-1] - 1
    if j > - 1 and colors[j] == color:
        ans.append(str(j+1))
    else:
        ans.append("-1")
    print(i, ans)

print(' '.join(ans))
