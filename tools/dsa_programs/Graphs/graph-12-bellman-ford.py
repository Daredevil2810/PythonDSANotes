edges=[("A","B",4),("A","C",5),("B","C",-2),("C","D",3)]; d={"A":0,"B":float("inf"),"C":float("inf"),"D":float("inf")}
for _ in range(len(d)-1):
 changed=False
 for u,v,w in edges:
  if d[u]!=float("inf") and d[u]+w<d[v]: d[v]=d[u]+w; changed=True
 if not changed: break
print(d)
