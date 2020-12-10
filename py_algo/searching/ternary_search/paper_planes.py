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