from collections import deque
d = [(1,0), (-1,0), (0,1), (0,-1)]
N, M = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]
answer = [[-1] * M for _ in range(N)]

queue = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            answer[i][j] = 0
        elif graph[i][j] == 2:
            queue.append((i,j))
            answer[i][j] = 0
while queue:
    x, y = queue.popleft()
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 > nx or 0 > ny or N <= nx or M <= ny: continue
        if graph[nx][ny] == 0 : continue
        if answer[nx][ny] != -1: continue
        answer[nx][ny] = answer[x][y] + 1
        queue.append((nx,ny))

for i in range(N):
    print(*answer[i])