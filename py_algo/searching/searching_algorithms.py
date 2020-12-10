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

    Requires a sorted array.
    Small modifications needed to work
    with descending order as well.
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


def ternary_search(array, lower, upper):
    """
    Ternary Search
    Complexity: O(log3/2(N))

    Requires a unimodal array. That means
    that the array has to be increasing and then
    decreasing (or the opposite). The point is to
    find the maximum (or minimum) element. Small
    modifications needed to work with descending
    and then ascending order as well.
    """

    if lower < upper:
        first_third = lower + (upper-lower)//3
        second_third = upper - (upper-lower)//3

        if array[first_third] > array[second_third]:
            return ternary_search(array, lower, second_third - 1)
        else:
            return ternary_search(array, first_third + 1, upper)

    # We can return either lower or upper. That happens
    # because the code is going to stop when lower = upper.
    return lower


def ternary_search_func(x1, x2, c, precision, lower, upper):
    """
    Ternary Search
    Complexity: O(log3/2(N/e)
    Where e is the precision we want to achieve amd
    N is the range between between the lower and upper
    point. Basically, it's like having an array of length
    N/e.

    Requires a unimodal function.
    Small modifications needed to work
    with descending and then ascending order
    as well.
    """

    while upper - lower > precision:
        first_third = lower + (upper-lower)/3
        second_third = upper - (upper-lower)/3

        if ternary_helper(first_third, x1, x2, c) > ternary_helper(second_third, x1, x2, c):
            upper = second_third
        else:
            lower = first_third

    # Both lower and upper will be very close to the
    # answer. Choose whichever you want.
    return ternary_helper(lower, x1, x2, c)


def ternary_helper(x, x1, x2, c):
    return x1 * (x**2) + x2 * x + c


temp_array = [1, 2, 5, 8, 10, 80, 79, 3, 1]
print(ternary_search(temp_array, 0, len(temp_array) - 1))
print(ternary_search_func(-1, 2, 3, 0.000000001, 0, 1))
