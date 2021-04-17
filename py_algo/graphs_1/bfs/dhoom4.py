"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/dhoom-4/

Samarpit is the main hero of the Dhoom 4.He is trying to steal from the Code Bank Of Hackers.Samarpit has a key with an
integer value printed on it. He also has N other keys with each key having its own specific value.Samarpit is trying to
break the Lock for which he is supposed to get to the lock's key value. He can perform one type of operation.Take his
own key and one of the other N keys and merge them.During merging Samarpit's Key value changes to product of both the
keys modulus 100000. For example if his key value was X and he took a key with value Y the his new key will be
(X*Y)%100000.The other key that was used during the merging process remains along with other N-1 keys. This entire
process of merging takes 1 second.Now since he is in a hurry he asks to you to find the minimum time in which he could
reach to the lock's key value.

Input - Output:
The first line contains 2 integers they are Samarpit's Key value and the Lock's key value.
The second line contains N indicating the number of other keys Samarpit has.
Third line contains N space separated integers indicating the value of N other keys.
Print the minimum time required to get to the Lock's Key. If he is unable to reach that print -1.

Sample input:
3 30
3
2 5 7

Sample Output:
2
"""

"""
This problem introduces the concept in which we don't actually have knowledge of all the nodes but we know the condition
to find them. Since we know the starting key and all the possible keys we can merge with, we will use BFS with the
next nodes being the merge of the current key with all the other keys (here the merging of the keys is considered to
produce the actual nodes). We make sure to count the steps after each merge for the produced node. This can be easily
calculated recursively while performing the BFS with the help of a simple array. We stop the process when i reach the
desired value.

O(NODES+EDGES) for the BFS. 
Can we be sure that the process will end though?
Can we be sure for the number of NODES+EDGES?
Maybe the complexity differs.

Final complexity: Undetermined
"""


def bfs(array, begin, goal):
    start = 0
    end = 1

    # BFS with a custom made queue
    # and a simple visited array. The
    # dimensions of both cannot be bigger
    # than 100000 because we mod with 100000
    # when merging.
    queue = [-1] * 100001
    queue[0] = begin
    visited = [False] * 100001
    visited[begin] = True
    steps = [0] * 100001
    while start != end:
        current = queue[start]
        queue[start] = -1
        start += 1
        for i in range(len(array)):
            merge = (current*array[i]) % 100000
            if not visited[merge]:
                visited[merge] = True
                steps[merge] += steps[current] + 1
                if merge == goal:
                    return steps[merge]
                queue[end] = merge
                end += 1
    return -1


first_key, lock = map(int, input().split())
n = int(input())
keys = list(map(int, input().split()))
print(bfs(keys, first_key, lock))
