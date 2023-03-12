from collections import deque
dx, dy = [1,-1,0,0], [0,0,1,-1]
def bfs(x, y, color, R_G):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    if not R_G:
        while queue:
            x, y = queue.popleft()
            for q in range(4):
                nx, ny = x + dx[q], y + dy[q]
                if 0 > nx or 0 > ny or n <= nx or n <= ny or visited[nx][ny]: continue
                if graph[nx][ny] == color:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1

    if R_G:
        while queue:
            x, y = queue.popleft()
            if color == 'R' or color == 'G':
                for q in range(4):
                    nx, ny = x + dx[q], y + dy[q]
                    if 0 > nx or 0 > ny or n <= nx or n <= ny or visited2[nx][ny]: continue
                    if graph[nx][ny] == 'R' or graph[nx][ny] == 'G':
                        queue.append((nx, ny))
                        visited2[nx][ny] = 1
            else:
                for q in range(4):
                    nx, ny = x + dx[q], y + dy[q]
                    if 0 > nx or 0 > ny or n <= nx or n <= ny or visited2[nx][ny]: continue
                    if graph[nx][ny] == color:
                        queue.append((nx, ny))
                        visited2[nx][ny] = 1

n = int(input())
graph = [list(input()) for _ in range(n)]

# 적록색약 아닌 사람
visited = [[0]*n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j,graph[i][j],0)
            cnt += 1

# 적록색약인 사람
visited2 = [[0]*n for _ in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visited2[i][j]:
            bfs(i,j,graph[i][j], 1)
            cnt2 += 1

print(cnt, cnt2)