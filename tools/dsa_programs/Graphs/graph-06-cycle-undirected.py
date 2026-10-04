g={1:[2,3],2:[1,3],3:[1,2]}; seen=set()
def cycle(u,p):
 seen.add(u)
 for v in g[u]:
  if v not in seen:
   if cycle(v,u): return True
  elif v!=p: return True
 return False
print(cycle(1,-1))
