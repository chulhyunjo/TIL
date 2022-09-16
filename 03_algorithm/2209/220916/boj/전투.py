z=input;r=range;rw=rb=0
A,B=map(int,z().split());g=[list(z()) for _ in '_'*B]
def dfs(x,y,c):
 global w,b
 if c=='W':w+=1;
 else:b+=1;
 g[x][y]=0
 for i,j in (1,0),(-1,0),(0,1),(0,-1):
  m,n=x+i,y+j;
  if 0<=m<B and 0<=n<A and g[m][n]==c:dfs(m,n,c)
for i in r(B):
 for j in r(A):
  if g[i][j]!=0:
   w=b=0;dfs(i,j,g[i][j]);rw+=w**2;rb+=b**2
print(rw,rb)