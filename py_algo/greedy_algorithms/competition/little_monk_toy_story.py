# https://www.hackerearth.com/problem/algorithm/little-monk-and-his-toy-story-f9f49f23/

n = int(input())
w = list(map(int, input().split()))
w = sorted(w)
count = 0
length = 0
row_sum = 0
prev_row_sum = 0
row_total = 0
prev_row_total = 0
while length < n:
    row_sum += w[length]
    row_total += 1
    if row_sum > prev_row_sum and row_total > prev_row_total:
        count += 1
        prev_row_sum = row_sum
        prev_row_total = row_total
        row_total = 0
        row_sum = 0
    length += 1

print(count)
