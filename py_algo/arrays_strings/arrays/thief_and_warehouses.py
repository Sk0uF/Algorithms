"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/thief-and-warehouses-6ebf4e07/

There are N warehouses. The warehouses are located in a straight line and are indexed from 1 to N. Each warehouse
contains some number of sacks. A thief decides to rob these warehouses. Thief figured out that he can escape the police
if and only if he follows both the following 2 constraints: He will rob only one continuous segment of warehouses.
He will rob same number of sacks from each warehouse. Thief wants to calculate the maximum number of sacks he can steal
without getting caught by the police.

Input - Output:
The first line contains the number test cases.
The first line of each test case contains a single integer N denoting number of warehouses.
The second line of each test case contains N space-separated integers denoting the number of sacks
in the ith warehouse.
For each test case output maximum number of sacks thief can steal without getting caught.

Sample input:
2
5
2 4 3 2 1
6
3 0 5 4 4 4

Sample Output:
8
16
"""

"""
The problem is equivalent to the Largest Rectangular Area in a Histogram problem. The thought is the following. For 
every index representing the number of sacks of a the ith warehouse, which basically can be represented as a rectangle,
we need to find the closest rectangle on the left and on the right that have less sacks and keep the indices. That way,
for each rectangle we will know the range we can still from, thus, we find the area and then from all the areas we
choose the maximum. Obviously, for a certain rectangle and its range, it would be silly to still less than the value of
the rectangle from all the rectangles in the range. To solve the problem with complexity O(N) we will use a beautiful
data structure called Priority Queue with Attrition (PQA) (sometimes known as Monotonous Deque). This data structure
is always order in ascending order and each time we need to add an element, we remove from the right of the queue all 
the elements that are smaller than the element we want to insert. Thus, to remove all the elements that are smaller, the
worst case scenario is O(N), but after a worst case scenario the insertions will have a O(1) complexity. That leads to
the conclusion that every insertion (which leads to several pops from the queue) have amortized complexity of O(1). So,
the complexity of O(N) comes from the fact that we need to do N insertions, for every rectangle. To better understand
the solution, lets see an example: 2 4 3 2 1. The queue becomes [0], then [0, 1] because at first it was empty and then
4 is bigger than 2. Then because we have 3 < 4, we need to pop the 4 to add the 3 (meaning that we need to pop the index
1 to add the index 2). When we do that, we know the range for the index 1 (4 sacks), it is only itself, thus we get an
area of 4 and the queue becomes [0, 2]. Now we have 2 < 3, we need to pop the 3 and add the 2 (indices 2, 3). That means
that we know the range for the index 2 and the area is 2 * 3 = 6, because the first smaller index on its left is the
index 0 and the first smaller index on its right is the index 3, so 3 - 0 - 1 = 2 is the range. The queue becomes [0, 3]
and the same thing happens again for the 3rd index and we get an area of 3 * 2 = 6. Now we have [0], so that means that 
we count from the beginning, so the area is 4 * 2 = 8. Now the queue becomes [4] and the final area is 5 * 1 = 5. The
maximum is the 8 and that's the solution. 

Final complexity: O(N)
"""

inp_len = int(input())

for _ in range(inp_len):
    n = int(input())
    sacks = list(map(int, input().rstrip().split()))

    stack = list()
    max_area = 0
    index = 0

    # Insert the index in the queue if the sacks on the
    # right are more than the previous value.
    while index < len(sacks):
        if (not stack) or (sacks[stack[-1]] <= sacks[index]):
            stack.append(index)
            index += 1
        else:
            # If we find less sacks on the right
            # pop the last index from the queue.
            top_of_stack = stack.pop()
            # If the stack is not empty after the pop
            # then the range is the current index minus the
            # index on the left of the popped index minus 1.
            #
            # Otherwise, the range is just the index, because it
            # means that we count from the beginning.
            if stack:
                area = sacks[top_of_stack] * (index - stack[-1] - 1)
            else:
                area = sacks[top_of_stack] * index

            print(area)
            max_area = max(max_area, area)

    # If after completing the previous procedure there are
    # indices left, then do exactly the same until the
    # stack is empty.
    #
    # This could happen for example if
    # every rectangle is smaller than the next one.
    while stack:
        top_of_stack = stack.pop()
        if stack:
            area = sacks[top_of_stack] * (index - stack[-1] - 1)
        else:
            area = sacks[top_of_stack] * index

        max_area = max(max_area, area)

    print(max_area)
