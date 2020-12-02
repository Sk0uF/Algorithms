"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/find-the-string-4014dec6/

You are given a matrix of characters. The matrix has N rows and M columns. Given a string s, you have to tell if it is
possible to generate that string from given matrix. Rules for generating string from matrix are: You have to pick first
character of string from row 1, second character from row 2 and so on. The  character of string is to be picked from row
1, that is, you can traverse the rows in a cyclic manner (row 1 comes after row N). If an occurrence of a character is
picked from a row, you cannot pick the same occurrence again from that row. You have to print Yes if given string can be
generated from matrix using the given rules, else print No.

Input - Output:
The first contains the number of test cases.
Each test case consists of:
First line consists of two integers N and M, denoting the matrix dimensions.
Following N lines consist of M characters each.
Last line consists of a string s.

Sample input:
1
3 3
aba
xyz
bdr
axbaydb

Sample Output:
Yes
"""

"""
To solve the problem, we first create a helper array with dimensions n * 26. The 26 represents the 26 letters of the 
English alphabet. Each row of this array corresponds to a word. Each column of each row corresponds to a letter of the
words. The trick is to increase the equivalent column for each character of each word. For example, if the first word
is the word "aaa" then helper[0][0] = 3 and if the second word is "aba" then helper[1][0] = 2 and helper[1][1] = 1.
For each character of the desired word, we search the correct string by doing i % n, where i is the index of the current
char and n is the number of strings. Then we search if the specific string has the char we need available, simply by 
looking at our helper array. If we find it, meaning that the specific index of the array is not 0, then we decrease it
by 1.

O(N*M)) for the nested "for" statements. The other constraints are insignificant.

Final complexity: O(N*M)
"""

inp_len = int(input())

for _ in range(inp_len):
    n, m = map(int, input().rstrip().split())
    words = []
    temp = [[0] * 26 for _ in range(n)]

    for i in range(n):
        for c in input():
            temp[i][ord(c) - ord('a')] += 1  # This will give a number between 0 and 25

    needed_str = input()
    count = 0

    for i in range(len(needed_str)):
        if temp[i % n][ord(needed_str[i]) - ord('a')] != 0:
            temp[i % n][ord(needed_str[i]) - ord('a')] -= 1
            count += 1
        else:
            break

    if count == len(needed_str):
        print("Yes")
    else:
        print("No")
