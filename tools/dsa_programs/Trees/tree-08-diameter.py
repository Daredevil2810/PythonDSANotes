class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
def diameter(root):
    best=0
    def height(node):
        nonlocal best
        if not node: return 0
        left=height(node.left); right=height(node.right)
        best=max(best,left+right)
        return 1+max(left,right)
    height(root)
    return best

root=Node(1,Node(2,Node(4),Node(5)),Node(3))
print(diameter(root))
