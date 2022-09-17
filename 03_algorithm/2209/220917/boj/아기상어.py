from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
eat = 0
result = 0
size = 2

n = int(input())
graph = []
for i in range(n):
    l = list(map(int, input().split()))
    graph.append(l)
    for j in range(n):
        if l[j] == 9:
            start_x, start_y = i, j


while True:
    end_shark = 1
    if eat == size:
        size += 1
        eat = 0
    queue = deque()
    queue.append((start_x, start_y, 0))
    visited = [False] * (n**2)
    visited[start_x*n + start_y] = True
    while queue:
        x, y, time = queue.popleft()
        if 0< graph[x][y] < size:
            eat += 1
            result += time
            graph[start_x][start_y] = 0
            graph[x][y] = 9
            start_x, start_y = x, y
            end_shark = 0
            break
        for m in range(4):
            nx = x + dx[m]
            ny = y + dy[m]
            if 0 > nx or n <= nx or 0 > ny or n <= ny: continue
            if visited[nx*n + ny]: continue
            if graph[nx][ny] > size: continue
            queue.append((nx, ny, time + 1))
            visited[nx*n + ny] = True
    if end_shark:
        break
print(result)