"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/counting-frog-paths-1abd84d5/

There is a frog initially placed at the origin of the coordinate plane. In exactly 1 second, the frog can either move up
1 unit, move right 1 unit, or stay still. In other words, from position (x, y), the frog can spend 1 second to move to
(x+1, y), (x, y+1), (x, y). After T seconds, a villager who sees the frog reports that the frog lies on or inside a
square of side-length s with coordinates (X, Y), (X+s, Y), (X, Y+s), (X+s, Y+s). Calculate how many points with integer
coordinates on or inside this square could be the frog's position after exactly T seconds.

Input - Output:
The first and only line of input contains four space-separated integers: X, Y, s, and T.
Print the number of points with integer coordinates that could be the frog's position after T seconds.

Sample input:
2 2 3 6

Sample Output:
6
"""

"""
Scan the rectangle and find if the frog can end up in each tile.

Final complexity: O(S^2)
"""

x, y, s, t = map(int, input().strip().split())

end_x = x + s
end_y = y + s
total = 0

for i in range(x, end_x + 1):
    for j in range(y, end_y + 1):
        if t - (i + j) >= 0:
            total += 1

print(total)
