from collections import deque
n, m  = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]
dx, dy = [0,0,1,-1], [1,-1,0,0]
# bfs
queue = deque()
queue.append((0,0))
while queue:
    x, y = queue.popleft()
    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]
        if 0 <= nx < n and 0<= ny < m and graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx,ny))
print(graph[n-1][m-1])