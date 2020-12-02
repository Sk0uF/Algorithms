inp_len = int(input())

for _ in range(inp_len):
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))

    if b[0] <= a[-1]:
        print(0)
        continue

    final_value = 0
    for i in range(n):
        lower = 0
        upper = n - 1
        pos = -1
        while lower <= upper:
            mid = (lower+upper) // 2
            if b[mid] >= a[i]:
                pos = mid
                lower = mid + 1
            else:
                upper = mid - 1

        final_value = max(final_value, pos - i)

    print(final_value)


# inp_len = int(input())
#
# for _ in range(inp_len):
#     n = int(input())
#     a = list(map(int, input().strip().split()))
#     b = list(map(int, input().strip().split()))
#
#     if b[0] <= a[-1]:
#         print(0)
#         continue
#
#     final_value = 0
#     i = 0
#
#     for j in range(n):
#         if j >= i and b[j] >= a[i]:
#             final_value = max(final_value, j - i)
#         else:
#             i += 1
#             if i == n:
#                 break
#
#     print(final_value)
