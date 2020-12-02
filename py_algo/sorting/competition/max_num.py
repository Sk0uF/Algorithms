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
