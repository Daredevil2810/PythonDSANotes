g={"A":["B"],"B":["C"],"C":["A"]}; state={}
def dfs(u):
 state[u]=1
 for v in g[u]:
  if state.get(v,0)==1: return True
  if state.get(v,0)==0 and dfs(v): return True
 state[u]=2; return False
print(dfs("A"))
