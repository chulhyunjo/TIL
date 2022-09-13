from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    cnt = 1
    while queue:
        x, y = queue.popleft()
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                cnt += 1
    return cnt


n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
result = 0
cnt1 = 0

for q in range(n):
    for w in range(m):
        if graph[q][w] == 1:
            cnt1 = bfs(q, w)
    result = cnt1 if result < cnt1 else result

print(result)
