def dfs(v):
    global cnt
    visited[v] = True
    for q in graph[v]:
        if not visited[q]:
            cnt += 1
            dfs(q)


v = int(input())
e = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (v+1)
cnt = 0
dfs(1)
print(cnt)