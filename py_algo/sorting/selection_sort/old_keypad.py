
n = int(input())
frequencies = list(map(int, input().rstrip().split()))
k = int(input())
key_size = list(map(int, input().rstrip().split()))

if sum(key_size) < n:
    print("-1")
    exit()

frequencies = sorted(frequencies)

cost = 0
index = 1

while len(frequencies):
    for i in range(len(key_size)):
        try:
            cost += frequencies.pop() * index
        except IndexError:
            break
        key_size[i] -= 1

    keys_tbr = []
    for k in range(len(key_size)):
        if key_size[k] == 0:
            keys_tbr.append(k)

    keys_tbr = sorted(keys_tbr, reverse=True)
    for key_tbr in keys_tbr:
        del key_size[key_tbr]

    index += 1

print(cost)