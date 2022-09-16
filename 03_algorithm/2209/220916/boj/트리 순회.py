import sys
z=input;sys.setrecursionlimit(10**5);N=int(z());t={};
for _ in '_'*N:a,*b=map(int,z().rstrip().split());t[a]=b;
I=[]
def q(i):
 a,b=t.get(i)
 if a!=-1:q(a);
 I.append(i);
 if b!=-1:q(b)
q(1);c=0;
def w(i):
 global c
 a,b=t.get(i)
 if a!=-1:c+=1;w(a);
 if b!=-1:c+=1;w(b)
 if i==I[-1]:print(c);exit();
 c+=1
w(1)