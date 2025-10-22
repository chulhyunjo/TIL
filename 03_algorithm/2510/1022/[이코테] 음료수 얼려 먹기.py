"""
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000011111000
11111111110011
11100011111111
11100011111111
"""
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0 ,1, -1]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    graph[x][y] = 1
    while queue:
        now_x, now_y = queue.popleft()
        for i in range(4):
            next_x, next_y = now_x + dx[i], now_y + dy[i]
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M: continue
            if visited[next_x][next_y] or graph[next_x][next_y] == 1: continue
            visited[next_x][next_y] = True
            graph[next_x][next_y] = 1
            queue.append((next_x, next_y))

N, M = map(int, input().split())

visited = [[False] * M for _ in range(N)]
graph = []
for _ in range(N):
    line = list(input())
    graph.append(list(map(int, line)))

result = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            bfs(i, j)
            result += 1

print(result)