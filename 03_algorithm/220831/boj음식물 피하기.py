import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
dx = [0, 0, 1, -1]
dy = [1, -1, 0 ,0]


def dfs(x,y):
    global cnt
    graph[x][y] = 0
    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                cnt += 1
                dfs(nx,ny)


n, m, k = map(int,input().split())
graph = [[0] * m for _ in range(n)]

for _ in range(k):
    a, b = map(int,input().rstrip().split())
    graph[a-1][b-1] = 1

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt = 1
            dfs(i,j)
            result = max(cnt, result)

print(result)