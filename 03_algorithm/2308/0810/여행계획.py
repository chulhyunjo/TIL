import sys
input = sys.stdin.readline

def find(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parents[b] = a


N = int(input())
M = int(input())
parents = [i for i in range(N+1)]

for i in range(N):
    road = list(map(int,input().split()))
    for j in range(N):
        if road[j] == 1:
            union(i+1, j+1)

plans = list(map(int,input().split()))
p = parents[plans[0]]
flag = 1
for i in range(1,M):
    if find(plans[i]) != p:
        flag = 0
        break

if flag:
    print('YES')
else:
    print('NO')