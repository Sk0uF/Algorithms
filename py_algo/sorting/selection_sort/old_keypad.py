"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/sorting/selection-sort/practice-problems/algorithm/old-keypad-in-a-foreign-land-24/

Some people remain old fashioned and John is one of them. He doesn't like the new smart phones with full keypads and
still uses the old keypads which require you to tap a key multiple times to type a single letter. For example, if the
keyboard has two keys, one with the letters "adef" and the other one with the letters "zyx", then typing 'a' requires
one keystroke, typing 'f' requires four keystrokes, typing 'y' requires two keystrokes, and so on. He recently moved to
a new country where the language is such that his keypad is not the most efficient. In every language some characters
occur more often than others. He wants to create a specific keyboard for this language that uses N different letters. He
has a large body of text in this language, and has already analyzed it to find the frequencies of all N letters of its
alphabet. You are given an array 'frequencies' with N elements. Each element of frequencies is the number of times one
of the letters in the new language appears in the text John has. Each element of frequencies will be strictly positive.
(I.e., each of the N letters occurs at least once). You are also given an array keySize. The number of elements of
keySize is the number of keys on the keyboard. Each element of keySize gives the maximal number of letters that maybe
put on one of the keys. Find an assignment of letters to keys that minimizes the number of keystrokes needed to type the
entire text. Output that minimum number of keystrokes. If there is not enough room on the keys and some letters of the
alphabet won't fit, Output -1 instead.

Input - Output:
The first line will contain a number 'N' that specifies the size of 'frequencies' array.
The second line will contain N numbers that form the frequencies array.
The third line contains a number 'K' that specifies the size of the 'keySize' array.
The fourth line contains K numbers that form the keySize array.
Output a single integer that is answer to the problem.

Sample input:
4
7 3 4 1
2
2 2

Sample Output:
19
"""

"""
We need to assign the highest frequencies to the first stroke of each key size. If that's not possible, we choose the 
second key stroke, etc. If the sum of the keysize array is less than the numbers amount of letters N, then we don't have
a solution.

The overall complexity needs some work to be derived. 
However, the constraints are insignificant and we will consider
having constant complexity.

Final complexity: O(1)
"""

n = int(input())
frequencies = list(map(int, input().rstrip().split()))
k = int(input())
key_size = list(map(int, input().rstrip().split()))

if sum(key_size) < n:
    print("-1")
    exit()

frequencies = sorted(frequencies)

cost = 0
index = 1

while len(frequencies):
    for i in range(len(key_size)):
        try:
            cost += frequencies.pop() * index
        except IndexError:
            break
        key_size[i] -= 1

    # The following lines are used to effectively
    # delete the elements that don't have any more
    # key strokes.
    keys_tbr = []
    for k in range(len(key_size)):
        if key_size[k] == 0:
            keys_tbr.append(k)

    keys_tbr = sorted(keys_tbr, reverse=True)
    for key_tbr in keys_tbr:
        del key_size[key_tbr]

    index += 1

print(cost)
