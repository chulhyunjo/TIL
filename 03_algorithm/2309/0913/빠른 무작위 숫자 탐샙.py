from collections import deque
move = [(1,0),(-1,0),(0,1),(0,-1)]


def bfs(r, c, num):
    queue = deque([(r, c, 0)])
    visited = [[0] * 5 for _ in range(5)]
    visited[r][c] = 1
    while queue:
        x, y, cnt = queue.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 > nx or 0 > ny or 5 <= nx or 5 <= ny: continue
            if visited[nx][ny] or graph[nx][ny] == -1: continue
            visited[nx][ny] = 1
            if graph[nx][ny] > 0:
                distance[num][graph[nx][ny]] = cnt + 1
            queue.append((nx,ny,cnt + 1))


def dfs(now, d, cnt):
    global answer
    if cnt >= answer: return
    if d == 6:
        answer = min(answer, cnt)
    else:
        for i in range(1, 7):
            if visited[i]: continue
            if distance[now][i] == -1: continue
            visited[i] = 1
            dfs(i, d+1, cnt + distance[now][i])
            visited[i] = 0


graph = [list(map(int,input().split())) for _ in range(5)]
r, c = map(int,input().split())
distance = [[-1]*7 for _ in range(7)]
position = dict()

# 각 지점 위치 저장
for i in range(5):
    for j in range(5):
        if graph[i][j] > 0:
            position[graph[i][j]] = (i, j)

# bfs로 a -> b 거리 구하기
bfs(r, c, 0)
for k, v in position.items():
    x, y = v
    bfs(x, y, k)

# 백트래킹
visited = [0] * 7
visited[0] = 1
answer = 26
dfs(0, 0, 0)

if answer == 26:
    print(-1)
else:
    print(answer)