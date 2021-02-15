# https://www.hackerearth.com/problem/algorithm/little-monk-and-balanced-parentheses-32c6492b
n = int(input())
array = list(map(int, input().split()))
stack = [0]
count = 0
for i in range(1, n):
    if stack:
        if array[i] == -array[stack[-1]] and array[i] < 0:
            array[i] = 0
            array[stack.pop()] = 0
        else:
            stack.append(i)
    else:
        stack.append(i)

if not stack:
    print(n)
else:
    count = 0
    max_count = 0
    for i in range(n):
        if array[i] == 0:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0

    max_count = max(max_count, count)
    print(max_count)
