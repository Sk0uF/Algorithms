# https://www.hackerearth.com/problem/algorithm/lonely-monk-code-monk-ebca6e4a/
n = int(input())
array = list(map(int, input().split()))
current = 0
ans = 0
odd = 0
even = 1
for i in range(n):
    current += array[i]

    temp = current % 2
    if temp == 0:
        ans += even
        even += 1
    else:
        ans += odd
        odd += 1

print(ans)
