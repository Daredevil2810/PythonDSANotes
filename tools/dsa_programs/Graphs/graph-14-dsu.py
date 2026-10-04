parent=list(range(5)); size=[1]*5
def find(x):
 if parent[x]!=x: parent[x]=find(parent[x])
 return parent[x]
def union(a,b):
 a,b=find(a),find(b)
 if a==b:return False
 if size[a]<size[b]:a,b=b,a
 parent[b]=a; size[a]+=size[b]; return True
union(0,1); union(1,2); print(find(0)==find(2))
