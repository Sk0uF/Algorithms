x, y, s, t = map(int, input().strip().split())

end_x = x + s
end_y = y + s
total = 0

for i in range(x, end_x + 1):
    for j in range(y, end_y + 1):
        if t - (i + j) >= 0:
            total += 1

print(total)