from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    queue = deque([(x,y)])
    graph[x][y] = 2
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
            nx, ny = x + dx, y + dy
            if 0 > nx or 0 > ny or N <= nx or M <= ny: continue
            if graph[nx][ny] != 1: continue
            graph[nx][ny] = 2
            queue.append((nx,ny))

N, M = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]

answer = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            bfs(i,j)
            answer += 1

print(answer)