"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/practice-problems/algorithm/monk-and-champions-league/

Monk's favourite game is Football and his favourite club is "Manchester United". Manchester United has qualified for the
Champions League Final which is to be held at the Wembley Stadium in London. So, he decided to go there and watch his
favourite team play. After reaching the stadium, he saw that many people have lined up for the match tickets. He knows
that there are M rows in the stadium with different seating capacities. They may or may not be equal. The price of the
ticket depends on the row. If the row has K(always greater than 0) vacant seats, then the price of the ticket will be K
pounds(units of British Currency). Now, every football fan standing in the line will get a ticket one by one. Given the
seating capacities of different rows, find the maximum possible pounds that the club will gain with the help of the
ticket sales.

Input - Output:
The first line consists of M and N. M denotes the number of seating rows in the stadium
and N denotes the number of football fans waiting in the line to get a ticket for the match.
Next line consists of M space separated integers X[1],X[2],X[3].... X[M] where X[i] denotes
the number of empty seats initially in the ith row.
Print in a single line the maximum pounds the club will gain.

Sample input:
5 4 4
2 8 5 1
9 10 5 1

Sample Output:
5 4 1 3
"""

"""
Simple use of priority queues with heap implementation. Think about it.

Final complexity: O(N*logN)
"""


def add_to_heap(array, i):
    if i % 2 == 0:
        parent = i//2 - 1
    else:
        parent = i // 2

    if parent >= 0:
        if array[parent] < array[i]:
            array[parent], array[i] = array[i], array[parent]
            if parent != 0:
                add_to_heap(array, parent)


def create_heap(array):
    for i in range(len(array)):
        add_to_heap(array, i)
    return array


def maintain_heap(array):
    max_index = 0
    current_index = 0
    left_child = 1
    right_child = 2

    while True:
        if left_child < len(array):
            if array[left_child] > array[max_index]:
                max_index = left_child

        if right_child < len(array):
            if array[right_child] > array[max_index]:
                max_index = right_child

        if max_index != current_index:
            array[max_index], array[current_index] = array[current_index], array[max_index]
            current_index = max_index
            left_child = 2*max_index + 1
            right_child = 2*max_index + 2
        else:
            break


m, n = map(int, input().split())
seats = list(map(int, input().split()))
seats = create_heap(seats)

total = 0
for _ in range(n):
    total += seats[0]
    seats[0] -= 1
    maintain_heap(seats)

print(total)


"""
Used the build in heapq to achieve the exact same goal with the same implementation. Note that instead of heapify we
used add_to_heap to build the priority queue, just because i was bored to implement heapify (not that it is harder).

Final complexity: O(N*logN)
"""
import heapq
m, n = map(int, input().split())
seats = list(map(int, input().split()))
for i in range(len(seats)):
    seats[i] = -1 * seats[i]

heapq.heapify(seats)

total = 0
for _ in range(n):
    total += seats[0]
    seats[0] += 1
    heapq.heapreplace(seats, seats[0])
print(-total)
