class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
def insert(root,value):
    if not root: return Node(value)
    if value<root.value: root.left=insert(root.left,value)
    else: root.right=insert(root.right,value)
    return root

root=None
for x in [8,3,10,6]: root=insert(root,x)
print(root.left.right.value)
