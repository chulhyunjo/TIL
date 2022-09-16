import sys
z=input;sys.setrecursionlimit(10**6)
n=int(z());n+=1;p={};r=[0]*n;v=[1]*n
for _ in '_'*(n-2):a,b=map(int,z().split());p[a]=p.get(a,[])+[b];p[b]=p.get(b,[])+[a]
def t(f,g):
 r[f]=g;v[f]=0
 for h in p[f]:
  if v[h]:t(h,f)
t(1,1);print(*r[2:],sep='\n')