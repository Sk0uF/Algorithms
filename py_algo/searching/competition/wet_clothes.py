"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/wet-clothes-8a09a28e/

We have m completely wet clothes out under sunshine waiting to become dry. We are now at second t1 and it's raining.
It's going to rain again on seconds t2, ..., tn and after each rain clothes will be completely wet again. Cloth number i
needs ai seconds to become dry. We can go out and collect all dry clothes at any moment but can't do this more than g
times. What is the maximum number of clothes we can collect until second tn? Note that the duration of each rain is
almost zero, so we can ignore it. Also collecting clothes does not take any time from us.

Input - Output:
First line of input contains three integers n, m, g.
In the second line we have n increasing numbers denoting t1, ..., tn.
In the last line we have m numbers denoting a1, ..., am.
In a single line print the maximum number of clothes we can collect.

Sample input:
3 3 2
3 5 8
4 1 3

Sample Output:
2
"""

"""
Calculate all the time gaps between the rains and find the maximum. The key notice here is that we only need to collect
clothes on the maximum gap. That happens because we can collect any amount of clothes in that gap, so, at the maximum
gap we can collect all the clothes that we would be able to collect in the smaller gaps.

Final complexity: O(M)
"""

n, m, g = map(int, input().rstrip().split())
t = list(map(int, input().rstrip().split()))
a = list(map(int, input().rstrip().split()))
gaps = []

for i in range(n - 1):
    gaps.append(t[i+1] - t[i])

max_gap = max(gaps)
count = 0
for i in range(m):
    if a[i] <= max_gap:
        count += 1

print(count)
