"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/monk-and-nice-strings-3-e5800d05/

Monk's best friend Micro's birthday is coming up. Micro likes Nice Strings very much, so Monk decided to gift him one.
Monk is having N nice strings, so he'll choose one from those. But before he selects one, he need to know the Niceness
value of all of those. Strings are arranged in an array A, and the Niceness value of string at position i is defined as
the number of strings having position less than i which are lexicographicaly smaller than A[i]. Since nowadays, Monk is
very busy with the Codemonk series, he asked for your help. Array's index starts from 1.

Input - Output:
First line consists of a single integer denoting N.
N lines follow each containing a string made of lower case English alphabets.
Print N lines, each containing an integer, where the integer in ith line denotes
Niceness value of string A[i].

Sample input:
4
a
c
d
b

Sample Output:
0
1
2
1
"""

"""
The problem is straightforward. For each new character check all the previous ones to find how many are smaller.

Final complexity: O(N^2)
"""

inp_len = int(input())
first_char = input()
characters = [first_char]
print("0")

for i in range(1, inp_len):
    new_char = input()
    count = 0
    for j in range(len(characters)-1, -1, -1):
        if new_char > characters[j]:
            count += 1

    print(count)
    characters.append(new_char)
