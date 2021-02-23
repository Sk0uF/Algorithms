"""
Codemonk link: https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/monk-and-tasks/

Given an array, the number of tasks is represented by the number of ones in the binary representation of each integer
in the array. Print those integers in an increasing order based on the number of ones in the binary representation.

Input - Output:
First line contains the number of test cases.
The next line contains the length of the array.
The output is explained above.

Sample input:
1
4
3 4 7 10

Sample Output:
4 3 10 7
"""

"""
The problem is straightforward. We find the number of ones in the binary representation of each integer in the array and
we sort the integer based on this count, following an increasing order.

The input length is insignificant. O(N) for the second "for" statement. 
The while statement in insignificant. 
Python uses Timsort which has O(NlogN) complexity. 

Final complexity: O(N + NlogN) => O(NlogN)
"""

test_cases = int(input())

for i in range(test_cases):
    days = int(input())
    tasks = list(map(int, input().rstrip().split()))
    tasks_bin = []

    for j in range(len(tasks)):
        count = 0
        num = tasks[j]
        while num:
            # Count the number of 1's using bit manipulation.
            # num - 1 changes the LSB and the bits right to it.
            # Each time we make num & (num - 1) we remove the LSB.
            num = num & (num - 1)
            count += 1
        tasks_bin.append(count)

    # Sort based on the first element of each sub-pair.
    final = [x[1] for x in sorted(zip(tasks_bin, tasks), key=lambda pair: pair[0])]
    print(*final)

# Faster approach, bin returns string
# for i in range(int(input())):
#     n = int(input())
#     a = input().split()
#     print(" ".join(sorted(a, key=lambda x: bin(int(x)).count('1'))))
