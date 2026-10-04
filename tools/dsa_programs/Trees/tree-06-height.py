class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
def height(node):
    if not node: return 0
    return 1 + max(height(node.left), height(node.right))

root=Node(1,Node(2),Node(3,Node(4)))
print(height(root))
