inp_len = int(input())

for _ in range(inp_len):
    a, b, n = map(int, input().rstrip().split())
    calories = list(map(int, input().rstrip().split()))

    calories = sorted(calories)

    count_a = 0
    count_b = 0
    for i in range(n):
        if a >= calories[i]:
            a -= calories[i]
            count_a += 1
        if b >= calories[i]:
            b -= calories[i]
            count_b += 1

    if count_a > count_b:
        print("Raghu Won")
    elif count_a < count_b:
        print("Sayan Won")
    else:
        print("Tie")
