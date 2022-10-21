from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    global cnt
    queue = deque()
    queue.append((0, 0, [graph[0][0]]))
    while queue:
        x, y, z = queue.popleft()
        cnt = max(cnt, len(z))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in z:
                queue.append((nx, ny, z + [graph[nx][ny]]))


r, c = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 1

bfs()
print(cnt)