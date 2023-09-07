from collections import deque

def bfs():
    queue = deque([(0,0)])
    visited[0][0] = 0
    while queue:
        x, y = queue.popleft()
        now = visited[x][y]
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy
            # 그래프 밖이면
            if 0 > nx or 0 > ny or N <= nx or M <= ny: continue
            # 벽이면
            if graph[nx][ny] == 1:
                if visited[nx][ny] <= now + 1 : continue
                visited[nx][ny] = now + 1
            # 벽이 아니면
            else:
                if visited[nx][ny] <= now: continue
                visited[nx][ny] = now

            queue.append((nx,ny))


M, N = map(int,input().split())
graph = [list(map(int,input())) for _ in range(N)]

visited = [[int(1e4)] * M for _ in range(N)]

bfs()
print(visited[N-1][M-1])
