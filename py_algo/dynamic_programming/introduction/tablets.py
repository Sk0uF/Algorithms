# My thought:
# Begin from left to right and find only the increasing sequences.
# Then go from right to left and make corrections.
# e.g: 1 10 9 8 7 6 6 11 5 10 2 1 5
#      1  2 - - - - 1  2 1  2 - 1 2
#      1  5 4 3 2 1 1  2 1  3 2 1 2

n = int(input())
health_scores = []
for _ in range(n):
    health_scores.append(int(input()))


inc = True
current = 1
values = [1] * n
for i in range(len(health_scores)):
    if health_scores[i-1] < health_scores[i]:
        values[i] = values[i-1] + 1

total = values[-1]
for i in range(len(health_scores)-2, -1, -1):
    if health_scores[i+1] < health_scores[i] and values[i+1] >= values[i]:
        if health_scores[i+1] == health_scores[i]:
            values[i] = values[i+1]
        else:
            values[i] = values[i+1] + 1

    total += values[i]

print(total)
