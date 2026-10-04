g={0:[1],1:[2],2:[0,3],3:[]}; rev={u:[] for u in g}
for u in g:
 for v in g[u]: rev[v].append(u)
seen=set(); order=[]
def d1(u):
 seen.add(u)
 for v in g[u]:
  if v not in seen:d1(v)
 order.append(u)
for u in g:
 if u not in seen:d1(u)
seen=set(); comps=[]
def d2(u,c):
 seen.add(u); c.append(u)
 for v in rev[u]:
  if v not in seen:d2(v,c)
for u in reversed(order):
 if u not in seen:c=[]; d2(u,c); comps.append(c)
print(comps)
