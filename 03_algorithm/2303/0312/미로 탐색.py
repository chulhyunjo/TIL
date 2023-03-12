from collections import deque

def bfs():
    queue = deque()
    queue.append((0,0))
    while queue:
        x, y = queue.popleft()
        for q in range(4):
            nx , ny = x + dx[q], y + dy[q]
            if nx<0 or ny<0 or nx>=n or ny>=m or not graph[nx][ny]: continue
            if visited[nx][ny] : continue
            queue.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1


n, m = map(int,input().split())
dx, dy = [0,0,1,-1], [1,-1,0,0]
graph = [list(map(int,input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

bfs()
print(visited[n-1][m-1] + 1)