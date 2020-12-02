"""
Codemonk link: https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/practice-problems/algorithm/a-tryst-with-chess/

You are a bank account hacker. Initially you have 1 rupee in your account, and you want exactly N rupees in it.
You wrote two hacks, First hack can multiply the amount of money you own by 10, while the second can multiply it by 20.
These hacks can be used any number of times. Can you achieve the desired amount N using these hacks?

Input - Output:
First line contains the number of test cases.
For each test case you are given the number N.
Print "Yes" if you can make exactly N rupees or "No"
if you can't.

Sample input:
5
1
2
10
25
200

Sample Output:
Yes
No
Yes
No
Yes
"""

"""
We just have to find how many times 10 and 20 "fit" in our number. Each time we will create 2 numbers, one which will be
the current number divided by 10 and the other divided by 20. When and if the result is 1, this means that we will have
a match which means that by using a specific order of the hacks, we can achieve the desired number.

Final complexity: Undetermined
"""


def money_hack(n, first_hack=10, second_hack=20):
    first_n = n
    second_n = n
    first_n /= second_hack
    second_n /= first_hack

    if first_n == 1 or second_n == 1:
        return True
    # If the numbers is < 1 this means that we cant
    # reach the desired number with
    # the hack order that was followed
    if first_n < 1 or second_n < 1:
        return False
    if money_hack(first_n) or money_hack(second_n):
        return True


inp_len = int(input())

for _ in range(inp_len):
    n = int(input())

    if n == 1:
        print("Yes")
        continue

    if money_hack(n):
        print("Yes")
    else:
        print("No")
