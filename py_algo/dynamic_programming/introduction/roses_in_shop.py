# n = int(input())
# smell = list(map(int, input().split()))
# score = [0] * n
# score[0] = 1
# start = 0
# end = 0
# found = False
#
# # Initialization
# if smell[1] > smell[0]:
#     score[1] = 2
#     end = 1
# else:
#     score[1] = 1
#     found = True
#
#
# for i in range(2, n):
#     # If we find a bigger element we have to check if we can remove
#     # the previous. It would be pointless to do so if we didn't just
#     # move the start and end indices and the previous value isn't 1.
#     if smell[i] > smell[i-1]:
#         if not found:
#             score[i] = score[i-1] + 1
#             end += 1
#         else:
#             # If we can remove the element because then the previous
#             # will be bigger then we find the new value based on the
#             # indices and then we move them.
#             if smell[i] > smell[i-2]:
#                 score[i] = end - start + 2
#                 start = i-1
#                 end = i
#             # In other case we just move the indices and add 1 to the
#             # previous value.
#             else:
#                 start = i-1
#                 end = i
#                 score[i] = score[i-1] + 1
#             found = False
#     # If we find a smaller element we have to reset.
#     else:
#         # If we can't remove the element because then the previous
#         # will still be bigger then we have a value of 1.
#         # When we have multiple such elements in a row we have to move the
#         # start and end counters to the current index.
#         if smell[i-2] >= smell[i]:
#             score[i] = 1
#             if found:
#                 start = i
#                 end = i
#             found = True
#         # If we can remove the element then we find the value
#         # and once again move the start and end counters to the current index.
#         else:
#             score[i] = end - start + 1
#             found = False
#             start = i
#             end = i
#
# print(max(score))


n = int(input())
smell = list(map(int, input().split()))
pre = [1] * n
suff = [1] * n
ans = 1

for i in range(1, n):
    if smell[i] > smell[i-1]:
        pre[i] = pre[i-1] + 1
        ans = max(ans, pre[i])

for i in range(n-2, -1, -1):
    if smell[i+1] > smell[i]:
        suff[i] = suff[i+1] + 1
        ans = max(ans, suff[i])

for i in range(1, n-1):
    if smell[i-1] < smell[i+1]:
        ans = max(ans, pre[i-1]+suff[i+1])

print(ans)
