"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/practice-problems/algorithm/monk-and-multiplication/

The Monk learned about priority queues recently and asked his teacher for an interesting problem. So his teacher came up
with a simple problem. He now has an integer array A. For each index i, he wants to find the product of the largest,
second largest and the third largest integer in the range [1,i]. Note: Two numbers can be the same value-wise but they
should be distinct index-wise.

Input - Output:
The first line contains an integer N, denoting the number of elements in the array A.
The next line contains N space separated integers, each denoting the ith integer of the array A.
Print the answer for each index in each line. If there is no second largest or third largest number
 in the array A up to that index, then print "-1", without the quotes.

Sample input:
5
1 2 3 4 5

Sample Output:
-1
-1
6
24
60
"""

"""
We solve this problem by always keeping track of the 3 largest elements. If at any step a new value is bigger than the
smallest value then we replace the smallest value with that value. Since the elements are only 3 we don't care about 
the order because we can easily find it in O(1).

Final complexity: O(N)
"""

n = int(input())
a = list(map(int, input().split()))
arr = [a[0], a[1], a[2]]

print("-1")
print("-1")
print(arr[0]*arr[1]*arr[2])

for i in range(3, n):
    min_val = min(arr)
    if a[i] > min_val:
        arr[arr.index(min_val)] = a[i]

    print(arr[0] * arr[1] * arr[2])
