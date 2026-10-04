class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
def preorder(node):
    if not node: return
    print(node.value, end=" ")
    preorder(node.left)
    preorder(node.right)

root = Node(1, Node(2), Node(3))
preorder(root)
