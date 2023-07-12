N, M = map(int,input().split())

graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    graph[a][b] = 1

for k in range(1, N+1):
    for i in range(1,N+1):
        for j in range(1, N+1):
            if (graph[i][k] and graph[k][j]) or graph[i][j] == 1:
                graph[i][j] = 1

answer = 0
for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        cnt += graph[i][j] + graph[j][i]
    if cnt == N-1:
        answer += 1

print(answer)