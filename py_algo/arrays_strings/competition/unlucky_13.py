"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/the-unlucky-13-d7aea1ff/

Write a program to calculate the total number of strings that are made of exactly N characters. None of the strings can
have "13" as a substring. The strings may contain any integer from 0 - 9, repeated any number of times.

Input - Output:
The first line denotes the number of test cases T.
Next T lines: Each contains an integer N.
Print the result of each query modulo1000000009.
Answer for each test case should come in a new line.

Sample input:
2
2
1

Sample Output:
99
10
"""

"""
We can have 10 different independent states for each number, from 0-9. For a series of numbers a1a2, there are 10^2
different combinations. We only need to subtract the number of times 13 appears, in that case 1 times, so the total
result would be 100 - 1 = 99. We can think of the problem as a recursion. In each step, we divide the answer by 2, so
that the final result will be the answer for the first half multiplied by the answer for the second half, minus the
times the first half ends with the number 1 and the second half begins with the number 3. The answers for the two halves
already contain all the other possibilities of the number's 13 appearance, so that's the only extra subtraction we need 
to do. We keep doing the same thing until we reach a base case, namely for n = 0, 1, where the answer is 1 and 10
respectively. We can also add a cache of the answers above the base cases for more speed. If n is even then the answer
for the 2 halves is the same, lets say ans1 and we also need to make the final subtraction. The 1 has to be at the end
of the first half and the 3 at the beginning of the second, giving us n - 2 numbers that can change. So, the only thing
we need to do is find the possible combinations for n - 2 numbers. If we split that in 2, that can be computed as the
answer for (n-2)//2 = n//2 - 1 multiplied by itself. Lets assume that the result is ans2. The final result is given by
the following formula, if n is even: result = ans1^2 - ans2^2. If n is odd, we once again multiply the answer for the
2 halves but this time is not the same. It is the answer for n//2 multiplied by the answer for n//2 + 1. For the
subtraction that we need to do, once again n - 2 numbers can change. If we split that in 2, we have the answer for
n//2 - 1 multiplied by the answer for n//2. Lets call the answers ans1, ans3, ans2 respectively. The final formula when
n is odd is: result = ans1*ans3 - ans1*ans2 = ans1*(ans3 - ans2).  

Final complexity: Undetermined
"""

# We create 2 cache's, one for the first 1000000 input
# and one for the rest.
# We do that for speed purposes, just
# because the problem didn't accept the solution for just a small margin.
cache = {}
cache2 = {}
mod = 1000000009


def ans(n):
    if n < 1000000:
        if n in cache:
            return cache[n]

        if n == 0:
            cache[n] = 1
            return cache[n]
        if n == 1:
            cache[n] = 10
            return cache[n]

        temp1 = ans(n//2)     # Split in half.
        temp2 = ans(n//2-1)   # Split in half to find the number of times 13 appears in the middle.

        if (n % 2) == 0:
            cache[n] = (temp1*temp1 - temp2*temp2) % mod
        else:
            temp3 = ans(n//2 + 1)
            cache[n] = (temp1 * (temp3 - temp2)) % mod

        return cache[n]
    else:
        if n in cache2:
            return cache2[n]

        if n == 0:
            cache2[n] = 1
            return cache2[n]
        if n == 1:
            cache2[n] = 10
            return cache2[n]

        temp1 = ans(n // 2)
        temp2 = ans(n // 2 - 1)

        if (n % 2) == 0:
            cache2[n] = (temp1 * temp1 - temp2 * temp2) % mod
        else:
            temp3 = ans(n // 2 + 1)
            cache2[n] = (temp1 * (temp3 - temp2)) % mod

        return cache2[n]


inp_len = int(input())

for i in range(inp_len):
    cache2 = {}
    n = int(input())
    print(ans(n))


"""
Consider we have 2 states, the happy states, h(n), which are strings that end with {0, 2, 3, 4, 5, 6, 7, 8, 9} and
the sad states, s(n), which are strings that end with {1}. We can transition with 9 different ways from a happy
state to a happy state (there are 0 restrictions) and with 8 different ways from a sad state to a happy one because 
being on a sad state means the character ended with 1 and we can go to every number from the happy state but the number
3, {0, 2, 4, 5, 6, 7, 8, 9} Following the same logic, we have only 1 way to reach a sad state from a happy one and the
same holds to reach a sad state from a sad state. The above can be written down as:

9 * h(n-1) + 8 * s(n-1) = h(n) } => [h(n)] = [9 8] *[h(n-1)] (Tried to write it down in array form as efficiently as
1 * h(n-1) + 1 * s(n-1) = s(n) }    [s(n)]   [1 1]  [s(n-1)]  possible.)
 
Our base cases are h(1) = 9 and s(1) = 1. If we keep doing the same thing we will have:

[h(n)] = [9 8]^2 *[h(n-2)] => [h(n)] = [9 8]^n-1 *[h(1)] => [h(n)] = [9 8]^n-1 * [1]  
[s(n)]   [1 1]    [s(n-2)]    [s(n)]   [1 1]      [s(1)]    [s(n)]   [1 1]       [1]  

This is called matrix exponentiation and as we can see, we need to make array multiplication and we need to make it as
fast as we can. That's why we need to write our own exponentiation function, which uses the exact same logic as the
default one and has a complexity of O(logN). The difference here will be the fact that we will mod the results in each
step of the exponentiation. The default logic is the following: 2^11 = 2 * (2^10) = 2 * ((2^5)^2), etc. This can easily
be written down with a recursive function and has a complexity of O(logN). For the final result we add the happy and sad
states and we mod the final result.

Keep in mind the following rules to better understand the mod operations we are using.

(A + B)modC = (AmodC + BmodC)modC (1)
(A * B)modC = (AmodC * BmodC)modC (2)
A ^ BmodC = ((AmodC) ^ B)modC     (3)
(-A)modC = (-A + C)modC           (4)
mod(x,y)= x-(y*int(x/y))          (5)

Multiplying an array n x m by an array m x p takes O(n*p*m) time. 
In our case the dimensions are insignificant and the complexity only comes from 
the exponentiation which is O(logN).

Final complexity: O(logN)
"""

# mod = 1000000009
#
#
# def mult(A, B):
#     # zip matches the elements at the same index into
#     # tuples and then we multiply them and after that
#     # comes the final sum
#     # For that to be efficient
#     # we need the B array to be transposed zip(*B)
#     # transposes the array B
#     result = [[sum((a * b) % mod for a, b in zip(A_row, B_col)) % mod
#                for B_col in zip(*B)]
#               for A_row in A]
#     return result
#
#
# def ans(n, array1):
#     if n == 1:                      # Base case
#         return array1
#
#     if n == 0:
#         return [[1, 0], [0, 1]]     # Base case
#
#     arr = ans(n//2, array1)
#     if n % 2 == 0:
#         return mult(arr, arr)
#     else:
#         return mult(mult(arr, arr), array1)
#
# inp_len = int(input())
# array1 = [[9, 8], [1, 1]]
# array2 = [[9], [1]]
#
# for _ in range(inp_len):
#     n = int(input())
#
#     a = ans(n-1, array1)                        # Do the matrix exponentiation.
#     array3 = mult(a, array2)                    # Do the final multiplication of the equation.
#     print((array3[0][0] + array3[1][0]) % mod)  # Add the happy and sad states.
