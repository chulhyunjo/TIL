from itertools import permutations
import copy
n = int(input())
arr2 = sorted(list(map(int,input().split())),reverse=True)
math_ = list(map(int,input().split()))
r = []
ob = ['+','-','*','/']
maxV = int(-1e9)
minV = int(1e9)
for i in range(4):
    for j in range(math_[i]):
        r.append(ob[i])
for c in list(permutations(r,n-1)):
    arr = copy.deepcopy(arr2)
    a = arr.pop()
    for m in c:
        b = arr.pop()
        if m == '+':
            a += b
        elif m == '-':
            a -= b
        elif m == '*':
            a *= b
        elif m == '/':
            if a<0:
                a = -(abs(a)//b)
            else:
                a //= b
    minV = min(minV,a)
    maxV = max(maxV,a)
print(maxV,minV,sep='\n')
print(len(permutations(r,n-1)))