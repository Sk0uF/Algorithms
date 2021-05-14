# https://www.hackerearth.com/problem/algorithm/monk-and-conversion-game-code-monk-168d2bad/
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    add = 0
    for i in range(n):
        temp = a[i] + add
        add = temp - b[i]

    if add == 0:
        print("YES")
    else:
        print("NO")