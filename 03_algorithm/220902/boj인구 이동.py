from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x,y):
    global sum1
    global change_yn
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    change.append((x,y))
    while queue:
        x, y = queue.popleft()
        for q in range(4):
            nx = x + dx[q]
            ny = y + dy[q]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    change.append((nx,ny))
                    sum1 += graph[nx][ny]
                    change_yn = 1

n , l, r = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
time = 0
while True:
    change_yn = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                sum1 = graph[i][j]
                change = []
                bfs(i,j)
            avg = sum1 // len(change)
            for x, y in change:
                graph[x][y] = avg
    if not change_yn:
        break
    time += 1

print(time)