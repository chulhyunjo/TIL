from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]


def melt():
    result = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                c = 0
                if graph[i-1][j] == 0:
                    c += 1
                if graph[i+1][j] == 0:
                    c += 1
                if graph[i][j-1] == 0:
                    c += 1
                if graph[i][j+1] == 0:
                    c += 1
                result.append((i,j,c))
    while result:
        i,j,c = result.pop()
        graph[i][j] = graph[i][j] - c if graph[i][j] - c >= 0 else 0


def find_land(x,y):
    global cnt
    queue = deque()
    queue.append((x,y))
    visited[x][y] = cnt
    while queue:
        x, y = queue.popleft()
        for q in range(4):
            nx = x + dx[q]
            ny = y + dy[q]
            if not visited[nx][ny] and graph[nx][ny] != 0:
                queue.append((nx,ny))
                visited[nx][ny] = cnt

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
T = 0
while True:
    is_land = 0
    T += 1
    melt()
    cnt = 0
    visited = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                cnt += 1
                if cnt == 2:
                    break
                find_land(i,j)
                is_land = 1
        if cnt == 2: break
    if cnt == 2 or not is_land:
        break
if is_land:
    print(T)
else:
    print(0)