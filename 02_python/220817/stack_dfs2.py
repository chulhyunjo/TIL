def dfs(v):
    print(v)                    # 방문
    visited[v] = 1              # 시작점 방문 표시
    for w in adjList[v]:
        if visited[w] == 0:
            dfs(w)


V, E = map(int,input().split())
N = V + 1
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int,input().split())
    adjList[a].append(b)
    adjList[b].append(a)

visited = [0] * N
dfs(0)
print()