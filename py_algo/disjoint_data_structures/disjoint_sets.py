def disjoint_sets_array_1(n, m):
    disjoint_set = [-1] * n
    cycles = 0
    for i in range(m):
        x, y = map(int, input().split())
        index_x = x-1
        index_y = y-1
        while disjoint_set[index_x] >= 0 or disjoint_set[index_y] >= 0:
            if disjoint_set[index_x] >= 0:
                index_x = disjoint_set[index_x]

            if disjoint_set[index_y] >= 0:
                index_y = disjoint_set[index_y]

        if index_x != index_y:
            if disjoint_set[index_x] <= disjoint_set[index_y]:
                disjoint_set[index_x] += disjoint_set[index_y]
                disjoint_set[index_y] = index_x
            else:
                disjoint_set[index_y] += disjoint_set[index_x]
                disjoint_set[index_x] = index_y
        else:
            cycles += 1

    print(disjoint_set)
    print(cycles)


def disjoint_sets_array_2(n, m):
    disjoint_set = []
    sizes = []
    for i in range(n):
        disjoint_set.append(i)
        sizes.append(1)

    cycles = 0
    for i in range(m):
        x, y = map(int, input().split())
        root_x = disjoint_set[x-1]
        root_y = disjoint_set[y-1]

        if sizes[root_x] < sizes[root_y]:
            disjoint_set[root_x] = disjoint_set[root_y]
            sizes[root_y] += sizes[root_x]
        else:
            disjoint_set[root_y] = disjoint_set[root_x]
            sizes[root_x] += sizes[root_y]

    print(disjoint_set)
    print(cycles)


n, m = map(int, input().split())
disjoint_sets_array_2(n, m)
