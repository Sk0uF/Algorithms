def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_euclidean(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


from sys import stdin, stdout
from math import ceil, floor

t = int(stdin.readline())
for _ in range(t):
    a, b, d = map(int, stdin.readline().split())
    gcd, x, y = extended_euclidean(a, b)
    if d % gcd != 0:
        stdout.write(str(0) + "\n")
        continue

    first = ceil((-x)*d/b)
    second = floor(y*d/a)

    if first <= second:
        stdout.write(str(second - first + 1) + "\n")
    else:
        stdout.write(str(0) + "\n")
