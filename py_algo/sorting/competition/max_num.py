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


Final complexity:
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
