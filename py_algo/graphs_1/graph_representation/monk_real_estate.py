inp_len = int(input())
for _ in range(inp_len):
    edges = int(input())
    count = set()
    for _ in range(edges):
        city1, city2 = map(int, input().split())
        count.add(city1)
        count.add(city2)

    print(len(count))
