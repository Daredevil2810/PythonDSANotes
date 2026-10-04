class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
def inorder(node):
    if not node: return
    inorder(node.left)
    print(node.value, end=" ")
    inorder(node.right)

root = Node(2, Node(1), Node(3))
inorder(root)
