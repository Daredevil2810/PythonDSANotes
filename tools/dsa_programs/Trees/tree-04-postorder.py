class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
def postorder(node):
    if not node: return
    postorder(node.left)
    postorder(node.right)
    print(node.value, end=" ")

root = Node(1, Node(2), Node(3))
postorder(root)
