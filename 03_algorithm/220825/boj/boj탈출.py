from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def water():
    wat = deque()
    for a in range(n):
        for b in range(m):
            if graph[a][b] == '*':
                wat.append((a,b))
    while wat:
        a, b = wat.popleft()
        for q in range(4):
            nx = a + dx[q]
            ny = b + dy[q]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '.':
                graph[nx][ny] = '*'


n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
time = 0
x1 = y1 = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            x1, y1 = i, j
            break

queue = deque()
queue.append([x1, y1, 0])
result = 0
while True:
    time += 1
    water()
    while queue and queue[0][2] < time:
        p = queue.popleft()
        x, y, cnt = p[0], p[1], p[2]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '.':
                queue.append([nx, ny, cnt + 1])
                graph[nx][ny] = cnt + 1
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 'D':
                result = cnt + 1
    if not queue or result:
        break

if result:
    print(result)
else:
    print('KAKTUS')
