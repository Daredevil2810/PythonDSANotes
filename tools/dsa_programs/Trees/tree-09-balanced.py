class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
def balanced(root):
    def h(node):
        if not node: return 0
        a=h(node.left)
        if a==-1: return -1
        b=h(node.right)
        if b==-1 or abs(a-b)>1: return -1
        return 1+max(a,b)
    return h(root)!=-1

root=Node(1,Node(2),Node(3,Node(4)))
print(balanced(root))
