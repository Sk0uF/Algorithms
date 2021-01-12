"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/monk-and-chamber-of-secrets-6324dd92/

Hagrid says "follow the spiders" and so Harry and Ron head to the Forbidden Forest. There they meet Aragog, a giant
spider who tells them about the innocence of Hagrid. But Aragog only allows Hagrid to go back. These boys have got into
a serious trouble now. The only way to escape as Aragog says is to answer a question. Aragog shows them a queue of N
spiders of which only X spiders are to be selected. Each spider has some power associated with it. There are X
iterations on the queue. In each iteration, X spiders are dequeued (if queue has less than X entries, all of them will
be dequeued) and the one with maximum power is selected and remaining spiders are enqueued back to the queue (in the
order they were dequeued) but their power is decreased by one unit. If there are multiple spiders with maximum power in
those dequeued spiders, the one which comes first in the queue is selected. If at any moment, power of any spider
becomes 0, it can't be decremented any further, it remains the same. Now, Aragog asks the boys to tell him the positions
of all the selected spiders (positions in the initial given queue) in the order they are selected. As the boys are
frightened and can't think of anything , they call Monk for the rescue.

Input - Output:
The first line consists of two space separated integers N and X.
The next line consists of an array A.
For each of the X iterations, output the position of the selected
spider in that iteration. Position refers to the index at which the
spider was present in the initial given queue (1 based indexing).

Sample input:
6 5
1 2 2 3 4 5

Sample Output:
5 6 4 1 2
"""

"""
Crate a queue that has a pair of the elements and their initial positions. Enqueue the desired elements, find the max
based on the power, print its position, remove it, decrease all the others by 1 and enqueue them back with the correct
order.

Final complexity: O(X^2)
"""

n, x = map(int, input().rstrip().split())
spiders = list(map(int, input().rstrip().split()))

ans = []
queue = []
for i in range(n):
    queue.append([spiders[i], i])

for i in range(x):
    select = queue[:x]          # If x is bigger than n it is considered as -1.
    maximum = max(select, key=lambda power: power[0])
    max_index = maximum[1]
    select.remove(maximum)

    for j in range(len(select)):
        if select[j][0] > 0:
            select[j][0] -= 1

    queue = queue[x:] + select  # if x is bigger than n they array is considered empty.
    print(max_index+1, end=" ")
