N = int(input())
graph = [[] for _ in range(N)]

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def dfs(x):
    visited[x] = True
    for nx, p, q in graph[x]:
        if not visited[nx]:
            result[nx] = result[x] * q//p
            dfs(nx)

lcd = 1
result = [1] * N
visited = [False] * N

for _ in range(N-1):
    a, b, p, q = map(int,input().split())
    graph[a].append((b,p,q))
    graph[b].append((a,q,p))
    lcd *= (p * q // gcd(p, q))

result[0] = lcd
dfs(0)

mgcd = result[0]
for i in range(1, N):
    mgcd = gcd(mgcd, result[i])

print(*list(map(lambda x: x//mgcd, result)))