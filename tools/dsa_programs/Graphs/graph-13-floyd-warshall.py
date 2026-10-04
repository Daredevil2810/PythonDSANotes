INF=float("inf")
d=[[0,3,INF],[3,0,1],[INF,1,0]]
for k in range(3):
 for i in range(3):
  for j in range(3): d[i][j]=min(d[i][j],d[i][k]+d[k][j])
print(d[0][2])
