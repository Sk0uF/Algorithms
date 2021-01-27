a, b = map(int, input().split())

result = 1
while b > 0:
    if b % 2 == 1:
        result = (result * a) % 1000000007

    a = (a ** 2) % 1000000007
    b //= 2

print(result)
