"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/tablets/

Therasa is a Nurse. She wants to give some tablets to the patients in her practice. All the patients sit in a line and
each of them has a rating score according to his or her health score. Theresa wants to give at least 1 tablet for each
patient. Patients get jealous of their immediate neighbors, so if two patients sit next to each other then the one with
the higher rating must get more tablets. Theresa wants to save money, so she wants to minimize the total number of
tablets.

Input - Output:
The first line of the input is an integer N, the number of patients in Therasa’s practice.
Each of the following N lines contains an integer indicates the health score of each patient.
Output a single line containing the minimum number of tablets Theresa must give.

Sample input:
3
1
2
2

Sample Output:
4
"""

"""
Begin from left to right and find only the increasing sequences. Then go from right to left and make corrections.
e.g: 1 10 9 8 7 6 6 11 5 10 2 1 5
     1  2 - - - - 1  2 1  2 - 1 2
     1  5 4 3 2 1 1  2 1  3 2 1 2

Final complexity: O(N)
"""

n = int(input())
health_scores = []
for _ in range(n):
    health_scores.append(int(input()))

inc = True
current = 1
values = [1] * n
for i in range(len(health_scores)):
    if health_scores[i-1] < health_scores[i]:
        values[i] = values[i-1] + 1

total = values[-1]
for i in range(len(health_scores)-2, -1, -1):
    if health_scores[i+1] < health_scores[i] and values[i+1] >= values[i]:
        values[i] = values[i+1] + 1

    total += values[i]

print(total)
