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
