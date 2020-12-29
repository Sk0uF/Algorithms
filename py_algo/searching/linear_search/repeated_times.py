"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/repeated-k-times/

Given a List of N number a1, a2, a3, ........, an, You have to find smallest number from the List that is repeated in
the List exactly K number of times.

Input - Output:
First Line of Input Contain Single Value N, Size of List.
Second Line of Input Contain N Space Separated Integers.
Third Line of Input Contain Single Value K.
Smallest Integer Value That is Repeated Exactly K Number of Timeσ.

Sample input:
5
2 2 1 3 1
2

Sample Output:
1
"""

"""
Sort the array, begin from the smallest number and check the i + k - 1 position to see if the number is the same. If it 
is, that means that it was repeated k amount of times. Otherwise continue with the second to smallest number and keep 
going until the end of the array.

Final complexity: O(N^2)
"""

n = int(input())
array = list(map(int, input().strip().split()))
k = int(input())

array = sorted(array)

num = -1
for i in range(n):
    if array[i+k-1] == array[i]:
        num = array[i]
        break

print(num)
