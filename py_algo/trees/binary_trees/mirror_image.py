"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/trees/binary-and-nary-trees/practice-problems/algorithm/mirror-image-2/

You are given a binary tree rooted at 1. You have to find the mirror image of any node qi about node 1. If it doesn't
exist then print -1.

Input - Output:
First line of input is N and Q.
Next N-1 lines consists of two integers and one character first of whose is the parent node,
second is child node and character "L" representing Left child and "R" representing right child.
Next Q lines represents qi.
For each qi print it mirror node if it exists else print -1.

Sample input:
10 8
1 2 R
1 3 L
2 4 R
2 5 L
3 6 R
3 7 L
5 8 R
5 9 L
7 10 R
2
5
3
6
1
10
9
4

Sample Output:
3
6
2
5
1
-1
-1
7
"""

"""
We implement a simple binary tree. To do that we create all the nodes and place them in an array. Afterwards based on
the input we associate the nodes from the array with each other. Then, to find the mirror node we start from the root
going downwards the tree simultaneously, either from left and right children, or, if we don't find it there, we change
direction to right and left children. It sound strange but after thinking of it it makes sense.

Final complexity: O(Q*N)
"""


class BinaryTree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def find_mirror(left, right, mirror):
    if left is None or right is None:
        return -1
    if left == mirror:
        return right
    if right == mirror:
        return left

    res = find_mirror(left.left, right.right, mirror)
    if res != -1:
        return res

    return find_mirror(left.right, right.left, mirror)


n, q = map(int, input().split())
nodes_array = [BinaryTree(i) for i in range(1, n+1)]
for _ in range(n-1):
    node, child, which = input().split()
    node, child = int(node), int(child)

    temp_node = nodes_array[node-1]
    temp_child = nodes_array[child-1]
    if which == "R":
        temp_node.right = temp_child
    else:
        temp_node.left = temp_child

# nodes_array = [0] * n
# nodes_array[0] = BinaryTree(1)
# for _ in range(n-1):
#     node, child, which = input().split()
#     node, child = int(node), int(child)
#     temp_node = BinaryTree(child)
#     nodes_array[child-1] = temp_node
#     if which == "R":
#         nodes_array[node-1].right = temp_node
#     else:
#         nodes_array[node-1].left = temp_node

for i in range(q):
    mirror_node = int(input())
    if nodes_array[mirror_node-1] == nodes_array[0]:
        print(nodes_array[0].value)
    else:
        answer = find_mirror(nodes_array[0].left, nodes_array[0].right, nodes_array[mirror_node-1])
        if answer != -1:
            print(answer.value)
        else:
            print(-1)
