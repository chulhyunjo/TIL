from collections import deque

def bfs(x, y, s, w):
    global sheep, wolf
    queue = deque([(x,y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 > nx or 0 > ny or R <= nx or C <= ny: continue
            if visited[nx][ny] or graph[nx][ny] == '#': continue
            if graph[nx][ny] == 'o':
                s += 1
            elif graph[nx][ny] == 'v':
                w += 1
            visited[nx][ny] = True
            queue.append((nx,ny))
    if s > w:
        sheep += s
    else:
        wolf += w

R, C = map(int,input().split())
graph = [list(input()) for _ in range(R)]

sheep = 0
wolf = 0
visited = [[False] * C for _ in range(R)]
for x in range(R):
    for y in range(C):
        if visited[x][y]: continue
        if graph[x][y] == 'o':
            bfs(x, y, 1, 0)
        elif graph[x][y] == 'v':
            bfs(x, y, 0, 1)

print(sheep, wolf)