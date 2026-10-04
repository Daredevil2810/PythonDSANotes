g={"A":["B","C"],"B":["D"],"C":["D"],"D":[]}
seen=set(); order=[]
def dfs(u):
 seen.add(u); order.append(u)
 for v in g[u]:
  if v not in seen: dfs(v)
dfs("A"); print(order)
