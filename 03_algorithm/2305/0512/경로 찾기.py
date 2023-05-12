n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                graph[i][j] = 1 if graph[i][k] + graph[k][j] == 2 else 0

for i in range(n):
    print(*graph[i])