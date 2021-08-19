"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/odd-even-subarrays-72ad69db/

You are given an array A of N positive integer values. A sub array of this array is called Odd-Even sub array if the
number of odd integers in this sub array is equal to the number of even integers in this sub array. Find the number of
Odd-Even sub arrays for the given array.

Input - Output:
The input consists of two lines.
First line denotes N - size of array.
Second line contains N space separated positive integers denoting the elements of array A.
Print a single integer, denoting the number of Odd-Even sub arrays for the given array.

Sample input:
4
1 2 1 2

Sample Output:
4
"""

"""
We consider every odd number to be -1 and every even number to be 1. We then iterate through the array and add each 
number to the previous. We consider the result as key to a hash table and each time we reach that we add its value to 
the answer and then we add plus +1 to the hash table in that key. Each time we reach the same key the number of sub 
strings increases. For example if we have the numbers 1 2 1 2 1 2 => -1 1 -1 1 -1 1 and we hit the final 1, that would 
mean we reach the 0 but instead of just 1 new sub string, we actually have 2 more, 1 2 1 2 1 2, 1 2 1 2 and 1 2. We 
don't to account for sub strings that don't include the final 2 because we did that in the previous steps.

Final complexity: O(N)
"""

from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
for i, elem in enumerate(a):
    if elem % 2 == 0:
        a[i] = 1
    else:
        a[i] = -1

auxiliary = defaultdict(int)
auxiliary[0] = 1
count = 0
ans = 0
for elem in a:
    count += elem
    ans += auxiliary[count]
    auxiliary[count] += 1

print(ans)
