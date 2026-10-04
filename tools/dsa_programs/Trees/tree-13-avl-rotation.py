class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.height = 1

def h(n): return n.height if n else 0
def update(n): n.height=1+max(h(n.left),h(n.right))
def rotate_right(y):
    x=y.left; middle=x.right
    x.right=y; y.left=middle
    update(y); update(x)
    return x

y=Node(30); y.left=Node(20); y.left.left=Node(10)
update(y.left); update(y)
y=rotate_right(y)
print(y.value,y.left.value,y.right.value)
