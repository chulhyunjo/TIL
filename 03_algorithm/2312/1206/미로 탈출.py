from collections import deque

def bfs(x, y):
    queue = deque([(x,y,0,)])
    visited[x][y][0] = 0
    while queue:
        x, y, use = queue.popleft()
        if x == ex -1 and y == ey - 1:
            return visited[x][y][use]
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx = x + dx
            ny = y + dy
            if 0 > nx or 0 > ny or N <= nx or M <= ny: continue
            if visited[nx][ny][use] > visited[x][y][use] + 1 and graph[nx][ny] == 0:
                visited[nx][ny][use] = visited[x][y][use] + 1
                queue.append((nx,ny,use))
            if use == 0 and graph[nx][ny] == 1 and visited[nx][ny][use+1] > visited[x][y][use] + 1:
                visited[nx][ny][use+1] = visited[x][y][use] + 1
                queue.append((nx, ny, 1))
    return -1

N, M = map(int,input().split())
hx, hy = map(int,input().split())
ex, ey = map(int,input().split())
INF = 10**6 + 1
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[[INF,INF] for _ in range(M)]  for _ in range(N)]

print(bfs(hx-1, hy-1))
