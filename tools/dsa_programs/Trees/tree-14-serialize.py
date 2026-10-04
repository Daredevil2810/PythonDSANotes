class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
def serialize(root):
    out=[]
    def dfs(n):
        if not n: out.append('#'); return
        out.append(str(n.value)); dfs(n.left); dfs(n.right)
    dfs(root); return ','.join(out)

def deserialize(data):
    it=iter(data.split(','))
    def dfs():
        x=next(it)
        if x=='#': return None
        return Node(int(x),dfs(),dfs())
    return dfs()

root=Node(1,Node(2),Node(3))
s=serialize(root); copy=deserialize(s)
print(s,copy.right.value)
