"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/little-monk-and-steve-smith-575a56dc/

Little Monk knows what a dangerous batsman the captain of Australia, Steven Smith is. The bigger problem is that Monk
and his team have no idea about the weakness of Smith. But their coach tells them Smith's trick of scoring runs. His
trick is pretty simple: he is going to score maximum runs off bowlers who have minimum balls left to be bowled. For
instance, if there are three bowlers -- with 10, 11, 6 balls left respectively in their quota, then Smith would be able
to score maximum runs off bowler number 3, then bowler number 1 and then bowler number 2. Let's say bowler 2 bowls the
first ball so he'll also have 10 balls remaining, similar to bowler number 1. Now bowler 2 and bowler 1 are on the same
number of balls remaining, any of them can bowl the next delivery. But, Monk as the captain in such a case prefers the
bowler with in order of occurrence. So, the next ball will be bowled by bowler 1. So as the captain of the team, Monk
needs to know the order of bowlers so that Smith scores minimum runs possible off the K balls he is going to face!
Note: None of the bowlers can get Steven Smith out. Also, they are not allowed to bowl once their number of deliveries
left is 0.

Input - Output:
The first line contains two integers N and K, which denote the number of bowlers
faced by Smith and the total number of balls Smith is going to play.
The next line contains N space separated integers denoting the quota of each bowler.
Print K space separated integers denoting the order of the bowlers chosen by Monk. The bowlers are 1-indexed.

Sample input:
3 6
6 6 6

Sample Output:
1 2 3 1 2 3
"""

"""
Typical implementation of a priority queue. Think about it. 

Final complexity: O(Q*logN)
"""

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
