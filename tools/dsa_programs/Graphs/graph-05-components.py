g={1:[2],2:[1],3:[4],4:[3],5:[]}
seen=set(); count=0
def dfs(u):
 seen.add(u)
 for v in g[u]:
  if v not in seen: dfs(v)
for u in g:
 if u not in seen: count+=1; dfs(u)
print(count)
