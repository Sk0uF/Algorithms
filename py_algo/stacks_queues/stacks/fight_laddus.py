"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/fight-for-laddus/

Given an array, For each element find the value of nearest element to the right which is having frequency greater than
that of the current element. If there does not exist an answer for a position, then print '-1'.

Input - Output:
First line contains T denoting the number of test cases.
First line of each test case contains N denoting the number of elements in array.
Second line of each test case contains N integers (A1..An) denoting the given array.
For each test case print space separated N numbers denoting the answer corresponding answer.

Sample input:
3
10
1 3 7 2 5 1 4 2 1 5
5
1 1 1 1 1
6
1 1 2 2 2 3

Sample Output:
-1 2 2 1 1 -1 2 1 -1 -1
-1 -1 -1 -1 -1
2 2 -1 -1 -1 -1
"""

"""
Find the frequencies of the elements of the array. For each element of the array, check if the frequency of the next
element is bigger or not. If it isn't, add the index to the stack. If it is then this element is the answer for that 
element

Final complexity: Undetermined
"""

t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().rstrip().split()))
    freq = {}
    ans = {}
    stack = []

    for element in array:
        if freq.get(element):  # O(1) for dict.
            freq[element] += 1
        else:
            freq[element] = 1

    stack.append(0)
    for i in range(1, n):
        while stack and freq[array[i]] > freq[array[stack[-1]]]:
            ans[stack[-1]] = array[i]
            stack.pop()
        stack.append(i)

    while stack:
        ans[stack[-1]] = -1
        stack.pop()

    for i in range(n):
        print(ans[i], end=" ")
    print()


# t = int(input())
# for _ in range(t):
#     n = int(input())
#     array = list(map(int, input().rstrip().split()))
#     N = max(array)
#     freq = [0] * (N+1)
#     ans = [0] * n
#     stack = []
#
#     for j in array:
#         freq[j] += 1
#
#     stack.append(0)
#     for i in range(1, n):
#         while stack and freq[array[i]] > freq[array[stack[-1]]]:
#             ans[stack[-1]] = array[i]
#             stack.pop()
#         stack.append(i)
#
#     while stack:
#         ans[stack[-1]] = -1
#         stack.pop()
#
#     print(ans)
#     final = [str(elem) for elem in ans]
#     print(' '.join(final))
