"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/little-monk-and-williamson-af8a2022/

Little Monk is a huge cricket fan, so he decides that he'll meet his five favorite cricketers in this problem-set of
heaps. And he'll try to impress them. The first cricketer he wants to impress is: Kane Williamson. He asked Kane to
answer some queries in a press interview. Kane is irritated by Little Monk's constant interruption during his interview,
so he decides to give Monk a run for his money by asking him the answer to various queries. Williamson will give a query
of the types mentioned below, to the Monk and will expect him to answer those.
Push X    -- Insert Williamson's score in an array. - Query type 1.
Diff      -- Find out the difference between Willamson's current highest and current lowest score, currently present in
             the array. And then remove a singular instance of those values from the array. In case the current lowest
             and current highest score are same, then only one instance of that score will be removed from the array.
CountHigh -- Find out the number of times Williamson has scored his current highest score, currently present in array.
CountLow  -- Find out the number of times Williamson has scored his current lowest score, currently present in array.

Input - Output:
The first line contains an integer Q, which denotes the number of queries which have to be dealt by The Monk.
The next Q lines will contain a query like the ones mentioned above.
For the query type 2, 3, and 4, print the answer in a new line. If there is no record of any innings,
that is, the array of Williamson's score is empty for query type 2, 3 and 4, then print 1.

Sample input:
10
CountHigh
Push 442
CountHigh
Push 7555
Diff
Push 2799
Diff
Push 8543
Diff
Diff

Sample Output:
-1
1
7113
0
0
-1
"""

"""
We create a min and max heap to maintain the smallest and biggest values. The real question is how to perform the Diff
query. After we find the difference we have to remove the max and min values from BOTH heaps. It's easy to remove the 
max value from the max heap and easy to remove the min value from the min heap but not that straightforward when it
comes to removing the min value from the max the heap and the max value from the min heap. We have to think smart. Lets
take for example the max heap. At an instance, we remove the max value and have to remove the min value as well.
We don't need to do it right away though! Why remove it if it's not the root value? We are only going to remove it if
its frequency of occurencies in the max heap is bigger than the frequency of occurencies in the min heap because that
would mean that in some point we removed that value from the min heap. So, while it's the root value and the frequency
is bigger then keep deleting from the heap! This has an overall amortized complexity of O(N*logN) (i am not sure though)
and the same holds for the min heap.

Final complexity: O(Q*logN)
"""


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
