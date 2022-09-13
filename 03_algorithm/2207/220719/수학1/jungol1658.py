from math import gcd

x, y = map(int, input().split())
print(gcd(x,y))
print((x*y)//gcd(x,y))