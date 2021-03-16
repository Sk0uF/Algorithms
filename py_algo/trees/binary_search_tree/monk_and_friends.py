"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/monk-and-his-friends/

Monk is standing at the door of his classroom. There are currently N students in the class, ith student got Ai candies.
There are still M more students to come. At every instant, a student enters the class and wishes to be seated with a
student who has exactly the same number of candies. For each student, Monk shouts YES if such a student is found, NO
otherwise.

Input - Output:
First line contains an integer T. T test cases follow.
First line of each case contains two space-separated integers N and M.
Second line contains N + M space-separated integers, the candies of the students.
For each test case, output M new line, Monk's answer to the M students.
Print "YES" (without the quotes) or "NO" (without the quotes) pertaining to the Monk's answer.

Sample input:
1
2 3
3 2 9 11 2

Sample Output:
NO
NO
YES
"""

"""
The solution is straight forward. Think of it.

Final complexity: O(T*(N+M))
"""

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    students = list(map(int, input().split()))
    cache = {}
    for i in range(n):
        cache[students[i]] = 1

    for element in students[n:]:
        if element in cache:
            print("YES")
        else:
            print("NO")
            cache[element] = 1
