"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/help-fredo/

Fredo is assigned a task today. He is given an array A containing N integers. His task is to update all elements of
array to some minimum value x, that is, A[i] = x ; 1 <= i <= N  such that product of all elements of this new array is
strictly greater than the product of all elements of the initial array. Note that x should be as minimum as possible
such that it meets the given condition. Help him find the value of x.

Input - Output:
The first line consists of an integer N, denoting the number of elements in the array.
The next line consists of N space separated integers, denoting the array elements.
The only line of output consists of the value of x.

Sample input:
5
4 2 1 10 6

Sample Output:
4
"""

"""
Let our number be x, then x^n > a1*a2*...*an
logx^n > log(a1*a2*...*an)
10^logx > 10^log(a1*a2*...*an)/n
x > 10^(log(a1) + log(a2) + ... + log(an))/n
Better to compute additions with log rather than big multiplication and then log. That's a good usage of log. Of course
we can use log2 or whatever log we want. The answer is int(10^(log(a1) + log(a2) + ... + log(an))/n) + 1

Final complexity: O(N)
"""

from math import log10

n = int(input())
array = [int(element) for element in input().strip().split()]

log_value = 0

for element in array:
    log_value += log10(element)

print(int(10 ** (log_value/n)) + 1)


"""
Based on the previous train of thought, we can directly do: x > (a1*a2*...*an) ^ 1/n => x > a1^1/n *...* an^1/n.

Final complexity: O(N)
"""

# l = 1
# for element in array:
#     l *= element**(1.0/n)
#
# print(int(l) + 1)
