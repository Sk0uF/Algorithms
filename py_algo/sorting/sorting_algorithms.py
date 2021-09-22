def bubble_sort(array):
    """
    Bubble Sort
    Complexity: O(N^2)
    """
    array_len = len(array)
    for k in range(array_len - 1):
        for i in range(array_len - k - 1):
            if array[i] > array[i+1]:
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp
    return array


def selection_sort(array):
    """
    Selection Sort
    Complexity: O(N^2)
    """
    array_len = len(array)
    for k in range(array_len - 1):
        minimum = k
        for i in range(k + 1, array_len):
            if array[i] < array[minimum]:
                minimum = i
        temp = array[minimum]
        array[minimum] = array[k]
        array[k] = temp
    return array


def insertion_sort(array):
    """
    Insertion Sort
    Complexity: O(N^2)
    """
    array_len = len(array)
    for k in range(array_len):
        temp = array[k]
        i = k
        while i > 0 and temp < array[i-1]:
            array[i] = array[i-1]
            i -= 1
        array[i] = temp
    return array


def merge_sort(array):
    """
    Merge Sort
    Complexity: O(NlogN)
    """

    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        array = []

        # This is a queue implementation. We can also use
        # a deque but slicing it needs the itertools slice
        # function which I didn't want to use. More on that
        # in the stacks and queues chapter.
        l1 = l2 = 0
        while len(left) > l1 and len(right) > l2:
            if left[l1] < right[l2]:
                array.append(left[l1])
                l1 += 1
            else:
                array.append(right[l2])
                l2 += 1

        while len(left) > l1:
            array.append(left[l1])
            l1 += 1

        while len(right) > l2:
            array.append(right[l2])
            l2 += 1

    return array


def counting_sort(array):
    """
    Counting Sort
    Complexity: O(N + K)

    Imagine if array = [1, 100000].
    Then, N = 2 and K = 100000, K >> N^2.
    And thus, it far exceeds the O(N^2) complexity.
    That's why O(N + K) is deceptive.
    """
    max_value = max(array)
    temp = [0] * max_value

    for i in range(len(array)):
        temp[array[i]-1] += 1

    sorted_array = []
    for i in range(max_value):
        if temp[i] == 0:
            continue

        k = temp[i]
        value = i + 1

        while k:
            sorted_array.append(value)
            k -= 1

    return sorted_array


def radix_sort(array):
    """
    Radix Sort
    Complexity: O((N + B) * logb(max)

    Where B is the base for representing numbers and
    max is the maximum element of the input array. We
    basically try to lower the complexity of counting sort.
    Even though it seems good, it's good in specific cases only.
    """
    n = len(array)
    max_value = max(array)
    step = 1

    while max_value:
        temp = [0] * 10
        sorted_array = [0] * n
        for i in range(n):
            index = array[i] // step
            temp[index % 10] += 1

        for i in range(1, 10):
            temp[i] += temp[i-1]

        # By finding the partial sums and passing through the
        # initial array from the end to the beginning we can know
        # each time how many values exist with the same or lower digit.
        # For example, if temp = [1, 1, 0, 1, 0, 1, 0, 0, 0, 0]
        # then it will become [1, 2, 2, 3, 3, 4, 4, 4, 4, 4].
        # If the array is [3, 11, 10, 5] then in the first pass
        # (first digit), when we start from number 5 we will
        # have 5 mod 10 = 5, temp[5] = 4, which means that there
        # were 3 number before the number 5 with a smaller value
        # for their first digit.
        # So, this number will go to the 4 - 1 = 3rd position
        for i in range(n-1, -1, -1):
            index = array[i] // step
            sorted_array[temp[index % 10] - 1] = array[i]
            temp[index % 10] -= 1
        for i in range(n):
            array[i] = sorted_array[i]

        max_value //= 10
        step *= 10
    return array


import random


