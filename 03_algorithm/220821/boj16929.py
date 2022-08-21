import sys

sys.setrecursionlimit(10**6)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, a, b, ct):
    if ct >= 4 and x == a and y == b:
        print('Yes')
        exit()
    else:
        for q in range(4):
            nx = x + dx[q]
            ny = y + dy[q]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    dfs(nx, ny, a, b, ct+1)
                    visited[nx][ny] = False



n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
result = 'No'
for i in range(n):
    for j in range(m):
        cnt = 0
        visited = [[False] * m for _ in range(n)]
        dfs(i, j, i, j, cnt)

print(result)
