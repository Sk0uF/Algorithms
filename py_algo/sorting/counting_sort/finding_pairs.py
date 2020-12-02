
inp_len = int(input())

for _ in range(inp_len):
    n = int(input())

    array = list(map(int, input().rstrip().split()))
    helper_array = [0] * (2*10**6)

    total_amount = n

    for element in array:
        if element >= 0:
            helper_array[element + 10**6 - 1] += 1
        else:
            helper_array[-element] += 1
    for help in helper_array:
        if help > 0:
            total_amount += (help-1)*help//2

    print(total_amount)