def quick_sort(array, start, end):
    """
    Quick Sort
    Complexity: O(N^2)

    Most of the the times when using random pivot
    the complexity is O(NlogN). That is why we use
    the term "worst case complexity" O(N^2) and
    "expected worst case complexity" O(NlogN). Amortized
    and expected worst case complexity are not the same.
    """
    if start < end:
        pivot_pos = random.randint(start, end - 1)
        pivot = array[pivot_pos]
        array[start], array[pivot_pos] = array[pivot_pos], array[start]
        count = start + 1

        for i in range(start + 1, end):
            if array[i] < pivot:
                array[i], array[count] = array[count], array[i]
                count += 1

        array[start], array[count - 1] = array[count - 1], array[start]
        pivot_pos = count - 1

        quick_sort(array, start, pivot_pos)
        quick_sort(array, pivot_pos + 1, end)
    return array


def add_to_heap(array, n, i):
    """
    Heap Sort
    Complexity: O(NlogN)

    When using hipify (to create the heap) and deletion, the complexity is O(N + logN) => O(NlogN).
    When using insertion (to create the heap) and deletion, O(NloN + NlogN) = O(2*NlogN) => O(NlogN).
    It is clear that the first implementation is faster than the second. Even though we consider the
    difference not a "big deal" and we write both times O(NlogN), the difference still exists and we
    have to understand it.
    Why is it O(n)? If we have 1024 elements lets suppose that the time is O(1024). If we add 1024 more elements this
    means that we are going to add 1 more layer at the bottom. (Remember that half of the elements are at bottom). Now,
    for the new elements we don't need to do anything cause they don't violate anything. For the elements above we need
    O(1) for each, so if we have 2048 elements in total, we will have O(1024 + 1024), which means O(2048). So, this can
    be further be proved for any K value.
    """
    if i % 2 == 0:
        parent = i//2 - 1
    else:
        parent = i//2

    max_element = array[i]
    max_element_index = i

    if parent >= 0 and max_element > array[parent]:
        max_element_index = parent
        array[max_element_index], array[i] = array[i], array[max_element_index]
        if parent != 0:
            add_to_heap(array, n, max_element_index)


def heapify_or_delete(array, n, i):
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    max_element = array[i]
    max_element_index = i

    if left_child < n:
        if max_element < array[left_child]:
            max_element = array[left_child]
            max_element_index = left_child

    if right_child < n:
        if max_element < array[right_child]:
            max_element = array[right_child]
            max_element_index = right_child

    if max_element_index != i:
        array[i], array[max_element_index] = array[max_element_index], array[i]
        heapify_or_delete(array, n, max_element_index)

    # 2*i left child
    # 2*i + 1 right child
    # i//2 parent
    # max heap, every parent node is greater or equal to its children
    # To insert check every n//2 element and we swap if it's smaller than our new element (logn).
    # To delete we remove the root and the last element takes its place.
    # Then we compare from top to bottom to maintain (logn).
    # Height of binary tree is logn.
    # Note that when comparing with children, we only need to compare with the biggest of them.
    # Half the nodes are at bottom.


def heap_sort(array):
    n = len(array)

    # for i in range(n//2 - 1, -1, -1):
    #     heapify_or_delete(array, n, i)

    for i in range(1, n):
        add_to_heap(array, n, i)

    for i in range(n-1, 0, -1):
        # We can use the heapify that way cause it's like the deletion if we combine it
        # with the first line in which we swap the elements.
        array[i], array[0] = array[0], array[i]
        heapify_or_delete(array, i, 0)

    return array


"""
Bucket Sort
    
About bucket sort, we just divide the elements into buckets
and then we sort each bucket using an existing sorting algorithm.
It can be useful when the elements we have to sort are uniformly
distributed. The complexity is not straightforward to me, needs
further understanding.
"""


# a = [3, 11, 2, 3, 123, 9544, 2, 75, 23, 93, 121, 114, 10, 42, 12, 3]
a = [10, 20, 15, 12, 40, 25, 18]
# print(bubble_sort(a))
# print(selection_sort(a))
# print(insertion_sort(a))
# print(merge_sort(a))
# print(counting_sort(a))
# print(radix_sort(a))
# print(quick_sort(a, 0, len(a)))
print(heap_sort(a))
