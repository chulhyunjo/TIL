from collections import deque

d = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(start_x, start_y):
    visited[start_x][start_y] = 1
    queue = deque([(start_x, start_y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx, dy = d[i]
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if visited[nx][ny] < visited[x][y] or graph[nx][ny] == 0: continue
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))

INF = 99999999
N, M = map(int,input().split())
graph = [list(map(int, list(input()))) for _ in range(N)]
visited = [[INF] * M for _ in range(N)]
bfs(0, 0)

print(visited[N-1][M-1])