from collections import deque
g={0:[1,3],1:[0,2],2:[1,3],3:[0,2]}; color={}
for s in g:
 if s in color: continue
 color[s]=0; q=deque([s])
 while q:
  u=q.popleft()
  for v in g[u]:
   if v not in color: color[v]=1-color[u]; q.append(v)
   elif color[v]==color[u]: print(False); raise SystemExit
print(True)
