n = int(input())
array = list(map(int, input().strip().split()))
k = int(input())

array = sorted(array)

num = -1
for i in range(n):
    if array[i+k-1] == array[i]:
        num = array[i]
        break

print(num)
