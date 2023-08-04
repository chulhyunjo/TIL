def dfs(i):
    visited[i] = True
    for nx in graph[i]:
        if not visited[nx]:
            dfs(nx)

N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0
for x in range(1, N+1):
    if not visited[x]:
        dfs(x)
        ans += 1

print(ans)