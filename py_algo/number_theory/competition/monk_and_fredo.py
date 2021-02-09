"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/monk-and-fredo-cm-number-theory-97942213/

Given two weights of a and b units, in how many different ways you can achieve a weight of d units using only the given
weights? Any of the given weights can be used any number of times (including 0 number of times).

Input - Output:
The first line of input consists of an integer T denoting the number of test cases.
Each test case consists of only one line containing three space separated integers a, b and d.
For each test case, print the answer in a separate line.

Sample input:
4
2 3 7
4 10 6
6 14 0
2 3 6

Sample Output:
1
0
1
2
"""

"""
This is considered to be a common problem in number theory. However, even if the solution might seem simple at first,
the full Mathematical concept and all the proofs need study to be fully understood. Here, we will directly use the tools
without the proofs. The question can be translated into the following: Find all the possible x and y pairs for which
a*x + b*y = d (1). This is a linear diophantine equation and has solutions if and only if d % GCD(a, b) = 0. With simple 
words, it would how many a's and b's can we add together to get d? Is there only one way to do it or more? If a = b = 0
and d!=0 then there are no solutions. If a=b=c=0 then there are infinite solutions. To solve this equation we use the
extended Euclidean algorithm to solve a*x' + b*'y = GCD(a, b). Then, an initial integer solution for (1) is going to be
x0 = x`*d/GCD(a, b) and y0 = y'*d/GCD(a,b). From this initial solution we can generate all the other solutions which
will be x = x0 + k*b/GCD(a, b) and y = y0 - k*a/GCD(a, b). We now need to find k so that we only have non negative
solutions.

0 <= x0 + k*b/GCD(a, b) => -x0 <= k*b/GCD(a, b) => -x'*d/GCD(a, b) <= k*b/GCD(a, b) => k >= -x'*d/b (2)
0 <= y0 - k*a/GCD(a, b) => y0 >= k*a/GCD(a, b) => y'*d/GCD(a, b) >= k*a/GCD(a, b) => k <= y'*d/a    (3)

From (2) and (3) we have: -x'*d/b <= k <= y'*d/a 

So, the final answer will be: number_of_solutions = floor(y'*d/a) - ceil(-x'*d/b) + 1. Why floor, ceil and + 1 you may
ask? Since k must be integer (don't get confused with the integer solution) it means that if -x'*d/b is a float number,
for example 2.2, then k >= 2.2 and the first integer that's bigger than 2.2 is 3. We follow the exact same logic to
understand the ceil. Finally, we add +1 because we already find an initial solution, x0, y0 that we didn't count. 

O(log(min(A, B)) to find x', y' and GCD(a, b).

Final complexity: O(log(min(A, B)) 
"""


def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_euclidean(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


from sys import stdin, stdout
from math import ceil, floor

t = int(stdin.readline())
for _ in range(t):
    a, b, d = map(int, stdin.readline().split())
    gcd, x, y = extended_euclidean(a, b)
    if d % gcd != 0:
        stdout.write(str(0) + "\n")
        continue

    first = ceil((-x)*d/b)
    second = floor(y*d/a)

    if first <= second:
        stdout.write(str(second - first + 1) + "\n")
    else:
        stdout.write(str(0) + "\n")
