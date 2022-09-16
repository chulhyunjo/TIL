import sys
z=sys.stdin.readline;sys.setrecursionlimit(10**5)
n=int(z());n+=1;t=[[] for _ in '_'*n];v=[1]*n;d=[0]*n;r=0;p=print
for _ in '_'*(n-2): a,b=map(int,z().split());t[a].append(b);t[b].append(a)
def s(i):
    v[i]=0
    for m in t[i]:
        if v[m]:d[m]=d[i]+1;s(m)
s(1)
for k in range(2,n):
    if len(t[k])==1: r+=d[k]
p('Yes') if r%2 else p('No')