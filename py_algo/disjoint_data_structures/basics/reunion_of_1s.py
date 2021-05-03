def find_root_and_balance(array, value):
    if array[value] != value:
        array[value] = find_root_and_balance(array, array[value])
    return array[value]


n, k = map(int, input().split())
inp_str = input()
arr = []
for character in inp_str:
    arr.append(character)

sizes = [1] * n
disjoint = [0]
max_len = 0
for i in range(1, n):
    if arr[i] == "0":
        disjoint.append(i)
    else:
        if arr[i-1] == "1":
            disjoint.append(disjoint[i-1])
            sizes[disjoint[i-1]] += 1
            max_len = max(max_len, sizes[disjoint[i-1]])
        else:
            disjoint.append(i)

for _ in range(k):
    temp_input = input()
    if len(temp_input) == 1:
        print(max_len)
    else:
        x = int(temp_input.split()[1])
        if arr[x-1] == "0":
            if x-2 < 0:
                if arr[x] == "1":
                    root = find_root_and_balance(disjoint, x)
                    disjoint[x-1] = disjoint[root]
                    sizes[root] += 1
                    max_len = max(max_len, sizes[root])
            elif x >= n:
                if arr[x-2] == "1":
                    root = find_root_and_balance(disjoint, x-2)
                    disjoint[x-1] = disjoint[root]
                    sizes[root] += 1
                    max_len = max(max_len, sizes[root])
            else:
                if arr[x] == "1" and arr[x-2] == "1":
                    root_a = find_root_and_balance(disjoint, x)
                    root_b = find_root_and_balance(disjoint, x-2)
                    if root_a != root_b:
                        if sizes[root_a] < sizes[root_b]:
                            sizes[root_b] += (sizes[root_a] + 1)
                            disjoint[root_a] = disjoint[root_b]
                            disjoint[x-1] = disjoint[root_b]
                            max_len = max(max_len, sizes[root_b])
                        else:
                            sizes[root_a] += (sizes[root_b] + 1)
                            disjoint[root_b] = disjoint[root_a]
                            disjoint[x-1] = disjoint[root_a]
                            max_len = max(max_len, sizes[root_a])
                elif arr[x] == "1":
                    root = find_root_and_balance(disjoint, x)
                    disjoint[x-1] = disjoint[root]
                    sizes[root] += 1
                    max_len = max(max_len, sizes[root])
                elif arr[x-2] == "1":
                    root = find_root_and_balance(disjoint, x-2)
                    disjoint[x-1] = disjoint[root]
                    sizes[root] += 1
                    max_len = max(max_len, sizes[root])

        arr[x-1] = "1"
        max_len = max(max_len, 1)
