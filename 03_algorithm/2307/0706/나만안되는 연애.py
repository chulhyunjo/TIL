import sys
input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x > y:
        x, y = y, x
    if x != y:
        parents[y] = x
        return True
    return False


N, M = map(int,input().split())
s = list(input().rstrip().split())
parents = [i for i in range(N+1)]
edges = []

for _ in range(M):
    u, v, d = map(int,input().split())
    if s[u-1] == s[v-1]: continue
    edges.append((d,u,v))
edges.sort()

answer = 0
cnt = 0
for d, u, v in edges:
    if union(u,v):
        answer += d
        cnt += 1
if cnt == N-1:
    print(answer)
else:
    print(-1)