"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/terrible-chandu/

Reverse the given string.

Input - Output:
The first contains the number of test cases.
Each of the next T lines contains a single string S.

Sample input:
2
ab
aba

Sample Output:
ba
aba
"""

"""
The problem is straight forward.

Final complexity: O(N)
"""

inp_len = int(input())

for _ in range(inp_len):
    s = input()
    # The general case is a[begin:end:step]
    print(s[::-1])
