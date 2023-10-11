from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y):
    queue = deque([(x,y)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 > nx or 0 > ny or N <= nx or M <= ny: continue
            if graph[nx][ny] == 0 or answer[x][y] + 1 >= answer[nx][ny]: continue
            answer[nx][ny] = answer[x][y] + 1
            queue.append((nx,ny))

N, M = map(int,input().split())
INF = N * M + 2
graph = [list(map(int,input().split())) for _ in range(N)]
answer = [[INF] * M for _ in range(N)]

start_x, start_y = -1, -1
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            answer[i][j] = 0
        elif graph[i][j] == 2:
            start_x, start_y = i, j
            answer[i][j] = 0

bfs(start_x,start_y)
for i in range(N):
    for j in range(M):
        if answer[i][j] == INF:
            print(-1, end=' ')
        else:
            print(answer[i][j], end= ' ')
    print()