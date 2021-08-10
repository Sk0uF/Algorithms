# https://www.hackerearth.com/problem/algorithm/vaishu-and-tower-arrangements-fe7c349e

t = int(input())
for _ in range(t):
    n = int(input())
    towers = list(map(int, input().split()))
    neg = [0] * n
    pos = [0] * n
    if towers[0] == 1:
        pos[0] = 1

    if towers[-1] == -1:
        neg[-1] = 1

    for i in range(n-2, -1, -1):
        if towers[i] == -1:
            neg[i] = neg[i+1] + 1
        else:
            neg[i] = neg[i+1]

    ans = n
    for i in range(n-1):
        if towers[i] == 1:
            pos[i] = pos[i-1] + 1
        else:
            pos[i] = pos[i-1]

        ans = min(ans, pos[i] + neg[i+1])

    print(ans)
