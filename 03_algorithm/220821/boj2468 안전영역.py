import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def dfs(x,y):
    visited[x][y] = True
    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] >= h:
            dfs(nx,ny)


n = int(input())
graph = [list(map(int,input().rstrip().split())) for _ in range(n)]

min_arr = min(map(min, graph))
max_arr = max(map(max, graph))

result = 0
for h in range(min_arr, max_arr + 1):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] >= h:
                dfs(i,j)
                cnt += 1
            result = max(result, cnt)
print(result)