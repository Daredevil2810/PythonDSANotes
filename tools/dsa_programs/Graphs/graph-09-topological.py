from collections import deque
g={"A":["C"],"B":["C"],"C":["D"],"D":[]}; indeg={u:0 for u in g}
for u in g:
 for v in g[u]: indeg[v]+=1
q=deque([u for u in g if indeg[u]==0]); order=[]
while q:
 u=q.popleft(); order.append(u)
 for v in g[u]:
  indeg[v]-=1
  if indeg[v]==0:q.append(v)
print(order)
