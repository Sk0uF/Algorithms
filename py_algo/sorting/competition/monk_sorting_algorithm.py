inp_len = int(input())
array = list(map(int, input().rstrip().split()))
max_elem = max(array)
mul = 1
step = 10**5

while max_elem:
    array = sorted(array, key=lambda x: (x//mul) % step)
    print(' '.join(map(str, array)))
    mul *= step
    max_elem //= step
