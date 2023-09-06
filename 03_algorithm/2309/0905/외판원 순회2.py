def dfs(i, d, cost, first):
    global answer
    if cost >= answer:
        return
    if d == N:
        if graph[i][first]:
            answer = min(answer, cost+graph[i][first])
        return

    for j in range(N):
        if not graph[i][j]: continue
        if visited[j]: continue
        visited[j] = True
        dfs(j, d+1, cost + graph[i][j], first)
        visited[j] = False

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [False] * N
answer = int(1e10)

for i in range(N):
    visited[i] = True
    dfs(i, 1, 0, i)
    visited[i] = False

print(answer)