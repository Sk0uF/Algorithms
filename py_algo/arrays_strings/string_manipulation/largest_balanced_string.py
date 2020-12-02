"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/largest-balanced-string-bf93ce85/

An empty sequence is balanced. A sequence of the form (A) or [A] or {A} is balanced if A is balanced. A sequence of the
form AB is balanced if A and B both are balanced. You are given a string A, consisting of '(', ')', '[', ']', '{' and
'}' only. You have to find the maximum length of the balanced string after performing some valid operation(s). Valid
operations are: Remove any character from string A. Swap any two adjacent characters of string A. You can perform these
valid operations in any order and any numbers of times.

Input - Output:
The first contains the number of test cases.
Each of the next T lines contains a single string A.
For each case, print the maximum length of the balanced string in a separate line.

Sample input:
5
(){}()[]
))[]]((
{{{{{{{}
[]{}]
{}}

Sample Output:
8
6
2
4
2
"""

"""
We solve the problem by creating a helper 1d array with dimension equal to 6, which is the total available chars. Now, 
based on the properties of the problem, the only think we need to do is to calculate the number of times each char
occurs. The final result is the 2 times the minimum of each pair of chars. For example, if we have {{{{{{{}, the {
bracket appears 8 times and the } bracket appears 1 time. Thus, we can be sure that the result is 2 * min({, }) = 2 * 1
= 2. We also add with the same logic the number of appearances of the other char pairs.

The constraints are insignificant.

Final complexity: O(1)
"""

inp_len = int(input())

for _ in range(inp_len):
    helper = [0] * 6
    line = input()

    for s in line:
        if s == "(":
            helper[0] += 1
        elif s == ")":
            helper[1] += 1
        elif s == "[":
            helper[2] += 1
        elif s == "]":
            helper[3] += 1
        elif s == "{":
            helper[4] += 1
        else:
            helper[5] += 1

    balanced_num = (2*min(helper[0], helper[1])
                    + 2*min(helper[2], helper[3])
                    + 2*min(helper[4], helper[5]))
    print(balanced_num)
