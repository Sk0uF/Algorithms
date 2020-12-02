'''


'''


'''

To solve the problem, we are going to use merge sort. While sorting the sub arrays, we will make sure to count the
number of inversions and add to each element the corresponding value. We begin by implementing merge sort. Now, each
time we are sorting a sub array, we will count the inversions. They key here is to understand that each time we join 
two halves, only the left's elements might increase in inversions and only in comparison with the second half and not
with itself. That happens because each half is sorted in the previous step and in each previous step the number of
inversions is counted, following the exact same rule. Suppose for example that we have the following array, at the last
step of merge sort: [2, 5, 20, 22 | 4, 6, 9, 15]. We will define 3 variables, namely, left = 0, mid = 3, right = 7. The
second half begins from the value mid + 1. Let's now define 2 more variables, temp_left = left and temp_mid = mid + 1.
We begin by comparing the values at positions (temp_left, temp_mid => 2, 4). 2 is lower than 4, so now temp_left += 1
= 1. Once again, we compare the elements (5, 4), 4 is lower and temp_mid += 1 = 5 but this time we also increase the
number of inversions by 1, lets say inv += 1 = 1. Now, we compare the elements (5, 6), 5 is lower and because until now
we add plus 1 inversion to it (in the previous steps we could have more inversions added to it). According to the
previous steps we also increase temp_left += 1 = 2. Our sorted array until now equals [2, 4, 5]. We compare the elements
(20, 6), 6 is lower, inv = 2, temp_mid = 6. (20, 9), 9 is lower, inv = 3, temp_mid = 7. (20, 15) , 15 is lower, inv = 4,
temp_mid = 8. At this point, temp_mid is bigger than right, meaning that the second half has no more elements left. That
is why we will just take the elements 20 and 22 as they are and add inv = 4 to their number of inversions. Another
probable scenario would be left to become bigger than mid. That would mean that the first half would have no more
elements and we would just get the remaining elements of the second half, without of course adding inversions to them.

The complexity is the same as in merge sort.

Final complexity: O(NlogN)

'''


def merge_helper(weights, aux, helper, left, right):
    if left < right:
        mid = left + (right - left) // 2
        merge_helper(weights, aux, helper, left, mid)
        merge_helper(weights, aux, helper, mid + 1, right)
        merge(weights, aux, helper, left, mid, right)


def merge(weights, aux, helper, left, mid, right):
    temp_left = left        # First element the first half
    temp_mid = mid + 1      # First element of the second half
    count = 0
    cur = 0                 # Temporary number of inversions

    for i in range(left, right + 1):
        if temp_left > mid:                     # If the first half has no more elements
            aux[count] = weights[temp_mid]
            temp_mid += 1
        elif temp_mid > right:                  # If the second half has no more elements
            aux[count] = weights[temp_left]
            helper[weights[temp_left]] += cur
            temp_left += 1
        elif weights[temp_left] <= weights[temp_mid]:  # The element from the first half is lower
            aux[count] = weights[temp_left]
            helper[weights[temp_left]] += cur
            temp_left += 1
        else:
            aux[count] = weights[temp_mid]             # The element from the second half is lower
            temp_mid += 1
            cur += 1

        count += 1

    for i in range(count):
        weights[left + i] = aux[i]
    print(weights)


inp_len = int(input())

for _ in range(inp_len):
    n = int(input())
    weights = []
    for _ in range(n):
        weights.append(int(input()))

    copied = weights[:]
    aux = [0] * n
    helper = [0] * 1000005

    merge_helper(weights, aux, helper, 0, n - 1)

    if len(copied) > 0:
        for i, w in enumerate(copied):
            if i != n - 1:
                print(helper[w], end=' ')
            else:
                print(helper[w])
    else:
        print()