"""
Codemonk link: https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/chinu-and-his-project/

A project was going on related to image processing and to perform experiments and get desired result the image needs to
be converted to Gray-Scale using a parameter 'x' and the function P(x) represented the Gray-Code and calculated via
x xor (x div 2) where xor stands for bitwise exclusive OR (bitwise modulo 2 addition), and div means integer division.
It is interesting to note that function P(x) is invertible, which means it is always possible to uniquely restore x
given the value of P(x). So the group working on the project forgot to keep the original data related to parameter 'x'.
Write a program to restore number x from the given value of P(x).

Input - Output:
The input file contains an integer number y, the value of G(x).
The output file should contain a single integer x such that G(x) = y.

Sample input:
15

Sample Output:
10
"""

"""
A straightforward solution with an example is the following. Suppose we have b(N-1) b(N-2) ... b(0), where N is the 
number of bits and b is the bit the (N-k) th position. Then x/2 is b(N-1) b(N-2) ... b(1) and the x ^ x div 2 is equal 
to b(N-1)^0 b(N-2)^b(N-1) b(N-3)^b(N-2) ... b(0)^b(1) and we know for a fact that this equals to our input which is a 
known number, for example 1011. This means, that we know b(N-1) and it is equal to 1. Now, we can move to b(N-2)^b(N-1),
we will have b(N-2)^1 = 0, so b(N-2) = 0 ^ 1 = 1. Remember that the inverse of XOR is XOR! If we continue doing that 
then we will find the desired value. This is a O(N) solution.

There is a faster approach though! For simplicity, suppose that we have the number b3 b2 b1 b0 = x and 0 b3 b2 b1 = x/2
Now lets take x ^ x div 2 = b3^0 b2^b3 b1^b2 b0^b1 = input = 1111 = 15. Lets now suppose that y = a3 a2 a1 a0 = 1111
and we keep dividing by 2, and XORing each time, so:

a3 a2 a1 a0 = 1 1 1 1, 
   XOR
0 a3 a2 a1 
   XOR          -----------------------------------------------------------------------------------------
0 0 a3 a2       |            We have  b3 = a3,  b2^b3 = a2,   b1^b2 = a1,  b0^b1 = a0 (1)               |
   XOR          | After all the XORs  a3 a2^a3 a1^a2^a3 a0^a1^a2^a3  (2)                                |
0 0 0 a3        |   From (1) and (2)  b3 b2^b3^b3 b1^b2^b2^b3^b3 b0^b1^b1^b2^b2^b3^b3 = b3 b2 b1 b0 = x |
   XOR          -----------------------------------------------------------------------------------------
0 0 0 0         So a3 = b3 = 1, b2^1 = 1, so b2 = 1^1 = 0 and by doing so we find 1010 = 10 = CORRECT!

Final complexity: O(logN)
"""

x = 0
y = int(input())

while True:
    x ^= y
    y //= 2

    if y == 0:
        break

print(x)
