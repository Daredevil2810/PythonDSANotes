from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def level_order(root):
    if not root: return []
    q = deque([root]); result=[]
    while q:
        node=q.popleft(); result.append(node.value)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    return result

root=Node(1,Node(2),Node(3,Node(4),Node(5)))
print(level_order(root))
