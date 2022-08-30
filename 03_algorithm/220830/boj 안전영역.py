import sys
sys.setrecursionlimit(10**6)
dx = [0,0,1,-1]
dy = [1,-1,0,0]


def dfs(x,y,val):
    visited[x][y] = True
    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] >= val:
                dfs(nx,ny,val)


n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
minV = min(map(min,*graph))
maxV = max(map(max,*graph))
result = 0

for v in range(minV, maxV+1):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= v and not visited[i][j]:
                dfs(i,j,v)
                cnt += 1
    result = max(result, cnt)

print(result)