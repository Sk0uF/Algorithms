"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/little-jhool-and-the-magical-jewels/

Little Jhool is still out of his mind - exploring all his happy childhood memories. And one of his favorite memory is
when he found a magical ghost, who promised to fulfill one of Little Jhool's wish. Now, Little Jhool was a kid back
then, and so he failed to understand what all could he have asked for from the ghost. So, he ends up asking him
something very simple. (He had the intuition that he'd grow up to be a great Mathematician, and a Ruby programmer,
alas!). He asked the ghost the power to join a set of *the letters r, u, b and y * into a real ruby. And the ghost,
though surprised, granted Little Jhool his wish. Though he regrets asking for such a lame wish now, but he can still
generate a lot of real jewels when he's given a string. You just need to tell him, given a string, how many rubies can
he generate from it?

Input - Output:
The first line contains the number of test cases.
The next line contains the string.
Print the maximum number of ruby(ies) he can generate from the given string.

Sample input:
2
rrrruubbbyy
rubrubrubrubrubrubrubrubrubrubrubrubrubrb

Sample Output:
2
0
"""

"""
Straight forward problem. Think of it!

Final complexity: O(T*STRING_LENGTH)
"""

t = int(input())
for _ in range(t):
    hash_table = {"r": 0, "u": 0, "b": 0, "y": 0}
    temp_str = input()
    for character in temp_str:
        if character in "ruby":
            hash_table[character] += 1

    min_val = float('inf')
    for key in hash_table:
        min_val = min(min_val, hash_table[key])

    print(min_val)
