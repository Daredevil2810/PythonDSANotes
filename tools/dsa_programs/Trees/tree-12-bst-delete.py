class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
def delete(root,key):
    if not root: return None
    if key<root.value: root.left=delete(root.left,key)
    elif key>root.value: root.right=delete(root.right,key)
    else:
        if not root.left: return root.right
        if not root.right: return root.left
        s=root.right
        while s.left: s=s.left
        root.value=s.value
        root.right=delete(root.right,s.value)
    return root

root=Node(5,Node(3),Node(8,Node(6),Node(9)))
root=delete(root,8)
print(root.right.value)
