n = int(input())
k = int(input())
aux = set()
for _ in range(k):
    i, j = map(int, input().split())
    aux.add(j)

print(n-len(aux))
