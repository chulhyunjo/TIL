from collections import deque

n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)] # 적약색약 x
dx,dy=[0,0,1,-1],[1,-1,0,0]

def bfs(x,y,c):
    global near, is_RB,cnt1
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for q in range(4):
            nx, ny = x+dx[q], y+dy[q]
            if 0 > nx or n <= nx or 0 > ny or n <= ny:
                continue
            if is_RB and visited[nx][ny] and graph[nx][ny] != 'B' and graph[nx][ny] != c:
                near = 1
                is_RB = 0
            if not visited[nx][ny] and graph[nx][ny] == c:
                visited[nx][ny] = 1
                queue.append((nx,ny))
    cnt1 += 1
    return

cnt1 = 0
cnt2 = 0
is_RB = near = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            if graph[i][j] != 'B':
                is_RB = 1
            else:
                is_RB = 0
            visited[i][j] = 1
            bfs(i,j,graph[i][j])
            if near:
                near = 0
            else:
                cnt2 += 1

print(cnt1, cnt2)