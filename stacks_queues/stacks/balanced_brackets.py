"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/balanced-brackets-3-4fc590c6/

A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].
Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a
closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}
and (). A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example,
{[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a
single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket,
]. By this logic, we say a sequence of brackets is balanced if the following conditions are met: It contains no
unmatched brackets. The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched
pair of brackets. Given n strings of brackets, determine whether each sequence of brackets is balanced. If a string is
balanced, return YES. Otherwise, return NO.

Input - Output:
The first line contains a single integer n, the number of strings.
Each of the next n lines contains a single string s, a sequence of brackets.

Sample input:
3
{[()]}
{[(])}
{{[[(())]]}}

Sample Output:
YES
NO
YES
"""

"""
We are going to solve this problem by using a simple stack. Iterate through the brackets. If the stack is empty, add the
current bracket. If it's not, check if the bracket we are going to add is the opposite bracket of the top bracket of our
stack. If it is, don't add it and remove the top bracket from the stack, otherwise, add it to the stack. In the end, if
the stack is empty that means that the string is balanced, otherwise it isn't. Suppose we have the string {[()]}:

1) stack = {
2) stack = {[
3) stack = {[(
4) stack = {[
5) stack = {
6) stack = empty

The test cases are significant. 

Final complexity: O(S*N)
"""


n = int(input())

for _ in range(n):
    brackets = input()
    brackets_len = len(brackets)

    if brackets_len % 2 != 0:
        print("NO")
        continue

    brackets_stack = []
    index = 0
    while index < brackets_len:
        if len(brackets_stack) == 0:
            brackets_stack.append(brackets[index])
        elif (ord(brackets_stack[-1]) == ord(brackets[index])-1
              or ord(brackets_stack[-1]) == ord(brackets[index])-2):
            brackets_stack.pop()
        else:
            brackets_stack.append(brackets[index])
        index += 1

    if len(brackets_stack) > 0:
        print("NO")
    else:
        print("YES")
