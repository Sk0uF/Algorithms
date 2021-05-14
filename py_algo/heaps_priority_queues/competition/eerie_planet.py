# https://www.hackerearth.com/practice/data-structures/queues/basics-of-queues/practice-problems/algorithm/weird-planet-2000a170/
h, c, q = map(int, input().split())
crew = []

for _ in range(c):
    crew_h, s, e = map(int, input().split())
    crew.append((crew_h, s, e))

max_height = max(crew, key=lambda x: x[0])[0]

for _ in range(q):
    hi, ti = map(int, input().split())
    if hi > max_height:
        print("YES")
    else:
        ans = "YES"
        for member in crew:
            if member[1] <= ti <= member[2] and member[0] >= hi:
                ans = "NO"
                break

        print(ans)