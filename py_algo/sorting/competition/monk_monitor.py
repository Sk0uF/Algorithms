inp_len = int(input())

for _ in range(inp_len):
    n = int(input())
    heights = list(map(int, input().rstrip().split()))
    heights = sorted(heights)

    counter = 1
    min_val = 0
    max_val = -1
    first = True

    for i in range(1, len(heights)):
        if heights[i] == heights[i-1]:
            counter += 1
        else:
            if first:
                first = False
                min_val = counter
                counter = 1
                continue
            max_val = max(max_val, counter - min_val)
            min_val = min(min_val, counter)
            counter = 1

    if not first:
        max_val = max(max_val, counter - min_val)
    if max_val <= 0:
        print(-1)
    else:
        print(max_val)

