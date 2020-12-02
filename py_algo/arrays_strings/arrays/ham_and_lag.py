"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/hamiltonian-and-lagrangian/

Students have become secret admirers of SEGP. They find the course exciting and the professors amusing. After a superb
Mid Semester examination its now time for the results. The TAs have released the marks of students in the form of an
array, where arr[i] represents the marks of the ith student. Since you are a curious kid, you want to find all the marks
that are not smaller than those on its right side in the array.

Input - Output:
The first line of input will contain a single integer n denoting the number of students.
The next line will contain n space separated integers representing the marks of students.
Output all the integers separated in the array from left to right that are not smaller than
those on its right side.

Sample input:
6
16 17 4 3 5 2

Sample Output:
17 5 2
"""

"""
Starting from the end of the array and going leftwards, we try to find all the values that are bigger than our previous
temporary biggest value. We consider the first biggest value to be the last element of the array.

O(N) for the "for" statement.

Final complexity: O(N)
"""

n = int(input())
arr = list(map(int, input().rstrip().split()))
arr_grades = []

temp_max = arr[-1]
count = 0

for i in range(n - 1, -1, -1):
    if arr[i] >= temp_max:
        temp_max = arr[i]
        arr_grades.append(temp_max)
        count += 1

for i in range(count-1, -1, -1):
    print(arr_grades[i], end=" ")
