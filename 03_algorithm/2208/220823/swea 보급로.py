from collections import deque
import math
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    result[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for q in range(4):
            nx = x + dx[q]
            ny = y + dy[q]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if result[nx][ny] > result[x][y] + graph[nx][ny]:
                result[nx][ny] = result[x][y] + graph[nx][ny]
                queue.append((nx, ny))
    return result[n - 1][n - 1]


for tc in range(1, int(input()) + 1):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]
    result = [[math.inf] * n for _ in range(n)]
    print(f'#{tc} {bfs(0, 0)}')
