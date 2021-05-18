"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/little-monk-and-abd-56f25965/

Little Monk meets his another favorite cricketer this time: A-B-D. Little Monk says that he is the biggest fan of ABD.
ABD does not believe the Monk at all, and asks him to prove how much does he know about ABD's career. So, ABD tells the
Monk that given his latest N innings, he is going to ask him Q number of questions about his career which would involve
questions of two types:
Find the kth smallest score of his career - denoted by a query of type: "k S", where k is an integer and S denotes
smallest.
Find the kth largest score of his career - denoted by a query of type: "k L", where k is an integer and L denotes
largest.

Input - Output:
The first line contains an integer N, which denotes the number of innings played by ABD
which have to be dealt by The Monk.
The next line contains N space separated integers denoting the number of scores made by ABD.
The next line contains an integer Q denoting the number of questions ABD is going to be asking.
After that, the next Q lines will contain a query like the ones mentioned above.
Print the required answer for each query on a newline.

Sample input:
5
1 2 3 4 5
3
3 L
3 S
1 L

Sample Output:
3
3
5
"""

"""
We solve the problem by sorting the initial scores and then we can answer every query in O(1). 

Final complexity: O(Q)
"""

n = int(input())
scores = list(map(int, input().split()))
scores = sorted(scores)
q = int(input())
for _ in range(q):
    index, q_type = input().split()
    index = int(index) - 1

    if q_type == "S":
        print(scores[index])
    else:
        index += 1
        print(scores[-index])
