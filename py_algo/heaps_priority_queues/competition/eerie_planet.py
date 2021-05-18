"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/queues/basics-of-queues/practice-problems/algorithm/weird-planet-2000a170/

You own a club on eerie planet. The day on this planet comprises of H hours. You appointed C crew members to handle the
huge crowd that you get, being the best club on the planet. Each member of the crew has fixed number of duty hours to
work. There can be multiple or no crew members at work at any given hour of the day. Being on weird planet, the rules of
this club cannot be normal. Each member of the crew only allows people who are taller than him to enter the club when he
is at work. Given the schedule of work and heights of the crew members, you have to answer Q queries. Each query
specifies the time of entry and height of a person who is visiting the club. You have to answer if the person will be
allowed to enter the club or not.

Input - Output:
First line of the input contains 3 integers H, C, Q. Representing number of hours in a day, number of crew members and
number of queries respectively.
Next C lines follow, where each line contains 3 integers hi, Si, Ei , representing height of the crew member and start
and end hour of his/her work schedule. He/she works for hours [Si, Ei] both inclusive.
Next Q lines follow, each containing 2 integers hi, ti representing height and time (in hour) of the person trying to
enter the club.
Q lines, each line containing "YES" or "NO", without the quotes, answering if the person will be allowed to enter the
club or not.

Sample input:
10 1 5
50 2 6
10 1
10 2
50 5
51 6
100 10

Sample Output:
YES
NO
NO
YES
YES
"""

"""
Solved with the naive way. Solve it with priority queues if the test cases become harder and disallow N^2 time.  

Final complexity: O(N^2)
"""

h, c, q = map(int, input().split())
crew = []

for _ in range(c):
    crew_h, s, e = map(int, input().split())
    crew.append((crew_h, s, e))

max_height = max(crew, key=lambda x: x[0])[0]

for _ in range(q):
    hi, ti = map(int, input().split())
    if hi > max_height:
        print("YES")
    else:
        ans = "YES"
        for member in crew:
            if member[1] <= ti <= member[2] and member[0] >= hi:
                ans = "NO"
                break

        print(ans)