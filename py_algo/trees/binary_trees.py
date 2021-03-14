class Node:
    """
    Simple Node of a Binary Tree

    The binary tree is a simple tree that can have
    at maximum 2 children with no constraints at all.
    We can also add a pointer to the parent of each node.
    """
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def pre_order_traversal(node):
    """
    DFS Traversal - Pre Order Traversal
    Complexity: O(NODES)
    """
    print(node.value)
    if node.left:
        pre_order_traversal(node.left)
    if node.right:
        pre_order_traversal(node.right)


def post_order_traversal(node):
    """
    DFS Traversal - Post Order Traversal
    Complexity: O(NODES)
    """
    if node.left:
        post_order_traversal(node.left)
    if node.right:
        post_order_traversal(node.right)
    print(node.value)


def in_order_traversal(node):
    """
    DFS Traversal - In Order Traversal
    Complexity: O(NODES)
    """
    if node.left:
        in_order_traversal(node.left)
    print(node.value)
    if node.right:
        in_order_traversal(node.right)


def max_height(node):
    """
    Binary Tree max height
    Complexity: O(NODES)

    Find height with DFS.
    """
    if node is None:
        return 0
    else:
        left_height = max_height(node.left)
        right_height = max_height(node.right)

        if left_height > right_height:
            return left_height+1
        else:
            return right_height+1


def add(node, value):
    """
    Binary Search Tree addition
    Complexity: O(HEIGHT)

    For example, if the tree has only left or right children
    the HEIGHT i N. When a binary tree is complete the HEIGHT is
    logN. The implementation is simple. Check the needed value with
    the value of the node and decide to continue checking for a place
    to add the new node either left or right from the current node.
    """
    if node is None:
        return Node(value)
    else:
        if node.value == value:
            return node
        elif node.value < value:
            node.right = add(node.right, value)
        else:
            node.left = add(node.left, value)
    return node


def find(node, value):
    """
    Binary Search Tree find
    Complexity: O(HEIGHT)

    For example, if the tree has only left or right children
    the HEIGHT i N. When a binary tree is complete the HEIGHT is
    logN. The implementation is simple. Check the needed value with
    the value of the node and decide to continue checking either
    left or right.
    """
    if node is None:
        return None
    if node.value == value:
        return node
    elif node.value > value:
        return find(node.left, value)
    else:
        return find(node.right, value)


def min_value_node(node):
    """
    Binary Search Tree min value node
    Complexity: O(HEIGHT)

    Find the node with the minimum value in a
    binary search tree.
    """
    while node.left is not None:
        node = node.left
    return node


def remove(node, value):
    if node is None:
        return node

    if value < node.value:
        node.left = remove(node.left, value)
    elif value > node.value:
        node.right = remove(node.right, value)
    else:
        # Node with only one child or no child
        if node.left is None:
            temp = node.right
            node = None
            return temp

        elif node.right is None:
            temp = node.left
            node = None
            return temp

        temp = min_value_node(node.right)
        node.value = temp.value
        node.right = remove(node.right, temp.value)

    return node

# a = Node(1)
# a.left = Node(2)
# a.right = Node(3)
# a.left.left = Node(4)
# a.left.right = Node(5)
# a.right.left = Node(6)
# a.right.right = Node(7)

# pre_order_traversal(a)
# post_order_traversal(a)
# in_order_traversal(a)
# print(max_height(a))


root = Node(5)
root = add(root, 3)
root = add(root, 2)
root = add(root, 10)
root = remove(root, 10)
in_order_traversal(root)