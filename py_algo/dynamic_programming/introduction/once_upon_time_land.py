t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    bank = list(map(int, input().split()))
    dp = [0] * n

    if n == 0:
        print(0)
    elif n == 1:
        print((max(bank[0], bank[1])), 0)
    elif k > n:
        print(max(bank))
    else:
        for j in range(n):
            if j <= k:
                if bank[j] < 0:
                    if j == 0:
                        dp[j] = 0
                    else:
                        dp[j] = dp[j-1]
                else:
                    if j == 0:
                        dp[j] = bank[j]
                    else:
                        dp[j] = max(bank[j], dp[j-1])
            else:
                dp[j] = max(bank[j] + dp[j-k-1], dp[j-1])

        if dp[n-1] > 0:
            print(dp[n-1])
        else:
            print(0)
