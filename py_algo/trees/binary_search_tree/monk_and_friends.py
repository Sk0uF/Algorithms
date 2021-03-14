t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    students = list(map(int, input().split()))
    cache = {}
    for i in range(n):
        cache[students[i]] = 1

    for element in students[n:]:
        if element in cache:
            print("YES")
        else:
            print("NO")
            cache[element] = 1
