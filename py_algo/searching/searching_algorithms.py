def linear_search(array, element):
    """
    Linear Search
    Complexity: O(N)
    """
    indices = []

    for i in range(len(array)):
        if element == array[i]:
            indices.append(i)
    return indices


def binary_search(array, element):
    """
    Binary Search
    Complexity: O(logN)
    Requires a sorted array
    """
    lower = 0
    upper = len(array) - 1

    while lower <= upper:
        mid = (lower+upper) // 2
        if array[mid] < element:
            lower = mid + 1
        elif array[mid] > element:
            upper = mid - 1
        else:
            return mid

    return -1


def ternary_search(array, element, lower, upper):
    """
    Ternary Search
    Complexity: O(log3(N))
    Requires a sorted array
    """

    if lower <= upper:
        first_third = lower + (upper-lower)//3
        second_third = upper - (upper-lower)//3

        if array[first_third] == element:
            return first_third
        if array[second_third] == element:
            return second_third
        if element < array[first_third]:
            return ternary_search(array, element, lower, first_third - 1)
        elif element > array[second_third]:
            return ternary_search(array, element, second_third + 1, upper)
        else:
            return ternary_search(array, element, first_third + 1, second_third - 1)

    return -1


temp_array = [1, 2, 5, 8, 10, 15, 23]
print(ternary_search(temp_array, 23, 0, len(temp_array) - 1))
