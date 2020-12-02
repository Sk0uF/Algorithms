
inp_len = int(input())
array = list(map(int, input().rstrip().split()))

array = sorted(array, reverse=True)

days = 2 + array[0]
queue = array[0]

for i in range(1, inp_len):
    if array[i] < queue:
        queue -= 1
    else:
        days += 1

print(days)