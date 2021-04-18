"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/the-monk-and-kundan-6f73d491/

Kundan being a good friend of Monk, lets the Monk know that he has a following string Initial which consists of the
following letters in the mentioned order: "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ". He also has
various lists of strings, and now he wants the Monk to compute the Hash value of each list of strings. Here's the
following algorithm used by the Monk to do it. So, the Hash is the summation of all the character values in the input:
(currentIndex + (position of the character In the string initial) ). And then this hash is multiplied by the number of
strings in the list.

Input - Output:
The first line contains an integer T, denoting the number of test cases.
For every test case, on a single line, there will be N number of strings all of them
separated by a space, denoting all the strings of that particular list of strings.
Print the required hash for each of the mentioned list of strings.

Sample input:
3
aA1 b
a b c d
aa BB cc DD

Sample Output:
132
24
640
"""

"""
This problem is extremely straight forward. To speed up everything we has the initial alphabet with values the indices
of the characters in the original alphabet.

Everything is insignificant here.

Final complexity: O(1)
"""

alphabet = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
hash_table = {}
for i in range(len(alphabet)):
    hash_table[alphabet[i]] = i

t = int(input())
for _ in range(t):
    str_array = list(input().split())
    value = 0
    for i in range(len(str_array)):
        for j in range(len(str_array[i])):
            value += hash_table[str_array[i][j]] + j
    value *= len(str_array)
    print(value)
