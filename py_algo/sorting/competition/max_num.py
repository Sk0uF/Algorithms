"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/max-num-6fbf414b/

You are given an array A of n elements A1, A2, ..., An. Let us define a function F(x) = ΣAi&x. Here, & represents
bitwise AND operator. You are required to find the number of different values of x for which F(x) is maximized. There
exists a condition for x that it must have exactly l bits sets in its binary representation. Your task is to find a
number of such values for which this function is maximized. Print the required number. If there are infinite such
numbers, then print -1.

Input - Output:
The first line contains the number of test cases.
The second line contains two space-separated integers n and l.
The third line contains the array.
There are T lines of the output. The only line of output for each
test case contains a single integer as described in the problem statement.

Sample input:
2
5 2
3 5 7 1 4
5 1
3 5 7 1 4

Sample Output:
2
1
"""

"""
The idea is the following. We know in advance the amount of set bits in the final number. We are going to use the bits
that give the biggest decimal result in our array. For example, if the numbers are [3, 5, 7, 1, 4], their binary
equivalent is [011, 101, 111, 001, 100]. The x we want to find must maximize the following: 011&x + 101&x + 111&x
+ 001&x + 100&x. If we just need 1 bit to be set, we have to find which bit from the available 3 gives the biggest
decimal value after the sum. The first bit is set in 3 numbers (101, 111, 100) giving a total of 4 + 4 + 4 = 12, meaning
that this is the biggest value it can contribute. The second bit is set in 2 numbers (011, 111) giving a total of 2 + 2 
= 4 and the third bit is set in 4 numbers (011, 101, 111, 001) giving a total of 1 + 1 + 1 + 1 = 4. It is obvious that x
must have the first bit set and this is the only solution. But what if we wanted x to have 2 bits set? In that case, the
obvious choice is the first bit but for the second set bit we can either choose the second one or the third one. That
gives us a total of 2 numbers that maximize our function. If l is a number bigger than the number of bits of our max
value in our array then there are infinite solutions. In our example, if l=4, then we choose the first 3 bits to be set
but then, for the fourth bit we can choose whichever we want and the result will still be the same (that bit will always
turn to 0 after the & with each number in our array because no number has it set). To sum up, we are always going to
choose the bits that give the biggest decimal value after the bitwise "and" and the sum and if there are more than 1
then we can directly use the bionimial coefficient to find the desired value. To further clarify the usage of the
bionimial coefficient, if we had for example the array [12, 8, 4, 4, 4, 4] (corresponding to the decimal values of the 
bits -we don't actually care about the position of the bits-) and l had to be 3, then we would choose 12, 8 and 4, but 
we would need to account for all the different 4's we can choose. In that case that would be the ways we can choose 1 
number from 4 numbers (we would have 12, 8, 4 or 12, 8, 4 or 12, 8, 4 or 12, 8, 4, so 4 different x numbers maximize
our function). If l had to be 4, then we would account the different ways we can choose 2 numbers from 4 numbers etc.

Lets analyze the complexity. We will consider nothing to be insignificant
at the beginning and will simplify things later.
O(T) for the input cases. O(30*N) for finding the decimal values of each
bit after the "and" and the sum. O(30log30) for the sorting. O(30) for 
looping through this array and O(3*N) for the bionimial function.
Note that every calculation happens inside the first "for" loop of the
test cases, meaning that we multiply the complexities to get the final 
result.

Final complexity: O(T*(30log30 + 30*N + 3*N)) => O(T*N)
"""


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i

    return fact


def bionimial(n, k):
    bion = factorial(n)//(factorial(k)*(factorial(n-k)))
    return bion


inp_len = int(input())
for _ in range(inp_len):
    n, l = map(int, input().rstrip().split())
    array = list(map(int, input().rstrip().split()))

    # Creating an array that will hold the total
    # decimal value for each bit.
    final_list = [0] * 30
    for element in array:
        for j in range(30):
            final_list[j] += element & (1 << j)

    final_list = sorted(final_list, reverse=True)
    final_list_len = len(final_list)

    element = final_list[l-1]
    count = 0
    index = 0
    if element == 0:
        print(-1)
    else:
        for i in range(final_list_len):
            if final_list[i] == element:
                count += 1
                if count == 1:
                    index = l - i
        print(bionimial(count, index))


"""
Same as the above, with a slightly different technique for finding the total decimal value of each bit.
"""
# from math import log2, ceil
#
#
# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact = fact * i
#
#     return fact
#
#
# def bionimial(n, k):
#     bion = factorial(n)//(factorial(k)*(factorial(n-k)))
#     return bion
#
#
# inp_len = int(input())
#
# for _ in range(inp_len):
#     n, l = map(int, input().rstrip().split())
#     array = list(map(int, input().rstrip().split()))
#
#     final_list = [0] * 30
#     for i in range(n):
#         num = array[i]
#         while num:
#             right_most = num ^ (num & (num - 1))
#             num = num & (num - 1)
#             final_list[int(log2(right_most))] += right_most
#
#     final_list = sorted(final_list, reverse=True)
#     final_list_len = len(final_list)
#
#     element = final_list[l-1]
#     count = 0
#     index = 0
#     if element == 0:
#         print(-1)
#     else:
#         for i in range(final_list_len):
#             if final_list[i] == element:
#                 count += 1
#                 if count == 1:
#                     index = l - i
#         print(bionimial(count, index))
