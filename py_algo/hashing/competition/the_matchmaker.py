"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/little-monk-and-the-matchmaker-68aa7bf0/

Dawgie's logic for approving a girl with a boy or a boy with a girl, is simple: if the name of a girl has maximum
similar characters to the name of a guy, they are definitely not fit for being with each other. For example, a couple
with Shubhami and Shubham is less ideal than a couple with Shubham and Dhinsat. Since Shubhami and Shubham have 6
characters in common while the other couple has 3 characters in common, so the other couple is much more ideal. Now our
Little Jhool gives the list of all the crushes in his life to Dawgie, and asks him to tell the top K numbers of girls
out of the list of N girls, he gives who'll be a good match for Little Jhool.
Note-1: The case of the letters does NOT matter.
Note-2: The name of Little Jhool is: "LittleJhool", without the space and quotes, where the unique characters present in
his name are: [l, i, t, e, j,h,o].
Note-3: In case of a tie, print the names in order of their occurrence.

Input - Output:
The first line contains an integer, T, denoting the number of test cases.
The first line for every test case would contain two integers denoting the values of N and K.
The next line would contain N names separated by a space.
Print the names of the top K girls who will be a good match for our Little Jhool.

Sample input:
3
5 1
jhoolz littleboy cooldude findingathar findingnemo
3 1
bawa chunnu kundan
3 2
kaddu babykaddu littlejhool

Sample Output:
cooldude
bawa
kaddu babykaddu
"""

"""
We first has all the characters from the initial name littlejhool. Then, for each string we find the corresponding value
and save it in an array. We then sort our original string array based on the newly created values array. After doing so
we have the desired answer. We have to remember that we don't care if the characters are lower or upper case.

O(N) for the initial hashing of the name.
O(N) to find all the values and O(NlogN) for the sorting.
Here the test cases are considered significant.

Final complexity: O(T*(N+NlogN))
"""

t = int(input())
hash_table = {}
name = "littlejhool"
for i in range(len(name)):
    hash_table[name[i]] = 1

for _ in range(t):
    n, k = map(int, input().split())
    word_array = list(input().split())
    value_array = []

    for word in word_array:
        temp_hash = hash_table.copy()
        value = 0
        for letter in word:
            if letter.lower() in temp_hash:
                if temp_hash[letter.lower()] == 1:
                    value += 1
                    temp_hash[letter.lower()] -= 1
        value_array.append(value)

    ans = [x for _, x in sorted(zip(value_array, word_array), key=lambda pair: pair[0])]
    print(*ans[:k])
