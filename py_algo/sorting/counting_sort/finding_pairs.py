"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/sorting/counting-sort/practice-problems/algorithm/finding-pairs-4/

Given an array A of N numbers, find the number of distinct pairs (i, j) such that j >=i and A[i] = A[j].

Input - Output:
First line of the input contains number of test cases T.
Each test case has two lines, first line is the number N,
followed by a line consisting of N integers which are the
elements of array A.
For each test case print the number of distinct pairs.

Sample input:
3
4
1 2 3 4
3
1 2 1
5
1 1 1 1 1

Sample Output:
4
4
15
"""

"""
Each individual number counts for 1 in the total amount our answer. So, if the array has N elements, the initial value
of our answer is N. Find how many times each number appears in the array. After doing that, if a number occurs k times,
where k > 0 then we add to our answer [(k-1) * k] // 2. It basically contributes k-1 + k-2 + ... + 1. We know that
k + k-1 + ... + 1 = [(k+1) * k] // 2, so we just substitute k with k - 1.

Considering the amount of input cases insignificant, each 
"for" has linear complexity.

Final complexity: O(2*N) => O(N)
"""

inp_len = int(input())

for _ in range(inp_len):
    n = int(input())

    array = list(map(int, input().rstrip().split()))
    helper_array = [0] * (2*10**6)

    total_amount = n

    for element in array:
        if element >= 0:
            helper_array[element + 10**6 - 1] += 1
        else:
            helper_array[-element] += 1
    for hlp in helper_array:
        if hlp > 0:
            total_amount += (hlp-1)*hlp//2

    print(total_amount)
