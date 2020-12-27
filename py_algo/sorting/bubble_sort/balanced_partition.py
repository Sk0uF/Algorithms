"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/practice-problems/algorithm/balanced-partition-818edecd/

There are n people in a village. The location of each house in the village can be given as (xi, yi)  in the Cartesian
coordinate plane. There are hi persons living in the ith house. Central electricity authority of the village is set to
built a wire line across the village. The wire line is supposed to constructed in a way such that it is the north-east
direction. In other words the wire line is parallel to the line x=y. Given that the construction of such line is
considered to be effective only if the number of persons living in its left and right side are equal, can you tell if
the construction of such wire line is possible?
Note: If the wire line passes through any house, the house is not considered in either half.

Input - Output:
First line contains the number of test cases.
The first line of each test case contains n, the
number of house in the village. Next n lines contain
xi, yi, hi, space separated.
Print YES or NO for every test case.

Sample input:
3
3
-1 1 3
-2 1 1
1 -1 4
3
1 1 2
-1 1 1
1 -1 2
4
0 2 3
-1 1 2
0 1 2
3 1 5

Sample Output:
YES
NO
YES
"""

"""
We first observe that it would be much easier if we had to find a line parallel to y axis. Lucky for us, we can
transform all the points to their equivalent points if they were rotated by 45 degrees. In this case, we only care about
the new x coordinates of the houses. We make sure to add the people for all the same x coordinates. At this point, we
have the amount of people for each different x coordinate, for example a dictionary with key values all the different x
coordinates and with values the amount of people for each respective key value. We sort the x coordinates of this
dictionary and we begin "drawing" lines from the leftmost coordinate while counting the total amount of people temp up 
to this point. If temp at any point equals half the total people, we have found a solution. If temp is bigger than 
the total amount of people at any point then we check if 2*temp - people_at_point equals the total people, meaning that
we consider this line to pass through this x coordinate, negating all its people. If that's the case, then we have a
solution, otherwise we don't. It's pointless continuing further because temp is only going to increase further.

Rotating cartesian system: x' = x * cos(theta) - y * sin(theta)
                           y' = y * cos(theta) + x * sin(theta)

Considering input cases insignificant, we have 
O(N) for the second "for" statement, O(NlogN) for the sorting and
O(N/2 + 1) for the last "for" statement.

Final complexity: O(N + NlogN + N/2 + 1) => O(NlogN)
"""

inp_len = int(input())

for _ in range(inp_len):
    n = int(input())
    people = {}
    total_people = 0
    for _ in range(n):
        x, y, h = map(int, input().split())
        people[x - y] = people.get(x - y, 0) + h
        total_people = total_people + h

    half_people = total_people // 2
    temp_people = 0
    for key in sorted(people.keys()):
        temp_people = temp_people + people[key]

        if temp_people >= half_people:
            if temp_people > half_people:
                if total_people == 2 * temp_people - people[key]:
                    print('YES')
                else:
                    print('NO')
            else:
                print('YES')
            break
