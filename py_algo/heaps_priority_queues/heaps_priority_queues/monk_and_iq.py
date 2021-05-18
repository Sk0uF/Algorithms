"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/practice-problems/algorithm/monk-and-iq/

Monk and his P-1 friends recently joined a college. He finds that N students have already applied for different courses
before him. Courses are assigned numbers from 1 to C. He and his friends will follow the following conditions when
choosing courses: They will choose the course i (1 <= i <= C), for which the value of z is minimum. Here, z = x*c where
c is the number of students already enrolled in the course i and x is the sum of IQ of the last two students who
enrolled in that course. If a single student has applied for a course, then the value of x will be that student's IQ.
If no student has enrolled for that course, then value of x will be 0. If the value of z is same for two courses, then
they will choose the course with the minimum course number. You need to find which courses Monk and his friends should
take after following the above conditions. Note: Each of them will choose their courses, one at a time. Monk will choose
his course first followed by his friends.

Input - Output:
The first line contains the numbers C, P and N where C denotes the number of courses in that college,
P denotes Monk and his friends and N denotes the number of students who have already applied for the courses.
The next line consists of N space separated integers Y[i] which denotes the IQ of the ith student.
Here, the ith student chooses the ith course.
The next line consists of P space separated integers X[i] which denotes the IQ of Monk and his friends.
Print P space separated integers in a line which denotes the course number which Monk and his friends have applied for.

Sample input:
5 4 4
2 8 5 1
9 10 5 1

Sample Output:
5 4 1 3
"""

"""
We can solve this problem by using creating a priority queue by utilizing heaps. We save z, the iq from the previous
student, the number of students and the index into a tuple and we create the priority queue based on z. We create the
heap in O(N*logN) time because i used the add_to_heap and not heappipify (bored to implement it). Maintain heap is the
process of checking of the root is in the proper position, so it actually takes O(logN) time.

Final complexity: O(N*logN + P*logN) => O(P*logN)
"""


def add_to_heap(array, i):
    if i % 2 == 0:
        parent = i//2 - 1
    else:
        parent = i//2

    if parent >= 0:
        if array[parent][0] > array[i][0] or (array[parent][0] == array[i][0] and array[parent][3] > array[i][3]):
            array[parent], array[i] = array[i], array[parent]
            if parent != 0:
                add_to_heap(array, parent)


def maintain_heap(array):
    left_child = 1
    right_child = 2
    min_index = 0
    current_index = 0
    while True:
        if left_child < len(array):
            if array[left_child][0] < array[min_index][0] \
                    or (array[left_child][0] == array[min_index][0] and array[left_child][3] < array[min_index][3]):
                min_index = left_child

        if right_child < len(array):
            if array[right_child][0] < array[min_index][0] \
                    or (array[right_child][0] == array[min_index][0] and array[right_child][3] < array[min_index][3]):
                min_index = right_child

        if current_index != min_index:
            array[min_index], array[current_index] = array[current_index], array[min_index]
            left_child = 2*min_index + 1
            right_child = 2*min_index + 2
            current_index = min_index
        else:
            break


c, p, n = map(int, input().split())
iq_enrolled = list(map(int, input().split()))
iq_friends = list(map(int, input().split()))

for i in range(n):
    iq_enrolled[i] = (iq_enrolled[i], iq_enrolled[i], 1, i+1)

for i in range(n, c):
    iq_enrolled.append((0, 0, 0, i+1))

for i in range(len(iq_enrolled)):
    add_to_heap(iq_enrolled, i)

for i in range(len(iq_friends), p):
    iq_friends.append(0)

ans = []
for i in range(len(iq_friends)):
    temp_root = list(iq_enrolled[0])
    ans.append(temp_root[3])

    if temp_root[2] == 0:
        iq_enrolled[0] = (iq_friends[i], iq_friends[i], 1, temp_root[3])
    else:
        iq_enrolled[0] = ((temp_root[2]+1)*(temp_root[1]+iq_friends[i]), iq_friends[i], temp_root[2]+1, temp_root[3])

    maintain_heap(iq_enrolled)

print(*ans)
