class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
def leaves(node):
    if not node: return 0
    if not node.left and not node.right: return 1
    return leaves(node.left)+leaves(node.right)

root=Node(1,Node(2),Node(3,Node(4),Node(5)))
print(leaves(root))
