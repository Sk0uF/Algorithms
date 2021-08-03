t = int(input())
for _ in range(t):
    n = int(input())
    disks = []
    for _ in range(n):
        r, h = map(int, input().split())
        disks.append((r, h))

    disks = sorted(disks)
    dp = [0] * n
    dp[0] = disks[0][1]
    for i in range(1, n):
        dp[i] = disks[i][1]
        for j in range(i):
            if disks[j][0] < disks[i][0] and disks[j][1] < disks[i][1]:
                dp[i] = max(dp[i], dp[j] + disks[i][1])

    print(max(dp))
