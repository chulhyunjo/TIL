def dfs(now,d):
    global result
    if d == 4:
        result = 1
    else:
        for i in graph[now]:
            if not visited[i]:
                visited[now]= True
                dfs(i, d+1)
                visited[now] = False

n, m = map(int,input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
for f in range(n):
    visited = [False] * n
    dfs(f,0)
    if result: break

print(result)