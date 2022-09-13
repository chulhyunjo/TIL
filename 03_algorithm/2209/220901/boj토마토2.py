from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dm = [1, -1]

n, m, h = map(int,input().rstrip().split())
graph = [list(map(int,input().rstrip().split())) for _ in range(m*h)]
queue = deque()

for i in range(m*h):
    for j in range(n):
        if graph[i][j] == 1:
            queue.append((i,j,0))

while queue:
    x, y, cnt = queue.popleft()
    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]

        if x // m * m <= nx < x // m * m + m and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx,ny,cnt+1))

    for w in range(2):
        for e in range(h):
            nm = x + dm[w] * m * e

            if 0 <= nm < m * h and graph[nm][y] == 0:
                graph[nm][y] = 1
                queue.append((nm, y, cnt + 1))
for i in graph:
    if i.count(0):
        cnt = -1

print(cnt)