# https://www.hackerearth.com/problem/algorithm/little-monk-and-abd-56f25965/
n = int(input())
scores = list(map(int, input().split()))
scores = sorted(scores)
q = int(input())
for _ in range(q):
    index, q_type = input().split()
    index = int(index) - 1

    if q_type == "S":
        print(scores[index])
    else:
        index += 1
        print(scores[-index])
