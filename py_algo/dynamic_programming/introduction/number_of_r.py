"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/knapsack-with-large-weights-33a2433a/

As we all know RK loves his name very much especially the character 'R' so this time task for you is based on his
awesome name. RK gives you a string S consisting of characters 'R' and 'K' only. Now you are allowed to do exactly one
move that is you have to choose two indices i and j (1<=i<=j<=|S| where |S| is string length ) and flip all the
characters at position X where i<=X<=j. Now your goal is that after exactly one move you have to obtain the maximum
number of R's as RK loves this character very much. So help RK with maximum R's.

Input - Output:
The first line contains the number of test cases T.
Each test case contains a string S consisting of characters 'R' and 'K' only.
For each test case print the maximal number of R's that can be obtained after exactly one move.

Sample input:
2
RKKRK
RKKR

Sample Output:
4
4
"""

"""
If we consider every R to be -1 and every K to be 1 then we can simply implement Kadane's algorithm and find the 
largest continuous sub array we have to flip. If we add to this the starting amount of R's then we have our answer. That
problem can also be easily solved with a non dp solution by just counting the number of K's, if we find an R subtract
one from the count and if the count becomes less than 0 then reset the count to 0. If we add to that counter the amount
of R's then we once again have our answer.

Final complexity: O(N)
"""


def non_dp(inp):
    max_count = -1
    count = 0
    total = 0
    found = False

    for i in range(len(inp)):
        if inp[i] == "R":
            total += 1
            count -= 1
        else:
            found = True
            count += 1

        if count < 0:
            count = 0

        if count > max_count:
            max_count = count

    if found:
        print(max_count + total)
    else:
        print(len(inp) - 1)


def dp(inp):
    """
    Kadane’s Algorithm
    Largest Contiguous Sub-Array
    """
    count = 0
    inp = [-1 if inp[i] == "R" else 1 for i in range(len(inp))]
    for val in inp:
        if val == -1:
            count += 1

    dp_list = [0] * len(inp)
    dp_list[0] = inp[0]
    max_count = dp_list[0]

    for i in range(1, len(inp)):
        dp_list[i] = max(inp[i], inp[i] + dp_list[i-1])
        max_count = max(max_count, dp_list[i])

    print(max_count + count)
    print(dp_list)
    print(max_count, count)


t = int(input())
for _ in range(t):
    sequence = input()
    # non_dp(sequence)
    dp(sequence)
