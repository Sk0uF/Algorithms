def non_dp(inp):
    max_count = -1
    count = 0
    total = 0
    found = False

    for i in range(len(inp)):
        if inp[i] == "R":
            total += 1
            count -= 1
        else:
            found = True
            count += 1

        if count < 0:
            count = 0

        if count > max_count:
            max_count = count

    if found:
        print(max_count + total)
    else:
        print(len(inp) - 1)


def dp(inp):
    '''
    Kadane’s Algorithm
    Largest Contiguous Sub-Array
    '''
    count = 0
    inp = [-1 if inp[i] == "R" else 1 for i in range(len(inp))]
    for val in inp:
        if val == -1:
            count += 1
    dp_list = [0] * len(inp)
    dp_list[0] = inp[0]
    max_count = dp_list[0]

    for i in range(1, len(inp)):
        dp_list[i] = max(inp[i], inp[i] + dp_list[i-1])
        max_count = max(max_count, dp_list[i])

    print(max_count + count)


t = int(input())
for _ in range(t):
    sequence = input()
    non_dp(sequence)
    # dp(sequence)
