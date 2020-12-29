"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/monk-being-monitor-709e0fd3/

Monk being the monitor of the class needs to have all the information about the class students. He is very busy with
many tasks related to the same, so he asked his friend Mishki for her help in one task. She will be given heights of all
the students present in the class and she needs to choose 2 students having heights h1 and h2 respectively, such that
h1 > h2 and difference between the number of students having height h1 and number of students having height h2 is
maximum. Note: The difference should be greater than 0. As Mishki has never been a monitor of the class, help her in the
same. If there exists such students then print the required difference else print "1" (without quotes).

Input - Output:
The first line will consists of one integer T, which denotes the number of test cases.
For each test case: One line consists of a integer N, denotes the number of students in the class.
Second line contains N space separated integers, where th integer denotes the height of the ith
student in the class.
For each test case, if the required difference exists then print its value, otherwise print -1.

Sample input:
1
6
3 1 3 2 3 2

Sample Output:
2
"""

"""
Sort the heights. After that, we can find the the desired value in linear time. Start iterating from the smaller to the
biggest height. Increase a counter when the height is the same. If it's not the same, the maximum difference of heights
is the maximum between our current maximum and counter - minimum, where the minimum is the minimum between our current
minimum number of heights and counter.

Final complexity: O(N)
"""

inp_len = int(input())

for _ in range(inp_len):
    n = int(input())
    heights = list(map(int, input().rstrip().split()))
    heights = sorted(heights)

    counter = 1
    min_val = 0
    max_val = -1
    first = True

    for i in range(1, len(heights)):
        if heights[i] == heights[i-1]:
            counter += 1
        else:
            # The first time we find a different value
            # we initialize our current min.
            if first:
                first = False
                min_val = counter
                counter = 1
                continue
            max_val = max(max_val, counter - min_val)
            min_val = min(min_val, counter)
            counter = 1

    # Account for the last heights, in case we
    # ended with a height that was the same as
    # the previous.
    if not first:
        max_val = max(max_val, counter - min_val)

    if max_val <= 0:
        # In case where all the heights were the same.
        print(-1)
    else:
        print(max_val)
