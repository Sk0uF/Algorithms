"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/infinity-array-715a233b/

You are given an array A of size N. You have also defined an array Bas the concatenation of array A for infinite number
of times. For example, if A = [A1, A2, A3], then B = [A1, A2, A3, A1, A2, A3, ...]. Now, you are given Q queries. Each
query consists of two integers Li and Ri. Your task is to calculate the sum of the subarray of N  from index Li to  Ri.


Input - Output:
The first contains the number of test cases.
For each test case:
First line: Contains N, the size of the array.
Second line: Contains N space-separated integers corresponding to Ai.
Third line: Contains Q denoting the number of queries.
Fourth line: Contains Q space-separated integers corresponding to Li.
Fifth line: Contains Q space-separated integers corresponding to Ri.
For each test case, print Q space-separated integers that denote the
answers of the provided Q queries. Print the answer to each test case in a new line.

Sample input:
1
3
4 1 5
3
1 3 9
4 7 10

Sample Output:
14 19 9
"""

"""
The proposed solution uses partial sums. We first calculate the partial sums array of the array A. The next step is to 
find how many times the range of our query contains the whole array A. If there is no remainder then we can directly 
calculate the sum, in fact, it is stored in our partial sum array as its last index. It's essential to understand that
if the array A = [4, 1, 5] and we want from B the (3 to 7) elements [5, 4, 1, 5, 4], then the array A is contained only
one time (5/3 = 1) and the order is [5, 4, 1], which means that any order of 3 elements has the same sum as the original
array A, so we only need to find how many times it's contained and we don't care about the order. If there is a
remainder as in the previous example, we need to account for some more values. In the example, these values are the 5
and 4, so the 4th and 5th index starting from 1. This means that by doing (Ri - remainder) % N, we can directly find the
lower point of the query in the original array, and by doing Ri % N, we can find the upper point of the query in the 
original array. There are three cases. In the first case upper >=lower, so we add helper[upper] - helper[lower-1] to our
sum. If any of these is 0, we add helper[upper], because that means that the lower bound begins from the first index.
If lower>upper, we add helper[upper] plus helper[end] - helper[lower-1], meaning that from the lower index we reach the
end of the array and then from the beginning we reach the upper bound. Some alternations of +-1 in the helper array 
might occur based on the language used. In our example the lower point will be index 2 and the upper point will be index
0. So from index 2-1 to the end, that gives us the number 5 plus the beginning to index 0, which gives us the number 4,
meaning that we will add a total of 9 in our sum.

O(N) to create the partial sums array plus O(N) for the second "for" statement.
The input constraint is insignificant.

Final complexity: O(2*N) => O(N)
"""


def solve(A, R, L):
    partial_sums = []
    partial_sums.append(A[0])
    sums = []

    # Create the partial sums array.
    for i in range(1, N):
        partial_sums.append(A[i] + partial_sums[i-1])

    sum = 0
    for i in range(Q):
        diff = R[i] - L[i] + 1
        whole_sums = diff // N
        remaining = diff % N

        if remaining != 0:
            # Find the lower point in the original array.
            # Find the upper point in the original array.
            lower = (R[i] - remaining + 1 - 1) % N
            upper = (R[i] - 1) % N

            # From the beginning to the upper bound.
            # From lower bound to the upper bound.
            # From the lower bound to the end plus from the beginning to the upper bound.
            # Those are the possible steps.
            if upper >= lower:
                if upper == 0 or lower == 0:
                    sum += partial_sums[upper]
                else:
                    sum += partial_sums[upper] - partial_sums[lower-1]
            else:
                sum += (partial_sums[-1] - partial_sums[lower-1]) + partial_sums[upper]

        sum += whole_sums * partial_sums[-1]
        sums.append(sum)
        sum = 0
    return sums


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))

    out = solve(A, R, L)
    print(' '.join(map(str, out)))
