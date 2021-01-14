n = int(input())
array = list(map(int, input().rstrip().split()))

stack = []
left = []

for i in range(0, n):
    while stack:
        print(stack)
        print(left)
        print()
        k = stack[-1]
        if array[i] < array[k]:
            left.append(k+1)
            stack.append(i)
            break
        else:
            stack.pop()
    if not stack:
        left.append(-1)
        stack.append(i)

print(left)
right = []
stack = []

for i in range(n-1, -1, -1):
    while stack:
        k = stack[-1]
        if array[i] < array[k]:
            right.append(k+1)
            stack.append(i)
            break
        else:
            stack.pop()

    if not stack:
        right.append(-1)
        stack.append(i)

final = []
for i in range(len(left)):
    final.append(left[i] + right[len(right)-1-i])

print(*final)
