"""
Codemonk link: https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-2/practice-problems/algorithm/ashu-and-prime-factors-4/description/

Ashu is very fond of Prime numbers and he like challenging his friends by giving them various problems based on
Mathematics and Prime number. One of his friend Harshit is jealous and challenges him to solve a task. Task is: Given a
prime number X, you need to give the count of all numbers in range 1 to 10^6 inclusive which have minimum prime factor
X.

Input - Output:
First line consist of numer of test cases T.
Each test case contains a single number X.

Sample input:
2
2
11

Sample Output:
500000
20779
"""

"""
We are going to use a simple modification in Eratosthenes sieve and mark the minimum prime divisor for each number as
well as how many numbers this prime divides. This will run in O(MAX_VAL*loglogMAX_VAL) and then we need O(T) time to 
access those numbers. 

Final complexity: O(MAX_VAL*loglogMAX_VAL + T) => O(MAX_VAL*loglogMAX_VAL) 
"""

max_val = 10 ** 6
min_prime_factor = [0] * (max_val + 1)
ans = [0] * (max_val + 1)

for i in range(2, int(max_val**0.5)+1):
    if min_prime_factor[i] == 0:
        for j in range(i * i, max_val + 1, i):
            if min_prime_factor[j] == 0:
                min_prime_factor[j] = i
                ans[i] += 1

t = int(input())
for _ in range(t):
    x = int(input())
    print(ans[x]+1)
