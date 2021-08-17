
# Bottom - Up
t = int(input())
for k in range(t):
    n = int(input())
    judges = list(map(int, input().split()))
    points = [0] * n
    if n == 1:
        print(f"Case {k+1}: {judges[0]}")
    elif n == 2:
        print(f"Case {k+1}: {max(judges[0], judges[1])}")
    else:
        points[0] = judges[0]
        points[1] = max(judges[0], judges[1])
        for i in range(2, n):
            points[i] = max(points[i-2] + judges[i], points[i-1])

        print(f"Case {k+1}: {points[-1]}")

# Top - Down
# import sys
# sys.setrecursionlimit(10 ** 6)
#
#
# def solve(index):
#     if index == 0:
#         return judges[0]
#
#     if index == 1:
#         return max(judges[0], judges[1])
#
#     if points[index] != -1:
#         return points[index]
#
#     points[index] = max(solve(index-2) + judges[index], solve(index-1))
#     return points[index]
#
#
# t = int(input())
# for k in range(t):
#     n = int(input())
#     judges = list(map(int, input().split()))
#     points = [-1] * n
#     print(f"Case {k+1}: {solve(n-1)}")
