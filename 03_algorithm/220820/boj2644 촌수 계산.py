def dfs(v,find):
    global cnt

    if v == find:
        return 1
    else:
        visited[v] = True
        for i in graph[v]:
            if not visited[i]:
                if dfs(i,find):
                    cnt += 1
                    return 1
        return 0


n = int(input())
s, e = map(int,input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 0
if dfs(s,e):
    print(cnt)
else:
    print(-1)