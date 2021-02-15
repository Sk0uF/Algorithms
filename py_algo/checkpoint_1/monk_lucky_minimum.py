# https://www.hackerearth.com/problem/algorithm/monk-and-lucky-minimum-3-8e22f1cb/

t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))

    count = 0
    num_min = min(array)
    for i in range(n):
        if num_min == array[i]:
            count += 1

    if count % 2 == 0:
        print("Unlucky")
    else:
        print("Lucky")
