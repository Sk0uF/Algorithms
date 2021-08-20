"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/vaishu-and-tower-arrangements-fe7c349e

Vaishu is fond of building wooden towers. Currently, she has N wooden towers. Since, she is a big fan of uniformity, she
arranges the towers in such a way that the first few consecutive towers should be facing downwards and then after a
certain specific point, all should be facing upwards. But, there needs to be at least one tower facing in both upward
and downward directions. Now, Vaishu's notorious brother Vibhu has distorted the arrangement by toggling the direction
of few towers and made her pretty sad. He is feeling sorry and is ready to help her. But he is smart and knows that she
doesn't remember the number of towers that were arranged initially. So, he decided to toggle the direction of fewest
number of towers to make the uniform arrangement that she likes. Though the final arrangement may not be same as the
initial arrangement Vaishu had. Can you help her brother to toggle direction of minimum number of towers to make
arrangement she likes?

Input - Output:
First line of the input contains integer T denoting the number of test cases.
For each test case, there will be two separate lines.
First line of each test case contains N denoting the number of towers Vaishu had initially.
The next and the last line denotes an array of length N having values 1 and 1, where 1 denotes that tower is
facing downwards and 1 denotes tower is facing upwards.
For each test case, you need to print minimum number of towers her brother needs to toggle so that Vaishu's
uniform arrangement is sustained.

Sample input:
1
5
1 -1 1 1 -1

Sample Output:
2
"""

"""
That's a classic problem that can be solved by calculating 2 arrays, one that contains the maximum amount amount of
1's ending at each index and 1 that contains the maximum amount of -1's starting from each index. Iterating through the
whole array the answer can be given by ans = min(ans, ending[i] + starting[i+1]).

Final complexity: O(N)
"""

t = int(input())
for _ in range(t):
    n = int(input())
    towers = list(map(int, input().split()))
    neg = [0] * n
    pos = [0] * n
    if towers[0] == 1:
        pos[0] = 1

    if towers[-1] == -1:
        neg[-1] = 1

    for i in range(n-2, -1, -1):
        if towers[i] == -1:
            neg[i] = neg[i+1] + 1
        else:
            neg[i] = neg[i+1]

    ans = n
    for i in range(n-1):
        if towers[i] == 1:
            pos[i] = pos[i-1] + 1
        else:
            pos[i] = pos[i-1]

        ans = min(ans, pos[i] + neg[i+1])

    print(ans)
