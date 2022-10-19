from collections import deque
def bfs(x,y,use):
    queue = deque()
    queue.append((x,y,use))
    while queue:
        x, y, u = queue.popleft()
        if x == n-1 and y == m-1:
            return v[x][y][u]
        for dx, dy in [[1,0],[-1,0],[0,1],[0,-1]]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx>=n or ny>=m or v[nx][ny][u] != 0: continue
            if graph[nx][ny] == 0:
                queue.append((nx,ny,u))
                v[nx][ny][u] = v[x][y][u] + 1
            if graph[nx][ny] == 1 and not u:
                v[nx][ny][1] = v[x][y][0] + 1
                queue.append((nx,ny,1))
    return -1


n, m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
v = [[[0]*2 for _ in range(m)] for _ in range(n)]
v[0][0][0] = 1
result = bfs(0,0,0)
print(result)
