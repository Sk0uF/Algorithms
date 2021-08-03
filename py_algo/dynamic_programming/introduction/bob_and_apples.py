t = int(input())
n, m = map(int, input().split())
for _ in range(n):
    apples = []
    v, p = map(int, input().split())
    apples.append((v, p))
    apples = sorted(apples, key=lambda x: x[0], reverse=True)

