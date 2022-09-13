from collections import deque

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j, 0))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while queue:
    x, y, cnt = queue.popleft()

    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]

        if 0 > nx or n <= nx or 0 > ny or m <= ny or box[nx][ny] !=0:
            continue

        box[nx][ny] = 1
        queue.append((nx,ny,cnt+1))
    if not queue:
        result = cnt

for i in range(n):
    if box[i].count(0):
        result = -1
        break

print(result)