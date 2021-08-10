# https://www.hackerearth.com/problem/algorithm/vaishu-and-queries-17506e73/

def solve(index, current_red, current_blue):
    if current_red < 0 or current_blue < 0:
        return -100

    if index == n:
        return 0

    if dp[index][current_red][current_blue] != -1:
        return dp[index][current_red][current_blue]

    red_count = red[index]
    blue_count = blue[index]

    ans = max(solve(index+1, current_red, current_blue),
              1 + solve(index+1, current_red-red_count, current_blue-blue_count))

    dp[index][current_red][current_blue] = ans
    return ans


n = int(input())
red = [0] * n
blue = [0] * n
dp = [[[-1 for _ in range(102)] for _ in range(102)] for _ in range(n)]
for i in range(n):
    row = input()
    red[i] = row.count("R")
    blue[i] = row.count("B")

q = int(input())
for _ in range(q):
    x, y = map(int, input().split())
    print(solve(0, x, y))
