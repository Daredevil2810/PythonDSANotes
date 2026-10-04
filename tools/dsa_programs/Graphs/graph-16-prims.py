import heapq
g={"A":[("B",1),("C",2)],"B":[("A",1),("C",3)],"C":[("A",2),("B",3),("D",4)],"D":[("C",4)]}; seen={"A"}; h=[(w,"A",v) for v,w in g["A"]]; heapq.heapify(h); total=0
while h:
 w,u,v=heapq.heappop(h)
 if v in seen: continue
 seen.add(v); total+=w
 for x,nw in g[v]:
  if x not in seen: heapq.heappush(h,(nw,v,x))
print(total)
