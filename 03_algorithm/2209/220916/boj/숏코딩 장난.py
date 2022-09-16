import sys
z=input;sys.setrecursionlimit(10**5)
def q(node):
    if t[node][1] != -1:return 1+q(t[node][1])
    return 1
n=int(z());t=[0]*(n+1)
for _ in '_'*n:p,l,r=map(int,z().split());t[p]=(l,r);
print(2*n-q(1)-1)