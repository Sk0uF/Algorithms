t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))

    pre = [0] * n
    suf = [0] * n

    pre[0] = array[0]
    for i in range(1, n):
        pre[i] = max(array[i], pre[i-1] + array[i])
    print(pre)
    for i in range(1, n):
        pre[i] = max(pre[i], pre[i-1])

    print(pre)
    suf[-1] = array[-1]
    for i in range(n-2, -1, -1):
        suf[i] = max(array[i], suf[i+1] + array[i])
    print(suf)
    maximum = max(max(pre), max(suf))
    maximum = max(maximum, 0)
    for i in range(1, n):
        maximum = max(maximum, pre[i-1] + suf[i])

    print(maximum)
