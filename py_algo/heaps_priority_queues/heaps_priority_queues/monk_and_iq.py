def add_to_heap(array, i):
    if i % 2 == 0:
        parent = i//2 - 1
    else:
        parent = i//2

    if parent >= 0:
        if array[parent][0] > array[i][0] or (array[parent][0] == array[i][0] and array[parent][3] > array[i][3]):
            array[parent], array[i] = array[i], array[parent]
            if parent != 0:
                add_to_heap(array, parent)


def maintain_heap(array):
    left_child = 1
    right_child = 2
    min_index = 0
    current_index = 0
    while True:
        if left_child < len(array):
            if array[left_child][0] < array[min_index][0] \
                    or (array[left_child][0] == array[min_index][0] and array[left_child][3] < array[min_index][3]):
                min_index = left_child

        if right_child < len(array):
            if array[right_child][0] < array[min_index][0] \
                    or (array[right_child][0] == array[min_index][0] and array[right_child][3] < array[min_index][3]):
                min_index = right_child

        if current_index != min_index:
            array[min_index], array[current_index] = array[current_index], array[min_index]
            left_child = 2*min_index + 1
            right_child = 2*min_index + 2
            current_index = min_index
        else:
            break


c, p, n = map(int, input().split())
iq_enrolled = list(map(int, input().split()))
iq_friends = list(map(int, input().split()))

for i in range(n):
    iq_enrolled[i] = (iq_enrolled[i], iq_enrolled[i], 1, i+1)

for i in range(n, c):
    iq_enrolled.append((0, 0, 0, i+1))

for i in range(len(iq_enrolled)):
    add_to_heap(iq_enrolled, i)

for i in range(len(iq_friends), p):
    iq_friends.append(0)

ans = []
for i in range(len(iq_friends)):
    temp_root = list(iq_enrolled[0])
    ans.append(temp_root[3])

    if temp_root[2] == 0:
        iq_enrolled[0] = (iq_friends[i], iq_friends[i], 1, temp_root[3])
    else:
        iq_enrolled[0] = ((temp_root[2]+1)*(temp_root[1]+iq_friends[i]), iq_friends[i], temp_root[2]+1, temp_root[3])

    maintain_heap(iq_enrolled)

print(*ans)
