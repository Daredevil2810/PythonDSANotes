edges=[(1,"A","B"),(3,"B","C"),(2,"A","C"),(4,"C","D")]; parent={x:x for x in "ABCD"}
def find(x):
 while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
 return x
mst=[]
for w,u,v in sorted(edges):
 a,b=find(u),find(v)
 if a!=b: parent[b]=a; mst.append((u,v,w))
print(mst)
