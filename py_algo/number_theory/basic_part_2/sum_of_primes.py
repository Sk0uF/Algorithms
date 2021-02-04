"""
Codemonk link: https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-2/practice-problems/algorithm/sum-of-primes-7/description/

We define the function F(l, r) = Σχ where x is a prime number between l and r inclusive. In short, we need to find the
summation of all the primes inside the range defined by r and l.

Input - Output:
The first line contains a single integer N denoting the number of queries.
Each of the next N lines contains two integers l and r.
For each query, output the answer on a new line.

Sample input:
2
1 6
4 13

Sample Output:
10
36
"""

"""
Using Eratosthenes sieve we find all the primes in the whole range, from 0 to 10^6 and then we create the partial sums
array. Afterwards, given l and r, we can directly answer each query. 

O(MAX_NUM*loglogMAX_NUM) for the sieve, O(MAX_NUM) for
the partial sums array and O(N) to answer all the queries.

Final complexity: O(MAX_NUM*loglogMAX_NUM + MAX+NUM + N) => O(MAX_VAL*loglogMAX_VAL) 
"""

from sys import stdin, stdout

# Basic Eratosthenes sieve implementation.
num_max = 1000001
primes = [True] * num_max
primes_sum = [0] * num_max
primes[0] = False
primes[1] = False

for i in range(2, int(num_max ** 0.5)):
    if primes[i]:
        for j in range(i * i, num_max, i):
            primes[j] = False

# Find the summation of all primes.
for i in range(num_max):
    if primes[i]:
        primes_sum[i] = i + primes_sum[i - 1]
    else:
        primes_sum[i] = primes_sum[i - 1]

# Using stdin for large amount of data is faster.
# Since n can be 5*10^5 that's our case.
for i in range(int(stdin.readline())):
    l, r = map(int, stdin.readline().split())
    stdout.write(str(primes_sum[r] - primes_sum[l - 1]) + "\n")
