n1, n2 = map(int,input().split())
a = (100-n1)
b = (100-n2)
c = 100 - (a+b)
d = a*b
q = d//100
r = d%100

r1 = c + q
r2 = r
print(a,b,c,d,q,r)
print(r1,r2)