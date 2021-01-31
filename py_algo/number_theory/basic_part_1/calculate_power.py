"""
Codemonk link: https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/practice-problems/algorithm/calculate-the-power/

Given two number A and B. Calculate the value of A^B. Output may be too large so print the answer modulo 10^9+7.

Input - Output:
Input contains two integers A and B separated by space.
Print value of AB modulo 10^9+7.

Sample input:
2 5

Sample Output:
32
"""

"""
Straight forward problem.

Final complexity: O(logB)
"""

a, b = map(int, input().split())

result = 1
while b > 0:
    if b % 2 == 1:
        result = (result * a) % 1000000007

    a = (a ** 2) % 1000000007
    b //= 2

print(result)
