z=input
for t in range(1,int(z())+1):
    n,m=map(int,z().split())
    q=list([0]*n for _ in '_'*n)
    p=n//2;q[p-1][p-1]=q[p][p]=2;q[p][p-1]=q[p-1][p]=1
    for _ in '_'*m:
        x,y,c=map(int,z().split())
        x-=1;y-=1
        q[x][y]=c
        for a,b in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]:
            nx,ny,f,o=x+a,y+b,0,[]
            while 0<=nx<n and 0<=ny<n and q[nx][ny]!=0:
                if q[nx][ny]==c:f=1;break
                o.append((nx,ny));nx+=a;ny+=b;
            if f:
                for a,b in o: q[a][b]=c
    w=b=0
    for i in q:w+=i.count(2);b+=i.count(1);
    print(f'#{t} {b} {w}')