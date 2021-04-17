"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/mancunian-and-liverbird-go-bar-hopping-2/

There are N bars (numbered from 1 to N) located in a straight line. The ith is located at point i on the line. Apart
from this, there are N-1 roads, the ith of which connects the ith and i+1th bars. Note that the roads are
unidirectional. You are given the initial orientation of each road. On celebratory occasions such as these, there are a
lot of people on the streets. Hence, the police have to take special measures to combat traffic congestion.
Periodically, they issue a directive to reverse the direction of all the roads. What this means is that, if there was a
road directed from bar numbered i to bar i+1, after the update, it will be directed from i+1 to i. You are given a set
of operations. Each operation can be either an update or a query. Update is the one described above. In each query, you
are given the location of the bar the two partyers are located at currently. You have to count the number of bars
(including the current location) that are reachable from their current location).

Input - Output:
The first line contains a single integer N denoting the number of bars on the road.
The second line contains N-1 integers denoting the directions of the roads.
The ith integer is 1 if the ith road is directed from i to i+1 and 0 if directed from i+1 to i.
The third line contains a single integer Q denoting the number of operations.
Each of the next Q lines is either an update or a query.
An update is given by a single character U.
A query is given in the form of the character Q followed by an integer S denoting the current location of the pair.
For each query, output a single integer which is the answer to the corresponding query.

Sample input:
4
1 1 0
3
Q 1
U
Q 2

Sample Output:
3
2
"""

"""
To solve the problem we pre calculate for every bar all the possible possible bar it can reach. That basically means we
have to do 2 calculations, one for the bars for which their direction is rightwards and one for the bars for which their
directions is leftwards. We repeat the same process for the reversed roads. Now, we can directly find the answer for 
every input in O(1). The cool about this technique is that we can make the calculations for the bars in O(N) time. We
simply find the starting and ending positions for all the 1s, if 1s represent the rightward bars and we do the exact
same thing for the 0s. For example, if we have 0 1 1 0 1 1 1 1 0 0 0, we will only save [1, 2] and [4, 7] for the 1s.
These pairs have all the information we need, because, for example we know that the bar at index 4 can reach 7-4+1=4
bars and the one at position 7-5+1=3 bars, etc. That basically means we can find the pairs in O(N) time and then we 
need O(N) time as well to find the total amount bars for each bar. That would mean O(2*N). We do the exact same thing
3 times, so we have a complexity O(8*N) + O(N) to find the reverse bar array, giving a total O(9*N). Thus, the final 
complexity is going to be O(9*N+Q).

Final complexity: O(9*N+Q)
"""


def finder(target):
    array = []
    start = 1
    end = 1
    found = False
    for i in range(1, n):
        if roads[i - 1] == target:
            if not found:
                start = i
                end = i
            end += 1
            found = True
        else:
            if found:
                array.append([start, end])
                start = end
            found = False

    if found:
        array.append([start, end])

    return array


n = int(input())
roads = list(map(int, input().split()))
auxiliary_1 = [1] * n
auxiliary_2 = [1] * n

right = finder(1)
for i in range(len(right)):
    for j in range(right[i][0], right[i][1]+1):
        auxiliary_1[j-1] += right[i][1] - j

left = finder(0)
for i in range(len(left)):
    for j in range(left[i][0], left[i][1] + 1):
        auxiliary_1[j - 1] += abs(left[i][0] - j)

for i in range(len(roads)):
    if roads[i] == 1:
        roads[i] = 0
    else:
        roads[i] = 1

right = finder(1)
for i in range(len(right)):
    for j in range(right[i][0], right[i][1]+1):
        auxiliary_2[j-1] += right[i][1] - j

left = finder(0)
for i in range(len(left)):
    for j in range(left[i][0], left[i][1] + 1):
        auxiliary_2[j - 1] += abs(left[i][0] - j)

q = int(input())
which_aux = 0
for _ in range(q):
    query = input()
    if len(query) == 1:
        which_aux += 1
        which_aux %= 2
    else:
        query, element = query.split()
        element = int(element)
        if which_aux == 0:
            print(auxiliary_1[element-1])
        else:
            print(auxiliary_2[element - 1])
