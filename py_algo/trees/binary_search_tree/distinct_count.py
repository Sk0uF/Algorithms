"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/distinct-count/

Given an array A of N integers, classify it as being Good Bad or Average. It is called Good, if it contains exactly X
distinct integers, Bad if it contains less than X distinct integers and Average if it contains more than X distinct
integers.

Input - Output:
First line consists of a single integer T denoting the number of test cases.
First line of each test case consists of two space separated integers denoting N and X.
Second line of each test case consists of N space separated integers denoting the array elements.
Print the required answer for each test case on a new line.

Sample input:
4
4 1
1 4 2 5
4 2
4 2 1 5
4 3
5 2 4 1
4 4
1 2 4 5

Sample Output:
Average
Average
Average
Good
"""

"""
We create a set (the implementation of a set is NOT easy but it depends on binary search trees) from the array and then
we can directly answer the question. The set in Python is unordered, it has only distinct values inside and the 
insertion is O(1). The time complexity to create the set is O(N).

We consider the input cases significant. 

Final complexity: O(T*N)
"""

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    array = list(map(int, input().split()))
    distinct = set(array)
    if len(distinct) == x:
        print("Good")
    elif len(distinct) > x:
        print("Average")
    else:
        print("Bad")
