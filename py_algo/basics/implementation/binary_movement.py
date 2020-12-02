"""
Codemonk link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/binary-movement/

You are given a bit array (0 and 1) of size n. Your task is to perform Q queries. In each query you have to toggle all
the bits from the index L to R (L and R inclusive). After performing all the queries, print the count of all the set
bits and the newly updated array.

Input - Output:
The first line contains an integer N denoting the size of the array.
The Second line contains N space-separated binary numbers.
The third line contains Q denoting the number of queries.
The next Q lines contain L and R for each ith query.
Print the count of all the set bits and newly updated array in the new line.

Sample input:
6
1 0 1 1 0 1
3
1 3
4 5
2 5

Sample Output:
3
0 0 1 1 0 1
"""

"""
The problem can be translated to the following: To find the value of each index, find how many queries start before this
index and how many end before or after this specific index. If, overall, we find an even odd number of queries starting
before and ending after or at the  position of the index, then we change its value.

O(N) for the first and second "for".

Final complexity: O(2*N) => O(N)
"""

inp_len = int(input())
bit_list = list(map(int, input().rstrip().split()))
q_len = int(input())
# Creating 2 supplementary arrays
count_queries_before = [0] * inp_len
count_queries_after = [0] * inp_len
count = 0
count_ones = 0

for i in range(0, q_len):
    rl = list(map(int, input().rstrip().split()))
    # The first array contains the starting positions of all the queries
    # The second array contains the ending positions of all the queries
    count_queries_before[rl[0]-1] += 1
    count_queries_after[rl[1]-1] += 1

count += count_queries_before[0]
if count % 2 != 0:
    if bit_list[0] == 0:
        bit_list[0] = 1
    else:
        bit_list[0] = 0

for i in range(1, inp_len):
    # For each next index
    # Add the amount of of queries starting from there
    # Subtract the amount of queries ending 1 index before
    count += count_queries_before[i]
    count -= count_queries_after[i-1]

    if count % 2 != 0:
        if bit_list[i] == 0:
            bit_list[i] = 1
        else:
            bit_list[i] = 0

    count_ones += bit_list[i]

print(count_ones)
print(*bit_list)
