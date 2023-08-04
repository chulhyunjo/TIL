from collections import deque
INF = 10**5

def bfs():
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0 > nx or N <= nx or 0 > ny or M <= ny or graph[nx][ny] == 0: continue
            if visited[x][y] + 1 >= visited[nx][ny]: continue
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))
            if nx == N-1 and ny == M-1:
                return visited[nx][ny]

N, M = map(int,input().split())
graph = [list(map(int,input())) for _ in range(N)]
visited=[[INF]*M for _ in range(N)]
visited[0][0] = 1
bfs()

print(visited[N-1][M-1])