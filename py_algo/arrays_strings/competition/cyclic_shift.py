"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/maximum-binary-number-cb9a58c1/

A large binary number is represented by a string A of size N and comprises of 0s and 1s. You must perform a cyclic shift
on this string. The cyclic shift operation is defined as follows: If the string A is [A0, A1, A2, ..., AN-1], then after
performing one cyclic shift, the string becomes [A1, A2, ..., AN-1, A0]. You performed the shift infinite number of
times and each time you recorded the value of the binary number represented by the string. The maximum binary number
formed after performing (possibly 0) the operation is B. Your task is to determine the number of cyclic shifts that can
be performed such that the value represented by the string A will be equal to B for the Kth time.

Input - Output:
The first line denotes the number of test cases.
For each test case:
First line: Two space-separated integers N and K.
Second line: A denoting the string.
For each test case, print a single line containing one integer
that represents the number of cyclic shift operations performed
such that the value represented by string A is equal to B for the Kth time.

Sample input:
2
5 2
10101
6 2
010101

Sample Output:
9
3
"""

"""
The important think to this problem is how many bits python uses for the binary representation of an integer. The answer
to this question is 32 bits. Thus, the number 10101 when shifted to the left would become 101010 which we is an unwanted
result. We would like to have the number 01011.To do that, we we will be using the mask 11111 in this particular example
but this can be further generalized. To perform a left cyclic shift, meaning that the binary number 1010, after 1 left
cyclic shift, must become 0101 and not 0100. To do that, we use the operation: mask and (bin << i or bin >> (bits - i)).
The "and" operation with the mask is needed as mentioned before to maintain the result in the bits' length range. From 
this point there are 2 cases. The first case is if there is no symmetry at all. For example, the binary number 1011 is
not symmetric and will become 0111, 1110, 1101, 1011. After 4 shifts, which is equal to the number of the bits of the 
number, we know that the maximum number is the number 1110, thus, from that point, at every 4 shifts we will arrive at
the same number. If there is a symmetry, it means that we will arrive at the maximum number in less than 4 steps (for
our example). For example, if the number is 1010, then after 2 shift we will arrive again at the same number and this
pattern will continue.

The complexity depends on the number of bits, thus it is insignificant.

Final complexity: O(1)
"""

inp_len = int(input())

for _ in range(inp_len):

    n, k = map(int, input().rstrip().split())
    a = input().rstrip()
    bits = len(a)
    mask = (1 << bits) - 1  # We find the mask by doing: 2^bits - 1, for example 2^5 - 1 = 31 = 11111.
    dec_a = int(a, 2)
    max_num = dec_a
    index = 0
    symmetric = 0

    for i in range(1, bits):
        temp = mask & (dec_a << i) | (dec_a >> (bits - i))

        # If the max is equal to temp then it means that there is some kind of symmetry
        # in the binary representation and we don't need full circular shifts to reach
        # again the maximum number.
        if temp == max_num:
            symmetric = i - index
            break

        if temp > max_num:
            max_num = temp
            index = i

    if symmetric > 0:
        print(index + symmetric * (k-1))
    else:
        print(index + (k-1) * bits)
