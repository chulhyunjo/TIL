from math import gcd
def dfs(i):
    for next, p, q in graph[i]:
        if not visited[next]:
            visited[next] = 1
            result[next] = result[i] * q//p
            dfs(next)

n = int(input())
graph = [[] for _ in range(n)]
visited = [0] * n
result = [0]*n
lcm = 1

for _ in range(n-1):
    a, b, p, q = map(int,input().split())
    graph[a].append((b,p,q))
    graph[b].append((a,q,p))
    lcm *= (p*q // gcd(p,q)) # 가장 큰 애가 됨

result[0] = lcm
visited[0] = 1
dfs(0)

m = result[0]
for i in range(1, n):
    m = gcd(m, result[i])

for i in range(n):
    print(result[i] // m, end=" ")