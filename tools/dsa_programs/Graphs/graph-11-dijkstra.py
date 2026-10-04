import heapq
g={"A":[("B",4),("C",1)],"B":[("D",1)],"C":[("B",2),("D",5)],"D":[]}; d={u:float("inf") for u in g}; d["A"]=0; h=[(0,"A")]
while h:
 du,u=heapq.heappop(h)
 if du!=d[u]: continue
 for v,w in g[u]:
  nd=du+w
  if nd<d[v]: d[v]=nd; heapq.heappush(h,(nd,v))
print(d)
