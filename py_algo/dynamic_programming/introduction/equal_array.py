t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    partial_sums = [array[0]]
    for i in range(1, n):
        partial_sums.append(array[i]+partial_sums[i-1])

    ans = float("inf")
    stop = False
    for i in range(n):
        if partial_sums[i] < partial_sums[-1] - partial_sums[i]:
            val = partial_sums[-1] - 2*partial_sums[i]
            ans = min(ans, val)
        if partial_sums[i] == partial_sums[-1] - partial_sums[i]:
            print(0)
            stop = True
            break

    if not stop:
        if ans != float("inf"):
            print(ans)
        else:
            print(-1)

