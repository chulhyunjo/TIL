from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x,y, cnt):
    queue = deque()
    queue.append((x,y, cnt))
    visited[x][y] = True
    while queue:
        x, y, cnt = queue.popleft()
        for q in range(4):
            nx = x + dx[q]
            ny = y + dy[q]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 'L' and not visited[nx][ny]:
                    queue.append((nx,ny,cnt+1))
                    visited[nx][ny] = True
    return cnt

n, m = map(int,input().rstrip().split())
graph = [list(input().rstrip()) for _ in range(n)]
maxV = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            visited = [[False] * m for _ in range(n)]
            depth = bfs(i,j,0)
            maxV = max(maxV, depth)

print(maxV)
