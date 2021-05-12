def add_to_heap(array, i):
    if i % 2 == 0:
        parent = i//2 - 1
    else:
        parent = i // 2

    if parent >= 0:
        if array[parent] < array[i]:
            array[parent], array[i] = array[i], array[parent]
            if parent != 0:
                add_to_heap(array, parent)


def create_heap(array):
    for i in range(len(array)):
        add_to_heap(array, i)
    return array


def maintain_heap(array):
    max_index = 0
    current_index = 0
    left_child = 1
    right_child = 2

    while True:
        if left_child < len(array):
            if array[left_child] > array[max_index]:
                max_index = left_child

        if right_child < len(array):
            if array[right_child] > array[max_index]:
                max_index = right_child

        if max_index != current_index:
            array[max_index], array[current_index] = array[current_index], array[max_index]
            current_index = max_index
            left_child = 2*max_index + 1
            right_child = 2*max_index + 2
        else:
            break


m, n = map(int, input().split())
seats = list(map(int, input().split()))
seats = create_heap(seats)

total = 0
for _ in range(n):
    total += seats[0]
    seats[0] -= 1
    maintain_heap(seats)

print(total)
