"""
Codemonk link: https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/danny-and-his-loneliness/

We have an array of integers. In this array, all the numbers appear even amount of times, except one that appears odd
amount of times. Find this number.

Input - Output:
First line contains the n (2*n+1 is the array length)
Print the required number.

Sample input:
2
1 2 3 2 1

Sample Output:
3
"""

"""
We solve this problem by using the XOR operation. XOR is commutative and associative, A XOR 0 = A and A XOR A = 0. That
means that by XORing all the values of the array a[0] xor a[1]... xor a[2*n] we will get the number that appears odd
amount of times.

O(N) for the "for" statement.

Final complexity: O(N)
"""

inp_len = 2 * int(input()) + 1
inp_array = list(map(int, input().rstrip().split()))
num = inp_array[0]

for i in range(1, inp_len):
    num = num ^ inp_array[i]

print(num)


"""
A harder version of the problem is when we have 2 numbers that appear odd amount of times. To solve this problem, we
first XOR all the values of the array. The number we get is the odd1 XOR odd2. In this number, every set bit means
that the numbers that we XORed had different bit values. So, if we XOR all the numbers that have the same LSB as 
the number odd1 XOR odd2, we are sure that all will appear even amount of times except one, the odd1 or the odd2. This
way we will get the 1 of the 2 numbers. If we XOR all the other numbers that don't the same LSB as the odd1 XOR odd2
we will get the second needed number. Note that we can do the same for whichever set bit we want. Finding the LSB is 
easier though.

O(N) and O(N) for the "for" statements.

Final complexity: O(2*N) = O(N)
"""

# harder_array = [4, 1, 5, 4, 8, 1, 9, 9]
# harder_len = len(harder_array)
# num = harder_array[0]
#
# for i in range(1, harder_len):
#     num = num ^ harder_array[i]
#
# lsb = num ^ (num & (num - 1))
# num1 = num2 = num
#
# for i in range(harder_len):
#     temp_lsb = harder_array[i] ^ (harder_array[i] & (harder_array[i] - 1))
#
#     if lsb == temp_lsb:
#         num1 = num1 ^ harder_array[i]
#     else:
#         num2 = num2 ^ harder_array[i]
#
# print(num1, num2)
