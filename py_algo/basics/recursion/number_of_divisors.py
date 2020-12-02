"""
Codemonk link: https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/practice-problems/algorithm/k-excess-1-be669e5a/

You are given two numbers n and k. For each number in the interval [1, n], your task is to calculate its largest divisor
that is not divisible by k. Print the sum of these divisors.Note that k is a prime number.

Input - Output:
First line contains the number of test cases.
The next lines contain the integers n and k.
Print the sum of the divisors.

Sample input:
4
10 3
10 2
10 5
1000000000 97

Sample Output:
41
36
43
494897959532893312
"""

"""
We first observe that if the number ni < k or it is not perfectly divisible by k, then we need to add ni in the sum. To
begin, we can find the sum of all the numbers in arr = [1, ..., n] by simple doing n*(n+1)/2. We now are sure that we 
need to subtract all the values ni that are perfectly divisible by k. How many are these numbers? Simply n//k. Which are
these numbers? 1*k, 2*k, ..., n//k * k. What is the sum of those numbers? 1*k + 2*k + ... + n//k * k = k * (1 + 2 + ...
+ n//k) = k * (n//k * (n//k + 1))//2. For these numbers, we need to add the correct values. We know that k is a prime 
number, meaning that it can only by divided by itself and by 1. For every ni that is perfectly divisible by k, that 
means that the number ni is a multiple of k, or in other words, it can be expressed like ni = i*...*k. So, we can be
sure that if we remove the k from the number which is equal to dividing ni by k, the number that will occur will be the
maximum that is not divisible by k. If the are 2 or more k's in ni, then we have to once again divide by k. If k wasn't
a prime number, even if we did divide by k, then there would be a chance that the number would still be divisible by k.
For example lets take the array n = [1, ..., 20] and see the result for k = 3 and k = 4. If k = 3, then the multiples of
k are 3, 6, 9, 12, 15, 18. From these, 3, 6, 12, 15 contain only one k, 1*3, 2*3, 4*3, 5*3 and so the answer would be
1, 2, 4, 5. The numbers 9 and 18 contain 2 k's, 3*3 and 3*3*2, so we have to divide to 2 times by k. If k = 4, then the
numbers that are multiple of k are, 4, 8, 12, 16, 20. From these, 4, 8, 12, 20 contain only one k, 1*4, 2*4, 3*4, 4*5
but the answer is not 1, 2, 3, 5. This happens because even if we divide by a non prime number, there can still exist
numbers in the factorization that are multiple of the non prime number that we divided with. With a prime number, no
such possibility exists. This problem can be solved with recursion. In each step we find the total sum, we subtract the
values of the multiples of k and and we call again the function but with n = n//k, meaning that we remove the k from all
the multiples of k. We continue this process until the array is 0.

Final complexity: Undetermined
"""


def divisor(n, k):
    if n == 0:
        return 0

    # If n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, then 3, 6, 9 are multiples of k
    # By doing 10//3 = 3, we have n = [1, 2, 3] = [3/3, 6/3, 9/3]
    jump = n//k
    return divisor(jump, k) + n * (n+1) // 2 - k * jump * (jump+1) // 2


inp_len = int(input())

for _ in range(inp_len):
    n, k = map(int, input().rstrip().split())

    print(int((divisor(n, k))))
