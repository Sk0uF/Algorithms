def lower_bound(lower, upper, a, num):
    while lower < upper:
        mid = (lower+upper) // 2
        if a[mid] >= num:
            upper = mid
        else:
            lower = mid + 1
    return lower  # Can return upper as well.


def upper_bound(lower, upper, a, num):
    while lower < upper:
        mid = (lower + upper) // 2
        if a[mid] <= num:
            lower = mid + 1
        else:
            upper = mid
    return lower  # Can return upper as well.


n = int(input())
a = list(map(int, input().rstrip().split()))
q = int(input())

a = sorted(a)
for _ in range(q):
    query, num = map(int, input().rstrip().split())

    if query == 0:
        if num > a[-1]:
            print(0)
            continue
        elif num <= a[0]:
            print(n)
            continue
        print(n - lower_bound(0, n - 1, a, num))
    else:
        if num >= a[-1]:
            print(0)
            continue
        elif num < a[0]:
            print(n)
            continue
        print(n - upper_bound(0, n - 1, a, num))
