from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m, h = map(int,input().split())
graph = [[list(map(int,input().rstrip().split())) for _ in range(m)] for _ in range(h)]
a = []
for i in graph:
    for j in range(m):
        for k in range(n):
            if i[j][k] == 1:
                a.append((j,k))
result = 0
cnt = -1
for i in graph:
    queue = deque()
    for x,y in a:
        if i[x][y]:
            queue.append((x,y,0))
        else:
            queue.append((x,y,1))

    while queue:
        x, y, cnt = queue.popleft()
        i[x][y] = 1
        for q in range(4):
            nx = x + dx[q]
            ny = y + dy[q]
            if 0 <= nx < m and 0 <= ny < n:
                if i[nx][ny] == 0:
                    queue.append((nx,ny,cnt+1))
    result = max(cnt,result)

ans = 0
for i in graph:
    for j in range(m):
        if i[j].count(0):
            ans = 1
            break

if ans:
    print(-1)
else:
    print(result)