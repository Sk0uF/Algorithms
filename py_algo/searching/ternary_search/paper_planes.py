"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/searching/ternary-search/practice-problems/approximate/paper-planes-8cb51f55/

Two paper planes are thrown upwards simultaneously. You are provided with the following data:
The flight time of both planes is denoted by t (seconds).
The initial coordinates of the first plane are denoted by (bx, by, bz).
The initial velocity of the first plane is denoted by (bvx, bvy, bvz).
The initial coordinates of the second plane are denoted by (mx, my, mz).
The initial velocity of the second plane is denoted by (mvx, mvy, mvz).
Write a program to find the minimum distance between the two planes during their flight. Let the jury answer be A and
let your answer be B. Your answer will be considered correct if |A - B| <= 10^6

Input - Output:
First line: t.
Second line: Three space-separated integers (denoting bx, by, and bz).
Third line: Three space-separated integers (denoting bvx, bvy, and bvz).
Fourth line: Three space-separated integers (denoting mx, my, and mz).
Fifth line: Three space-separated integers (denoting mvx, mvy, and mvz).
Print the minimum distance between the two planes during their flight.

Sample input:
20
10 10 10
-1 -1 -1
-10 -10 -10
1 1 1

Sample Output:
0.000000
"""

"""
Find the distance function and substitute the positions with the function for linear smooth motion (x = x0 + v*t). Then,
implement ternary sort from 0 to t. Why does this work? The distance function in this particular example is unimodal.
The two airplanes either are going to directly move apart from each other, or they are going to get close to each other
and then apart from each other. If this doesn't make sense to your intuition then you can try proving it by 
differentiating the distance function. If you do that though, there will be no point of using ternary search!

Final complexity: O(log3/2(T/e)
"""


def dist(time):
    d = (((b_x + bv_x*time) - (m_x + mv_x*time))**2
         + ((b_y + bv_y*time) - (m_y + mv_y*time))**2
         + ((b_z + bv_z*time) - (m_z + mv_z*time))**2) ** (1/2)

    return d


t = int(input())
b_x, b_y, b_z = map(int, input().rstrip().split())
bv_x, bv_y, bv_z = map(int, input().rstrip().split())
m_x, m_y, m_z = map(int, input().rstrip().split())
mv_x, mv_y, mv_z = map(int, input().rstrip().split())


lower = 0
upper = t
precision = 0.0000001
while upper - lower > precision:
    first_third = lower + (upper - lower) / 3
    second_third = upper - (upper - lower) / 3

    if dist(first_third) < dist(second_third):
        upper = second_third
    else:
        lower = first_third

print(dist(lower))
