from collections import deque
from pprint import pprint
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def make_land(x,y,landnum):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = landnum
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = landnum
                    queue.append((nx,ny))
                if graph[nx][ny] == 0:
                    end.add((x,y))


def make_bridge(x,y,cnt,landnum):
    global result
    visited = [0] * (n**2)
    queue = deque()
    queue.append((x,y,cnt))
    visited[x*n+y] = 1
    find = 0
    while queue:
        x, y, cnt = queue.popleft()
        if cnt >= result: return 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != landnum:
                if not visited[nx*n+ny]:
                    queue.append((nx,ny,cnt+1))
                    visited[nx*n + ny] = 1
                    if graph[nx][ny] != 0:
                        find = 1
                        break
        if find: return cnt
    return 0
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
land = 2
end = set()
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            make_land(i,j,land)
            land += 1

result = int(100*2)
for i,j in end:
    length = make_bridge(i,j,0,graph[i][j])
    if length:
        result = min(result, length)
print(result)