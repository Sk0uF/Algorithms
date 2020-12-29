"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/the-old-monk/

Big Chandan is a dire lover of Biryani, especially Old Monk's Biryani. Today, he went over to have some of it. To his
surprise, the waiter turns out be to be a coding geek and refuses to serves him unless Chandu solves his two- arrays
problem, stated as: Given two non-increasing array of integers A,B i.e A[i] >= A[i+1] and B[i] >= B[i+1] and for all
i, 0 ≤ i < n-1. The monkiness of two numbers is given by: M (A[i],B[j]) = j - i , if j >=i and B[j] >= A[i], or 0
otherwise. Find the monkiness of the two arrays, that is given by: M (A,B)= max (M(A[i],B[j])) for 0≤ i, j< n-1.

Input - Output:
The first line contains an integer, tc, denoting the number of test cases.
The next line contains an integer, n, denoting the size of the two arrays.
The size of both the arrays will be equal.
After that line, the next line contains n integers denoting the numbers in
the array A, and in the next line, there will be n numbers denoting the numbers in the array B.
Print the monkiness of the two arrays.

Sample input:
2
9
7 7 3 3 3 2 2 2 1
8 8 7 7 5 5 4 3 2
6
6 5 4 4 4 4
2 2 2 2 2 2

Sample Output:
5
0
"""

"""
If the biggest element of B is smaller than the smallest element of A then the answer is 0. Otherwise, loop through all
elements of array A and use binary search on array B to find the number that is further away and bigger or equal to the
element. The answer is the biggest possible distance.

Final complexity: O(NlogN)
"""

inp_len = int(input())

for _ in range(inp_len):
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))

    if b[0] <= a[-1]:
        print(0)
        continue

    final_value = 0
    for i in range(n):
        lower = 0
        upper = n - 1
        pos = -1
        while lower <= upper:
            mid = (lower+upper) // 2
            if b[mid] >= a[i]:
                pos = mid
                lower = mid + 1
            else:
                upper = mid - 1

        final_value = max(final_value, pos - i)

    print(final_value)



"""
Loop through array B. If the index of the B array is bigger than the index of A array and the B value on that index is
bigger or equal to the A value on its respective index, then calculate the distance. Otherwise, increase the index of 
array A by 1. Find the maximum possible distance. That technique guarantees that each time we find a distance, the B
index will be bigger or equal to the A index.

Final complexity: O(N)
"""

# inp_len = int(input())
#
# for _ in range(inp_len):
#     n = int(input())
#     a = list(map(int, input().strip().split()))
#     b = list(map(int, input().strip().split()))
#
#     if b[0] <= a[-1]:
#         print(0)
#         continue
#
#     final_value = 0
#     i = 0
#
#     for j in range(n):
#         if j >= i and b[j] >= a[i]:
#             final_value = max(final_value, j - i)
#         else:
#             i += 1
#             if i == n:
#                 break
#
#     print(final_value)
