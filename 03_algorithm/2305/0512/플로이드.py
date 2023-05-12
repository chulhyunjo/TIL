import sys
input = sys.stdin.readline

INF = int(1e8)
N = int(input())
M = int(input())

graph = [[INF] * (N+1) for _ in range(N+1)]
for i in range(1,N+1):
    graph[i][i] = 0

for _ in range(M):
    a, b, c = map(int,input().rstrip().split())
    if graph[a][b] > c:
        graph[a][b] = c

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1,N+1):
    for j in range(1,N+1):
        print(graph[i][j] if graph[i][j] != INF else 0, end = ' ')
    print()
