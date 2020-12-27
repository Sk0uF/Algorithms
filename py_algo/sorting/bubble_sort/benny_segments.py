"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/practice-problems/algorithm/benny-and-segments-marcheasy/

One day Benny was walking and realized that her life was boring. Everything was grey, even roads in the best park were
grey. Therefore she decided to make roads a little bit brighter. She know that every road in the park is a segment
laying on the X axis with coordinates Xl, Xr (Xl ≤ Xr). Roads may intersect or overlap. She chooses any subset of roads
and paints them in red. After that she wants to get one continuous red segment. As she really likes number L the length
of this segment has to be equal to L. Your task is to determine if it is possible to choose some subset of roads and
paint them to get one red segment with the length equal to L? If it's possible print in a single line "Yes"
(without quotes), otherwise print "No" (without quotes).

Input - Output:
The first line contains one integer T - the number of test cases.
Each test case starts with two integers N and L, denoting the number
of roads and Benny's favorite number L. The next N lines contain two
Print Yes or No.

Sample input:
2
5 3
1 2
2 3
3 4
1 5
2 6
2 3
1 2
2 6

Sample Output:
No
No
"""

"""
The constraints allow us to implement a naive solution. Sort all the points based on their starting coordinate. Then,
begin from each point and keep moving to the right. A move to the right is only possible if the ending point is in 
between the next's point starting and ending position. Find the length when making this movement. If at any particular
point we find the desired length, we stop the algorithm and print Yes, otherwise, we will print No after the algorithm
finishes.
 
Note: In the example, [2, 3] and [1, 5] seem to give the desired length but this segment is not continues because it
completely ignores some distance in the second array. That's why we sort based on the starting position. Thus, the
answer for the first test case is No and not Yes.

O(NlogN) for the sorting and O(N^2) for the nested
"for" loops. It's O(N^2) because it will run N + N-1
+ N-2 + ... + 1 times => N*(N+1)/2 times.

Final complexity: O(NlogN + N^2) => O(N^2)
"""

inp_len = int(input())

for _ in range(inp_len):
    n, l = map(int, input().split())

    coord = []
    for _ in range(n):
        temp_coord = list(map(int, input().split()))
        coord.append(temp_coord)

    coord = sorted(coord, key=lambda element: element[0])
    found = False
    print(coord)
    for i in range(n):
        if found:
            break

        starting_point = coord[i][0]
        ending_point = coord[i][1]

        for j in range(i, n):
            if ending_point < coord[j][0] or ending_point > coord[j][1]:
                continue

            total_len = coord[j][1] - starting_point
            ending_point = coord[j][1]

            if total_len == l:
                print("Yes")
                found = True
                break

    if not found:
        print("No")
