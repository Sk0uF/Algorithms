"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/i-hate-even-subarrays/

You are given a binary string, (string which contains 0's and 1's), You have to perform several operations on this
string, in one operation choose a non-empty even length substring containing only 0's or only 1's and remove it from the
string. Your goal is to minimize the final length of the string after performing several operations.It is possible that
the final string may become empty, in that case print "KHALI" without quotes. And it can be proved that there is always
an unique string with minimal length after performing the operations.

Input - Output:
First line of input contains an intger T denoting number of testcases.
Next T lines of input contains a binary string S.
For each testcase print the required minimal string.

Sample input:
2
101001
1001

Sample Output:
10
KHALI
"""

"""
We are going to solve this problem by using a simple stack. Iterate through the string. If the stack is empty, add the
current char. If it's not, check if the char we are going to add is the same as the one at the top of our stack. If it
is, don't add it and remove the top char from the stack, otherwise, add it to the stack. In the end, if the stack is
empty that means that we have to print the string KHALI, otherwise the final string. Suppose we have the string 101001:

1) stack = 1
2) stack = 10
3) stack = 101
4) stack = 1010
5) stack = 101
6) stack = 10

Final complexity: O(S)
"""

n = int(input())

for _ in range(n):
    s = input().rstrip()
    stack = []

    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        else:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])

    if len(stack) == 0:
        print("KHALI")
    else:
        print("".join(stack))
