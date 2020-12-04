"""
Codemonk link: https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/practice-problems/algorithm/simran-and-stairs/

Simran is running up a staircase with N steps, and can hop(jump) either 1 step, 2 steps or 3 steps at a time.You have to
count, how many possible ways Simran can run up to the stairs.

Input - Output:
First line contains the number of steps N.
Output the number of possible ways Simran can go up the stairs.

Sample input:
4

Sample Output:
7
"""

"""
Solution with recursion. We can reach each stair of the staircase with 3 different ways, from the 3 stairs below the 
current. For each of the 3 stairs below, the same holds. We compute the result for the first 3 stairs "by hand" and then
with a recursive way, we find the result based on the above approach. The recursion stops when we reach the first 4
manually computed steps. 

Final complexity: Undetermined
"""


def count_steps(count):
    # For the first and second stairs, there 1 and 2 ways to get there.
    # For the third stair, there are 4 ways to get there.
    # For the rest stairs that we know, return the ways to get there.
    if count <= 2:
        steps[count] = count
        return steps[count]

    if count == 3:
        steps[count] = 4
        return steps[count]

    if steps[count]:
        return steps[count]

    # Lastly, call the function for the 3 previous steps.
    steps[count] = count_steps(count-1) + count_steps(count-2) + count_steps(count-3)
    return steps[count]


final_steps = int(input())
steps = [0] * max(final_steps + 1, 4)

print(count_steps(final_steps))
print(steps[0])


"""
Solution without recursion. The logic is the same.

Final complexity: O(N)
"""

# final_steps = int(input())
#
# steps = [0] * max(final_steps + 1, 4)
# steps[1] = 1
# steps[2] = 2
# steps[3] = 4
#
# for i in range(4, final_steps+1):
#     steps[i] = steps[i-1] + steps[i-2] + steps[i-3]
#
# print(steps[final_steps])
