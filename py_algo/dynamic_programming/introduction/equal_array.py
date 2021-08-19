"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/equal-array-84cf6c5f/

You are given an array A of size N. Find the minimum non negative number X such that there exists an index j that when
you can replace Aj by Aj+X, the sum of elements of the array from index 1 to j and j+1 to  N become equal where
1 <= j <= N-1. Assume array to be 1-indexed. If there is no possible X print -1 in a separate line.

Input - Output:
The first line contains the number of test cases.
The first line of each test case contains an integer N,which denotes the size of the array.
The second line contains N space-separated integers where the ith integer denotes Ai.

Sample input:
1
5
1 2 3 2 1

Sample Output:
3
"""

"""
We can simply find the partial sums array, iterate throught the array end at each step check for the minimum X number 
that is required.

Final complexity: O(N)
"""

t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    partial_sums = [array[0]]
    for i in range(1, n):
        partial_sums.append(array[i]+partial_sums[i-1])

    ans = float("inf")
    stop = False
    for i in range(n):
        if partial_sums[i] < partial_sums[-1] - partial_sums[i]:
            val = partial_sums[-1] - 2*partial_sums[i]
            ans = min(ans, val)
        if partial_sums[i] == partial_sums[-1] - partial_sums[i]:
            print(0)
            stop = True
            break

    if not stop:
        if ans != float("inf"):
            print(ans)
        else:
            print(-1)

