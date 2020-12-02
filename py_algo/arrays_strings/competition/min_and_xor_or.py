"""
Given an array A of N integers, find out the minimum value of the following expression for all valid i, j.
(Ai and Aj) xor (Ai or Aj), where i != j

Input - Output:
The first line denotes the number of test cases.
For each test case:
First line contains a single integer N, denoting the size of the array.
Second line contains N space separated integers A1, A2, ..., An.
For each test case, print a single line containing one integer
that represents the minimum value of the given expression.

Sample input:
2
5
1 2 3 4 5
3
2 4 7

Sample Output:
1
3
"""

"""
Lets expand the operation, (AB) xor (A + B) = AB(~A)(~B) + (~A + ~B)(A + B) = (~A + ~B)(A + B) = A xor B. Now then,    
suppose the given array is the following: 8 2 9 1 7 4 12. We will prove that if we sort the array, 1 2 4 7 8 9 12, then
by xoring each pair, 1 xor 2, 2 xor 4, 4 xor 7 etc, one of the resulted values will be the minimum. To prove that, 
suppose we have three values, A <= C <= B. Let A = 169, C = 185 and B = 187. Let i be the leftmost (biggest) index such
that A[i] differs from B[i].

A = 1010 1001
B = 1011 1011
C = 1011 1001

There are 2 cases now:

1) C[i] = A[i] = 0. Then (A XOR C)[i] = 0 and (A XOR B)[i] = 1. This implies (A XOR C) < (A XOR B).

2) C[i] = B[i] = 1. Then (B XOR C)[i] = 0 and (A XOR B)[i] = 1. This implies (B XOR C) < (A XOR B).

A[i] cannot be 1 because then B[i] has to be 0. This is the first bit that they differ and because B > A, B[i] must be 1
and A[i] 0.
"""

inp_len = int(input())

for _ in range(inp_len):
    n = int(input())
    a = list(map(int, input().rstrip().split()))

    a = sorted(a)
    min_val = float("inf")

    for i in range(n-1):
        min_val = min(min_val, a[i] ^ a[i+1])

    print(min_val)
