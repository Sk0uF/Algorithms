def binary_helper(partial_sums, lower, upper, x, i):
    while lower <= upper:
        mid = (lower+upper) // 2
        mid_value = partial_sums[mid]

        if i != 0:
            mid_value = partial_sums[mid+i] - partial_sums[i-1]

        if mid_value <= x:
            lower = mid + 1
        else:
            upper = mid - 1

    return lower, upper


n, x = map(int, input().rstrip().split())
a = list(map(int, input().rstrip().split()))

partial_sums = [a[0]]
for i in range(1, n):
    partial_sums.append(partial_sums[i-1] + a[i])

lower = 0
upper = n - 1
for i in range(n):
    lower, upper = binary_helper(partial_sums, 0, upper, x, i)

    if upper == n - i - 1:
        print(upper+1)
        break
