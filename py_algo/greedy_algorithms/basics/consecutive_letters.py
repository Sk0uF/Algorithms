"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/chandu-and-consecutive-letters/

Chandu is very fond of strings. (Or so he thinks!) But, he does not like strings which have same consecutive letters. No
one has any idea why it is so. He calls these strings as Bad strings. So, Good strings are the strings which do not have
same consecutive letters. Now, the problem is quite simple. Given a string S, you need to convert it into a Good String.
You simply need to perform one operation - if there are two same consecutive letters, delete one of them.

Input - Output:
The first line contains an integer T, denoting the number of test cases.
Each test case consists of a string S, which consists of only lower case letters.
For each test case, print the answer to the given problem.

Sample input:
3
abb
aaab
ababa

Sample Output:
ab
ab
ababa
"""

"""
Very easy problem. Think about it.

Final complexity: O(t*S)
"""

t = int(input())
for _ in range(t):
    bad_string = input()
    good_string = ""
    prev = ""
    for char in bad_string:
        if char != prev:
            good_string += char
        prev = char

    print(good_string)
