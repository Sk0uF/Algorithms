def two_2d_minimum_cost_path():
    """
    Find the minimum cost path in a 2D array (moving right or bottom)
    Complexity: O(N^2)
    """
    cost = [[5, 4, 10, 2], [3, 1, 5, 6], [10, 2, 5, 3], [3, 1, 1, 7]]
    min_cost = [[0] * 4 for _ in range(4)]
    min_cost[0][0] = cost[0][0]

    for j in range(1, 4):
        min_cost[0][j] = min_cost[0][j-1] + cost[0][j]

    for i in range(1, 4):
        min_cost[i][0] = min_cost[i-1][0] + cost[i][0]

    for i in range(1, 4):
        for j in range(1, 4):
            min_cost[i][j] = min(min_cost[i-1][j], min_cost[i][j-1]) + cost[i][j]

    return min_cost[-1][-1]


print(two_2d_minimum_cost_path())


def two_2d_number_of_ways():
    """
    Find the number of ways we can reach each cell in a 2D grid
    Complexity: O(N^2)
    """
    num_ways = [[0] * 10 for _ in range(10)]
    num_ways[0][0] = 1

    for j in range(1, 10):
        num_ways[0][j] = 1

    for i in range(1, 10):
        num_ways[i][0] = 1

    for i in range(1, 10):
        for j in range(1, 10):
            num_ways[i][j] = num_ways[i-1][j] + num_ways[i][j-1]

    return num_ways[-1][-1]


print(two_2d_number_of_ways())


def two_2d_number_of_ways_blocked():
    """
    Find the number of ways we can reach each cell in a 2D grid
    containing blocked positions
    Complexity: O(N^2)
    """
    num_ways = [[0] * 10 for _ in range(10)]
    num_ways[3][5] = -1  # Blocked position
    num_ways[0][7] = -1
    num_ways[7][2] = -1

    for j in range(1, 10):
        if num_ways[0][j-1] == -1:
            num_ways[0][j] = -1
        else:
            num_ways[0][j] = 1

    for i in range(1, 10):
        if num_ways[i-1][0] == -1:
            num_ways[i][0] = -1
        else:
            num_ways[i][0] = 1

    for i in range(1, 10):
        for j in range(1, 10):
            if num_ways[i][j] == -1:
                continue

            if num_ways[i][j-1] != -1:
                num_ways[i][j] += num_ways[i][j-1]

            if num_ways[i-1][j] != -1:
                num_ways[i][j] += num_ways[i-1][j]

    return num_ways[-1][-1]


print(two_2d_number_of_ways_blocked())


def two_2d_number_of_points(points):
    """
    Find the number of points collected by 2 people in a 2D grid
    Complexity: O(N^2)

    In that problem we have 2 persons beginning from (0, 0) and (n, 0), they
    can meet only once and we have to find the maximum points collected by both
    without taking in account the meeting place. We consider in this problem

    Person1:                            Person2:
    (i,j-1)-->(i,j)-->(i,j+1)           (i,j-1)-->(i,j)-->(i,j+1)
    (i,j-1)-->(i,j)-->(i+1,j)           (i,j-1)-->(i,j)-->(i-1,j)
    (i-1,j)-->(i,j)-->(i,j+1)           (i+1,j)-->(i,j)-->(i,j+1)
    (i-1,j)-->(i,j)-->(i+1,j)           (i+1,j)-->(i,j)-->(i-1,j)

    Meeting:
    1) (i,j-1)-->(i,j)-->(i,j+1) and (i+1,j)-->(i,j)-->(i-1,j)
    2) (i-1,j)-->(i,j)-->(i+1,j) and (i,j-1)-->(i,j)-->(i,j+1)
    """
    n = 3
    m = 3

    # We allocate more space so that we can avoid wasting "for" loops for the first initialization.
    p1_start = [[0 for _ in range(m+2)] for _ in range(n+2)]
    p1_end = [[0 for _ in range(m+2)] for _ in range(n+2)]

    p2_start = [[0 for _ in range(m+2)] for _ in range(n+2)]
    p2_end = [[0 for _ in range(m+2)] for _ in range(n+2)]

    # Person1 start to end.
    for i in range(1, n+1):
        for j in range(1, m+1):
            p1_start[i][j] = max(p1_start[i-1][j], p1_start[i][j-1]) + points[i-1][j-1]

    # Person1 end to start.
    for i in range(n, 0, -1):
        for j in range(m, 0, -1):
            p1_end[i][j] = max(p1_end[i+1][j], p1_end[i][j+1]) + points[i-1][j-1]

    # Person2 start to end.
    for i in range(n, 0, -1):
        for j in range(1, m+1):
            p2_start[i][j] = max(p2_start[i+1][j], p2_start[i][j-1]) + points[i-1][j-1]

    # Person2 end to start.
    for i in range(1, n+1):
        for j in range(m, 0, -1):
            p2_end[i][j] = max(p2_end[i-1][j], p2_end[i][j+1]) + points[i-1][j-1]

    # We use both person1 arrays and both person2 arrays to not take in account the meeting point.
    # The meeting cell can range from 2 <= i <= n-1 and 2 <= j <= m-1.
    # We consider every point to be a meeting point.
    ans = 0
    for i in range(2, n):
        for j in range(2, m):
            op1 = p1_start[i][j-1] + p1_end[i][j+1] + p2_start[i+1][j] + p2_end[i-1][j]
            op2 = p1_start[i-1][j] + p1_end[i+1][j] + p2_start[i][j-1] + p2_end[i][j+1]
            ans = max(ans, max(op1, op2))

    return ans


print(two_2d_number_of_points([[100, 100, 100], [100, 1, 100], [100, 100, 100]]))


def edit_distance(s1, s2):
    """
    Levenshtein distance
    Complexity: O(len(s1)*len(s2))
    """
    n = len(s1)
    m = len(s2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for j in range(1, m):
        dp[0][j] = j

    for i in range(1, n):
        dp[i][0] = i

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])

    return dp[-1][-1]


print(edit_distance("kittfgen", "sitting"))
