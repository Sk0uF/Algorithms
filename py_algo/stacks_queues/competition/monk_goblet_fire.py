"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/little-monk-and-goblet-of-fire-3c1c6865/

Albus Dumbledore announced that the school will host the legendary event known as Wizard Tournament where four magical
schools are going to compete against each other in a very deadly competition by facing some dangerous challenges. Since
the team selection is very critical in this deadly competition. Albus Dumbledore asked Little Monk to help him in the
team selection process. There is a long queue of students from all the four magical schools. Each student of a school
have a different roll number. Whenever a new student will come, he will search for his schoolmate from the end of the
queue. As soon as he will find any of the schoolmate in the queue, he will stand behind him, otherwise he will stand at
the end of the queue. At any moment Little Monk will ask the student, who is standing in front of the queue, to come and
put his name in the Goblet of Fire and remove him from the queue. There are Q operations of one of the following types:
E x y: A new student of school x (1<=x<=4) whose roll number is y (1<=y<=50000) will stand in queue according to the
method mentioned above.
D: Little Monk will ask the student, who is standing in front of the queue, to come and put his name in the Goblet of
Fire and remove him from the queue.
Now Albus Dumbledore asked Little Monk to tell him the order in which student put their name. Little Monk is too lazy to
that so he asked you to write a program to print required order. Number of dequeue operations will never be greater than
enqueue operations at any point of time.

Input - Output:
First line contains an integer Q 1<=Q<=10000, denoting the number of operations.
Next Q lines will contains one of the 2 types of operations.
For each  type of operation, print two space separated integers,
the front student's school and roll number.

Sample input:
E 1 1
E 2 1
E 1 2
D
D

Sample Output:
1 1
1 2
"""

"""
We can solve this problem in linear time by using simple arrays in an efficient way. Instead of creating a queue with 
all the students, we are going to create a queue that contains 4 queues, one for each school. By doing that, we are able
to directly insert a student behind the student of the same school in constant time. The only thing that's missing now,
is the order of the schools. To solve tha problem we will create one more queue that is going to hold that order. We 
have to notice that the order of the schools will be maintained as long as there is at least one student there. If there
are no more students, then the new student that is going to come will be placed at the end, creating a new order for
that school. Now, each, time a school queue is empty and we add a student in it, we insert the number of the school in
that array. For example, if we have:

E 1 5
E 2 3
E 1 1
E 3 2

then, school_queue = [[5, 1], [3], [2], [0]] and order_queue = [1, 2, 3]. How can we achieve a O(1) dequeue in our case? 
In python if we remove an element all the other elements of the array shift. To avoid that, we will simply create 5
counters and completely avoid the dequeue. The 4 counters will be responsible to count the amount of students removed 
from each school. The 5th counter will be responsible for the change of the index in the order queue. That way, instead
of dequeueing, we just increase those counters and consider the the next elements to be the front.

Final complexity: O(Q)
"""

q = int(input())
structure = [[] for _ in range(4)]
s_counter = [0] * 4
order = []
o_counter = 0


for _ in range(q):
    info = input().rstrip().split()

    if info[0] == "E":
        school = int(info[1]) - 1

        # If the schools queue is empty or doesn't have any more students,
        # meaning that the counter is bigger than its length, then we add
        # that school to the order queue.
        if not structure[school] or s_counter[school] >= len(structure[school]):
            order.append(school)

        # Add the student to its responsive school.
        structure[school].append(int(info[2]))
    else:
        # Print the school and the student's roll,
        # increase the counter for the respective school
        # (instead of dequeueing) and if there are no more
        # student's left in that school then increase the
        # order counter (instead of dequeueing).
        school = order[o_counter]
        print(school + 1, structure[school][s_counter[school]])
        s_counter[school] += 1
        if s_counter[school] >= len(structure[school]):
            o_counter += 1
