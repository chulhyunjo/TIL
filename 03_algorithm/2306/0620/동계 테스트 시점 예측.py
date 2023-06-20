from collections import deque
import sys
input = sys.stdin.readline
d = [(1,0), (-1,0), (0,1), (0,-1)]

def findIce(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = -1
    while queue:
        x, y = queue.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 > nx or N <= nx or 0 > ny or M <= ny: continue
            if graph[nx][ny] == -1: continue
            if graph[nx][ny] >= 1:
                graph[nx][ny] += 1
                if graph[nx][ny] == 3:
                    nxtIce.append((nx,ny))
            else:
                graph[nx][ny] = -1
                queue.append((nx,ny))

N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
nxtIce = []
findIce(0,0)
time = 0
while nxtIce:
    time += 1
    if nxtIce:
        tmp = nxtIce[::]
        nxtIce = []
        for x,y in tmp:
            graph[x][y] = 0
            findIce(x,y)

print(time)