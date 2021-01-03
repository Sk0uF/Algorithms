"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/monk-and-special-integer-code-monk-e4b52aad/

Monk and his best friend Micro were taking a stroll, when they found an array A having N integers lying on the road. The
array was injured badly, so they took it with them and treated it. When the array came back to senses, it told them,
that some crazy guy came and started beating it. The array started crying and while Monk and Micro were comforting it,
the last element of the array informed that the special integer is missing from its pocket. After hearing that, the
array started crying even louder because it is supposed to appear in the next Code Monk Challenge with that Special
Integer. Special integer, K, of an array, is an integer such that none of its subarray of size K has sum of elements
greater than X. To calm the array down, Monk decided to gift it the maximum possible value of special integer K. Now
since Monk is busy with Code Monk he asked Micro to find the maximum value of special integer but right now, all Micro
can think of is a Potato, so Micro asked for your help.

Input - Output:
First line consists of two space separated integers denoting N and X.
Second line consists of N space separated integers denoting the array A.
Print the maximum possible value of special integer.

Sample input:
4 8
1 2 3 4

Sample Output:
2
"""

"""
To begin with, find the partial sum of the array. This partial sum array actually holds the sums for the first subarray
of each size. The key notice here is that we can find every sum for each subarray from this initial partial sum array.
To do that, the only thing we have to do is partial_sum[index+size] - partial_sum[index-1]. We notice that if we find
the biggest number in the initial partial sum array that is equal or less to x, then the answer is the size that derives
from this index or from an index smaller than that. To find that we use binary search. This index will now be our upper 
point. We once again use binary search from lower to our new upper point but this time we will translate all the values
to the sums of the second subarray for each size. If at any point the upper value is the same as the previous, that
means that the subarrays of that specific size give us the asnwer. Example:
5 26
2 10 9 5 1

 2 10  9 5 1  size 1
12 19 14 6    size 2
21 24 15      size 3
26 25         size 4
27            size 5

The first time, the binary search will find the number 26, index 3 (counting from 0). The second time it will find 
number 24, index 2. The third time it will find number 15, index 2 and it will end. The answer is index + 1 = 3. That
is the maximum possible size that follows the rules of the problem.

Final complexity: O(NlogN)
"""


def binary_helper(partial_sums, lower, upper, x, i):
    while lower <= upper:
        mid = (lower+upper) // 2
        mid_value = partial_sums[mid]

        if i != 0:
            mid_value = partial_sums[mid+i] - partial_sums[i-1]

        if mid_value <= x:
            lower = mid + 1
        else:
            upper = mid - 1

    return lower, upper


n, x = map(int, input().rstrip().split())
a = list(map(int, input().rstrip().split()))

partial_sums = [a[0]]
for i in range(1, n):
    partial_sums.append(partial_sums[i-1] + a[i])

lower = 0
upper = n - 1
for i in range(n):
    lower, upper = binary_helper(partial_sums, 0, upper, x, i)

    if upper == n - i - 1:
        print(upper+1)
        break

"""


Final complexity: 
"""
