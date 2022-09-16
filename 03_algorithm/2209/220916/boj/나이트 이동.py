z=input;j=int
for _ in '_'*j(z()):
    n=j(z());a,b=map(j,z().split());c,d=map(j,z().split());v=[1]*(n**2)
    x=[(a,b,0)];v[a*n+b]=0
    while x:
        a,b,r=x.pop(0)
        if (a,b)==(c,d): print(r);break;
        for w,e in [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]:
            o,p=a+w,b+e
            if 0<=o<n and 0<=p<n and v[n*o+p]:
                v[n*o+p]=0;x.append((o,p,r+1))
