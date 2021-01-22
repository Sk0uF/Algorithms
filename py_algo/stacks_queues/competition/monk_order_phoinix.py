"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/monk-and-order-of-phoenix-72814f05/

Voldemort has a big army, so he has maintained his people in N rows to fight Harry's army. Each row contains the heights
of the fighters and is sorted in non-decreasing order from the start to end, except for the first row, which may contain
the heights of the fighters in any order, as it contains all the legendary fighters. During the war, at any time period,
Voldemort can remove a fighter from any row, and can also add any new fighter to any row (maintaining the non-decreasing
order of heights. except in the first row).Voldemort will never remove any fighter from an empty row. Voldemort can only
remove or add a fighter from/to the end of row. Now Harry has a special wand which can kill exactly N fighters in one go
but with following conditions: There should be exactly N fighters, and exactly one fighter (which can be anyone in the
row) should be chosen from each row. The first fighter can only be chosen from the first row, the second one from second
row, and so on. Basically the ith fighter should be chosen from ith the row, where i ranges from 1 to N. The order of
the heights of the chosen fighters should be strictly increasing. Now Harry wants to know whether he can kill N fighters
using special wand. As Harry is busy in fighting Voldemort, he gave this task to Monk.

Input - Output:
The First line consists of a single integer N denoting the number of stacks.
In each of the next N lines, first integer X denotes the size of the stack,
followed by the X space separated integers denoting the heights of the fighters in the stack.
The next lines consists of single integer Q, denoting the number operations.
Each of the next Q lines will contain a integer v, which will decide the type of operation.
For u=1 , extra 2 integers k and h will be given , which shows that Voldemort will add one fighter
of height h in kth  stack, maintaining the order of the stack, if k is not equal to 1 .
For u=0, 1 more integer k will be given, which shows that Voldemort will remove a fighter from kth stack.
For u=2, Monk needs to know whether Harry can use his special wand or not.
For each u=2, print "YES" (without quotes) if Harry can use his special wand or print "NO" (without quotes).

Sample input:
2
3 3 5 4
3 1 1 2
8
0 1
2
1 1 1
2
0 1
2
1 2 4
2

Sample Output:
NO
YES
NO
YES
"""

"""
For the queries of type 0 and 1 and for all the rows apart from the first one, it is guaranteed by the problem that the
order will be maintained. That means that can use 1 stack for each of the rows. For the first row we are going to use
an auxiliary stack. That stack is going to have the same length as the first row. Each index of tha auxiliary stack will
have the smallest element up to this position. For example, if the first row is [4, 5, 3, 6, 5, 1, 1] the auxiliary
stack is going to be [4, 4, 3, 3, 3, 1, 1]. The stack can be easily implemented. We begin by pushing the first element 
from the first row and then we check the next element with the top element from our auxiliary stack and if it is bigger
it will be the one that will be pushed, otherwise the top element from the auxiliary stack will be pushed again. That 
way, it takes O(length(first_row)) to create the auxiliary stack and then we can perform queries 1 and 2 in O(1). For
the last query we are always going to pick the smallest element from the first row and then perform binary search in all
the other rows. Each time, we try to find the first bigger element and if exists, we go to the next row and try to find 
the next bigger element from the previous value we found. If at any point a value like that doesn't exist, then we will
print "NO", otherwise "YES".

Final complexity: O(Q)
"""


def ans_binary_search(array, element):
    for j in range(len(array)):
        lower = 0
        upper = len(array[j]) - 1
        temp_array = array[j]

        while lower < upper:
            mid = (lower + upper) // 2
            if temp_array[mid] <= element:
                lower = mid + 1
            else:
                upper = mid

        if temp_array[upper] <= element:
            return False
        else:
            element = temp_array[upper]
    return True


n = int(input())
first_row = list(map(int, input().split()))
first_row = first_row[1:]
min_first_row = [first_row[0]]
fighters = []

# Creating the auxiliary stack.
for i in range(1, len(first_row)):
    if first_row[i] < min_first_row[-1]:
        min_first_row.append(first_row[i])
    else:
        min_first_row.append(min_first_row[-1])

# Creating the rows (not the first one).
for i in range(n-1):
    temp_fighter = list(map(int, input().split()))[1:]
    fighters.append(temp_fighter)

q = int(input())
for i in range(q):
    query = list(map(int, input().split()))

    # Remove element if it exists.
    if query[0] == 0:
        if query[1] == 1 and first_row:
            first_row.pop()
            min_first_row.pop()
        elif query[1] != 1 and fighters[query[1] - 2]:
            fighters[query[1] - 2].pop()
    # Add element.
    elif query[0] == 1:
        if query[1] == 1:
            first_row.append(query[2])
            if first_row[-1] < min_first_row[-1]:
                min_first_row.append(first_row[-1])
            else:
                min_first_row.append(min_first_row[-1])
        else:
            fighters[query[1] - 2].append(query[2])
    # Perform binary search.
    else:
        if ans_binary_search(fighters, min_first_row[-1]):
            print("YES")
        else:
            print("NO")
