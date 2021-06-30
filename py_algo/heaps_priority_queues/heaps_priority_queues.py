"""
In the examples we are implementing only a max heap. The same logic holds for the min heap.
"""


def add_to_heap(array, i):
    """
    Add to heap
    Complexity: O(logN)
    """
    if i % 2 == 0:
        parent = i//2 - 1
    else:
        parent = i//2

    if parent >= 0 and array[parent] < array[i]:
        array[parent], array[i] = array[i], array[parent]
        if parent != 0:
            add_to_heap(array, parent)


def delete_from_heap(array, new_array):
    """
    Delete from heap
    Complexity: O(logN)
    """
    array[0], array[len(array)-1] = array[len(array)-1], array[0]
    left_child = 1
    right_child = 2
    max_index = 0
    current_index = 0
    new_array.append(array.pop())

    while True:
        if left_child < len(array):
            if array[max_index] < array[left_child]:
                max_index = left_child

        if right_child < len(array):
            if array[max_index] < array[right_child]:
                max_index = right_child

        if max_index != current_index:
            array[max_index], array[current_index] = array[current_index], array[max_index]
            current_index = max_index
            left_child = 2*max_index + 1
            right_child = 2*max_index + 2
        else:
            break

    return new_array


def heapify(array, i):
    """
    Heapify
    Complexity: O(1)

    The code here is almost the same as with the delete_from_heap function. We get O(1) because we use it in a specific
    way. See the create_heap_heapify to understand it.
    """
    left_child = 2*i + 1
    right_child = 2*i + 2
    max_index = i

    if left_child < len(array):
        if array[max_index] < array[left_child]:
            max_index = left_child

    if right_child < len(array):
        if array[max_index] < array[right_child]:
            max_index = right_child

    if max_index != i:
        array[max_index], array[i] = array[i], array[max_index]
        heapify(array, max_index)


def create_heap_add(array):
    """
    Create heap with add operation
    Complexity: O(N*logN)
    """
    for i in range(1, len(array)):
        add_to_heap(array, i)
    return array


def create_heap_heapify(array):
    """
    Create heap with heapify
    Complexity: O(N)

    Why is it O(N)? If we have 1024 elements lets suppose that the time is O(1024). If we add 1024 more elements this
    means that we are going to add 1 more layer at the bottom. (Remember that half of the elements are at bottom). Now,
    for the new elements we don't need to do anything cause they don't violate anything. For the elements above we need
    O(1) for each, so if we have 2048 elements in total, we will have O(1024 + 1024), which means O(2048). So, this can
    be further be proved for any K value.
    """
    for i in range(len(array)//2-1, -1, -1):
        heapify(array, i)
    return array


def heap_sort(array):
    """
    Heap sort
    Complexity: O(N*logN)

    If we use the add operation to create heap it's O(N*logN + N*logN) => O(N*logN).
    If we use heapify to create the heap it's O(N + N*logN) => O(N*logN).
    """
    # array = create_heap_add(array)
    array = create_heap_heapify(array)
    sorted_array = []
    for i in range(len(array)):
        sorted_array = delete_from_heap(array, sorted_array)

    return sorted_array


temp_array = [3, 11, 2, 3, 123, 9544, 2, 75, 23, 93, 121, 114, 10, 42, 12, 3]
temp_array_alt = [3, 11, 2, 3, 123, 9544, 2, 75, 23, 93, 121, 114, 10, 42, 12, 3]
print(heap_sort(temp_array))


# We can also use Python's build in heapq library to achieve the exact same goal.
# The following is for min heap. For max heap we use the same but with negative values.
import heapq
heapq.heapify(temp_array_alt)
heapq_sorted = []
for i in range(len(temp_array_alt)):
    heapq_sorted.append(heapq.heappop(temp_array_alt))

print(heapq_sorted)


def priority_queue():
    """
    Priority queue

    Max and min heaps are priority queues. We can implement another type of
    priority queues by using max and min heaps. The only thing we have to do
    is create the heap with the priority we are given. That way we can maintain
    the nice complexity time of max or min heaps. To do that, we can we use our
    own implementation or use the build in heapq with a class representing the
    heap's elements, with an __lt__(self, other) function inside that decides
    the priority. Otherwise, if we just want a simple priority with one comparison
    but with some other values stored as well, we can use a tuple with the first
    value being the value we are going to compare with.
    """
    class PriorityElement:
        def __init__(self, value, weight):
            self.value = value
            self.weight = weight

        def __lt__(self, other):
            return self.weight < other.weight

    # The following will produce the exact same results
    priority_1 = []
    priority_2 = []
    heapq.heappush(priority_1, PriorityElement(0, 15))
    heapq.heappush(priority_1, PriorityElement(0, 6))

    heapq.heappush(priority_2, (0, 15))
    heapq.heappush(priority_2, (0, 6))
