from collections import deque

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(x, y):
    if visited[x][y] != 0 : return
    visited[x][y] = -1
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 > nx or nx >= N or 0 > ny or ny >= M: continue
            if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                queue.append((nx,ny))
                visited[nx][ny] = -1
            elif graph[nx][ny] == 1:
                visited[nx][ny] += 1
                if visited[nx][ny] == 2:
                    air.append((nx,ny))


N, M = map(int, input().split())

graph = [list(map(int,input().split())) for _ in range(N)]

nums = 0
air = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            nums += 1

visited = [[0]*M for _ in range(N)]

bfs(0,0)

time = 1
while True:
    tmp = air[:]
    for x, y in tmp:
        graph[x][y] = 0
        visited[x][y] = 0
        nums -= 1
    if not nums: break
    air = []
    for x, y in tmp:
        bfs(x, y)
    time += 1

print(time)