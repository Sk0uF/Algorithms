def finder(target):
    array = []
    start = 1
    end = 1
    found = False
    for i in range(1, n):
        if roads[i - 1] == target:
            if not found:
                start = i
                end = i
            end += 1
            found = True
        else:
            if found:
                array.append([start, end])
                start = end
            found = False

    if found:
        array.append([start, end])

    return array


n = int(input())
roads = list(map(int, input().split()))
auxiliary_1 = [1] * n
auxiliary_2 = [1] * n

right = finder(1)
for i in range(len(right)):
    for j in range(right[i][0], right[i][1]+1):
        auxiliary_1[j-1] += right[i][1] - j

left = finder(0)
for i in range(len(left)):
    for j in range(left[i][0], left[i][1] + 1):
        auxiliary_1[j - 1] += abs(left[i][0] - j)

for i in range(len(roads)):
    if roads[i] == 1:
        roads[i] = 0
    else:
        roads[i] = 1

right = finder(1)
for i in range(len(right)):
    for j in range(right[i][0], right[i][1]+1):
        auxiliary_2[j-1] += right[i][1] - j

left = finder(0)
for i in range(len(left)):
    for j in range(left[i][0], left[i][1] + 1):
        auxiliary_2[j - 1] += abs(left[i][0] - j)

q = int(input())
which_aux = 0
for _ in range(q):
    query = input()
    if len(query) == 1:
        which_aux += 1
        which_aux %= 2
    else:
        query, element = query.split()
        element = int(element)
        if which_aux == 0:
            print(auxiliary_1[element-1])
        else:
            print(auxiliary_2[element - 1])
