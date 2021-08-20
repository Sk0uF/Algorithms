"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/vaishu-and-queries-17506e73/

Vaishu is having set of red balls and blue balls arranged in N rows. Vaishu's brother Vibhu tries to mimic the same
arrangement of balls as Vaishu. So, he asks his dad to get same type of color balls for him too. But his father instead
started asking him queries of the following type. Son! Tell me how many maximum rows of balls you can mimic, if I buy
you X Red balls and Y Blue balls? Vibhu wants to answer these queries desperately and takes your help. Help him answer
his father's queries as quick as possible.

Input - Output:
First line of the input contains a single integer N denoting the number of rows in Vaishu's arrangement of balls.
Each of next N lines contains a string consisting of two types of characters: R and B where R denotes red colored b
alls and B denotes blue color balls.
Next line contain a single integer Q, denoting the number of queries that are being asked by Vibhu's father.
Each of the next Q line contains two space separated integers, X and Y denoting count of red and blue balls
respectively, his father wishes to buy for him.
For each query of type X Y, you need to print the maximum number of rows that can be mimicked by Vibhu if he
was to get X red balls and Y blue balls.

Sample input:
3
RRBB
BB
R
1
2 3

Sample Output:
2
"""

"""
At each step we try to either mimic the row or not. If we mimic it we continue with the new amount of balls ans we 
memoize the answer for each row and for the current amount of red and blue balls.

Final complexity: UNDETERMINED
"""


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
