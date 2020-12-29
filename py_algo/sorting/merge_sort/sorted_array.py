"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/the-sorted-array/

Adi loves to play with arrays. He simply wants to sort this array in increasing order. For doing this he can swap any
two adjacent elements i.e. a[i] and a[i+1] where 1 <= i <= N-1  (1 based indexing). In swapping the value of a[i]
decreases by 1 while a[i+1] increases by 1. This operation can be applied any number of times he want. Can you help him
find the final sorted array?

Input - Output:
In first line you are given an integer t, the number of test cases.
In each of t lines the first line contains an integer n.
Then next line contains n space separated integers.
If the sorted array exists then Print “YES” and print the sorted
array in next line. Else print “NO”.

Sample input:
2
4
7 3 9 10
3
11 1 9

Sample Output:
YES
4 6 9 10
NO
"""

"""
We will showcase two different train of thoughts that are implemented with the exact same way.

In common sorting algorithms, our sorting condition is simple. To find out if an element a[i], will end at the left or
right side of an element a[j], we simply compare their numerical values. This is totally independent of their final
position. In our case, we need to find a sorting condition. Once again, suppose we have 2 elements, a[i] and a[j]. Lets
also suppose that these element will end at positions i' and j'. We now have two cases:

1) i' <= j' and a[i] + (i - i') <= a[j] + (j - j'). In this case, we consider that the element a[i] went at position i'
and the element a[j] at a position j', a[i'] = a[i] + (i - i'), a[j'] = a[j] + (j - j'). For our sorting condition to be
valid, we need a[i'] <= a[j'], otherwise the sorting condition wouldn't be valid. Continuing with the inequality:
a[i] + i - a[j] - j = i'- j'. From the inequality, we derive that a[i] + i cannot be bigger than a[j] + j because the
first part of the inequality would be positive while the second part is negative. Thus, we need a[i] + i <= a[j] + j.

2) i' >= j' and a[j] + (j - j') <= a[i] + (i - i'). In this case, we consider that the element a[i] went at position i'
and the element a[j] at a position j', a[i'] = a[i] + (i - i'), a[j'] = a[j] + (j - j'). For our sorting condition to be
valid, we need a[i'] >= a[j'], otherwise the sorting condition wouldn't be valid. Continuing with the inequality:
a[j] + j - a[i] - i = j' - i'. From the inequality, we derive that a[j] + j cannot be bigger than a[i] + i because the
first part of the inequality would be positive while the second part is negative. Thus, we need a[i] + i >= a[j] + j.

We found our sorting condition, we need to compare with the element's numerical value plus its position with other
elements' numerical values plus their position. We also need to make clear that a sorting condition must not contain 
loops. In this case we would have a loop and we wouldn't be able to sort, if at any point we had a[i] + i = a[j] + j.
To implement this idea, we can add to each element its own index (a[i] + i), then sort the array and subtract from each
element its final index. That's not necessary though, as we can just use a conventional sorting algorithm but changing
the sorting condition. For example we can directly use merge sort.
-----------------------------------------------------------------------------------------------------------------------
Looking at the problem, we realize that if we have two elements a[i] and a[j] in an array of length n, the index they
will land to upon being sorted has nothing to do with their initial position. Those elements could be at the exact same
indices in an array of length 2*n and this time they could land in different positions. Their positions and values only
give us the hint of which will be left from each other. If their position doesn't matter, why not "move them" all at
the first index? That would mean they would move the maximum possible. Moving them is equivalent to adding their index
to their value. Now, which one should we choose to place first? The minimum from them, because if we didn't choose the 
minimum and we placed another element, then the minimum element would need to move one position right, making it even
lower. The only problem would be if two elements had the same value upon adding their indices to their value. We 
wouldn't be able to choose which one to place first because if we had chosen, lets say the first one, then the second
would move to right and decrease meaning that this would be now lower and the same would happen if we had chosen to
place the second one first. Finally, we once again subtract from each element of the final array its index to find the
final sorted array.

Final complexity: O(N + NlogN) => O(NlogN)
"""

inp_len = int(input())

for _ in range(inp_len):
    n = int(input())
    array = list(map(int, input().rstrip().split()))

    found = True
    for i in range(n):
        array[i] += i

    array = sorted(array)

    for i in range(n-1):
        if array[i] == array[i+1]:
            found = False
            break

    if found:
        for i in range(n):
            array[i] -= i
        print("YES")
        print(*array)
    else:
        print("NO")
