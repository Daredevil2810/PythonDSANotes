class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
def contains(root,target):
    while root:
        if root.value==target: return True
        root=root.left if target<root.value else root.right
    return False

root=Node(8,Node(3,Node(1),Node(6)),Node(10))
print(contains(root,6))
print(contains(root,7))
