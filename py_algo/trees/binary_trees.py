class BinaryTree:
    """
    Binary Tree
    """
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_node_value(self, value):
        self.value = value

    def get_node_value(self):
        return self.value


def pre_order_traversal(node):
    """
    DFS - Pre Order Traversal

    Complexity: O(NODES)
    """
    print(node.value)
    if node.left:
        pre_order_traversal(node.left)
    if node.right:
        pre_order_traversal(node.right)


def post_order_traversal(node):
    """
    DFS - Post Order Traversal

    Complexity: O(NODES)
    """
    if node.left:
        post_order_traversal(node.left)
    if node.right:
        post_order_traversal(node.right)
    print(node.value)


def in_order_traversal(node):
    """
    DFS - In Order Traversal

    Complexity: O(NODES)
    """
    if node.left:
        in_order_traversal(node.left)
    print(node.value)
    if node.right:
        in_order_traversal(node.right)


def max_height(node):
    """
    Find height with DFS

    Complexity: O(NODES)
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


a = BinaryTree(1)
a.left = BinaryTree(2)
a.right = BinaryTree(3)
a.left.left = BinaryTree(4)
a.left.right = BinaryTree(5)
a.right.left = BinaryTree(6)
a.right.right = BinaryTree(7)

# pre_order_traversal(a)
# post_order_traversal(a)
# in_order_traversal(a)
print(max_height(a))
