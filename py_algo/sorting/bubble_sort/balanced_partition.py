# Rotating cartesian system: x' = x * cos(theta) - y * sin(theta)
#                            y' = y * cos(theta) + x * sin(theta)
# After we rotate we need to find lines parallel to y
# So we all the houses that have the same x coordinate
# We then find the average and we sort based on x
# Now, we begin from the leftmost house and if we have that the people are equal to half the total houses
# then we have a solution. If the people are more, then we negate the last house because the line can pass through it
# and once again if the total amount of houses is equal to 2 times the houses we already have - the people in the current house
# we have a solution. We keep doing that for each house, each time adding the people from our left side.

inp_len = int(input())

for _ in range(inp_len):

    n = int(input())
    houses = {}
    total_houses = 0
    for _ in range(n):
        x, y, l = map(int, input().split())
        houses[x - y] = houses.get(x - y, 0) + l
        total_houses = total_houses + l

    average_houses = total_houses // 2
    temp_houses = 0

    for key in sorted(houses.keys()):
        temp_houses = temp_houses + houses[key]

        if temp_houses >= average_houses:
            if temp_houses > average_houses:
                if total_houses == 2 * temp_houses - houses[key]:
                    print('YES')
                else:
                    print('NO')
            else:
                print('YES')
            break