import sys
sys.setrecursionlimit(10**6)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]


def dfs(x,y):
    global cnt
    graph[x][y] = 0
    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                dfs(nx,ny)
                cnt += 1


result = 0
maxV = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt = 1
            dfs(i,j)
            result += 1
            maxV = max(cnt, maxV)

print(result)
print(maxV)