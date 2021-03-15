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
