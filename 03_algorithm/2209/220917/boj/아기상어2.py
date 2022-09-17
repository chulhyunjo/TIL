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
    eat_time = 400
    move_x = move_y = 400
    if eat == size:
        if size > 7: size = 7
        size += 1
        eat = 0
    queue = deque()
    queue.append((start_x, start_y, 0))
    visited = [False] * (n**2)
    visited[start_x*n + start_y] = True
    while queue:
        x, y, time = queue.popleft()
        if time > eat_time: break
        if 0 < graph[x][y] < size:
            if x < move_x:
                move_x, move_y = x, y
                eat_time = time
                end_shark = 0
            if x == move_x and y < move_y:
                move_x, move_y = x, y
        for m in range(4):
            nx = x + dx[m]
            ny = y + dy[m]
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx*n+ny] and graph[nx][ny]<=size:
                    queue.append((nx, ny, time + 1))
                    visited[nx*n + ny] = True
    if end_shark:
        break
    eat += 1
    result += eat_time
    graph[start_x][start_y] = 0
    graph[move_x][move_y] = 9
    start_x, start_y = move_x, move_y

print(result)