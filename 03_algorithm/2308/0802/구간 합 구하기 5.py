import sys
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[0] * (N+1)]
graph += [[0] + list(map(int,input().split())) for _ in range(N)]
sums = [[0] * (N+1) for _ in range(N+1)]
sums[1][1] = graph[1][1]

for i in range(2, N+1):
    sums[1][i] = sums[1][i-1] + graph[1][i]
    sums[i][1] = sums[i-1][1] + graph[i][1]

for i in range(2, N+1):
    for j in range(2, N+1):
        sums[i][j] = sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] + graph[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int ,input().split())
    print(sums[x2][y2] - sums[x2][y1-1] - sums[x1-1][y2] + sums[x1-1][y1-1])