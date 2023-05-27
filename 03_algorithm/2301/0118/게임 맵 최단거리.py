from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(maps):
    n = len(maps)
    m = len(maps[0])
    queue = deque()
    queue.append((0, 0, 1))
    while queue:
        x, y, cnt = queue.popleft()
        maps[x][y] = cnt
        for q in range(4):
            nx, ny = x + dx[q], y + dy[q]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if maps[nx][ny] + maps[x][y] <= maps[x][y]: continue
            if nx == n - 1 and ny == m - 1: return cnt + 1
            queue.append((nx, ny, cnt + 1))

    return -1

m = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
a = bfs(m)
print(a)
