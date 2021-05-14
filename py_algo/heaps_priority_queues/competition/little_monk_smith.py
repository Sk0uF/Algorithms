# https://www.hackerearth.com/problem/algorithm/little-monk-and-steve-smith-575a56dc/?utm_source=header&utm_medium=search&utm_campaign=he-search
from sys import stdin, stdout


def heapify(array, i):
    left_child = 2*i + 1
    right_child = 2*i + 2
    max_index = i

    if left_child < len(array):
        if (array[max_index][0] == array[left_child][0] and array[max_index][1] > array[left_child][1]) or \
                (array[max_index][0] < array[left_child][0]):
            max_index = left_child

    if right_child < len(array):
        if (array[max_index][0] == array[right_child][0] and array[max_index][1] > array[right_child][1]) or \
                (array[max_index][0] < array[right_child][0]):
            max_index = right_child

    if max_index != i:
        array[max_index], array[i] = array[i], array[max_index]
        heapify(array, max_index)


def create_heap(array):
    for i in range(len(array)//2-1, -1, -1):
        heapify(array, i)
    return array


def maintain_heap(array, delete=False):
    current_index = 0
    max_index = 0
    left_child = 1
    right_child = 2
    if delete:
        array[0], array[-1] = array[-1], array[0]
        array.pop()

    while True:
        if left_child < len(array):
            if (array[max_index][0] == array[left_child][0] and array[max_index][1] > array[left_child][1]) or \
                    (array[max_index][0] < array[left_child][0]):
                max_index = left_child

        if right_child < len(array):
            if (array[max_index][0] == array[right_child][0] and array[max_index][1] > array[right_child][1]) or \
                    (array[max_index][0] < array[right_child][0]):
                max_index = right_child

        if max_index != current_index:
            array[max_index], array[current_index] = array[current_index], array[max_index]
            current_index = max_index
            left_child = 2*max_index + 1
            right_child = 2*max_index + 2
        else:
            break


n, k = map(int, stdin.readline().split())
balls = list(map(int, stdin.readline().split()))
balls = [(balls[i], i+1) for i in range(n)]
balls = create_heap(balls)
priority = []

for i in range(k):
    while balls[0][0] == 0:
        maintain_heap(balls, delete=True)

    if i != k-1:
        stdout.write(str(balls[0][1]))
        stdout.write(" ")
    else:
        stdout.write(str(balls[0][1]))

    temp_ball = list(balls[0])
    balls[0] = (temp_ball[0]-1, temp_ball[1])
    maintain_heap(balls)
