from collections import deque
g={"A":["B","C"],"B":["D"],"C":["D"],"D":[]}; dist={"A":0}; q=deque(["A"])
while q:
 u=q.popleft()
 for v in g[u]:
  if v not in dist: dist[v]=dist[u]+1; q.append(v)
print(dist["D"])
