n=4
edges=[(0,1),(0,2),(2,3)]
m=[[0]*n for _ in range(n)]
for u,v in edges: m[u][v]=m[v][u]=1
print(m[0][2]); print(m[1][3])
