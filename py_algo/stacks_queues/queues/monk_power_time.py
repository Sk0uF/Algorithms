"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/queues/basics-of-queues/practice-problems/algorithm/monk-and-power-of-time-3a648bf0/

There are N processes to be completed by you, the chosen one, since you're Monk's favorite student. All the processes
have a unique number assigned to them from 1 to N. Now, you are given two things: The calling order in which all the
processes are called and the ideal order in which all the processes should have been executed. Now, let us demonstrate
this by an example. Let's say that there are 3 processes, the calling order of the processes is: 3 - 2 - 1. The ideal
order is: 1 - 3 - 2, i.e., process number 3 will only be executed after process number 1 has been completed, process
number 2 will only be executed after process number 3 has been executed. Executing a process takes 1 unit of time.
Changing the position takes 1 unit of time.

Input - Output:
The first line a number N, denoting the number of processes.
The second line contains the calling order of the processes.
The third line contains the ideal order of the processes.
Print the total time taken for the entire queue of processes to be executed.

Sample input:
3
3 2 1
1 3 2

Sample Output:
5
"""

"""
To solve this problem we need the following clarification: The operation we are allowed to do on the array is a circular
shift only to the left. From that point, the problem is straight forward.

The constraints are insignificant and the program
will run in O(1). The complexity of the actual implementation
though is O(N^2) because nested inside the "for" we have the 
index() function that has O(N) complexity.

Final complexity: O(N^2)
"""

n = int(input())
calling = list(map(int, input().rstrip().split()))
ideal = list(map(int, input().rstrip().split()))
count = n

for element in ideal:
    if element == calling[0]:
        calling.remove(element)  # Removes the first occurrence starting from left.
    else:                        # In our case it's the same as pop(0).
        ind = calling.index(element)
        calling = calling[ind:] + calling[:ind]
        calling.remove(element)
        count += ind

print(count)
