from collections import deque

def fire():
    n = len(fires)
    for _ in range(n):
        i, j = fires.popleft()
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            ni, nj = i + dx, j + dy
            if ni < 0 or nj < 0 or ni >= R or nj >= C: continue
            if graph[ni][nj] == "#" or graph[ni][nj] == "F": continue
            fires.append((ni,nj))
            graph[ni][nj] = "F"

def bfs():
    time = -1
    while queue:
        x, y, cnt = queue.popleft()
        if cnt > time:
            time = cnt
            fire()
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= R or ny >= C: return cnt + 1
            if graph[nx][ny] == "#" or graph[nx][ny] == "F" or visited[nx][ny]: continue
            visited[nx][ny] = 1
            queue.append((nx, ny, cnt + 1))
    return "IMPOSSIBLE"

R, C = map(int,input().split())
graph = [list(input()) for _ in range(R)]
fires = deque()
queue = deque()
visited = [[0] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'J':
            queue.append((i,j,0))
            visited[i][j] = 1
        if graph[i][j] == 'F':
            fires.append((i,j))

print(bfs())
