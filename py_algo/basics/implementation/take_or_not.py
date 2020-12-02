"""
Codemonk link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/totakeornottotake/

We have B balloons. For each balloon, we can choose to take it or not. If we take the ballon, then we take the energy
noted by a certain operation. The operations are +, -, *, / and N, which means we take the negated value we previously
had. We begin by having a starting value of +1.

Input - Output:
The first line contains an integer N denoting the number of test cases.
The first of every test case contains B, which is the number of the balloons.
The B lines that follow, contain the operations of each balloon.
For each test case, output the maximum energy (meaning the max value) we can take
by choosing the right balloons.

Sample input:
2
3
N
- 2
N
3
- 1
* 4
/ 2

Sample Output:
3
4
"""

"""
We can get a big value be either increasing our starting value (* and +) or decreasing it (-, / and * if it's already
negative) and then at the first N operation we change the value. For example, if the starting value is 1 and at the
first N we have reached +5 or -10, then by choosing the the N operation we can have a value of +10. It becomes clear
that we need to choose the N operation for both our values and continue accordingly. This means that we will have +5,
-10, -5 and +10. From this point we can keep only the maximum and minimum values and continue increasing or decreasing
them.

The constraints for our values are low. We consider them having an upper bound of N.
O(N) for the first and second "for".

Final complexity: O(2*N) => O(N)
"""

inp_len = int(input())

for k in range(inp_len):
    ballons_len = int(input())
    max_score_arr = [1, 1]

    for i in range(ballons_len):
        temp_ballon = input().split()

        temp = 0
        for j in range(len(max_score_arr)):
            if j % 2 != 0:
                if temp_ballon[0] == "-":
                    max_score_arr[j] -= int(temp_ballon[1])
                elif temp_ballon[0] == "*":
                    max_score_arr[j] *= int(temp_ballon[1])
                elif temp_ballon[0] == "/" and max_score_arr[j] > 0:
                    max_score_arr[j] //= int(temp_ballon[1])
                elif temp_ballon[0] == "N":
                    max_score_arr[0] = max(max_score_arr[0], -max_score_arr[j])
                    max_score_arr[1] = min(max_score_arr[1], temp)
                    # max_score_arr.append(-max_score_arr[j])
                    # max_score_arr.append(temp)
            else:
                if temp_ballon[0] == "+":
                    max_score_arr[j] += int(temp_ballon[1])
                elif temp_ballon[0] == "*":
                    max_score_arr[j] *= int(temp_ballon[1])
                elif temp_ballon[0] == "N":
                    temp = -max_score_arr[j]

    print(max(max_score_arr))
