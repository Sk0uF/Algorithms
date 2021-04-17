"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/the-witches-of-hegwarts-1/

Little PandeyG is a curious student, studying in HEgwarts. Being smarter, faster and displaying more zeal for magic than
any other student, one by one he managed to impress the three hidden witches of the school. They knew his secret desire
to be a warrior, so each of them gave him some super power to use if he's up for a fight against one of his enemies.
The first witch: She gave PandeyG the power to take away one unit of strength from his enemies.
The second witch: Jealous of the first witch, the second one gave the kid the power to half the strength of his enemies.
The third witch: Even better, she gave him the power to reduce the strength of his enemies to one third of what it
initially was. The witches, though, clearly told him that he'll be only able to use these powers if the strength of the
opponent is an integer, otherwise not.Since, PandeyG is one smart kid, he knew that by using all three of the powers he
has got, he'll be able to defeat every enemy he's ever going to face, sometime or the other, in some number of moves.
Now, here's the twist: In spite of having all these powers, PandeyG was still losing matches against his enemies
because he was unable to use them in the optimal fashion. To defeat an opponent, you need to make sure that the enemy
has only 1 unit of strength left in him.Given the value 'k' - k being the units of the enemy of PandeyG's strength,
help PandeyG figure out the minimum number of magical hits he'll be needing to defeat his opponent, using his powers.

Input - Output:
The first line represents the number of test cases, t.
Followed by t lines - and on every line, a number n - with the strength unit of your enemy.
For every number n, print the minimum number of hits needed to defeat his enemy by making his strength equal to 1.

Sample input:
5
1
2
3
4
5

Sample Output:
0
1
1
2
3
"""

"""
This is the kind of problem in which we don't know the vertices but we know how to get there (in that case by performing
the 3 operations given to us). We use BFS but with a nice little trick in the known implementation. We are going to use
a custom made queue but we will also keep track of nodes we reached in each step. That way, we will know when to count
1 more step. For example, if we have reached 3 nodes, [34, 12, 95], then, for each node we will need to perform the 3
operations. This could lead to something like [34, 12, 95, 17, 23, 11, 94] and then we would count plus 1 only when
reaching the 17 and until we reach 94 we wont count again. We stop when we find 1 somewhere. As we can see, its just 
a queue (and we keep track of the lower and upper bounds but we do it in such a way that allows us to add the step at
the correct time.

O(NODES+EDGES) for the BFS. 
Can we be sure that the process will end though?
Can we be sure for the number of NODES+EDGES?
Maybe the complexity differs.

Final complexity: Undetermined
"""


inp_len = int(input())
for _ in range(inp_len):
    n = int(input())
    if n == 1:
        print(0)
        continue

    visited = set()
    auxiliary = [n]
    c1, c2, c3 = -1, -1, -1
    lower = 0
    upper = 1
    steps = 0
    found = False
    while True:
        steps += 1
        for i in range(lower, upper):
            current = auxiliary[i]
            if current % 2 == 0:
                c1 = current // 2
                if c1 not in visited:
                    auxiliary.append(c1)
                    visited.add(c1)
            if current % 3 == 0:
                c2 = current // 3
                if c2 not in visited:
                    auxiliary.append(c2)
                    visited.add(c2)
            c3 = current - 1
            if c3 not in visited:
                auxiliary.append(c3)
                visited.add(c3)
            if c1 == 1 or c2 == 1 or c3 == 1:
                print(steps)
                found = True
                break

        if found:
            break

        lower = upper
        upper = len(auxiliary)
