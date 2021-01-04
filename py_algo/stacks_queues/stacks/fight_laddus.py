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
element is bigger or not. If it isn't, add the index to the stack. If it is then this element is the answer for our 
current element. Remove the current element from the stack and check with the new top element of the stack until that
same next element is not bigger. Finally, add that element to the stack and repeat the same process. If the stack is 
empty, it means that we found an answer for every element. Otherwise, the elements left on the stack have an answer -1,
meaning we didn't find the desired value. This technique works because we always make sure to keep elements on the stack
that have descending frequencies. The moment we find a bigger frequency than the frequency of the current top element of
the stack we have find how many of the previous elements this element satisfies. For example: 1 3 7 2 5 1 4 2 1 5 which
has a frequency array 3 1 1 2 2 3 1 2 3 2.

1)  stack = 1      answer = [-]
2)  stack = 13     answer = [-, -]
3)  stack = 137    answer = [-, -, -]
4)  stack = 12     answer = [-, 2, 2, -]
5)  stack = 125    answer = [-, 2, 2, -, -] 
6)  stack = 11     answer = [-, 2, 2, 1, 1]              
7)  stack = 114    answer = [-, 2, 2, 1, 1, -]
8)  stack = 112    answer = [-, 2, 2, 1, 1, 2, -]
9)  stack = 111    answer = [-, 2, 2, 1, 1, 2, 1, -]
10) stack = 1115   answer = [-1, 2, 2, 1, 1, 2, 1, -1, -1]

The worst case complexity is if we end up with an empty stack
which means that we went through the array twice. Such an example
is the array = [5, 5, 5, 5, 5, 5, 10]. In that particular case 
we will first loop through all the elements until we reach the last
one and then we will go back to the beginning because the last element
satisfies the condition for all the previous elements.

Final complexity: O(2*N) => O(N)
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

"""
The only difference here is that we are using lists instead of dictionaries for our calculations. The speed difference 
between the methods is not significant. Prefer lists when the elements are very dense, for example 1, 2, 3, 4, 5 and
dictionaries when they are sparse, for example 1, 834759, 123132123712983.

Final complexity: O(2*N) => O(N)
"""

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
