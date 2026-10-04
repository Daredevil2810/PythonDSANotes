from collections import deque
g={"A":["B","C"],"B":["D"],"C":["D"],"D":[]}
q=deque(["A"]); seen={"A"}; order=[]
while q:
 u=q.popleft(); order.append(u)
 for v in g[u]:
  if v not in seen: seen.add(v); q.append(v)
print(order)
