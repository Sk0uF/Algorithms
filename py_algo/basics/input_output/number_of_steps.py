"""
Codemonk link: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/make-all-equal-90a21ab2/

Find the number of steps needed for an array a to have all it's columns equal to its lowest value. Consider an array b
of the same length as a and reach the desired equality by doing a[i] - b[i] if a[i] >= b[i].

Input - Output:
First line contains the array length.
Second line and third lines contain the values of a and b.
The output is either the minimum amount of steps need to make
all values of a equal or -1 if that's impossible.

Sample input:
5
5 7 10 5 15
2 2 1 3 5

Sample Output:
8
"""

"""
We will find the minimum value of a and in each step we will make the subtraction if and only if the value of array a at
a specific index is not equal to the min value. If we drop below the min value at a specific index, we change our goal
and to try to reach the next min value. We continue this process for values >= 0.

Final complexity: Undetermined
"""

ar_count = int(input())
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

fs = 0
minVal = min(a)
steps = 0

while True:
    dark = False
    for i in range(0, ar_count):
        if a[i] != minVal and a[i] >= b[i]:
            if b[i] == 0 and a[i] != minVal:
                break
            dark = True
            steps += 1
            a[i] = a[i] - b[i]

    if not dark:
        break
    minVal = min(a)

if len(set(a)) <= 1:
    print(steps)
else:
    print("-1")
