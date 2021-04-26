# 8 7
# 1 2
# 3 4
# 1 3
# 5 6
# 7 8
# 5 8
# 4 8
def find_root_and_balance(array, value):
    # if array[value] != value:
    #     array[value] = find_root_and_balance(array, array[value])
    # return array[value]

    while array[value] != value:
        array[value] = array[array[value]]
        value = array[value]
    return array[value]


def disjoint_sets_array(n, m):
    disjoint_set = [i for i in range(n)]
    sizes = [1] * n
    cycles = 0
    for i in range(m):
        x, y = map(int, input().split())
        root_x = find_root_and_balance(disjoint_set, x-1)
        root_y = find_root_and_balance(disjoint_set, y-1)

        if root_x != root_y:
            if sizes[root_x] < sizes[root_y]:
                # disjoint_set[root_y] = root_y
                # and the same goes for root_x.
                # Think about it!
                disjoint_set[root_x] = disjoint_set[root_y]
                sizes[root_y] += sizes[root_x]
            else:
                disjoint_set[root_y] = disjoint_set[root_x]
                sizes[root_x] += sizes[root_y]
        else:
            cycles += 1

    print(disjoint_set)
    print(cycles)


n, m = map(int, input().split())
disjoint_sets_array(n, m)
