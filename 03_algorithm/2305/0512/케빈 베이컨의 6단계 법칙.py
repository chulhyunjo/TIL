import sys
INF = sys.maxsize

N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1,N+1):
    graph[i][i] = 0

for _ in range(N):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1,N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

minNum = INF
idx = -1
for i in range(1, N+1):
    sum1 = 0
    for j in range(1, N+1):
        sum1 += graph[i][j]
    if minNum > sum1:
        minNum = sum1
        idx = i

print(idx)