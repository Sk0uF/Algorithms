inp_len = int(input())
for _ in range(inp_len):
    n = int(input())
    if n == 1:
        print(0)
        continue

    visited = set()
    auxiliary = [n]
    c1, c2, c3 = -1, -1, -1
    lower = 0
    upper = 1
    steps = 0
    found = False
    while True:
        steps += 1
        for i in range(lower, upper):
            current = auxiliary[i]
            if current % 2 == 0:
                c1 = current // 2
                if c1 not in visited:
                    auxiliary.append(c1)
                    visited.add(c1)
            if current % 3 == 0:
                c2 = current // 3
                if c2 not in visited:
                    auxiliary.append(c2)
                    visited.add(c2)
            c3 = current - 1
            if c3 not in visited:
                auxiliary.append(c3)
                visited.add(c3)
            if c1 == 1 or c2 == 1 or c3 == 1:
                print(steps)
                found = True
                break

        if found:
            break

        lower = upper
        upper = len(auxiliary)
