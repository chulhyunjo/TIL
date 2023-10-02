import sys
input = sys.stdin. readline

N, M = map(int,input().split())
parties = [[] for _ in range(N+1)]

graph = [list(map(int,input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for _ in range(M):
    a, b, c = map(int,input().split())
    if graph[a-1][b-1] <= c:
        print('Enjoy other party')
    else:
        print('Stay here')