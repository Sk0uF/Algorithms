def bfs(array, begin, goal):
    start = 0
    end = 1
    queue = [-1] * 100001
    queue[0] = begin
    visited = [False] * 100001
    visited[begin] = True
    steps = [0] * 100001
    while start != end:
        current = queue[start]
        queue[start] = -1
        start += 1
        for i in range(len(array)):
            merge = (current*array[i]) % 100000
            if not visited[merge]:
                visited[merge] = True
                steps[merge] += steps[current] + 1
                if merge == goal:
                    return steps[merge]
                queue[end] = merge
                end += 1
    return -1


first_key, lock = map(int, input().split())
n = int(input())
keys = list(map(int, input().split()))
print(bfs(keys, first_key, lock))
