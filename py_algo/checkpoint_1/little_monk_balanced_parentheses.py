"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/little-monk-and-balanced-parentheses-32c6492b

Given an array of positive and negative integers, denoting different types of parentheses. The positive numbers xi
denote opening parentheses of type xi and the negative numbers -xi denote closing parentheses of type xi. Open
parentheses must be closed by the same type of parentheses. Open parentheses must be closed in the correct order. Thus,
[1, 2, -2, -1] is balanced, while [1, 2, -1, -2] is not balanced. You have to find out the length of the longest
sub array that is balanced.

Input - Output:
First line contains an input N, denoting the number of parentheses.
Second line contains N space separated integers, denoting the ith parenthesis of the array.
Print the length of the longest sub array that is balanced.

Sample input:
5
1 -1 2 3 -2

Sample Output:
2
"""

"""
The problem can be solved by making a simple alternation to the classic problem of finding if a sequence of parentheses
is balanced or not. The classic problem can be solved in O(N) by using a single stack. At each step, we compare the top
element of the stack with the next element. If the next element "closes" the parenthesis at the top of the stack then
we remove the top element from the stack, otherwise, we add the next element to the stack. In the end, if the stack is
empty then the parentheses are balanced, otherwise they are not. The fact that we are able to do that makes true that
we can split the problem to multiple sub problems, each corresponding to a segment of the parentheses. Thus, if we end
with an empty stack, the answer is the length of the array and if we end with a non empty stack, it means that some
portions of the the array were balanced (unless we end with a stack which is the same as the array, meaning that array
doesn't have any sub array that is balanced) and some not. To solve the problem we just have to find the length of those
sub arrays, if they exist. Each time we find a closing parenthesis we go to that specific index in our array and make
the values of those those indices 0 (x != 0 in that problem). If we end with an array full of 0, then the array is
balanced and the answer is its length, otherwise we count the amount of subsequent 0's and we chose the maximum amount.

Final complexity: O(2*N) => O(N)
"""

n = int(input())
array = list(map(int, input().split()))
stack = [0]
count = 0
for i in range(1, n):
    if stack:
        if array[i] == -array[stack[-1]] and array[i] < 0:
            array[i] = 0
            array[stack.pop()] = 0
        else:
            stack.append(i)
    else:
        stack.append(i)

if not stack:
    print(n)
else:
    count = 0
    max_count = 0
    for i in range(n):
        if array[i] == 0:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0

    max_count = max(max_count, count)
    print(max_count)
