"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/monk-and-suffix-sort-ebacdaf5/

Monk loves to play games. On his birthday, his friend gifted him a string S. Monk and his friend started playing a new
game called as Suffix Game. In Suffix Game, Monk's friend will ask him lexicographically kth smallest suffix of the
string S. Monk wants to eat the cake first so he asked you to play the game.

Input - Output:
First line contains a string S and an integer k.
Print the lexicographically kth smallest suffix of the string S.

Sample input:
aacb 3

Sample Output:
b
"""

"""
The problem is straightforward. Find all the suffices, sort them lexicographically and print the position.

Final complexity: O(NlogN)
"""

inp = input().rstrip().split()
inp_string = inp[0]
position = int(inp[1])

suffices = []

prev = ""
for i in range(len(inp_string) - 1, -1, -1):
    temp_string = inp_string[i]
    prev = temp_string + prev
    suffices.append(prev)

suffices = sorted(suffices)
print(suffices[position-1])
