import sys
input = sys.stdin.readline
INF = int(1e7)

V, E = map(int,input().split())
graph = [[INF] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int,input().split())
    # a->b
    graph[a][b] = c

for i in range(1, V+1):
    for j in range(1, V+1):
        for k in range(1, V+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = INF
for i in range(1, V+1):
    answer = min(answer, graph[i][i])

print(answer if answer != INF else -1)
