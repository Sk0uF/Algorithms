n = int(input())
a = list(map(int, input().split()))
arr = [a[0], a[1], a[2]]

print("-1")
print("-1")
print(arr[0]*arr[1]*arr[2])

for i in range(3, n):
    min_val = min(arr)
    if a[i] > min_val:
        arr[arr.index(min_val)] = a[i]

    print(arr[0] * arr[1] * arr[2])
