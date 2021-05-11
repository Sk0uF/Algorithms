"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/practice-problems/algorithm/reunion-of-1s-1b5bd063/

You are given a string of size n consisting of 0s and/or 1s. You have to perform total k queries and there are two types
of queries possible:
"1" (without quotes): Print length of the longest sub-array which consists of all '1'.
"2 X" (without quotes): where X is an integer between 1 to n. In this query, you will change character at the Xth
position to '1' (It is possible that the character at i-th position was already '1').

Input - Output:
First line of input contains n and k, where n is the length of the string, k is the number of queries.
Next line contains a string of 0's and/or 1's of length n.
Each of next k lines contains query of any one type(i.e 1 or 2).
For each query of type 1, print in a new line the maximum size of the sub array with all 1's

Sample input:
5 7
00000
1
2 3
1
2 5
1
2 4
1

Sample Output:
0
1
1
3
"""

"""
The problem can be solved using a disjoint set. We being by calculating all the groups of sequential 1's and their 
respective sizes. Then, if we have to make a 0 value 1, we check (if they exist) its left and right value. If both are
1 then we perform find and union and we also add +1 to account for the current 1. If one of the two is 1 then we do the
exact same thing but this time the set will consist of the initial group plus one more 1.

Final complexity: O(N) + O(K*INVERSE_ACKERMAN) => O(K*INVERSE_ACKERMAN) 
"""


def find_root_and_balance(array, value):
    if array[value] != value:
        array[value] = find_root_and_balance(array, array[value])
    return array[value]


n, k = map(int, input().split())
inp_str = input()
arr = []
for character in inp_str:
    arr.append(character)

sizes = [1] * n
disjoint = [0]
max_len = 0
for i in range(1, n):
    if arr[i] == "0":
        disjoint.append(i)
    else:
        if arr[i-1] == "1":
            disjoint.append(disjoint[i-1])
            sizes[disjoint[i-1]] += 1
            max_len = max(max_len, sizes[disjoint[i-1]])
        else:
            disjoint.append(i)

for _ in range(k):
    temp_input = input()
    if len(temp_input) == 1:
        print(max_len)
    else:
        x = int(temp_input.split()[1])
        if arr[x-1] == "0":
            if x-2 < 0:
                if arr[x] == "1":
                    root = find_root_and_balance(disjoint, x)
                    disjoint[x-1] = disjoint[root]
                    sizes[root] += 1
                    max_len = max(max_len, sizes[root])
            elif x >= n:
                if arr[x-2] == "1":
                    root = find_root_and_balance(disjoint, x-2)
                    disjoint[x-1] = disjoint[root]
                    sizes[root] += 1
                    max_len = max(max_len, sizes[root])
            else:
                if arr[x] == "1" and arr[x-2] == "1":
                    root_a = find_root_and_balance(disjoint, x)
                    root_b = find_root_and_balance(disjoint, x-2)
                    if root_a != root_b:
                        if sizes[root_a] < sizes[root_b]:
                            sizes[root_b] += (sizes[root_a] + 1)
                            disjoint[root_a] = disjoint[root_b]
                            disjoint[x-1] = disjoint[root_b]
                            max_len = max(max_len, sizes[root_b])
                        else:
                            sizes[root_a] += (sizes[root_b] + 1)
                            disjoint[root_b] = disjoint[root_a]
                            disjoint[x-1] = disjoint[root_a]
                            max_len = max(max_len, sizes[root_a])
                elif arr[x] == "1":
                    root = find_root_and_balance(disjoint, x)
                    disjoint[x-1] = disjoint[root]
                    sizes[root] += 1
                    max_len = max(max_len, sizes[root])
                elif arr[x-2] == "1":
                    root = find_root_and_balance(disjoint, x-2)
                    disjoint[x-1] = disjoint[root]
                    sizes[root] += 1
                    max_len = max(max_len, sizes[root])

        arr[x-1] = "1"
        max_len = max(max_len, 1)
