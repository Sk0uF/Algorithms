t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    array = list(map(int, input().split()))
    distinct = set(array)
    if len(distinct) == x:
        print("Good")
    elif len(distinct) > x:
        print("Average")
    else:
        print("Bad")
