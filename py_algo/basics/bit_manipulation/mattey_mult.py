"""
Codemonk link: https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/mattey-multiplication-6/

We need to write the multiplication N * M, in the format (N<<p1) + (N<<p2) + ... + (N<<pk) where p1 >= p2 >= ... >= pk
and k is minimum.

Input - Output:
First line contains the number of test cases.
The next line contains the integers N,M.
The output is explained above.

Sample input:
2
2 1
2 3

Sample Output:
(2<<0)
(2<<1) + (2<<0)
"""

"""
To solve this problem, we find the binary representation of M, for e.g. N = 2 and M = 3, so M = 11 and then we do the
multiplication 2 * (11) = 2 * 2^1 + 2 * 2^0 = 2 << 1 + 2 << 0

We will consider the input length significant and the same as N and M. The bin function has complexity O(logN).
The first "for" statement will have O(N) and the other for statements are insignificant.

Final complexity: O(N*logN)
"""

inp_len = int(input())

for k in range(inp_len):
    num1, num2 = map(int, input().rstrip().split())

    needed_result = num1 * num2

    bin_num2 = (bin(num2))[2:]
    count = len(bin_num2) - 1
    set_bits_pos = []

    for i in range(len(bin_num2)):
        if bin_num2[i] == "1":       # Note the position of set bits
            set_bits_pos.append(i)

    last_set_bit = max(set_bits_pos)
    cnt = 0
    for bit in bin_num2:
        # If statement to determine when we reach the last set bit
        # That way we will stop printing the "+" sign
        if bit == "1" and (last_set_bit - cnt) != 0:
            print("(" + str(num1) + "<<" + str(count) + ") + ", end="")
        elif bit == "1" and (last_set_bit - cnt) == 0:
            print("(" + str(num1) + "<<" + str(count) + ")")
        count -= 1
        cnt += 1
