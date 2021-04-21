"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/a-needle-in-the-haystack-1/

Our hacker, Little Stuart lately has been fascinated by ancient puzzles. One day going through some really old books he
finds something scribbled on the corner of a page. Now Little Stuart believes that the scribbled text is more mysterious
than it originally looks, so he decides to find every occurrence of all the permutations of the scribbled text in the
entire book. Since this is a huge task, Little Stuart needs your help, he needs you to only figure out if any
permutation of the scribbled text exists in the given text string, so he can save time and analyze only those text
strings where a valid permutation is present.

Input - Output:
First line contains the number of test cases T.
Each test case contains two lines, first line contains the pattern and
the next line contains a text string.
All characters in both strings are in lowercase only [a-z].
For each test case print "YES" or "NO" (quotes for clarity).

Sample input:
3
hack
indiahacks
code
eddy
coder
iamredoc

Sample Output:
YES
NO
YES
"""

"""
The cool fact about permutations is that we only care about the frequency of the characters in a given range. This is 
the property we are going to use to solve the problem. Imagine we have the following string: "hello" and we want to find
if there exists a permutation of that string  in the string "klapalolhegq". The first thing we have to do is calculate
the frequencies for the first string. Now then, the second step is to calculate the frequencies of the second string 
for beginning in the range of the length of the first string. Why? "hello" has a length of 5. That's "klapa" from the
first string. If those have the same frequencies for the same characters then a permutation has been found. We continue
by iterating in the second string step by step from the range of the length of the first string until the end. In each
step, we decrease the frequency from the character of the last index and increase that of the character of the new
index. It's basically like looping through all the the string keep always a chunk of frequencies of the length equal to
the length of the initial string. Note that for the frequencies we used 2 arrays of length 26, equal to the lenght of 
the English alphabet.

Final complexity: O(T*(PATTERN+26*STRING_LENGTH))
"""

t = int(input())
for _ in range(t):
    first_word = input()
    new_word = input()
    freq_first = [0] * 26
    freq_new = [0] * 26

    for i in range(len(first_word)):
        freq_first[ord(first_word[i]) - ord("a")] += 1

    for i in range(len(first_word)):
        freq_new[ord(new_word[i]) - ord("a")] += 1

    ans = "NO"
    for i in range(len(first_word), len(new_word)):
        found = True
        for j in range(26):
            if freq_first[j] != freq_new[j]:
                found = False
                break

        if found:
            ans = "YES"
            break

        freq_new[ord(new_word[i-len(first_word)]) - ord("a")] -= 1
        freq_new[ord(new_word[i]) - ord("a")] += 1

    found = True
    for i in range(26):
        if freq_first[i] != freq_new[i]:
            found = False
            break

    if found:
        ans = "YES"

    print(ans)
