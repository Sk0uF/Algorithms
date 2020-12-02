"""
Codemonk link: https://www.hackerearth.com/practice/basic-programming/complexity-analysis/time-and-space-complexity/practice-problems/algorithm/vowel-game-f1a1047c/

Natural Language Understanding is the subdomain of Natural Language Processing where people used to design AI based
applications have ability to understand the human languages. HashInclude Speech Processing team has a project named
Virtual Assistant. For this project they appointed you as a data engineer (who has good knowledge of creating clean
datasets by writing efficient code). As a data engineer your first task is to make vowel recognition dataset. In this
task you have to find the presence of vowels in all possible substrings of the given string. For each given string you
have to print the total number of vowels.

Input - Output:
First line contains an integer T, denoting the number of test cases.
Each of the next lines contains a string, string contains both lower case and upper case.
Print the vowel sum for each input on a new line.

Sample input:
1
baceb

Sample Output:
16
"""

"""
There is a simple way to determine how many times a char is present to all the substrings. This is given by the formula
(counting from 1 to N): (pos + 1) * (str_len - pos)

O(N) for the "for" and O(10) for the input "for", because 1 <= input <= 10.

Final complexity: O(N)
"""

inp_len = int(input())
for k in range(0, inp_len):
    str = input()
    counter = 0
    str_len = len(str)
    for i in range(str_len):
        if str[i] in "aeiouAEIOU":
            # baceb | (pos+1) * (str_len - pos) = (1 + 1) * (5 - 1)  + (3 + 1) * (5 - 3) = 8 + 8 = 16
            # 01234 | str_len = 5
            counter += (i+1)*(str_len-i)
    print(counter)
