"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/monk-and-divisor-conundrum-56e0eb99/

Given an integer array A of size N, Monk needs you to answer T queries for him. In each query, he gives you 2 integers
P and Q. In response to each of these queries, you need to tell Monk the count of numbers in array A that are either
divisible by P, Q, or both. For example if the P, Q = 2, 3 and the array is 2, 3, 6 then the answer is 3 and not 4.

Input - Output:
The first line contains a single integer N denoting the size of array A.
The next line contains N space separated integers, where the ith integer
denotes A[i]. The next line contains a single integer T denoting the number
of queries Monk poses to you. Each of the next T lines contains 2 space
separated integers P and Q. For each query, print the answer on a new line.

Sample input:
6
2 3 5 7 4 9
2
4 5
3 7

Sample Output:
2
3
"""

"""
In problems like that one, we have to compute values for the whole range of possible numbers because we only have one
array but many queries. It would be a waste to compute values for every query. At first, we have to notice that answer
can be given by finding all the numbers that are divided by p, add them to all the numbers that are divided by q and 
subtract all the double counts, for all the numbers that are divided by both. A OR B = A + B - A AND B. We can find
these number in O(1) time if we compute some values at the beginning. We create an array of length equal to the biggest
number in our array and note the frequency of the numbers. For example, if the array is 1, 5, 5, 8, then our array will 
be [0, 1, 0, 0, 0, 2, 0, 0, 1]. Now comes the first awesome part. We can loop through the array we just created and find
the amount of multiples of every number inside that array (which are the numbers that are divided by that number) in 
O(NlogN) time where N is length of that array. How is tha possible? For each number, we skip to next multiple. The first
time, this will run N times, because the first number will be 1 (we begin from 1 and to from 0). The next time, we begin
from 2 and then 4, 6, 8, etc, meaning this will run N/2 times. This keeps going until it runs 1 time. We basically have
N + N/2 + N/3 + N/4 + ... + 1 => N * (1 + 1/2 + 1/3 + 1/4 + 1/N) => O(NlogN). The next awesome part, is that we can find
the lowest common divisor of p and q, by finding the GCD of p and q. We have that GCD * LCM = p * q and thus we derive
LCM(p, q) = p*q/GCD(p, q). If we save the amount of multiples for number into an array then we can directly answer for 
every p and q. Be careful because p, q and lcm might not be in the range of our array, in which case, the ones that are 
not in the range will yield 0.

O(MAX) to create the frequencies array, O(MAXlogMAX) to
create the amount of multiples of every number in that array
and O(log(min(a, b))) to find the GCD

Final complexity: O(MAX + MAXlogMAX + log(min(a,b))) => O(MAXlogMAX)
"""

from sys import stdin, stdout


def euclidean_gcd(a, b):
    if b == 0:
        return a

    return euclidean_gcd(b, a % b)


n = int(stdin.readline())
array = list(map(int, stdin.readline().split()))
num_max = max(array)
auxiliary = [0] * (num_max+1)
frequencies = [0] * (num_max+1)

for i in range(n):
    frequencies[array[i]] += 1


# 1+1/2+...1/N - approx: O(logN)
# N + N/2 + N/3 + N/4 +...+ 1 => N * (1+1/2+...1/N) - approx: O(N*logN)
for i in range(1, num_max+1):
    for j in range(i, num_max+1, i):
        auxiliary[i] += frequencies[j]

t = int(stdin.readline())
for _ in range(t):
    p, q = map(int, input().split())
    lcm = (p*q)//euclidean_gcd(p, q)
    if p > num_max:
        first = 0
    else:
        first = auxiliary[p]

    if q > num_max:
        second = 0
    else:
        second = auxiliary[q]

    if lcm > num_max:
        cross_section = 0
    else:
        cross_section = auxiliary[lcm]

    stdout.write(str(first + second - cross_section) + "\n")
