class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
root = Node(1, Node(2), Node(3))
root.left.left = Node(4)
print(root.value, root.left.value, root.right.value)
