"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/little-monk-and-his-toy-story-f9f49f23/

Little Monk has N number of toys, where each toy has some width Wi. Little Monk wants to arrange them in a pyramdical
way with two simple conditions in his mind. The first being that the total width of the ith row should be less than
(i+1)th row. The second being that the total number of toys in the ith row should be less than (i+1)th row. Help Monk
find the maximum height which is possible to be attained! Note: It is NOT necessary to use all the boxes.

Input - Output:
The first line contains an integer N, which denotes the number of Monk's toys.
The next line contains N integers each denoting the width of the Monk's every single toy.
Print the maximum height of the toy pyramid.

Sample input:
4
40 100 20 30

Sample Output:
2
"""

"""
Very easy problem. Think about it.

Final complexity: O(N*logN)
"""

n = int(input())
w = list(map(int, input().split()))
w = sorted(w)
count = 0
length = 0
row_sum = 0
prev_row_sum = 0
row_total = 0
prev_row_total = 0
while length < n:
    row_sum += w[length]
    row_total += 1
    if row_sum > prev_row_sum and row_total > prev_row_total:
        count += 1
        prev_row_sum = row_sum
        prev_row_total = row_total
        row_total = 0
        row_sum = 0
    length += 1

print(count)
