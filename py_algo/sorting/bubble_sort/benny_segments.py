# 100 mil / sec, so if n = 10000, we can have complexity of O(n^2)

inp_len = int(input())

for _ in range(inp_len):
    n, l = map(int, input().split())

    coord = []
    for _ in range(n):
        temp_coord = list(map(int, input().split()))
        coord.append(temp_coord)

    coord = sorted(coord, key=lambda element: element[0])
    found = False

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

