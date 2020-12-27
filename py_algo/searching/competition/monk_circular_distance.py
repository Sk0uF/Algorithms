n = int(input())
distance = []
for _ in range(n):
    x, y = map(int, input().rstrip().split())
    distance.append((x**2 + y**2)**(1/2))

distance = sorted(distance)
q = int(input())
for _ in range(q):
    r = int(input())

    lower = 0
    upper = n - 1
    while lower <= upper:
        mid = (lower+upper) // 2

        if distance[mid] <= r:
            lower = mid + 1
        else:
            upper = mid - 1

    print(lower)