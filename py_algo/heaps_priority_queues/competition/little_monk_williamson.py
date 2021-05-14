# https://www.hackerearth.com/problem/algorithm/little-monk-and-williamson-af8a2022/
def add_to_heap(array, i, heap_type):
    if i % 2 == 0:
        parent = i//2 - 1
    else:
        parent = i//2

    if parent >= 0:
        if heap_type == "max":
            if array[parent] < array[i]:
                array[parent], array[i] = array[i], array[parent]
                if parent != 0:
                    add_to_heap(array, parent, heap_type)
        else:
            if array[parent] > array[i]:
                array[parent], array[i] = array[i], array[parent]
                if parent != 0:
                    add_to_heap(array, parent, heap_type)


def delete_from_heap(array, heap_type):
    array[0], array[len(array)-1] = array[len(array)-1], array[0]
    left_child = 1
    right_child = 2
    max_index = 0
    current_index = 0
    array.pop()

    while True:
        if left_child < len(array):
            if heap_type == "max":
                if array[max_index] < array[left_child]:
                    max_index = left_child
            else:
                if array[max_index] > array[left_child]:
                    max_index = left_child

        if right_child < len(array):
            if heap_type == "max":
                if array[max_index] < array[right_child]:
                    max_index = right_child
            else:
                if array[max_index] > array[right_child]:
                    max_index = right_child

        if max_index != current_index:
            array[max_index], array[current_index] = array[current_index], array[max_index]
            current_index = max_index
            left_child = 2*max_index + 1
            right_child = 2*max_index + 2
        else:
            break


q = int(input())
holder_max = {}
holder_min = {}
min_heap = []
max_heap = []
for _ in range(q):
    inp = input().split()
    if len(inp) == 2:
        value = int(inp[1])
        if value in holder_max:
            holder_max[value] += 1
            holder_min[value] += 1
        else:
            holder_max[value] = 1
            holder_min[value] = 1

        max_heap.append(value)
        min_heap.append(value)
        add_to_heap(min_heap, len(min_heap)-1, "min")
        add_to_heap(max_heap, len(max_heap)-1, "max")
    else:
        if inp[0] == "CountHigh":
            if max_heap:
                print(holder_max[max_heap[0]])
            else:
                print(-1)
        elif inp[0] == "CountLow":
            if min_heap:
                print(holder_min[min_heap[0]])
            else:
                print(-1)
        else:
            if max_heap and min_heap:
                print(max_heap[0]-min_heap[0])
                holder_max[max_heap[0]] -= 1
                holder_min[min_heap[0]] -= 1
                delete_from_heap(max_heap, "max")
                delete_from_heap(min_heap, "min")

                if len(max_heap) != 0:
                    while holder_max[max_heap[0]] > holder_min[max_heap[0]]:
                        holder_max[max_heap[0]] -= 1
                        delete_from_heap(max_heap, "max")
                        if len(max_heap) == 0:
                            break

                if len(min_heap) != 0:
                    while holder_min[min_heap[0]] > holder_max[min_heap[0]]:
                        holder_min[min_heap[0]] -= 1
                        delete_from_heap(min_heap, "min")
                        if len(min_heap) == 0:
                            break

            else:
                print(-1)
