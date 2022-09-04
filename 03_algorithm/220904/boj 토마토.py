from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0 ,0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

m, n, h = map(int,input().rstrip().split())
graph = [[list(map(int,input().rstrip().split())) for _ in range(n)] for _ in range(h)]
queue = deque()
need = 0
for k in range(0, h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0:
                need +=1
            if graph[k][i][j] == 1:
                queue.append((k, i, j, 0))

while queue:
    for _ in range(len(queue)):
        k, x, y, cnt = queue.popleft()
        for q in range(6):
            nx = x + dx[q]
            ny = y + dy[q]
            nz = k + dz[q]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if graph[nz][nx][ny] == 0:
                    queue.append((nz,nx,ny,cnt +1))
                    graph[nz][nx][ny] = 1
                    need -= 1
if need:
    print(-1)
else:
    print(cnt)