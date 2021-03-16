"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/monk-and-cursed-tree-eae36b06/

Monk has an array A having N distinct integers and a Binary Search Tree which is initially empty. He inserts all the
elements of the array from index 1 to N in the BST in the order given in the array. But wait! The tree so formed turns
out to be cursed. Monk is having some weird experiences since he made that tree. So, now to stop all that, Monk has two
options, to destroy the BST or to pray to God and ask for a solution. Now since Monk has to use this BST in a Code Monk
Challenge, he cannot destroy it. So he prays to God. God answer his prayers and sends an angel named Micro. Now, Micro
asks Monk to find something. He tells him two values, X and Y, present in the BST and ask him to find the maximum value
that lie in the path between node having value X and node having value Y. (including X and Y ). Now, since Monk is very
afraid of that tree he asks for your help.

Input - Output:
First line consists of a single integer denoting N.
Second line consists of N space separated integers denoting the array A.
Third line consists of two space separated integers denoting X and Y.
Print the maximum value that lie in the path from node having
value X and node having value Y in a new line.

Sample input:
5
4 7 8 6 3
3 7

Sample Output:
7
"""

"""
The problem is simple. We create a simple binary search tree with a pointer to the parent of each node. We also
implement the classic search algorithm but a bit twisted to also find the depth of the node we search for. To find the 
path, we will simply jump to the parent of each node at the same time until they reach the same parent. In the meanwhile
we will be finding the current maximum value. The thing we have to take care is that to start jumping to the parents 
from both nodes at the same time we first have to reach the same height from the node that is deeper in the tree. If
when we reach the same height the nodes are the same then that was the whole path, otherwise we follow the above
mentioned technique.

O(N) to create the binary search tree, 2*O(N) for the search
and O(N) to find the maximum in the path.

Final complexity: O(3*N) => O(N)
"""

import sys
sys.setrecursionlimit(1500)


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.parent = None


def add(node, value, parent=None):
    if node is None:
        new_node = Node(value)
        new_node.parent = parent
        return new_node
    else:
        if node.value < value:
            node.right = add(node.right, value, node)
        elif node.value > value:
            node.left = add(node.left, value, node)
    return node


def find(node, value, depth=1):
    if node is None:
        return -1
    if node.value < value:
        depth += 1
        return find(node.right, value, depth)
    elif node.value > value:
        depth += 1
        return find(node.left, value, depth)
    else:
        return node, depth


n = int(input())
array = list(map(int, input().split()))
x, y = map(int, input().split())

bst = None
for i in range(n):
    bst = add(bst, array[i])

first = find(bst, x)
second = find(bst, y)
depth1 = first[1]
depth2 = second[1]
first = first[0]
second = second[0]

deep = first
deeper = second
if depth1 > depth2:
    deeper = first
    deep = second

ans = max(first.value, second.value)
for i in range(abs(depth1-depth2)):
    deeper = deeper.parent
    ans = max(ans, deeper.value)

if deep == deeper:
    print(ans)
else:
    while True:
        if deep.parent == deeper.parent:
            ans = max(ans, deeper.parent.value)
            print(ans)
            break
        deeper, deep = deeper.parent, deep.parent
        ans = max(ans, deeper.value)
        ans = max(ans, deep.value)
