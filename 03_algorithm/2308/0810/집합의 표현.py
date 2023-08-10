import sys
input = sys.stdin.readline

def find(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parents[b] = a

n, m = map(int,input().split())
parents = [i for i in range(n+1)]

for _ in range(m):
    x, a, b = map(int,input().split())
    if x == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')