"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/array-operations-3-96b9f0e0/

You are given an array A consisting of N elements. Your task is to find the maximal sub array sum after applying the
following operation exactly once: Select any sub array and set all the elements in it to zero.

Input - Output:
The first line contains an integer T denoting the number of test cases. For each test case:
The first line of each test case contains an integer N denoting the number of elements in array A.
The second line contains space-separated integers of array A.
For each test case, print a single line representing the max sub array sum after applying the
operation no more than once.

Sample input:
1
4
-1 4 -1 2

Sample Output:
6
"""

"""
By applying Kadane's algorithm we are able to find the largest continues sub array. We can do that to find the largest
continues sub array for every index from the beginning up until the end of an array. That will result in the largest
continues sub array ending to each index. If we think backwards and we iterate the array the other way around then we 
get the largest continues sub array beginning from each index. If we calculate those 2 arrays one would think that we
can simply iterate through the array and at each index add the 2 arrays in that particular index. That's not true. The
problem is that if we are at index i then even though we have the largest continues sub array up to i, that doesn't 
mean it is the biggest sub array up to that point. So, what we have to do is keep track of the overall largest continues
sub array. Then, if PRE is the array that has the largest overall continues sub array in it and SUF has the largest 
continues sub array starting from each index, we can simply iterate through the array and the answer will be
max(ans, PRE[i-1] + SUF[i]). That would simply mean that we start from the point in which the PRE[i-1] starts, then from
the end of PRE[i-1] up to the start of SUF[i] we make everything 0 and we continue from the start of SUF[i] up to its
end. That's a linear solution.

Final complexity: O(N)
"""

t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))

    pre = [0] * n
    suf = [0] * n

    pre[0] = array[0]
    for i in range(1, n):
        pre[i] = max(array[i], pre[i-1] + array[i])

    for i in range(1, n):
        pre[i] = max(pre[i], pre[i-1])

    suf[-1] = array[-1]
    for i in range(n-2, -1, -1):
        suf[i] = max(array[i], suf[i+1] + array[i])

    maximum = max(max(pre), max(suf))
    maximum = max(maximum, 0)
    for i in range(1, n):
        maximum = max(maximum, pre[i-1] + suf[i])

    print(maximum)
