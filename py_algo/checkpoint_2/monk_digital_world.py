"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/monk-and-digital-world-code-monk-5cd78708/

After doing a lot of hardwork, Monk has finally reached to the second checkpoint. He became such an awesome programmer
that he found a way to enter into the Digital World. While observing the beauty of the new world, he saw two strings A
and B of same length N, fighting with each other. String A has the power to take any two characters of its own and swap
them, and can perform this swap operation any number of times. Monk being curious, wants to know whether String A can
convert itself into String B using swap operations.

Input - Output:
First line of input will consists of integer N.
Next line will consists of N lowercase English alphabets('a'-'z') denoting string A.
Next line will consists of N lowercase English alphabets('a'-'z') denoting string B.
Print "YES" (without quotes), if String A can convert itself to string B using this
swap operation any number of times, else print "NO" (without quotes).

Sample input:
4
abcd
bcda

Sample Output:
YES
"""

"""
We find the frequencies of both strings. For all the characters in the first string we check if they exist in the second
string and if yes then we check if their frequencies match. If all exist they they match then it's a "YES"!

Final complexity: O(N)
"""

n = int(input())
first = input()
second = input()
occ_first = {}
occ_second = {}
for character in first:
    if character in occ_first:
        occ_first[character] += 1
    else:
        occ_first[character] = 1

for character in second:
    if character in occ_second:
        occ_second[character] += 1
    else:
        occ_second[character] = 1

ans = "YES"
for character in occ_first:
    if character not in occ_second:
        ans = "NO"
        break
    else:
        if occ_first[character] != occ_second[character]:
            ans = "NO"
            break

print(ans)
